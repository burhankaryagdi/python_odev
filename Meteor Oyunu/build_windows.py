#!/usr/bin/env python3
"""
Windows için Meteor Kaçış Oyunu Build Script
Bu script oyunu Windows'ta çalıştırılabilir .exe dosyasına dönüştürür
"""

import subprocess
import sys
import os
import shutil

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
    print("Meteor Kaçış Oyunu - Windows Build Script")
    print("=" * 50)
    print()
    
    # Mevcut dizine geç
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # PyInstaller kontrolü
    print("PyInstaller kontrol ediliyor...")
    result = subprocess.run("where pyinstaller", shell=True, capture_output=True)
    if result.returncode != 0:
        print("PyInstaller bulunamadı. Yükleniyor...")
        if not run_command("pip install pyinstaller"):
            print("PyInstaller yüklenemedi!")
            input("Devam etmek için Enter'a basın...")
            sys.exit(1)
    
    # Gerekli paketler
    print("\nGerekli paketler yükleniyor...")
    if not run_command("pip install -r requirements.txt"):
        print("Paketler yüklenemedi!")
        input("Devam etmek için Enter'a basın...")
        sys.exit(1)
    
    # Eski build dosyalarını temizle
    print("\nEski build dosyaları temizleniyor...")
    for item in ['build', 'dist', '__pycache__']:
        if os.path.exists(item):
            try:
                if os.path.isdir(item):
                    shutil.rmtree(item)
                else:
                    os.remove(item)
            except Exception as e:
                print(f"Uyarı: {item} silinemedi: {e}")
    
    # .spec dosyalarını temizle
    for spec_file in os.listdir('.'):
        if spec_file.endswith('.spec'):
            try:
                os.remove(spec_file)
            except Exception as e:
                print(f"Uyarı: {spec_file} silinemedi: {e}")
    
    # Build
    print("\n.exe dosyası oluşturuluyor...")
    build_command = (
        "pyinstaller --onefile --windowed "
        "--name \"Meteor Kacis Oyunu\" "
        "--noconfirm "
        "meteor_kaçış_oyunu_kodlar.py"
    )
    
    if not run_command(build_command):
        print("Build başarısız!")
        input("Devam etmek için Enter'a basın...")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("Build tamamlandı!")
    print("=" * 50)
    print()
    print("Oyunu 'dist\\Meteor Kacis Oyunu.exe' dosyasında bulabilirsiniz.")
    print()
    print("Kullanım:")
    print("1. 'dist\\Meteor Kacis Oyunu.exe' dosyasını çift tıklayarak çalıştırabilirsiniz")
    print("2. Bu dosyayı istediğiniz yere kopyalayabilirsiniz")
    print()
    input("Devam etmek için Enter'a basın...")

if __name__ == "__main__":
    main()

