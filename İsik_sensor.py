const int TRIG_1 = 4;
const int ECHO_1 = 5;
const int TRIG_2 = 6;
const int ECHO_2 = 7;
const int ROLE_PIN = 13;

int iceridekiKisi = 0;
const int mesafeSiniri = 100; // 100 cm sınırınız

// Geçiş durumlarını kontrol eden değişkenler
int durum = 0; // 0: Beklemede, 1: Giriş Sürecinde, 2: Çıkış Sürecinde
unsigned long sonIslemZamani = 0;
const int zamanAsimi = 2500; // 2.5 saniye içinde geçiş bitmeli

long mesafeOlc(int trig, int echo) {
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  
  // pulseIn süresini kısıtlayarak sensörün takılmasını önlüyoruz (yaklaşık 1.5 metreye ayarlı)
  long sure = pulseIn(echo, HIGH, 10000); 
  if (sure == 0) return 999; // Engel yoksa yüksek değer döndür
  return sure * 0.034 / 2;
}

void setup() {
  pinMode(TRIG_1, OUTPUT); pinMode(ECHO_1, INPUT);
  pinMode(TRIG_2, OUTPUT); pinMode(ECHO_2, INPUT);
  pinMode(ROLE_PIN, OUTPUT);
  
  digitalWrite(ROLE_PIN, HIGH); // Başlangıçta kapalı
  Serial.begin(9600);
  Serial.println("--- Akilli Sayac Baslatildi ---");
}

void loop() {
  // Sensörler arası paraziti önlemek için çok kısa bir farkla oku
  long d1 = mesafeOlc(TRIG_1, ECHO_1);
  delay(30); 
  long d2 = mesafeOlc(TRIG_2, ECHO_2);

  // DURUM 0: BEKLEME - Hangi yöne gidileceği belirleniyor
  if (durum == 0) {
    if (d1 < mesafeSiniri && d1 > 2) { // Önce SOL tetiklendi -> GİRİŞ
      durum = 1; 
      sonIslemZamani = millis();
      Serial.println("Islem: Giris basladi...");
    } 
    else if (d2 < mesafeSiniri && d2 > 2) { // Önce SAĞ tetiklendi -> ÇIKIŞ
      durum = 2; 
      sonIslemZamani = millis();
      Serial.println("Islem: Cikis basladi...");
    }
  }

  // DURUM 1: GİRİŞ SÜRECİ - Sol tetiklenmişti, şimdi Sağ'ın tetiklenmesini bekliyoruz
  else if (durum == 1) {
    if (d2 < mesafeSiniri && d2 > 2) {
      iceridekiKisi++;
      Serial.println(">>> GIRIS TAMAMLANDI. Icerideki: " + String(iceridekiKisi));
      gecisBitisiniBekle(TRIG_2, ECHO_2); // Kişi tamamen geçene kadar sistemi kilitler
    }
  }

  // DURUM 2: ÇIKIŞ SÜRECİ - Sağ tetiklenmişti, şimdi Sol'un tetiklenmesini bekliyoruz
  else if (durum == 2) {
    if (d1 < mesafeSiniri && d1 > 2) {
      if (iceridekiKisi > 0) iceridekiKisi--;
      Serial.println("<<< CIKIS TAMAMLANDI. Icerideki: " + String(iceridekiKisi));
      gecisBitisiniBekle(TRIG_1, ECHO_1); // Kişi tamamen geçene kadar sistemi kilitler
    }
  }

  // ZAMAN AŞIMI KONTROLÜ
  // Eğer kişi sensörün önünde durur veya vazgeçip geri dönerse sistemi sıfırla
  if (durum != 0 && (millis() - sonIslemZamani > zamanAsimi)) {
    durum = 0;
    Serial.println("Hata: Gecis tamamlanamadi, sifirlandi.");
  }

  // RÖLE KONTROLÜ (İçeride en az 1 kişi varsa röleyi çek)
  digitalWrite(ROLE_PIN, (iceridekiKisi > 0) ? LOW : HIGH);
}

// ÇİFT TETİKLEMEYİ ÖNLEYEN ANA FONKSİYON
void gecisBitisiniBekle(int hedefTrig, int hedefEcho) {
  int bosOkumaSayisi = 0;
  unsigned long emniyetZamani = millis();

  // Kişi sensörün önünden çekilene kadar (üst üste 5 temiz okuma gelene kadar) bekle
  while (bosOkumaSayisi < 5 && (millis() - emniyetZamani < 3000)) {
    long mesafe = mesafeOlc(hedefTrig, hedefEcho);
    if (mesafe > mesafeSiniri || mesafe == 0) {
      bosOkumaSayisi++;
    } else {
      bosOkumaSayisi = 0; // Eğer hala bir engel varsa sayacı sıfırla
    }
    delay(40);
  }

  // Sizin istediğiniz 0.2 saniyelik "tam durma" süresi
  delay(200); 
  durum = 0; // Yeni geçiş için sistemi hazır hale getir
  Serial.println("Sistem yeni kisiye hazir.");
}
