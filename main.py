assa
import psutil, time, subprocess, sys, signal
from firewall import block_apps, unblock_all
from optimizer import disable_services, enable_services

GAME_PROCESSES = ["valorant.exe", "csgo.exe", "minecraft.exe"]
BLOCKED_APPS = ["chrome.exe", "firefox.exe", "discord.exe", "edge.exe"]
DISABLE_SERVICES = ["SysMain", "DiagTrack"]

running = False
active_game = None

def detect_game():
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] and proc.info['name'].lower() in GAME_PROCESSES:
                return proc.info['name'].lower()
        except: continue
    return None

def cleanup(sig, frame):
    print("🧹 Temizlik yapılıyor...")
    unblock_all()
    enable_services(DISABLE_SERVICES)
    sys.exit(0)

signal.signal(signal.SIGINT, cleanup)
signal.signal(signal.SIGTERM, cleanup)

# Güncelleme çağrısı
try:
    subprocess.run([sys.executable, "update.py"], check=True)
except Exception as e:
    print(f"⚠️ Güncelleme sırasında hata: {e}")

print("🚀 FPS Booster çalışıyor...")

while True:
    game = detect_game()
    if game:
        if not running:
            print(f"🎮 {game} algılandı, optimizasyon başlıyor...")
            block_apps(BLOCKED_APPS)
            disable_services(DISABLE_SERVICES)
            running = True
            active_game = game
    else:
        if running:
            print(f"🛑 {active_game} kapandı, sistem eski haline dönüyor...")
            unblock_all()
            enable_services(DISABLE_SERVICES)
            running = False
            active_game = None
    time.sleep(3)
