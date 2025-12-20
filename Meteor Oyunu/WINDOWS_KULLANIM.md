# Windows Bilgisayarda Çalıştırma Talimatları

## Gereksinimler

1. **Python 3.6 veya üzeri** yüklü olmalı
   - Python yüklü mü kontrol etmek için: `python --version` komutunu çalıştırın
   - Yüklü değilse: https://www.python.org/downloads/ adresinden indirin

2. **pip** (Python paket yöneticisi) yüklü olmalı
   - Genellikle Python ile birlikte gelir

## Adım Adım Talimatlar

### 1. Klasöre Gitme

Windows'ta **Komut İstemi (CMD)** veya **PowerShell** açın ve şu komutu çalıştırın:

```cmd
cd "C:\Users\KULLANICI_ADINIZ\...\Meteor Oyunu"
```

**Örnek:** Eğer dosyalar masaüstündeyse:
```cmd
cd "C:\Users\KULLANICI_ADINIZ\Desktop\Meteor Oyunu"
```

**Not:** Klasör yolunu bulmak için:
- Windows Gezgini'nde klasöre sağ tıklayın
- "Yol olarak kopyala" seçeneğini seçin
- Komut satırına yapıştırın ve başına `cd ` ekleyin

### 2. Build İşlemi

#### Yöntem A: Batch Dosyası ile (Kolay)

1. Windows Gezgini'nde `Meteor Oyunu` klasörüne gidin
2. `build_windows.bat` dosyasına **çift tıklayın**
3. İşlem tamamlanana kadar bekleyin

#### Yöntem B: Komut Satırından

Komut İstemi veya PowerShell'de şu komutu çalıştırın:

```cmd
build_windows.bat
```

veya Python script'i ile:

```cmd
python build_windows.py
```

### 3. Build İşlemi Sırasında

- İlk kez çalıştırıyorsanız, PyInstaller ve pygame otomatik olarak yüklenecek
- Bu işlem birkaç dakika sürebilir
- İnternet bağlantınızın olması gerekir (paket indirme için)

### 4. Build Tamamlandıktan Sonra

Build işlemi tamamlandığında:

1. `dist` klasörü oluşturulacak
2. Bu klasörün içinde `Meteor Kacis Oyunu.exe` dosyasını bulacaksınız
3. Bu `.exe` dosyasını:
   - Çift tıklayarak çalıştırabilirsiniz
   - İstediğiniz yere kopyalayabilirsiniz (masaüstü, başka bir klasör vb.)
   - Başka Windows bilgisayarlara kopyalayabilirsiniz (Python yüklü olmasına gerek yok)

## Sorun Giderme

### "python komutu bulunamadı" hatası

- Python yüklü değil veya PATH'e eklenmemiş olabilir
- Çözüm: Python'u yeniden yükleyin ve "Add Python to PATH" seçeneğini işaretleyin

### "pip komutu bulunamadı" hatası

- pip yüklü değil olabilir
- Çözüm: `python -m ensurepip --upgrade` komutunu çalıştırın

### Antivirus uyarısı

- Bazı antivirus programları PyInstaller ile oluşturulan .exe dosyalarını şüpheli görebilir
- Bu normal bir durumdur, dosya güvenlidir
- Antivirus ayarlarından istisna ekleyebilirsiniz

### Build başarısız olursa

1. Tüm gereksinimlerin yüklü olduğundan emin olun:
   ```cmd
   pip install pygame pyinstaller
   ```

2. Python sürümünüzü kontrol edin (3.6+ olmalı):
   ```cmd
   python --version
   ```

3. Build dosyalarını temizleyip tekrar deneyin:
   ```cmd
   rmdir /s /q build dist __pycache__
   del *.spec
   ```

## Klasör Yapısı

Build işleminden sonra klasör yapısı şöyle olacak:

```
Meteor Oyunu/
├── meteor_kaçış_oyunu_kodlar.py
├── requirements.txt
├── build_windows.bat
├── build_windows.py
├── build/              (geçici build dosyaları)
├── dist/               (oluşturulan .exe burada)
│   └── Meteor Kacis Oyunu.exe
└── ...
```

## Önemli Notlar

- `.exe` dosyası oluşturulduktan sonra `build` klasörünü silebilirsiniz (gerekli değil)
- `dist` klasöründeki `.exe` dosyası bağımsız çalışır (Python gerekmez)
- `.exe` dosyasını başka Windows bilgisayarlara kopyalayabilirsiniz
- İlk çalıştırmada Windows Defender uyarısı çıkabilir, "Daha fazla bilgi" > "Yine de çalıştır" seçeneğini kullanın

