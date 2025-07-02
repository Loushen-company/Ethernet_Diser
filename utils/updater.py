import urllib.request, zipfile, os
from config.config import VERSION

def check_and_update():
    try:
        print("🔍 Sürüm kontrol ediliyor...")
        with urllib.request.urlopen("https://raw.githubusercontent.com/kullaniciadi/projeadi/main/version.txt") as response:
            github_version = response.read().decode().strip()
            print(f"🌐 GitHub Sürüm : {github_version}")
            print(f"📝 Lokal Sürüm   : {VERSION}")
            if github_version != VERSION:
                print("⬇️ Yeni sürüm bulundu, indiriliyor...")
                urllib.request.urlretrieve("https://github.com/kullaniciadi/projeadi/archive/refs/heads/main.zip", "update.zip")
                with zipfile.ZipFile("update.zip", 'r') as zip_ref:
                    zip_ref.extractall("update_temp")
                # Burada üzerine yazma ve restart işlemleri yapılmalı
                print("✅ Güncelleme indirildi.")
            else:
                print("✅ Güncel sürüm kullanılıyor.")
    except Exception as e:
        print(f"❌ Güncelleme hatası: {e}")
