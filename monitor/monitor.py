import time, psutil
from config.config import GAME_PROCESSES, BLOCKED_APPS, DISABLE_SERVICES
from system.services import stop_service, start_service
from system.firewall import block_apps, unblock_apps
from system.benchmark import snapshot_before, snapshot_after, print_diff
from system.cleaner import run_cleaning
from utils.logs import write_log
from utils.discord_presence import init_presence, stop_presence

active_game = None

def start_monitoring():
    init_presence()
    snapshot_before()
    while True:
        game = detect_game()
        if game and not active_game:
            write_log(f"{game} başlatıldı")
            block_apps(BLOCKED_APPS)
            for s in DISABLE_SERVICES:
                stop_service(s)
            global active_game
            active_game = game

        elif not game and active_game:
            write_log(f"{active_game} kapandı")
            unblock_apps(BLOCKED_APPS)
            for s in DISABLE_SERVICES:
                start_service(s)
            snapshot_after()
            print_diff()
            run_cleaning()
            stop_presence()
            break

        time.sleep(5)

def detect_game():
    for proc in psutil.process_iter(['name']):
        try:
            name = proc.info['name'].lower()
            if name in GAME_PROCESSES:
                return name
        except:
            continue
    return None
