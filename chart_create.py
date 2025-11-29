"""
Kütüphane Yönetim Sistemi - Basit Akış Şeması
matplotlib kullanarak PNG oluşturur (graphviz gerektirmez)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Polygon, FancyArrowPatch


def draw_box(ax, x, y, width, height, text, color='lightblue'):
    """Dikdörtgen kutu çizer"""
    box = FancyBboxPatch((x, y), width, height,
                        boxstyle="round,pad=0.1",
                        edgecolor='black', facecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(x + width/2, y + height/2, text, ha='center', va='center',
            fontsize=11, weight='bold')


def draw_oval(ax, x, y, width, height, text, color='lightgray'):
    """Oval çizer (başlangıç/bitiş için)"""
    center_x = x + width / 2
    center_y = y + height / 2
    ellipse = mpatches.Ellipse((center_x, center_y), width, height,
                              facecolor=color, edgecolor='black', linewidth=2)
    ax.add_patch(ellipse)
    ax.text(center_x, center_y, text, ha='center', va='center',
            fontsize=12, weight='bold')


def draw_diamond(ax, x, y, width, height, text, color='yellow'):
    """Elmas çizer (karar için)"""
    center_x = x + width / 2
    center_y = y + height / 2
    points = [[center_x, y + height], [x + width, center_y],
              [center_x, y], [x, center_y]]
    diamond = Polygon(points, closed=True,
                     edgecolor='black', facecolor=color, linewidth=2)
    ax.add_patch(diamond)
    ax.text(center_x, center_y, text, ha='center', va='center',
            fontsize=11, weight='bold')


def draw_parallelogram(ax, x, y, width, height, text, color='lightgreen'):
    """Paralel kenar çizer (girdi/çıktı için)"""
    offset = 0.3
    points = [[x + offset, y], [x + width, y],
              [x + width - offset, y + height], [x, y + height]]
    parallelogram = Polygon(points, closed=True,
                           edgecolor='black', facecolor=color, linewidth=2)
    ax.add_patch(parallelogram)
    center_x = x + width / 2
    center_y = y + height / 2
    ax.text(center_x, center_y, text, ha='center', va='center',
            fontsize=11, weight='bold')


def draw_arrow(ax, x1, y1, x2, y2, label=''):
    """Ok çizer"""
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=25,
                           linewidth=2, color='black')
    ax.add_patch(arrow)
    if label:
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        ax.text(mid_x + 0.3, mid_y, label, fontsize=10, weight='bold',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                        edgecolor='black'))


def create_flowchart():
    """Ana akış şeması oluştur"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 14))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 16)
    ax.axis('off')

    # Başlık
    ax.text(5, 15.5, 'KÜTÜPHANE YÖNETİM SİSTEMİ - AKIŞ ŞEMASI',
           ha='center', fontsize=14, weight='bold',
           bbox=dict(boxstyle='round', facecolor='lightgray', edgecolor='black'))

    y = 14

    # 1. Başla
    draw_oval(ax, 3.5, y, 3, 0.8, 'BAŞLA', '#D3D3D3')
    draw_arrow(ax, 5, y, 5, y - 1.2)
    y -= 1.4

    # 2. Kütüphane oluştur
    draw_box(ax, 2.5, y, 5, 0.9, 'Kütüphane Oluştur', '#ADD8E6')
    draw_arrow(ax, 5, y, 5, y - 1.2)
    y -= 1.4

    # 3. Örnek kitaplar ekle
    draw_box(ax, 2.5, y, 5, 0.9, 'Örnek Kitaplar Ekle', '#ADD8E6')
    draw_arrow(ax, 5, y, 5, y - 1.2)
    y -= 1.4

    # 4. Menüyü göster
    menu_y = y
    draw_box(ax, 2.8, y, 4.4, 0.9, 'Menüyü Göster', '#FFB6C1')
    draw_arrow(ax, 5, y, 5, y - 1.2)
    y -= 1.4

    # 5. Kullanıcı seçimi
    draw_box(ax, 2.8, y, 4.4, 0.9, 'Kullanıcı Seçim', '#FFB6C1')
    draw_arrow(ax, 5, y, 5, y - 1.2)
    y -= 1.4

    # 6. Karar
    decision_y = y
    draw_diamond(ax, 3.2, y, 3.6, 1.2, 'Seçim?', '#FFFFE0')
    y -= 1.8

    # 7. İşlem yap (1-4)
    draw_arrow(ax, 5, decision_y, 5, decision_y - 1.4, '1-4')
    draw_box(ax, 2.8, y, 4.4, 0.9, 'İşlem Yap', '#DDA0DD')
    draw_arrow(ax, 5, y, 5, y - 1.2)
    y -= 1.4

    # 8. Sonuç Göster (paralel kenar - çıktı)
    draw_parallelogram(ax, 2.8, y, 4.4, 0.9, 'Sonuç Göster', '#98FB98')

    # Menüye geri dön
    ax.annotate('', xy=(2.5, menu_y), xytext=(2.8, y + 0.45),
               arrowprops=dict(arrowstyle='->', lw=2, color='black',
                             connectionstyle="arc3,rad=-0.5"))

    # 8. Çıkış (5)
    draw_arrow(ax, 6.8, decision_y + 0.3, 8.5, decision_y - 2, '5')
    draw_box(ax, 7.5, y, 2, 0.9, 'Çıkış', '#90EE90')
    draw_arrow(ax, 8.5, y, 8.5, y - 1.2)
    draw_oval(ax, 7.5, y - 1.6, 2, 0.7, 'BİTİR', '#D3D3D3')

    # Kaydet
    plt.tight_layout()
    output_filename = 'kutuphane_akis_semasi_basit.png'
    plt.savefig(output_filename, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Akis semasi '{output_filename}' olarak kaydedildi.")
    plt.close()

if __name__ == '__main__':
    create_flowchart()