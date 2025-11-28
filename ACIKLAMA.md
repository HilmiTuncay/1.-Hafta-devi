# Kütüphane Yönetim Sistemi - Detaylı Açıklama

## Projenin Genel Amacı ve İşleyişi

Bu proje, bir kütüphanedeki kitapları dijital ortamda yönetmek için tasarlanmış basit bir sistemdir. Kullanıcı programı açtığında, bir menü ile karşılaşır ve kitap ekleme, silme, arama ve listeleme işlemlerini gerçekleştirebilir.

### Kullanıcı Programı Açınca Hangi Adımları Takip Eder?

1. **Program Başlangıcı**:
   - Program çalıştırılır (kutuphane_yonetimi.py:145)
   - Otomatik olarak `main()` fonksiyonu çağrılır
   - "Merkez Kütüphane" adlı bir Kutuphane nesnesi oluşturulur (kutuphane_yonetimi.py:108)
   - Örnek olarak 2 kitap otomatik eklenir (kutuphane_yonetimi.py:111-112)

2. **Ana Menü Döngüsü**:
   - Kullanıcıya 5 seçenekli bir menü gösterilir (kutuphane_yonetimi.py:114)
   - Kullanıcının seçimi beklenir (kutuphane_yonetimi.py:115)

3. **İşlem Seçimi**:
   - Kullanıcı 1-5 arası bir sayı girer
   - Seçime göre ilgili kod bloğu çalışır (kutuphane_yonetimi.py:117-141)
   - İşlem tamamlandıktan sonra tekrar menüye dönülür (döngü)

4. **Program Sonlandırma**:
   - Kullanıcı "5" seçtiğinde `break` komutuyla döngü kırılır (kutuphane_yonetimi.py:139)
   - Program sonlanır

---

## Sınıflar Neden Böyle Tasarlandı?

### 1. Kitap Sınıfı (kutuphane_yonetimi.py:7-19)

```python
class Kitap:
    def __init__(self, isbn, baslik, yazar, yil):
        self.isbn = isbn
        self.baslik = baslik
        self.yazar = yazar
        self.yil = yil
        self.odunc_durumu = False
```

**Tasarım Kararları:**

- **Neden bir sınıf?**: Her kitap birden fazla bilgiye sahiptir (ISBN, başlık, yazar, yıl, ödünç durumu). Bu bilgileri bir arada tutmak için sınıf yapısı kullanıldı.

- **Attribute'lar (Özellikler)**:
  - `isbn`: Kitabın benzersiz kimlik numarası. Her kitabı diğerinden ayırmak için kullanılır
  - `baslik`: Kitabın adı
  - `yazar`: Kitabın yazarı
  - `yil`: Yayın yılı
  - `odunc_durumu`: Boolean (True/False) - Kitap ödünçte mi değil mi? (İleride genişletme için eklendi)

- **Method'lar**:
  - `__init__()`: Nesne oluşturulurken çalışır, kitap bilgilerini alır ve saklar
  - `bilgileri_goster()`: Kitap bilgilerini düzenli şekilde ekrana yazdırır

**Neden bu yapı seçildi?**
Gerçek hayatta bir kitap, fiziksel bir nesnedir ve özellikleri vardır. Bunu kodda temsil etmenin en mantıklı yolu bir sınıf oluşturmaktır. Bu sayede her kitap, kendi bilgilerini taşıyan bağımsız bir nesne haline gelir.

---

### 2. Kutuphane Sınıfı (kutuphane_yonetimi.py:22-79)

```python
class Kutuphane:
    def __init__(self, isim):
        self.isim = isim
        self.kitaplar = []
```

**Tasarım Kararları:**

- **Neden bir sınıf?**: Kütüphane, kitapları barındıran ve yöneten bir yapıdır. Tüm kitap işlemlerini (ekleme, silme, arama) bir arada toplamak için sınıf yapısı idealdir.

- **Attribute'lar**:
  - `isim`: Kütüphanenin adı (örn: "Merkez Kütüphane")
  - `kitaplar`: Boş bir liste - tüm Kitap nesnelerini bu listede saklarız

- **Method'lar**: Her method belirli bir işlevi yerine getirir (detaylı açıklama aşağıda)

**Neden bu yapı seçildi?**
Kütüphane, kitapları yöneten merkezi bir birimdir. Tüm kitap işlemlerini dağınık fonksiyonlar yerine bir sınıf içinde toplamak:
- Kodu daha organize eder
- İlgili işlemleri bir arada tutar
- Kütüphane bilgilerine (kitaplar listesi) kolay erişim sağlar

---

## Fonksiyonlar Hangi Amaçla Yazıldı?

