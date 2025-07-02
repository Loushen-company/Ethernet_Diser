import ctypes
from config.config import VERSION
from gui.gui import start_gui
from utils.updater import check_and_update

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    if not is_admin():
        print("⚠️ Bu uygulamayı yönetici olarak çalıştırmalısınız!")
        input("Enter'a basarak çıkın...")
        exit()

    print(f"📝 FPS Booster {VERSION} başlatılıyor...")
    check_and_update()
    start_gui()
