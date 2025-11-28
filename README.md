# Kütüphane Yönetim Sistemi

Basit ve kullanışlı bir kitap yönetim programı. Python öğrenme sürecinde edinilen temel kavramları (sınıflar, fonksiyonlar, döngüler, koşullar) kullanarak geliştirilmiştir.

## Proje Hakkında

Bu proje, bir kütüphanedeki kitapların yönetimini sağlayan konsolda çalışan bir Python uygulamasıdır. Kullanıcılar kitap ekleyebilir, silebilir, arayabilir ve mevcut kitapları listeleyebilir.

## Özellikler

- **Kitap Ekleme**: Yeni kitapları ISBN, başlık, yazar ve yayın yılı bilgileriyle ekleyin
- **Kitap Silme**: ISBN numarasıyla kitapları kütüphaneden kaldırın
- **Kitap Arama**: Kitap adı veya yazar adına göre arama yapın
- **Listeleme**: Kütüphanedeki tüm kitapları görüntüleyin
- **ISBN Kontrolü**: Aynı ISBN'li kitabın tekrar eklenmesini önler
- **Kullanıcı Dostu Arayüz**: Anlaşılır menü ve mesajlar

## Teknik Detaylar

### Kullanılan Yapılar

**Sınıflar (Classes):**
- `Kitap`: Her bir kitabın bilgilerini tutar
- `Kutuphane`: Kütüphane işlemlerini yönetir

**Fonksiyonlar (Functions):**
- `kitap_ekle()`: Yeni kitap ekleme
- `kitap_sil()`: Kitap silme
- `kitap_ara()`: Kitap arama
- `tum_kitaplari_listele()`: Tüm kitapları görüntüleme
- `menu_goster()`: Menü gösterimi
- `main()`: Ana program döngüsü

**Özellikler:**
- OOP (Nesne Yönelimli Programlama) prensipleri
- Liste veri yapısı
- Döngüler (for, while)
- Koşul ifadeleri (if-elif-else)
- String işlemleri

## Kurulum ve Çalıştırma

### Gereksinimler
- Python 3.6 veya üzeri

### Çalıştırma
```bash
python kutuphane_yonetimi.py
```

## Kullanım

Program başlatıldığında ana menü görünür:

```
==================================================
📚 KÜTÜPHANE YÖNETİM SİSTEMİ
==================================================
1. Yeni Kitap Ekle
2. Kitap Sil
3. Kitap Ara
4. Tüm Kitapları Listele
5. Çıkış
==================================================
```

### Örnek Kullanım Senaryoları

#### 1. Yeni Kitap Ekleme
```
Seçiminiz (1-5): 1

--- Yeni Kitap Ekle ---
ISBN: 978-3
Başlık: 1984
Yazar: George Orwell
Yıl: 1949

✓ '1984' kütüphaneye eklendi.
```

#### 2. Kitap Arama
```
Seçiminiz (1-5): 3

Kitap adı veya yazar adı: orwell

🔍 'orwell' için 1 sonuç bulundu:
ISBN: 978-3 | Başlık: 1984 | Yazar: George Orwell | Yıl: 1949 | Durum: Mevcut
```

#### 3. Kitap Listeleme
```
Seçiminiz (1-5): 4

📚 Merkez Kütüphane - Toplam 3 kitap:
--------------------------------------------------------------------------------
ISBN: 978-1 | Başlık: Sefiller | Yazar: Victor Hugo | Yıl: 1862 | Durum: Mevcut
ISBN: 978-2 | Başlık: Suç ve Ceza | Yazar: Dostoyevski | Yıl: 1866 | Durum: Mevcut
ISBN: 978-3 | Başlık: 1984 | Yazar: George Orwell | Yıl: 1949 | Durum: Mevcut
```

## Kod Yapısı

```
kutuphane_yonetimi.py
│
├── Kitap (Class)
│   ├── __init__()           # Yapıcı method
│   └── bilgileri_goster()   # Kitap bilgilerini yazdırma
│
├── Kutuphane (Class)
│   ├── __init__()                # Yapıcı method
│   ├── kitap_ekle()              # Kitap ekleme fonksiyonu
│   ├── kitap_sil()               # Kitap silme fonksiyonu
│   ├── kitap_ara()               # Kitap arama fonksiyonu
│   └── tum_kitaplari_listele()   # Listeleme fonksiyonu
│
├── menu_goster()            # Menü gösterme fonksiyonu
└── main()                   # Ana program fonksiyonu
```

## Proje İstatistikleri

- **Toplam Satır Sayısı**: ~145 satır (yorumlarla birlikte)
- **Sınıf Sayısı**: 2
- **Fonksiyon Sayısı**: 6
- **Kod Satırı**: ~100 satır (yorumlar hariç)

## Güvenlik Özellikleri

- ISBN benzersizlik kontrolü
- Boş liste kontrolü
- Geçersiz giriş kontrolü
- Hata mesajları ve kullanıcı bilgilendirme

## Geliştirme Fikirleri

Bu projeyi geliştirmek için:
- Dosyaya kaydetme/yükleme özelliği eklenebilir
- Ödünç verme/iade sistemi geliştirilebilir
- Kitap kategorileri eklenebilir
- Veritabanı entegrasyonu yapılabilir
- GUI (Grafik Arayüz) eklenebilir

## Lisans

Bu proje eğitim amaçlı hazırlanmıştır ve özgürce kullanılabilir.

## İletişim

Sorularınız için GitHub Issues bölümünü kullanabilirsiniz.

---
**Not**: Bu proje, Python programlama dilinin temel özelliklerini öğrenmek ve uygulamak için hazırlanmış bir eğitim projesidir.
