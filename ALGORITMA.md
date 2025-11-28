# Kütüphane Yönetim Sistemi - Algoritma

## Problem Tanımı
Kütüphanedeki kitapları eklemek, silmek, aramak ve listelemek için bir sistem gerekiyor.

## Algoritma

### Ana Program
```
1. BAŞLA
2. Kutuphane nesnesi oluştur
3. Örnek kitaplar ekle
4. DÖNGÜ (kullanıcı çıkış yapana kadar)
   4.1. Menüyü göster
   4.2. Kullanıcıdan seçim al
   4.3. EĞER seçim = 1 İSE
        - Kitap bilgilerini al
        - Kitap ekle
   4.4. EĞER seçim = 2 İSE
        - ISBN al
        - Kitabı sil
   4.5. EĞER seçim = 3 İSE
        - Arama terimi al
        - Kitap ara
   4.6. EĞER seçim = 4 İSE
        - Tüm kitapları listele
   4.7. EĞER seçim = 5 İSE
        - Döngüden çık
5. BİTİR
```

### Kitap Ekleme Algoritması
```
1. Kullanıcıdan ISBN, başlık, yazar, yıl bilgilerini al
2. Yeni Kitap nesnesi oluştur
3. HER kitap İÇİN kütüphanede
   3.1. EĞER ISBN zaten varsa
        - Hata mesajı göster
        - Fonksiyonu sonlandır
4. Kitabı listeye ekle
5. Başarı mesajı göster
```

### Kitap Arama Algoritması
```
1. Kullanıcıdan arama terimini al
2. Arama terimini küçük harfe çevir
3. Boş sonuç listesi oluştur
4. HER kitap İÇİN kütüphanede
   4.1. EĞER arama terimi kitap başlığında VEYA yazar adında varsa
        - Kitabı sonuç listesine ekle
5. EĞER sonuç listesi boş değilse
   5.1. Bulunan kitapları göster
   DEĞILSE
   5.2. "Sonuç bulunamadı" mesajı göster
```

## Girdiler
- ISBN numarası
- Kitap başlığı
- Yazar adı
- Yayın yılı
- Menü seçimi
- Arama terimi

## İşlemler
- Kitap ekleme
- Kitap silme
- Kitap arama
- Listeleme

## Çıktılar
- Kitap listesi
- Arama sonuçları
- Başarı/hata mesajları
