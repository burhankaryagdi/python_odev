# Mac Bilgisayarda Çalıştırma Talimatları

## Gereksinimler

1. **Python 3.6 veya üzeri** yüklü olmalı
   - Python yüklü mü kontrol etmek için Terminal'de: `python3 --version` komutunu çalıştırın
   - Yüklü değilse: https://www.python.org/downloads/ adresinden indirin

2. **pip3** (Python paket yöneticisi) yüklü olmalı
   - Genellikle Python ile birlikte gelir

## Adım Adım Talimatlar

### 1. Klasöre Gitme

Terminal'i açın ve şu komutu çalıştırın:

```bash
cd "/Applications/Castlexe/Codexe/Python/python_odev/Meteor Oyunu"
```

**Not:** Klasör yolunu bulmak için:
- Finder'da klasöre sağ tıklayın
- "Yol Bilgisini Göster" seçeneğini seçin
- Terminal'de `cd ` yazıp klasörü sürükleyip bırakın

### 2. Build İşlemi

#### Yöntem A: Bash Script ile (Kolay)

Terminal'de şu komutu çalıştırın:

```bash
./build_mac.sh
```

#### Yöntem B: Python Script ile

Terminal'de şu komutu çalıştırın:

```bash
python3 build_mac.py
```

### 3. Build İşlemi Sırasında

- İlk kez çalıştırıyorsanız, PyInstaller ve pygame otomatik olarak yüklenecek
- Bu işlem birkaç dakika sürebilir
- İnternet bağlantınızın olması gerekir (paket indirme için)
- Şifre istenebilir (paket yükleme için)

### 4. Build Tamamlandıktan Sonra

Build işlemi tamamlandığında:

1. `dist` klasörü oluşturulacak
2. Bu klasörün içinde `Meteor Kacis Oyunu.app` dosyasını bulacaksınız
3. Bu `.app` dosyasını:
   - Çift tıklayarak çalıştırabilirsiniz
   - Applications klasörüne sürükleyip bırakabilirsiniz
   - Dock'a ekleyebilirsiniz

## macOS Güvenlik Uyarısı

İlk çalıştırmada macOS güvenlik uyarısı çıkabilir:

1. "Meteor Kacis Oyunu.app açılamıyor çünkü geliştiricisi tanınmıyor" uyarısı
2. **Çözüm:**
   - Sistem Ayarları > Güvenlik ve Gizlilik bölümüne gidin
   - "Yine de Aç" butonuna tıklayın
   - Veya `.app` dosyasına sağ tıklayıp "Aç" seçeneğini seçin

## Sorun Giderme

### "python3 komutu bulunamadı" hatası

- Python yüklü değil olabilir
- Çözüm: Homebrew ile yükleyin: `brew install python3`

### "pip3 komutu bulunamadı" hatası

- pip3 yüklü değil olabilir
- Çözüm: `python3 -m ensurepip --upgrade` komutunu çalıştırın

### "Permission denied" hatası

- Script çalıştırma izni yok
- Çözüm: `chmod +x build_mac.sh` komutunu çalıştırın

### Build başarısız olursa

1. Tüm gereksinimlerin yüklü olduğundan emin olun:
   ```bash
   pip3 install pygame pyinstaller
   ```

2. Python sürümünüzü kontrol edin (3.6+ olmalı):
   ```bash
   python3 --version
   ```

3. Build dosyalarını temizleyip tekrar deneyin:
   ```bash
   rm -rf build dist __pycache__ *.spec
   ```

## Klasör Yapısı

Build işleminden sonra klasör yapısı şöyle olacak:

```
Meteor Oyunu/
├── meteor_kaçış_oyunu_kodlar.py
├── requirements.txt
├── build_mac.sh
├── build_mac.py
├── build/              (geçici build dosyaları)
├── dist/               (oluşturulan .app burada)
│   └── Meteor Kacis Oyunu.app
└── ...
```

## Önemli Notlar

- `.app` dosyası oluşturulduktan sonra `build` klasörünü silebilirsiniz (gerekli değil)
- `dist` klasöründeki `.app` dosyası bağımsız çalışır (Python gerekmez)
- `.app` dosyasını başka Mac bilgisayarlara kopyalayabilirsiniz
- İlk çalıştırmada macOS güvenlik uyarısı çıkabilir, bu normaldir

