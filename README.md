# 2025-2026-Guz-BL271-Yonlendirilmis-Calisma
Bu proje, eğitim ortamlarında enerji verimliliğini artırmak, gereksiz enerji tüketimini önlemek ve kullanıcı
konforunu geliştirmek amacıyla geliştirilecek bir akıllı aydınlatma sistemi tasarımını konu almaktadır.
Günümüzde birçok okul, sınıf ve ofis ortamında aydınlatma sistemleri manuel olarak kontrol edilmekte, bu da
çoğu zaman ışıkların açık unutulmasına ve enerji israfına neden olmaktadır. Bu proje kapsamında geliştirilecek
sistem, sınıfa giren ve çıkan kişileri sensörler aracılığıyla tespit ederek aydınlatmayı otomatik biçimde
yönetecektir. İlk kişi sınıfa girdiğinde ışıklar otomatik olarak yanacak, son kişi çıktığında ise sistem ışıkları
kapatarak enerji tasarrufu sağlayacaktır. Böylece hem enerji verimliliği artırılacak hem de sürdürülebilir çevre
hedeflerine katkı sağlanacaktır.
Proje donanım ve yazılım açısından bütünleşik bir yapıya sahip olacaktır. Donanım bileşenleri arasında
Arduino Uno mikrodenetleyici kartı, HC-SR04 ultrasonik sensörler, röle modülleri, LED lambalar,
breadboard, güç kaynağı ve Wattmetre yer alacaktır. Sensörlerden gelen veriler Arduino tarafından
işlenecek, kişi giriş-çıkış yönleri tespit edilerek kişi sayısı belirlenecektir. Kişi sayısı bir veya daha fazla
olduğunda röle modülü aktif hale gelerek ışıklar açılacak, sayı sıfıra düştüğünde ışıklar kapatılacaktır. Sistem,
gerçek zamanlı ölçümlerle test edilerek enerji tasarrufu oranı Wattmetre yardımıyla hesaplanacaktır.
Proje aynı zamanda yazılım algoritmasının optimizasyonuna odaklanacaktır. Kişi sayımında yanlış algılama
oranını minimize etmek için debounce filtreleme, EEPROM veri kaydı, seri port izleme ve paralel sensör
koordinasyonu teknikleri kullanılacaktır. Böylece sistem, farklı ışık koşullarında, farklı yönlerden giriş ve
çıkışlarda kararlılığını koruyacaktır.
Literatürde hareket algılama tabanlı aydınlatma sistemleri yaygın olarak incelenmiş olsa da, kişi sayımına
dayalı enerji yönetim sistemleri sınırlı sayıdadır. Bu çalışma, bu boşluğu doldurmayı hedeflemekte ve düşük
maliyetli, açık kaynaklı, yüksek doğruluk oranına sahip bir enerji yönetim sistemi önermektedir. Ayrıca proje
çıktıları, gelecekte akıllı şehir altyapılarıyla uyumlu hale getirilerek kamu binaları, okullar ve ofislerde
kullanılabilir düzeyde olacaktır.
Proje, 12. Kalkınma Planı (2024-2028) ve 2030 Sanayi ve Teknoloji Stratejisi’nde vurgulanan “yeşil
dönüşüm, dijitalleşme ve enerji verimliliği” hedefleriyle tam uyum içindedir. Bu sistem, çevresel
sürdürülebilirliğe katkı sağlayacağı gibi, enerji maliyetlerini düşürerek ekonomik fayda da oluşturacaktır.
