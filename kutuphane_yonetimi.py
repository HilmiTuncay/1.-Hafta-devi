"""
Kütüphane Yönetim Sistemi
Basit bir kitap yönetim programı
"""

class Kitap:
    """Kitap bilgilerini tutan sınıf"""

    def __init__(self, isbn, baslik, yazar, yil):
        self.isbn = isbn  # Kitabın benzersiz kimliği
        self.baslik = baslik  # Kitap adı
        self.yazar = yazar  # Yazar adı
        self.yil = yil  # Yayın yılı
        self.odunc_durumu = False  # Ödünç verildi mi?

    def bilgileri_goster(self):
        """Kitap bilgilerini ekrana yazdırır"""
        durum = "Ödünçte" if self.odunc_durumu else "Mevcut"
        print(f"ISBN: {self.isbn} | Başlık: {self.baslik} | Yazar: {self.yazar} | Yıl: {self.yil} | Durum: {durum}")


class Kutuphane:
    """Kütüphane işlemlerini yöneten sınıf"""

    def __init__(self, isim):
        self.isim = isim
        self.kitaplar = []  # Tüm kitapları tutan liste

    def kitap_ekle(self, kitap):
        """Kütüphaneye yeni kitap ekler"""
        # ISBN kontrolü - aynı ISBN'li kitap var mı?
        for mevcut_kitap in self.kitaplar:
            if mevcut_kitap.isbn == kitap.isbn:
                print(f"❌ Hata: {kitap.isbn} ISBN'li kitap zaten mevcut!")
                return False

        self.kitaplar.append(kitap)
        print(f"✓ '{kitap.baslik}' kütüphaneye eklendi.")
        return True

    def kitap_sil(self, isbn):
        """ISBN numarasına göre kitap siler"""
        for kitap in self.kitaplar:
            if kitap.isbn == isbn:
                self.kitaplar.remove(kitap)
                print(f"✓ '{kitap.baslik}' kütüphaneden silindi.")
                return True

        print(f"❌ {isbn} ISBN'li kitap bulunamadı.")
        return False

    def kitap_ara(self, arama_terimi):
        """Kitap adı veya yazara göre arama yapar"""
        bulunan_kitaplar = []
        arama_terimi = arama_terimi.lower()

        for kitap in self.kitaplar:
            if (arama_terimi in kitap.baslik.lower() or
                arama_terimi in kitap.yazar.lower()):
                bulunan_kitaplar.append(kitap)

        if bulunan_kitaplar:
            print(f"\n🔍 '{arama_terimi}' için {len(bulunan_kitaplar)} sonuç bulundu:")
            for kitap in bulunan_kitaplar:
                kitap.bilgileri_goster()
        else:
            print(f"❌ '{arama_terimi}' için sonuç bulunamadı.")

        return bulunan_kitaplar

    def tum_kitaplari_listele(self):
        """Kütüphanedeki tüm kitapları listeler"""
        if not self.kitaplar:
            print("📚 Kütüphane boş.")
            return

        print(f"\n📚 {self.isim} - Toplam {len(self.kitaplar)} kitap:")
        print("-" * 80)
        for kitap in self.kitaplar:
            kitap.bilgileri_goster()


def menu_goster():
    """Ana menüyü ekrana yazdırır"""
    print("\n" + "="*50)
    print("📚 KÜTÜPHANE YÖNETİM SİSTEMİ")
    print("="*50)
    print("1. Yeni Kitap Ekle")
    print("2. Kitap Sil")
    print("3. Kitap Ara")
    print("4. Tüm Kitapları Listele")
    print("5. Çıkış")
    print("="*50)


def main():
    """Ana program fonksiyonu"""
    kutuphane = Kutuphane("Merkez Kütüphane")

    # Örnek kitaplar ekle
    kutuphane.kitap_ekle(Kitap("978-1", "Sefiller", "Victor Hugo", 1862))
    kutuphane.kitap_ekle(Kitap("978-2", "Suç ve Ceza", "Dostoyevski", 1866))

    while True:
        menu_goster()
        secim = input("\nSeçiminiz (1-5): ").strip()

        if secim == "1":
            # Kitap ekleme
            print("\n--- Yeni Kitap Ekle ---")
            isbn = input("ISBN: ")
            baslik = input("Başlık: ")
            yazar = input("Yazar: ")
            yil = input("Yıl: ")

            yeni_kitap = Kitap(isbn, baslik, yazar, yil)
            kutuphane.kitap_ekle(yeni_kitap)

        elif secim == "2":
            # Kitap silme
            isbn = input("\nSilinecek kitabın ISBN numarası: ")
            kutuphane.kitap_sil(isbn)

        elif secim == "3":
            # Kitap arama
            arama = input("\nKitap adı veya yazar adı: ")
            kutuphane.kitap_ara(arama)

        elif secim == "4":
            # Tüm kitapları listele
            kutuphane.tum_kitaplari_listele()

        elif secim == "5":
            print("\n👋 Programdan çıkılıyor...")
            break

        else:
            print("❌ Geçersiz seçim! Lütfen 1-5 arası bir sayı girin.")


if __name__ == "__main__":
    main()
