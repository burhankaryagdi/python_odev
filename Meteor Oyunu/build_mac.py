#!/usr/bin/env python3
"""
Mac için Meteor Kaçış Oyunu Build Script
Bu script oyunu Mac'te çalıştırılabilir .app dosyasına dönüştürür
"""

import subprocess
import sys
import os

def run_command(command):
    """Komutu çalıştır ve sonucu göster"""
    print(f"Çalıştırılıyor: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Hata: {result.stderr}")
        return False
    if result.stdout:
        print(result.stdout)
    return True

def main():
    print("Meteor Kaçış Oyunu - Mac Build Script")
    print("=" * 50)
    print()
    
    # Mevcut dizine geç
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # PyInstaller kontrolü
    print("PyInstaller kontrol ediliyor...")
    if not run_command("which pyinstaller"):
        print("PyInstaller bulunamadı. Yükleniyor...")
        if not run_command("pip3 install pyinstaller"):
            print("PyInstaller yüklenemedi!")
            sys.exit(1)
    
    # Gerekli paketler
    print("\nGerekli paketler yükleniyor...")
    if not run_command("pip3 install -r requirements.txt"):
        print("Paketler yüklenemedi!")
        sys.exit(1)
    
    # Eski build dosyalarını temizle
    print("\nEski build dosyaları temizleniyor...")
    for item in ['build', 'dist', '__pycache__']:
        if os.path.exists(item):
            run_command(f"rm -rf {item}")
    # .spec dosyalarını temizle
    for spec_file in os.listdir('.'):
        if spec_file.endswith('.spec'):
            os.remove(spec_file)
    
    # Build
    print("\n.app bundle oluşturuluyor...")
    build_command = (
        "pyinstaller --windowed "
        "--name 'Meteor Kacis Oyunu' "
        "--noconfirm "
        "meteor_kaçış_oyunu_kodlar.py"
    )
    
    if not run_command(build_command):
        print("Build başarısız!")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("Build tamamlandı!")
    print("=" * 50)
    print()
    print("Oyunu 'dist/Meteor Kacis Oyunu.app' klasöründe bulabilirsiniz.")
    print()
    print("Kullanım:")
    print("1. 'dist/Meteor Kacis Oyunu.app' dosyasını çift tıklayarak çalıştırabilirsiniz")
    print("2. Veya Applications klasörüne sürükleyip bırakabilirsiniz")
    print()
    print("Not: İlk çalıştırmada macOS güvenlik uyarısı çıkabilir.")
    print("     Sistem Ayarları > Güvenlik > 'Yine de Aç' seçeneğini kullanın.")

if __name__ == "__main__":
    main()

