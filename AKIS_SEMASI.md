# Kütüphane Yönetim Sistemi - Akış Şeması

```
                            ┌─────────────────────┐
                            │   PROGRAM BAŞLAT    │
                            └──────────┬──────────┘
                                       │
                                       ▼
                            ┌─────────────────────┐
                            │  Kutuphane Nesnesi  │
                            │    Oluştur          │
                            └──────────┬──────────┘
                                       │
                                       ▼
                            ┌─────────────────────┐
                            │  Örnek Kitapları    │
                            │      Ekle           │
                            └──────────┬──────────┘
                                       │
                    ┌──────────────────┴──────────────────┐
                    │                                      │
                    ▼                                      │
         ┌─────────────────────┐                          │
         │   MENÜYÜ GÖSTER     │ ◄────────────────────────┘
         │                     │
         │  1. Kitap Ekle      │
         │  2. Kitap Sil       │
         │  3. Kitap Ara       │
         │  4. Listele         │
         │  5. Çıkış           │
         └──────────┬──────────┘
                    │
                    ▼
         ┌─────────────────────┐
         │  Kullanıcı Seçimi   │
         │     Bekle (1-5)     │
         └──────────┬──────────┘
                    │
        ┌───────────┼───────────┬───────────┬───────────┐
        │           │           │           │           │
        ▼           ▼           ▼           ▼           ▼
    ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐
    │SEÇİM=1│  │SEÇİM=2│  │SEÇİM=3│  │SEÇİM=4│  │SEÇİM=5│
    └───┬───┘  └───┬───┘  └───┬───┘  └───┬───┘  └───┬───┘
        │          │          │          │          │
        ▼          ▼          ▼          ▼          ▼
    ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
    │ EKLE   │ │  SİL   │ │  ARA   │ │LİSTELE │ │ ÇIKIŞ  │
    └───┬────┘ └───┬────┘ └───┬────┘ └───┬────┘ └───┬────┘
        │          │          │          │          │
        ▼          ▼          ▼          ▼          ▼
    ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐
    │ISBN, Başlık,    │  │  ISBN Numarası  │  │  Program    │
    │Yazar, Yıl Gir   │  │     İste        │  │   Sonlan    │
    └────┬────────────┘  └────┬────────────┘  └─────────────┘
         │                    │
         ▼                    ▼
    ┌─────────────────┐  ┌─────────────────┐
    │ Kitap Nesnesi   │  │  ISBN ile Kitap │
    │    Oluştur      │  │      Bul        │
    └────┬────────────┘  └────┬────────────┘
         │                    │
         ▼                    ▼
    ┌─────────────────┐  ┌─────────────────┐
    │  ISBN Mevcut    │  │  Kitap Bulundu? │
    │     mu?         │  │                 │
    └────┬────────────┘  └────┬────────────┘
         │                    │
    ┌────┴────┐          ┌────┴────┐
    │         │          │         │
   EVET      HAYIR      EVET      HAYIR
    │         │          │         │
    ▼         ▼          ▼         ▼
 ┌──────┐ ┌──────┐   ┌──────┐ ┌──────┐
 │HATA  │ │EKLE  │   │SİL   │ │HATA  │
 │MESAJI│ │BAŞARI│   │BAŞARI│ │MESAJI│
 └──┬───┘ └──┬───┘   └──┬───┘ └──┬───┘
    │        │           │        │
    └────────┴───────────┴────────┘
             │
             ▼
    ┌─────────────────┐
    │  MENÜYE DÖN     │
    └─────────────────┘
             │
             └──────────────► (Döngü Devam)


## DETAYLI İŞLEM AKIŞLARI

### 1. KİTAP EKLEME İŞLEMİ
┌─────────────────────────────────────┐
│ Kullanıcıdan bilgileri al:          │
│ - ISBN (benzersiz kimlik)           │
│ - Başlık                            │
│ - Yazar                             │
│ - Yayın Yılı                        │
└──────────┬──────────────────────────┘
           ▼
┌─────────────────────────────────────┐
│ Yeni Kitap nesnesi oluştur          │
└──────────┬──────────────────────────┘
           ▼
┌─────────────────────────────────────┐
│ kitap_ekle() fonksiyonu çağır       │
└──────────┬──────────────────────────┘
           ▼
┌─────────────────────────────────────┐
│ Mevcut kitapları döngüyle kontrol   │
│ ISBN eşleşmesi var mı?              │
└──────────┬──────────────────────────┘
           │
      ┌────┴────┐
      ▼         ▼
    EVET      HAYIR
      │         │
      ▼         ▼
  [HATA]    [EKLE]
  Return    Listeye Ekle
  False     Return True


### 2. KİTAP SİLME İŞLEMİ
┌─────────────────────────────────────┐
│ Kullanıcıdan ISBN al               │
└──────────┬──────────────────────────┘
           ▼
┌─────────────────────────────────────┐
│ kitap_sil(isbn) fonksiyonu çağır    │
└──────────┬──────────────────────────┘
           ▼
┌─────────────────────────────────────┐
│ Kitaplar listesinde döngü           │
│ ISBN eşleşmesi ara                  │
└──────────┬──────────────────────────┘
           │
      ┌────┴────┐
      ▼         ▼
   BULUNDU   BULUNAMADI
      │         │
      ▼         ▼
  [SİL]      [HATA]
  Listeden   Return
  Çıkar      False
  Return
  True


### 3. KİTAP ARAMA İŞLEMİ
┌─────────────────────────────────────┐
│ Kullanıcıdan arama terimi al        │
└──────────┬──────────────────────────┘
           ▼
┌─────────────────────────────────────┐
│ kitap_ara(terim) fonksiyonu çağır   │
└──────────┬──────────────────────────┘
           ▼
┌─────────────────────────────────────┐
│ Arama terimini küçük harfe çevir    │
└──────────┬──────────────────────────┘
           ▼
┌─────────────────────────────────────┐
│ Her kitap için:                     │
│ - Başlıkta terim var mı?            │
│ - Yazarda terim var mı?             │
└──────────┬──────────────────────────┘
           ▼
┌─────────────────────────────────────┐
│ Eşleşen kitapları listeye ekle      │
└──────────┬──────────────────────────┘
           │
      ┌────┴────┐
      ▼         ▼
   BULUNDU   BOŞ LİSTE
      │         │
      ▼         ▼
  [GÖSTER]  [HATA MESAJI]
  Sonuçları "Sonuç bulunamadı"
  Yazdır


### 4. LİSTELEME İŞLEMİ
┌─────────────────────────────────────┐
│ tum_kitaplari_listele() çağır       │
└──────────┬──────────────────────────┘
           ▼
┌─────────────────────────────────────┐
│ Kitaplar listesi boş mu?            │
└──────────┬──────────────────────────┘
           │
      ┌────┴────┐
      ▼         ▼
    BOŞ       DOLU
      │         │
      ▼         ▼
  [MESAJ]   [LİSTELE]
  "Kütüphane Her kitap için
   boş"      bilgileri_goster()
             çağır
```

## Akış Şeması Açıklaması

Bu akış şeması, kütüphane yönetim sisteminin çalışma mantığını görselleştirir:

1. **Başlangıç**: Program başlatılır ve Kutuphane nesnesi oluşturulur
2. **Ana Döngü**: Menü gösterilir ve kullanıcı seçimi beklenir
3. **İşlem Dağıtımı**: Seçime göre ilgili fonksiyon çalıştırılır
4. **Doğrulama**: Her işlemde veri kontrolü yapılır (ISBN kontrolü, varlık kontrolü)
5. **Geri Dönüş**: İşlem sonrası tekrar menüye dönülür
6. **Sonlandırma**: Kullanıcı 5'i seçtiğinde program sonlanır
