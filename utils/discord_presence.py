from pypresence import Presence
import time

client_id = "YOUR_DISCORD_APP_ID"
rpc = None

def init_presence():
    global rpc
    try:
        rpc = Presence(client_id)
        rpc.connect()
        rpc.update(state="Oyun performansı optimize ediliyor", details="FPS Booster Aktif", start=time.time())
    except:
        print("⚠️ Discord RPC bağlantısı başarısız.")

def stop_presence():
    try:
        if rpc:
            rpc.clear()
            rpc.close()
    except:
        pass
