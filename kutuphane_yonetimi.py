"""
Kütüphane Yönetim Sistemi
CSV dosyası veritabanı ile çalışan basit kitap yönetim programı
"""

import csv
import os

# Veritabanı dosyası
CSV_DOSYA = "kitaplar.csv"


class Kitap:
    """Kitap bilgilerini tutan sınıf"""

    def __init__(self, id, baslik, yazar, yil):
        self.id = id
        self.baslik = baslik
        self.yazar = yazar
        self.yil = yil

    def bilgileri_goster(self):
        """Kitap bilgilerini ekrana yazdırır"""
        print(f"ID: {self.id} | Baslik: {self.baslik} | Yazar: {self.yazar} | Yil: {self.yil}")


# ============ CSV VERİTABANI FONKSİYONLARI ============

def csv_olustur():
    """CSV dosyası yoksa oluştur"""
    if not os.path.exists(CSV_DOSYA):
        with open(CSV_DOSYA, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['ID', 'Baslik', 'Yazar', 'Yil'])
            writer.writeheader()
        print(f"[BILGI] Yeni veritabani olusturuldu: {CSV_DOSYA}")


def csv_kitap_ekle(kitap):
    """Kitabı CSV dosyasına ekle"""
    # Önce ID kontrolü yap
    if csv_id_varmi(kitap.id):
        print(f"[HATA] {kitap.id} ID'li kitap zaten mevcut!")
        return False

    # CSV'ye ekle
    with open(CSV_DOSYA, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['ID', 'Baslik', 'Yazar', 'Yil'])
        writer.writerow({
            'ID': kitap.id,
            'Baslik': kitap.baslik,
            'Yazar': kitap.yazar,
            'Yil': kitap.yil
        })

    print(f"[OK] '{kitap.baslik}' eklendi.")
    return True


def csv_kitap_sil(id):
    """Kitabı CSV dosyasından sil"""
    kitaplar = csv_tum_kitaplari_oku()

    # Silinecek kitabı bul
    yeni_liste = []
    silindi = False

    for kitap in kitaplar:
        if kitap.id == id:
            silindi = True
            print(f"[OK] '{kitap.baslik}' silindi.")
        else:
            yeni_liste.append(kitap)

    if not silindi:
        print(f"[HATA] {id} ID'li kitap bulunamadi.")
        return False

    # CSV'yi yeniden yaz
    with open(CSV_DOSYA, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['ID', 'Baslik', 'Yazar', 'Yil'])
        writer.writeheader()
        for kitap in yeni_liste:
            writer.writerow({
                'ID': kitap.id,
                'Baslik': kitap.baslik,
                'Yazar': kitap.yazar,
                'Yil': kitap.yil
            })

    return True


def csv_tum_kitaplari_oku():
    """CSV'den tüm kitapları oku ve liste döndür"""
    kitaplar = []

    if not os.path.exists(CSV_DOSYA):
        return kitaplar

    with open(CSV_DOSYA, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            kitap = Kitap(row['ID'], row['Baslik'], row['Yazar'], row['Yil'])
            kitaplar.append(kitap)

    return kitaplar


def csv_id_varmi(id):
    """ID kontrolü - CSV'de bu ID var mı?"""
    kitaplar = csv_tum_kitaplari_oku()
    for kitap in kitaplar:
        if kitap.id == id:
            return True
    return False


def csv_kitap_ara(arama_terimi):
    """CSV'den kitap ara (başlık veya yazar)"""
    kitaplar = csv_tum_kitaplari_oku()
    bulunan = []

    arama_terimi = arama_terimi.lower()

    for kitap in kitaplar:
        if (arama_terimi in kitap.baslik.lower() or
            arama_terimi in kitap.yazar.lower()):
            bulunan.append(kitap)

    return bulunan


# ============ MENÜ VE ANA PROGRAM ============

def menu_goster():
    """Ana menüyü göster"""
    print("\n" + "="*50)
    print("KUTUPHANE YONETIM SISTEMI")
    print("="*50)
    print("1. Yeni Kitap Ekle")
    print("2. Kitap Sil")
    print("3. Kitap Ara")
    print("4. Tum Kitaplari Listele")
    print("5. Cikis")
    print("="*50)


def main():
    """Ana program"""
    # CSV dosyasını oluştur (yoksa)
    csv_olustur()

    # Eğer veritabanı boşsa örnek kitaplar ekle
    kitaplar = csv_tum_kitaplari_oku()
    if len(kitaplar) == 0:
        print("[BILGI] Veritabani bos. Ornek kitaplar ekleniyor...")
        csv_kitap_ekle(Kitap("978-1", "Sefiller", "Victor Hugo", "1862"))
        csv_kitap_ekle(Kitap("978-2", "Suc ve Ceza", "Dostoyevski", "1866"))

    # Ana döngü
    while True:
        menu_goster()
        secim = input("\nSeciminiz (1-5): ").strip()

        if secim == "1":
            # Kitap Ekle
            print("\n--- Yeni Kitap Ekle ---")
            id = input("ID: ").strip()
            baslik = input("Baslik: ").strip()
            yazar = input("Yazar: ").strip()
            yil = input("Yil: ").strip()

            if id and baslik and yazar and yil:
                yeni_kitap = Kitap(id, baslik, yazar, yil)
                csv_kitap_ekle(yeni_kitap)
            else:
                print("[HATA] Tum alanlari doldurun!")

        elif secim == "2":
            # Kitap Sil
            print("\n--- Kitap Sil ---")
            id = input("Silinecek kitabin ID'si: ").strip()
            if id:
                csv_kitap_sil(id)
            else:
                print("[HATA] ID girmelisiniz!")

        elif secim == "3":
            # Kitap Ara
            print("\n--- Kitap Ara ---")
            arama = input("Kitap adi veya yazar adi: ").strip()
            if arama:
                bulunan = csv_kitap_ara(arama)
                if bulunan:
                    print(f"\n[SONUC] {len(bulunan)} kitap bulundu:")
                    print("-" * 80)
                    for kitap in bulunan:
                        kitap.bilgileri_goster()
                else:
                    print("[BILGI] Hic kitap bulunamadi.")
            else:
                print("[HATA] Arama terimi girmelisiniz!")

        elif secim == "4":
            # Tüm Kitapları Listele
            kitaplar = csv_tum_kitaplari_oku()
            if kitaplar:
                print(f"\n[LISTE] Toplam {len(kitaplar)} kitap:")
                print("-" * 80)
                for kitap in kitaplar:
                    kitap.bilgileri_goster()
            else:
                print("[BILGI] Veritabani bos.")

        elif secim == "5":
            # Çıkış
            print("\nProgramdan cikiliyor...")
            break

        else:
            print("[HATA] Gecersiz secim! Lutfen 1-5 arasi bir sayi girin.")


if __name__ == "__main__":
    main()