### 1. kitap_ekle() Fonksiyonu (kutuphane_yonetimi.py:28-39)

```python
def kitap_ekle(self, kitap):
    for mevcut_kitap in self.kitaplar:
        if mevcut_kitap.isbn == kitap.isbn:
            print(f"❌ Hata: {kitap.isbn} ISBN'li kitap zaten mevcut!")
            return False

    self.kitaplar.append(kitap)
    print(f"✓ '{kitap.baslik}' kütüphaneye eklendi.")
    return True
```

**Amaç**: Kütüphaneye yeni kitap eklemek

**Nasıl Çalışır?**
1. Parametre olarak bir `Kitap` nesnesi alır
2. Mevcut kitaplar arasında aynı ISBN'li kitap var mı diye kontrol eder (döngü)
3. Eğer aynı ISBN varsa:
   - Hata mesajı yazdırır
   - `False` döner (ekleme başarısız)
4. Eğer yoksa:
   - Kitabı `self.kitaplar` listesine ekler (append)
   - Başarı mesajı yazdırır
   - `True` döner (ekleme başarılı)

**Neden bu kontrol?**
ISBN, kitabın benzersiz kimliğidir. Aynı ISBN'li iki kitap olamaz. Bu kontrol, veri bütünlüğünü sağlar.

---

### 2. kitap_sil() Fonksiyonu (kutuphane_yonetimi.py:41-51)

```python
def kitap_sil(self, isbn):
    for kitap in self.kitaplar:
        if kitap.isbn == isbn:
            self.kitaplar.remove(kitap)
            print(f"✓ '{kitap.baslik}' kütüphaneden silindi.")
            return True

    print(f"❌ {isbn} ISBN'li kitap bulunamadı.")
    return False
```

**Amaç**: ISBN numarasına göre kitap silmek

**Nasıl Çalışır?**
1. Parametre olarak bir `isbn` string'i alır
2. Kitaplar listesinde döngü ile arar
3. Eşleşen ISBN bulunursa:
   - `remove()` ile listeden çıkarır
   - Başarı mesajı yazdırır
   - `True` döner
4. Bulunamazsa:
   - Hata mesajı yazdırır
   - `False` döner

**Neden ISBN ile silme?**
ISBN benzersiz olduğu için, doğru kitabı sildiğimizden emin oluruz. Kitap adı ile silseydik, aynı isimli birden fazla kitap olabilirdi.

---

### 3. kitap_ara() Fonksiyonu (kutuphane_yonetimi.py:53-67)

```python
def kitap_ara(self, arama_terimi):
    bulunan_kitaplar = []
    arama_terimi = arama_terimi.lower()

    for kitap in self.kitaplar:
        if (arama_terimi in kitap.baslik.lower() or
            arama_terimi in kitap.yazar.lower()):
            bulunan_kitaplar.append(kitap)
```

**Amaç**: Kitap adı veya yazar adına göre arama yapmak

**Nasıl Çalışır?**
1. Arama terimi alınır ve küçük harfe çevrilir (`lower()`)
2. Boş bir `bulunan_kitaplar` listesi oluşturulur
3. Her kitap için kontrol edilir:
   - Başlıkta arama terimi var mı?
   - Yazar adında arama terimi var mı?
4. Eşleşme varsa kitap, bulunan listesine eklenir
5. Sonuçlar ekrana yazdırılır

**Neden `lower()` kullanıldı?**
Kullanıcı "orwell", "Orwell" veya "ORWELL" yazdığında da bulabilmek için büyük-küçük harf duyarlılığı kaldırıldı.

**Neden `in` operatörü?**
Tam eşleşme yerine kısmi eşleşme sağlar. Kullanıcı "Suç" yazdığında "Suç ve Ceza" kitabını bulabilir.

---

### 4. tum_kitaplari_listele() Fonksiyonu (kutuphane_yonetimi.py:69-79)

```python
def tum_kitaplari_listele(self):
    if not self.kitaplar:
        print("📚 Kütüphane boş.")
        return

    print(f"\n📚 {self.isim} - Toplam {len(self.kitaplar)} kitap:")
    print("-" * 80)
    for kitap in self.kitaplar:
        kitap.bilgileri_goster()
```

**Amaç**: Kütüphanedeki tüm kitapları listelemek

**Nasıl Çalışır?**
1. Önce liste boş mu diye kontrol eder (`if not self.kitaplar`)
2. Boşsa uyarı mesajı verir ve çıkar
3. Değilse:
   - Başlık yazdırır (kütüphane adı ve toplam kitap sayısı)
   - Ayırıcı çizgi yazdırır
   - Her kitap için `bilgileri_goster()` method'unu çağırır

