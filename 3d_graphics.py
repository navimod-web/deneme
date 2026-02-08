"""
3D Grafik Oluşturucu - Python ile 3 Boyutlu Görselleştirmeler
=============================================================
Matplotlib kullanarak çeşitli 3D grafikler oluşturur.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def yuzey_grafigi():
    """3D yüzey grafiği - Dalgalı yüzey"""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))

    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=True, alpha=0.9)
    fig.colorbar(surf, shrink=0.5, aspect=10, label='Z Değeri')

    ax.set_xlabel('X Ekseni')
    ax.set_ylabel('Y Ekseni')
    ax.set_zlabel('Z Ekseni')
    ax.set_title('3D Yüzey Grafiği - sin(√(x² + y²))', fontsize=14, fontweight='bold')

    plt.savefig('yuzey_grafigi.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ yuzey_grafigi.png kaydedildi")


def spiral_grafigi():
    """3D spiral (helis) grafiği"""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    t = np.linspace(0, 10 * np.pi, 1000)
    x = np.cos(t)
    y = np.sin(t)
    z = t / (2 * np.pi)

    ax.plot(x, y, z, color='crimson', linewidth=2, label='Spiral')
    ax.scatter(x[::50], y[::50], z[::50], color='navy', s=30, zorder=5)

    ax.set_xlabel('X Ekseni')
    ax.set_ylabel('Y Ekseni')
    ax.set_zlabel('Z Ekseni')
    ax.set_title('3D Spiral (Helis) Grafiği', fontsize=14, fontweight='bold')
    ax.legend()

    plt.savefig('spiral_grafigi.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ spiral_grafigi.png kaydedildi")


def dagilim_grafigi():
    """3D dağılım (scatter) grafiği"""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    np.random.seed(42)
    n = 300

    # 3 farklı küme oluştur
    kumeler = [
        {'merkez': (2, 2, 2), 'renk': '#FF6B6B', 'etiket': 'Küme A'},
        {'merkez': (-2, -2, 2), 'renk': '#4ECDC4', 'etiket': 'Küme B'},
        {'merkez': (0, 0, -2), 'renk': '#45B7D1', 'etiket': 'Küme C'},
    ]

    for kume in kumeler:
        mx, my, mz = kume['merkez']
        x = np.random.randn(n) + mx
        y = np.random.randn(n) + my
        z = np.random.randn(n) + mz
        ax.scatter(x, y, z, c=kume['renk'], s=15, alpha=0.6, label=kume['etiket'])

    ax.set_xlabel('X Ekseni')
    ax.set_ylabel('Y Ekseni')
    ax.set_zlabel('Z Ekseni')
    ax.set_title('3D Dağılım Grafiği - 3 Küme', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)

    plt.savefig('dagilim_grafigi.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ dagilim_grafigi.png kaydedildi")


def parametrik_yuzey():
    """Parametrik 3D yüzey - Torus (simit şekli)"""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    R = 3  # Ana yarıçap
    r = 1  # Tüp yarıçapı

    u = np.linspace(0, 2 * np.pi, 80)
    v = np.linspace(0, 2 * np.pi, 80)
    U, V = np.meshgrid(u, v)

    X = (R + r * np.cos(V)) * np.cos(U)
    Y = (R + r * np.cos(V)) * np.sin(U)
    Z = r * np.sin(V)

    ax.plot_surface(X, Y, Z, cmap=cm.plasma, alpha=0.9, linewidth=0, antialiased=True)

    ax.set_xlabel('X Ekseni')
    ax.set_ylabel('Y Ekseni')
    ax.set_zlabel('Z Ekseni')
    ax.set_title('3D Torus (Simit) Yüzeyi', fontsize=14, fontweight='bold')
    ax.set_box_aspect([1, 1, 0.4])

    plt.savefig('torus_grafigi.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ torus_grafigi.png kaydedildi")


def kontur_ve_yuzey():
    """3D yüzey + altında kontur haritası"""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-(X**2 + Y**2)) * np.cos(2 * X) * np.cos(2 * Y)

    # Yüzey
    ax.plot_surface(X, Y, Z, cmap=cm.viridis, alpha=0.8, linewidth=0)

    # Kontur haritası (alt düzlem)
    ax.contourf(X, Y, Z, zdir='z', offset=-1, cmap=cm.viridis, alpha=0.5)

    ax.set_xlabel('X Ekseni')
    ax.set_ylabel('Y Ekseni')
    ax.set_zlabel('Z Ekseni')
    ax.set_zlim(-1, 1)
    ax.set_title('3D Yüzey + Kontur Haritası', fontsize=14, fontweight='bold')

    plt.savefig('kontur_yuzey_grafigi.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ kontur_yuzey_grafigi.png kaydedildi")


def birlesik_grafik():
    """Tüm grafikleri tek bir figürde birleştirir"""
    fig = plt.figure(figsize=(18, 12))
    fig.suptitle('Python 3D Grafik Koleksiyonu', fontsize=18, fontweight='bold', y=0.98)

    # 1 - Dalgalı yüzey
    ax1 = fig.add_subplot(231, projection='3d')
    x = np.linspace(-5, 5, 80)
    y = np.linspace(-5, 5, 80)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    ax1.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0)
    ax1.set_title('Dalgalı Yüzey')

    # 2 - Spiral
    ax2 = fig.add_subplot(232, projection='3d')
    t = np.linspace(0, 8 * np.pi, 500)
    ax2.plot(np.cos(t), np.sin(t), t / (2 * np.pi), color='crimson', linewidth=2)
    ax2.set_title('Spiral')

    # 3 - Dağılım
    ax3 = fig.add_subplot(233, projection='3d')
    np.random.seed(42)
    for renk, m in [('#FF6B6B', (2, 2, 2)), ('#4ECDC4', (-2, -2, 2)), ('#45B7D1', (0, 0, -2))]:
        ax3.scatter(np.random.randn(100) + m[0], np.random.randn(100) + m[1],
                    np.random.randn(100) + m[2], c=renk, s=10, alpha=0.6)
    ax3.set_title('Küme Dağılımı')

    # 4 - Torus
    ax4 = fig.add_subplot(234, projection='3d')
    u = np.linspace(0, 2 * np.pi, 60)
    v = np.linspace(0, 2 * np.pi, 60)
    U, V = np.meshgrid(u, v)
    ax4.plot_surface((3 + np.cos(V)) * np.cos(U), (3 + np.cos(V)) * np.sin(U),
                     np.sin(V), cmap=cm.plasma, linewidth=0)
    ax4.set_title('Torus')
    ax4.set_box_aspect([1, 1, 0.4])

    # 5 - Kontur + Yüzey
    ax5 = fig.add_subplot(235, projection='3d')
    x2 = np.linspace(-3, 3, 80)
    y2 = np.linspace(-3, 3, 80)
    X2, Y2 = np.meshgrid(x2, y2)
    Z2 = np.exp(-(X2**2 + Y2**2)) * np.cos(2 * X2) * np.cos(2 * Y2)
    ax5.plot_surface(X2, Y2, Z2, cmap=cm.viridis, alpha=0.8, linewidth=0)
    ax5.contourf(X2, Y2, Z2, zdir='z', offset=-1, cmap=cm.viridis, alpha=0.5)
    ax5.set_zlim(-1, 1)
    ax5.set_title('Kontur + Yüzey')

    # 6 - Wireframe küre
    ax6 = fig.add_subplot(236, projection='3d')
    phi = np.linspace(0, np.pi, 30)
    theta = np.linspace(0, 2 * np.pi, 30)
    PHI, THETA = np.meshgrid(phi, theta)
    Xs = np.sin(PHI) * np.cos(THETA)
    Ys = np.sin(PHI) * np.sin(THETA)
    Zs = np.cos(PHI)
    ax6.plot_wireframe(Xs, Ys, Zs, color='steelblue', linewidth=0.5)
    ax6.set_title('Wireframe Küre')

    plt.tight_layout()
    plt.savefig('birlesik_3d_grafik.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ birlesik_3d_grafik.png kaydedildi")


def main():
    print("=" * 50)
    print("  3D Grafik Oluşturucu")
    print("=" * 50)
    print()

    print("Grafikler oluşturuluyor...\n")

    yuzey_grafigi()
    spiral_grafigi()
    dagilim_grafigi()
    parametrik_yuzey()
    kontur_ve_yuzey()
    birlesik_grafik()

    print()
    print("=" * 50)
    print("  Tüm grafikler başarıyla oluşturuldu!")
    print("  Toplam 6 adet PNG dosyası kaydedildi.")
    print("=" * 50)


if __name__ == '__main__':
    main()
