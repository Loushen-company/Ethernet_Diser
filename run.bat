@echo off
title FPS BOOSTER

rem Python yorumlayıcının yolu
set PYTHON=%~dp0WPy64-31241\python-3.12.4.amd64\python.exe

rem Ana programı çalıştır
"%PYTHON%" "%~dp0main.py"

pause
