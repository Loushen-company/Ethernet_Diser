@echo off
setlocal EnableDelayedExpansion
title 🚀 FPS Booster Başlatılıyor...

:: WinPython klasörüne göre ayarla
set PYTHON_DIR=.\WPy64-31241\python-3.12.4.amd64
set MAIN_SCRIPT=main.py

:: Python var mı kontrol et
if not exist "%PYTHON_DIR%\python.exe" (
    echo ❌ Python çalıştırılamadı. 'winpython' klasörü eksik veya bozuk.
    pause
    exit /b
)

:: Yönetici olarak çalışıyor mu kontrol et
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️ Lütfen bu dosyayı sağ tıklayıp 'Yönetici olarak çalıştır' seçeneğiyle çalıştırın!
    pause
    exit /b
)

:: Başlatılıyor
echo ✅ Python bulundu, uygulama çalıştırılıyor...
"%PYTHON_DIR%\python.exe" %MAIN_SCRIPT%
pause
