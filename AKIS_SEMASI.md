# Kütüphane Yönetim Sistemi - Akış Şeması

## Ana Program Akışı

```
         [BAŞLA]
            ↓
    Kutuphane Oluştur
            ↓
    Örnek Kitaplar Ekle
            ↓
      ┌─────────┐
      │ Menüyü  │◄────────┐
      │ Göster  │         │
      └────┬────┘         │
           ↓              │
    Kullanıcı Seçim       │
           ↓              │
       ╱Seçim?╲           │
      ╱         ╲         │
     ◇───────────◇       │
     │           │        │
  1-4│          │5        │
     │           │        │
  İşlem        Çıkış      │
  Yap           ↓         │ 
     │        [BİTİR]     │
     │                    │
     └───────────────────-┘
```

## Kitap Ekleme İşlemi

```
    [Kitap Ekle]
         ↓
  Bilgileri Al
  (ID, Başlık, Yazar, Yıl)
         ↓
    Kitap Oluştur
         ↓
    ╱ID Var mı?╲
   ╱            ╲
  ◇──────────────◇
  │Evet      Hayır│
  ↓              ↓
Hata Mesajı  Listeye Ekle
  ↓              ↓
Return      Başarı Mesajı
```

## Kitap Silme İşlemi

```
    [Kitap Sil]
         ↓
  ID Numarası Al
         ↓
   ┌─────────────┐
   │ Kitaplar    │
   │ Arasında Ara│
   └──────┬──────┘
          ↓
    ╱Bulundu mu?╲
   ╱             ╲
  ◇───────────────◇
  │Evet       Hayır│
  ↓               ↓
Sil          Hata Mesajı
  ↓
Başarı Mesajı
```

## Kitap Arama İşlemi

```
    [Kitap Ara]
         ↓
  Arama Terimi Al
         ↓
  Küçük Harfe Çevir
         ↓
   ┌─────────────┐
   │ Her Kitap   │
   │ için Kontrol│
   └──────┬──────┘
          ↓
    ╱Eşleşiyor?╲
   ╱            ╲
  ◇──────────────◇
  │Evet      Hayır│
  ↓              ↓
Listeye Ekle   Atla
  │              │
  └──────┬───────┘
         ↓
   ╱Liste Boş?╲
  ╱            ╲
 ◇──────────────◇
 │Evet      Hayır│
 ↓              ↓
Hata       Sonuçları
Mesajı     Göster
```

## Listeleme İşlemi

```
    [Listele]
         ↓
    ╱Liste Boş?╲
   ╱            ╲
  ◇──────────────◇
  │Evet      Hayır│
  ↓              ↓
"Boş"       Her Kitap İçin
Mesajı      Bilgileri Göster
```

## Simgeler

- `[  ]` - Başlangıç/Bitiş
- `┌──┐` - İşlem
- `◇` - Karar
- `↓` - Akış yönü
- `╱╲` - Karar kutusu
