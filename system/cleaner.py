import os, shutil, ctypes

def run_cleaning():
    temp = os.environ['TEMP']
    prefetch = os.path.join(os.environ['SystemRoot'], 'Prefetch')

    for folder in [temp, prefetch]:
        try:
            for filename in os.listdir(folder):
                filepath = os.path.join(folder, filename)
                if os.path.isfile(filepath) or os.path.islink(filepath):
                    os.unlink(filepath)
                elif os.path.isdir(filepath):
                    shutil.rmtree(filepath)
        except Exception as e:
            print(f"⚠️ Temizlik hatası: {e}")