**Neden boşluk kontrolü?**
Eğer hiç kitap yoksa, döngü çalışmaz ve ekran boş kalır. Bu kullanıcı deneyimi açısından kötüdür, o yüzden açıklayıcı mesaj verilir.

---

### 5. menu_goster() Fonksiyonu (kutuphane_yonetimi.py:82-92)

```python
def menu_goster():
    print("\n" + "="*50)
    print("📚 KÜTÜPHANE YÖNETİM SİSTEMİ")
    print("="*50)
    print("1. Yeni Kitap Ekle")
    # ... diğer seçenekler
```

**Amaç**: Kullanıcıya menüyü göstermek

**Neden ayrı bir fonksiyon?**
- Menü birden fazla kez gösterilecek (her işlemden sonra)
- Kodu tekrar yazmamak için fonksiyon haline getirildi (DRY prensibi - Don't Repeat Yourself)
- Değişiklik yapmak kolaylaşır (menüyü tek yerden değiştiririz)

---

### 6. main() Fonksiyonu (kutuphane_yonetimi.py:95-143)

```python
def main():
    kutuphane = Kutuphane("Merkez Kütüphane")

    kutuphane.kitap_ekle(Kitap("978-1", "Sefiller", "Victor Hugo", 1862))
    kutuphane.kitap_ekle(Kitap("978-2", "Suç ve Ceza", "Dostoyevski", 1866))

    while True:
        menu_goster()
        secim = input("\nSeçiminiz (1-5): ").strip()

        if secim == "1":
            # Kitap ekleme işlemi
        # ... diğer seçenekler
```

**Amaç**: Programın ana döngüsünü yönetmek

**Nasıl Çalışır?**
1. Kütüphane nesnesi oluşturulur
2. Örnek kitaplar eklenir (kullanıcının test etmesi için)
3. Sonsuz döngü başlar (`while True`)
4. Her döngüde:
   - Menü gösterilir
   - Kullanıcı seçimi alınır
   - `if-elif` yapısı ile seçime göre işlem yapılır
   - Seçim 5 ise `break` ile döngü kırılır

---

## Koşullar Nasıl Çalışıyor?

### 1. ISBN Kontrol Koşulu (kutuphane_yonetimi.py:30-32)

```python
if mevcut_kitap.isbn == kitap.isbn:
    print(f"❌ Hata: {kitap.isbn} ISBN'li kitap zaten mevcut!")
    return False
```

**Mantık**:
- Eğer döngüdeki kitabın ISBN'i, eklenmeye çalışılan kitabın ISBN'i ile aynıysa
- Hata mesajı yazdır ve fonksiyondan çık (ekleme yapma)

**Neden gerekli?**
Aynı kitaptan iki tane olmasını engeller, veri tutarlılığı sağlar.

---

### 2. Boş Liste Kontrolü (kutuphane_yonetimi.py:70-72)

```python
if not self.kitaplar:
    print("📚 Kütüphane boş.")
    return
```

**Mantık**:
- `not self.kitaplar` → liste boşsa True, doluysa False döner
- Boşsa mesaj yazdırılır ve fonksiyon sonlandırılır

**Neden gerekli?**
Boş bir liste üzerinde döngü çalıştırmak anlamsızdır. Kullanıcıya bilgilendirici mesaj vermek daha iyidir.

---

### 3. Arama Koşulu (kutuphane_yonetimi.py:58-59)

```python
if (arama_terimi in kitap.baslik.lower() or
    arama_terimi in kitap.yazar.lower()):
```

**Mantık**:
- `in` operatörü: arama terimi, string içinde geçiyor mu?
- `or`: İki koşuldan biri doğruysa True
- Başlıkta VEYA yazarda geçiyorsa kitap eklenir

**Neden `or` kullanıldı?**
Kullanıcı hem kitap adıyla hem de yazar adıyla arama yapabilsin diye. Örneğin "Dostoyevski" yazdığında tüm Dostoyevski kitapları bulunur.

---

### 4. Menü Seçim Koşulları (kutuphane_yonetimi.py:117-141)

```python
if secim == "1":
    # Kitap ekleme
elif secim == "2":
    # Kitap silme
elif secim == "3":
    # Kitap arama
elif secim == "4":
    # Listeleme
elif secim == "5":
    break
else:
    print("❌ Geçersiz seçim!")
```

**Mantık**:
- `if-elif-else` zinciri: Sadece bir blok çalışır
- Her seçim için ayrı kod bloğu
- Hiçbiri uymazsa `else` bloğu çalışır (hata mesajı)

**Neden `elif`?**
Birden fazla koşul arasından sadece birini seçmek için. `if-if-if` kullanılsaydı, tüm koşullar kontrol edilirdi (gereksiz).

---

## Programın Genel İşleyişi - Adım Adım Örnek

### Senaryo: Kullanıcı yeni bir kitap ekliyor

1. **Program başlar** → `main()` çağrılır (kutuphane_yonetimi.py:145)

2. **Kutuphane nesnesi oluşturulur** (kutuphane_yonetimi.py:108)
   ```python
   kutuphane = Kutuphane("Merkez Kütüphane")
   ```

3. **Örnek kitaplar eklenir** (kutuphane_yonetimi.py:111-112)

4. **Döngü başlar** (kutuphane_yonetimi.py:114)

5. **Menü gösterilir** → `menu_goster()` çağrılır

6. **Kullanıcı "1" girer** → Kitap ekleme bloğu çalışır (kutuphane_yonetimi.py:117-126)

7. **Bilgiler istenir**:
   ```
   ISBN: 978-3
   Başlık: 1984
   Yazar: George Orwell
   Yıl: 1949
   ```

8. **Yeni Kitap nesnesi oluşturulur** (kutuphane_yonetimi.py:124)
   ```python
   yeni_kitap = Kitap("978-3", "1984", "George Orwell", "1949")
   ```

9. **kitap_ekle() fonksiyonu çağrılır** (kutuphane_yonetimi.py:125)

10. **ISBN kontrolü yapılır** (kutuphane_yonetimi.py:30-32)
    - Mevcut kitaplar arasında "978-3" yok
    - Kontrol geçildi

11. **Kitap listeye eklenir** (kutuphane_yonetimi.py:34)
    ```python
    self.kitaplar.append(yeni_kitap)
    ```

12. **Başarı mesajı gösterilir** (kutuphane_yonetimi.py:35)

13. **Döngü devam eder** → Tekrar menü gösterilir

---

## Önemli Programlama Kavramları

### 1. Nesne Yönelimli Programlama (OOP)
- **Sınıflar**: Kitap ve Kutuphane şablonlarıdır
- **Nesneler**: Her kitap, Kitap sınıfından oluşturulmuş bir örnektir
- **Encapsulation**: Kitap bilgileri, Kitap sınıfı içinde saklanır

### 2. Liste Veri Yapısı
- `self.kitaplar = []`: Dinamik bir koleksiyon
- `append()`: Eleman ekleme
- `remove()`: Eleman çıkarma
- Döngü ile gezinme

### 3. String İşlemleri
- `lower()`: Küçük harfe çevirme
- `in`: Kısmi eşleşme kontrolü
- `f-string`: Formatted string (örn: `f"ISBN: {isbn}"`)
- `strip()`: Baş-sondaki boşlukları temizleme

### 4. Kontrol Akışı
- `if-elif-else`: Koşullu dallanma
- `for`: Liste üzerinde döngü
- `while True`: Sonsuz döngü
- `break`: Döngüden çıkış
- `return`: Fonksiyondan dönüş

### 5. Fonksiyon Tasarımı
- **Single Responsibility**: Her fonksiyon tek bir işi yapar
- **Return Values**: Başarı/başarısızlık durumunu döner (True/False)
- **Parameters**: Gerekli bilgileri parametre olarak alır

---

## Kod Kalitesi ve İyi Pratikler

1. **Anlamlı İsimler**: `kitap_ekle()`, `isbn`, `arama_terimi` gibi açıklayıcı isimler

2. **Yorum Satırları**: Her sınıf ve fonksiyon açıklanmış (kutuphane_yonetimi.py:1-3, 7-8, 22-23)

3. **Kullanıcı Dostu Mesajlar**: ✓ ve ❌ sembolleri ile görsel geri bildirim

4. **Hata Kontrolü**: Geçersiz girişler ve boş durumlar kontrol edilir

5. **DRY Prensibi**: Tekrarlanan kod (menü gösterimi) fonksiyona alınmış

6. **Modülerlik**: Her işlem ayrı bir fonksiyon

---

## Sonuç

Bu proje, Python'un temel yapılarını (sınıflar, fonksiyonlar, döngüler, koşullar, listeler) gerçek bir uygulama senaryosunda kullanarak öğrenmeyi hedefler.

Kütüphane yönetimi örneği seçildi çünkü:
- Gerçek hayat problemine çözüm sunar
- OOP kavramlarını öğretir (Kitap = nesne, Kutuphane = yönetici)
- CRUD işlemlerini (Create, Read, Update, Delete) içerir
- Veri yapıları ve algoritmalar pratiği sağlar
- Kullanıcı etkileşimi içerir

Her satır kod, belirli bir amaca hizmet eder ve programın genel mantığına katkıda bulunur.
