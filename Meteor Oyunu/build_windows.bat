@echo off
REM Windows için Meteor Kaçış Oyunu Build Script
REM Bu script oyunu Windows'ta çalıştırılabilir .exe dosyasına dönüştürür

echo Meteor Kacis Oyunu - Windows Build Script
echo ==========================================
echo.

REM Mevcut dizine geç
cd /d "%~dp0"

REM PyInstaller kontrolü
echo PyInstaller kontrol ediliyor...
where pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo PyInstaller bulunamadi. Yukleniyor...
    pip install pyinstaller
    if %errorlevel% neq 0 (
        echo PyInstaller yuklenemedi!
        pause
        exit /b 1
    )
)

REM Gerekli paketler
echo.
echo Gerekli paketler yukleniyor...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Paketler yuklenemedi!
    pause
    exit /b 1
)

REM Eski build dosyalarını temizle
echo.
echo Eski build dosyalari temizleniyor...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist __pycache__ rmdir /s /q __pycache__
del /q *.spec 2>nul

REM Build
echo.
echo .exe dosyasi olusturuluyor...
pyinstaller --onefile --windowed --name "Meteor Kacis Oyunu" --noconfirm meteor_kaçış_oyunu_kodlar.py

if %errorlevel% neq 0 (
    echo Build basarisiz!
    pause
    exit /b 1
)

echo.
echo ==========================================
echo Build tamamlandi!
echo ==========================================
echo.
echo Oyunu 'dist\Meteor Kacis Oyunu.exe' dosyasinda bulabilirsiniz.
echo.
echo Kullanim:
echo 1. 'dist\Meteor Kacis Oyunu.exe' dosyasini cift tiklayarak calistirabilirsiniz
echo 2. Bu dosyayi istediginiz yere kopyalayabilirsiniz
echo.
pause

