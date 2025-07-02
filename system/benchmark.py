import psutil

before = {}
after = {}

def snapshot_before():
    global before
    before = {
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent
    }

def snapshot_after():
    global after
    after = {
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent
    }

def print_diff():
    print(f"🔍 CPU Değişimi: {before['cpu']}% → {after['cpu']}%")
    print(f"🔍 RAM Değişimi: {before['ram']}% → {after['ram']}%")
