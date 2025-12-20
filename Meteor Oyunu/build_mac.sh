#!/bin/bash

# Mac için Meteor Kaçış Oyunu Build Script
# Bu script oyunu Mac'te çalıştırılabilir .app dosyasına dönüştürür

echo "Meteor Kaçış Oyunu - Mac Build Script"
echo "======================================"
echo ""

# Mevcut dizini kaydet
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# PyInstaller'ın yüklü olup olmadığını kontrol et
if ! command -v pyinstaller &> /dev/null; then
    echo "PyInstaller bulunamadı. Yükleniyor..."
    pip3 install pyinstaller
fi

# Gerekli paketlerin yüklü olduğundan emin ol
echo "Gerekli paketler kontrol ediliyor..."
pip3 install -r requirements.txt

# Eski build dosyalarını temizle
echo ""
echo "Eski build dosyaları temizleniyor..."
rm -rf build dist __pycache__ *.spec

# PyInstaller ile .app bundle oluştur
echo ""
echo ".app bundle oluşturuluyor..."
pyinstaller --windowed \
    --name "Meteor Kacis Oyunu" \
    --noconfirm \
    meteor_kaçış_oyunu_kodlar.py

echo ""
echo "======================================"
echo "Build tamamlandı!"
echo "======================================"
echo ""
echo "Oyunu 'dist/Meteor Kacis Oyunu.app' klasöründe bulabilirsiniz."
echo ""
echo "Kullanım:"
echo "1. 'dist/Meteor Kacis Oyunu.app' dosyasını çift tıklayarak çalıştırabilirsiniz"
echo "2. Veya Applications klasörüne sürükleyip bırakabilirsiniz"
echo ""
echo "Not: İlk çalıştırmada macOS güvenlik uyarısı çıkabilir."
echo "     Sistem Ayarları > Güvenlik > 'Yine de Aç' seçeneğini kullanın."

