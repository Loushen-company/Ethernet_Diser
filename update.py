import requests, zipfile, io, os, shutil

GITHUB_REPO = "MountainCompany/Ethernet_Diser"
BRANCH = "main"
ZIP_URL = f"https://github.com/{GITHUB_REPO}/archive/refs/heads/{BRANCH}.zip"
VERSION_URL = f"https://raw.githubusercontent.com/{GITHUB_REPO}/{BRANCH}/version.txt"

DEST = os.path.dirname(os.path.abspath(__file__))
LOCAL_VERSION_PATH = os.path.join(DEST, "version.txt")


def get_local_version():
    try:
        with open(LOCAL_VERSION_PATH, "r") as f:
            return f.read().strip()
    except:
        return "v0.0.0"


def get_github_version():
    try:
        r = requests.get(VERSION_URL, timeout=10)
        if r.status_code == 200:
            return r.text.strip()
        else:
            return None
    except:
        return None


def update_program():
    print("⬇️ Güncelleme başlatılıyor...")
    try:
        r = requests.get(ZIP_URL)
        if r.status_code != 200:
            print("❌ GitHub erişimi başarısız.")
            return
        with zipfile.ZipFile(io.BytesIO(r.content)) as z:
            z.extractall("temp_update")

        new_folder = [d for d in os.listdir("temp_update") if os.path.isdir(os.path.join("temp_update", d))][0]
        source = os.path.join("temp_update", new_folder)
        for file in os.listdir(source):
            full_source = os.path.join(source, file)
            full_dest = os.path.join(DEST, file)
            if os.path.isfile(full_source):
                shutil.copy2(full_source, full_dest)

        shutil.rmtree("temp_update")
        print("✅ Güncelleme tamamlandı.")
    except Exception as e:
        print(f"⚠️ Hata: {e}")


if __name__ == "__main__":
    local_version = get_local_version()
    github_version = get_github_version()

    print(f"📝 Lokal Sürüm   : {local_version}")
    print(f"🌐 GitHub Sürüm : {github_version}")

    if github_version and local_version != github_version:
        print("🔁 Yeni sürüm mevcut, güncelleme başlatılıyor...")
        update_program()
    else:
        print("✅ Güncel sürüm kullanılıyor.")
