import pygame
import random
import sys

# Pygame başlatma
pygame.init()

# Sabitler
GENISLIK = 800
YUKSEKLIK = 600
FPS = 60

# Renkler
SIYAH = (0, 0, 0)
BEYAZ = (255, 255, 255)
KIRMIZI = (255, 0, 0)
TURUNCU = (255, 165, 0)
SARI = (255, 255, 0)
YESIL = (0, 255, 0)
MAVI = (0, 150, 255)
MOR = (128, 0, 128)
PEMBE = (255, 20, 147)
TURKUAZ = (64, 224, 208)
KOYU_MAVI = (30, 30, 100)
KIRMIZI_MAVI = (100, 30, 50)

# Meteor renkleri listesi
METEOR_RENKLERI = [KIRMIZI, TURUNCU, SARI, MOR, PEMBE, TURKUAZ, YESIL, MAVI]

# Oyun durumları
OYUN_DEVAM = 0
OYUN_KAYBETTI = 1
OYUN_KAZANDI = 2


class UzayGemisi:
    """Oyuncunun kontrol ettiği uzay gemisi"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.genislik = 40
        self.yukseklik = 30
        self.hiz = 8
        
    def hareket_et(self, yon):
        """Gemi sağa veya sola hareket eder"""
        if yon == "sol" and self.x > 0:
            self.x -= self.hiz
        elif yon == "sag" and self.x < GENISLIK - self.genislik:
            self.x += self.hiz
    
    def ciz(self, ekran):
        """Gemi ekrana çizilir (beyaz üçgen)"""
        # Üçgen noktaları
        nokta1 = (self.x + self.genislik // 2, self.y)  # Üst orta
        nokta2 = (self.x, self.y + self.yukseklik)  # Sol alt
        nokta3 = (self.x + self.genislik, self.y + self.yukseklik)  # Sağ alt
        pygame.draw.polygon(ekran, BEYAZ, [nokta1, nokta2, nokta3])
        # Gemi gövdesi için küçük bir kare
        pygame.draw.rect(ekran, BEYAZ, 
                        (self.x + 10, self.y + 15, 20, 10))
    
    def carpisma_kontrolu(self, meteor):
        """Gemi ile meteor arasında çarpışma kontrolü (dikdörtgen-daire)"""
        # Dairenin merkezine en yakın dikdörtgen noktasını bul
        en_yakin_x = max(self.x, min(meteor.x, self.x + self.genislik))
        en_yakin_y = max(self.y, min(meteor.y, self.y + self.yukseklik))
        
        # En yakın nokta ile daire merkezi arasındaki mesafe
        mesafe_x = meteor.x - en_yakin_x
        mesafe_y = meteor.y - en_yakin_y
        mesafe = (mesafe_x ** 2 + mesafe_y ** 2) ** 0.5
        
        # Mesafe yarıçaptan küçükse çarpışma var
        return mesafe < meteor.yaricap


class Meteor:
    """Yukarıdan düşen meteorlar"""
    
    def __init__(self, x, y, hiz, yaricap, renk):
        self.x = x
        self.y = y
        self.hiz = hiz
        self.yaricap = yaricap
        self.renk = renk
    
    def hareket_et(self):
        """Meteor aşağı doğru hareket eder"""
        self.y += self.hiz
    
    def ciz(self, ekran):
        """Meteor ekrana çizilir (renkli daire)"""
        pygame.draw.circle(ekran, self.renk, (int(self.x), int(self.y)), self.yaricap)
        # Meteor için parlaklık efekti (iç halka)
        if self.yaricap > 15:
            daha_acik_renk = tuple(min(255, c + 50) for c in self.renk)
            pygame.draw.circle(ekran, daha_acik_renk, (int(self.x), int(self.y)), self.yaricap - 3)
    
    def ekrandan_cikti_mi(self):
        """Meteor ekranın altından çıktı mı?"""
        return self.y > YUKSEKLIK + self.yaricap


class Oyun:
    """Ana oyun sınıfı"""
    
    def __init__(self):
        self.ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
        pygame.display.set_caption("Meteor Kaçış Oyunu")
        self.saat = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.kucuk_font = pygame.font.Font(None, 24)
        
        # Oyun değişkenleri
        self.yeniden_baslat()
    
    def yeniden_baslat(self):
        """Oyunu başlangıç durumuna getirir"""
        self.uzay_gemisi = UzayGemisi(GENISLIK // 2 - 20, YUKSEKLIK - 50)
        self.meteorlar = []
        self.skor = 0
        self.seviye = 1
        self.durum = OYUN_DEVAM
        self.meteor_timer = 0
        self.meteor_spawn_araligi = 60  # Frames cinsinden
    
    def seviye_bilgisi(self):
        """Mevcut seviyeye göre oyun parametrelerini döndürür"""
        if self.seviye == 1:
            return {
                "meteor_hiz": 2,  # Çok yavaş başlangıç
                "meteor_yaricap": 20,
                "spawn_araligi": 60,  # Çok az sık meteor
                "meteor_sayisi": 1,  # Her seferinde tek meteor
                "arka_plan": SIYAH
            }
        elif self.seviye == 2:
            return {
                "meteor_hiz": 2.5,  # Biraz daha hızlı
                "meteor_yaricap": 20,
                "spawn_araligi": 50,  # Biraz daha sık
                "meteor_sayisi": 1,  # Hala tek meteor
                "arka_plan": KOYU_MAVI
            }
        elif self.seviye == 3:
            return {
                "meteor_hiz": 3,  # Orta hız
                "meteor_yaricap": 22,
                "spawn_araligi": 40,  # Orta sıklık
                "meteor_sayisi": 2,  # İki meteor
                "arka_plan": KIRMIZI_MAVI
            }
        else:  # Seviye 4
            return {
                "meteor_hiz": 3.5,  # Biraz hızlı
                "meteor_yaricap": 20,
                "spawn_araligi": 35,  # Biraz daha sık
                "meteor_sayisi": 2,  # İki meteor
                "arka_plan": MOR
            }
    
    def meteor_olustur(self):
        """Yeni meteorlar oluşturur (birden fazla)"""
        params = self.seviye_bilgisi()
        meteor_sayisi = params["meteor_sayisi"]
        
        # Aynı anda birden fazla meteor oluştur
        for _ in range(meteor_sayisi):
            x = random.randint(30, GENISLIK - 30)
            y = random.randint(-100, -30)  # Farklı yüksekliklerden başlasın
            hiz = params["meteor_hiz"] + random.uniform(-0.5, 0.5)  # Hızlarda hafif varyasyon
            yaricap = params["meteor_yaricap"] + random.randint(-5, 5)  # Boyutlarda hafif varyasyon
            yaricap = max(15, min(30, yaricap))  # Min-max sınırları
            renk = random.choice(METEOR_RENKLERI)  # Rastgele renk seç
            meteor = Meteor(x, y, hiz, yaricap, renk)
            self.meteorlar.append(meteor)
    
    def olaylari_isle(self):
        """Klavye ve fare olaylarını işler"""
        for olay in pygame.event.get():
            if olay.type == pygame.QUIT:
                return False
            
            if olay.type == pygame.KEYDOWN:
                if olay.key == pygame.K_r and self.durum != OYUN_DEVAM:
                    self.yeniden_baslat()
        
        return True
    
    def guncelle(self):
        """Oyun mantığını günceller"""
        if self.durum != OYUN_DEVAM:
            return
        
        # Seviye kontrolü
        if self.skor >= 50 and self.seviye == 1:
            self.seviye = 2
        elif self.skor >= 150 and self.seviye == 2:
            self.seviye = 3
        elif self.skor >= 300 and self.seviye == 3:
            self.seviye = 4
        
        # Kazanma kontrolü
        if self.skor >= 500:
            self.durum = OYUN_KAZANDI
            return
        
        # Klavye girişi
        tuslar = pygame.key.get_pressed()
        if tuslar[pygame.K_LEFT] or tuslar[pygame.K_a]:
            self.uzay_gemisi.hareket_et("sol")
        if tuslar[pygame.K_RIGHT] or tuslar[pygame.K_d]:
            self.uzay_gemisi.hareket_et("sag")
        
        # Yeni meteor oluşturma
        params = self.seviye_bilgisi()
        self.meteor_timer += 1
        if self.meteor_timer >= params["spawn_araligi"]:
            self.meteor_olustur()
            self.meteor_timer = 0
        
        # Meteorları güncelle
        for meteor in self.meteorlar[:]:
            meteor.hareket_et()
            
            # Çarpışma kontrolü
            if self.uzay_gemisi.carpisma_kontrolu(meteor):
                self.durum = OYUN_KAYBETTI
                return
            
            # Meteor ekrandan çıktı mı?
            if meteor.ekrandan_cikti_mi():
                self.meteorlar.remove(meteor)
                self.skor += 1
    
    def ciz(self):
        """Oyunu ekrana çizer"""
        # Arka plan
        params = self.seviye_bilgisi()
        self.ekran.fill(params["arka_plan"])
        
        # Uzay gemisi
        self.uzay_gemisi.ciz(self.ekran)
        
        # Meteorlar
        for meteor in self.meteorlar:
            meteor.ciz(self.ekran)
        
        # Skor ve seviye
        skor_metni = self.font.render(f"Skor: {self.skor}", True, BEYAZ)
        seviye_metni = self.font.render(f"Seviye: {self.seviye}", True, BEYAZ)
        self.ekran.blit(skor_metni, (10, 10))
        self.ekran.blit(seviye_metni, (10, 50))
        
        # Oyun durumu mesajları
        if self.durum == OYUN_KAYBETTI:
            kaybetme_metni = self.font.render("Kaybettin! (R) Tuşuna basarak tekrar dene", 
                                              True, BEYAZ)
            metin_genislik = kaybetme_metni.get_width()
            metin_yukseklik = kaybetme_metni.get_height()
            self.ekran.blit(kaybetme_metni, 
                          (GENISLIK // 2 - metin_genislik // 2, 
                           YUKSEKLIK // 2 - metin_yukseklik // 2))
        
        elif self.durum == OYUN_KAZANDI:
            kazanma_metni = self.font.render("Tebrikler Kazandın!", True, BEYAZ)
            metin_genislik = kazanma_metni.get_width()
            metin_yukseklik = kazanma_metni.get_height()
            self.ekran.blit(kazanma_metni, 
                          (GENISLIK // 2 - metin_genislik // 2, 
                           YUKSEKLIK // 2 - metin_yukseklik // 2))
            
            devam_metni = self.kucuk_font.render("(R) Tuşuna basarak tekrar oyna", 
                                                 True, BEYAZ)
            devam_genislik = devam_metni.get_width()
            self.ekran.blit(devam_metni, 
                          (GENISLIK // 2 - devam_genislik // 2, 
                           YUKSEKLIK // 2 + 50))
        
        pygame.display.flip()
    
    def calistir(self):
        """Ana oyun döngüsü"""
        calisiyor = True
        
        while calisiyor:
            calisiyor = self.olaylari_isle()
            self.guncelle()
            self.ciz()
            self.saat.tick(FPS)
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    oyun = Oyun()
    oyun.calistir()

