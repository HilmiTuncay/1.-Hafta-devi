# Kütüphane Yönetim Sistemi

Python ile geliştirilmiş basit kitap yönetim programı.

## Özellikler

- Kitap ekleme, silme, arama ve listeleme
- ID kontrolü
- Kullanıcı dostu menü sistemi

## Çalıştırma

```bash
python kutuphane_yonetimi.py
```

## Proje Yapısı

### Sınıflar (2 adet)
- **Kitap**: Kitap bilgilerini tutar
- **Kutuphane**: Kütüphane işlemlerini yönetir

### Fonksiyonlar (4+ adet)
- `kitap_ekle()` - Yeni kitap ekler
- `kitap_sil()` - Kitap siler
- `kitap_ara()` - Kitap arar
- `tum_kitaplari_listele()` - Tüm kitapları gösterir

## Clean Code Prensipleri

### 1. Anlamlı İsimlendirme
```python
# İyi örnek
class Kutuphane:
    def kitap_ekle(self, kitap):

# Değişkenler ne yaptığını açıkça belirtiyor
```

### 2. Tek Sorumluluk
Her sınıf ve fonksiyon tek bir işten sorumlu:
- `Kitap` sınıfı sadece kitap bilgilerini tutar
- `Kutuphane` sınıfı sadece kütüphane işlemlerini yönetir
- Her fonksiyon tek bir işlem yapar (ekle, sil, ara, listele)

### 3. DRY Prensibi (Don't Repeat Yourself)
Tekrar eden kodlar fonksiyonlara alındı:
- `bilgileri_goster()` - Kitap bilgilerini göstermek için
- `menu_goster()` - Menüyü göstermek için

### 4. Koşullu Yapılar
```python
# ID kontrolü
if mevcut_kitap.id == kitap.id:
    return False

# Arama kontrolü
if arama_terimi in kitap.baslik.lower():
    bulunan_kitaplar.append(kitap)
```

### 5. Döngüler
```python
# Her kitap için kontrol
for kitap in self.kitaplar:
    kitap.bilgileri_goster()
```

## Program Mantığı

1. **Başlangıç**: Kutuphane nesnesi oluşturulur
2. **Döngü**: Kullanıcı menüden seçim yapar
3. **İşlem**: Seçime göre ilgili fonksiyon çalışır
4. **Kontrol**: Veri doğrulaması yapılır (ID kontrolü vb.)
5. **Çıktı**: Kullanıcıya sonuç gösterilir
6. **Tekrar**: Menüye geri dönülür (çıkış seçilene kadar)

## Algoritmik Düşünme

- **Girdi**: ID, başlık, yazar, yıl
- **İşlem**: Ekleme, silme, arama, listeleme
- **Çıktı**: Başarı/hata mesajları, kitap listesi

Detaylı algoritma için: [ALGORITMA.md](ALGORITMA.md)

Akış şeması için: [AKIS_SEMASI.md](AKIS_SEMASI.md)

## Kod İstatistikleri

- Satır: ~140
- Sınıf: 2
- Fonksiyon: 6
- Koşullu yapı: Var (if-elif-else)
- Döngü: Var (for, while)

---

Eğitim amaçlı proje - Özgürce kullanılabilir
