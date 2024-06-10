import os
import qrcode
import matplotlib.pyplot as plt


def create(ssid, passphrase, path):
    qrcode.make(f'WIFI:S:{ssid};T:WPA;P:{passphrase};;').save(path)

    plt.imshow(plt.imread(path), cmap='gray')
    plt.axis('off')

    # SSID
    plt.figtext(.5, .91, ssid,
                ha= 'center', fontname= 'monospace', fontsize= 14)

    # Passphrase
    plt.figtext(.5, .07, passphrase,
                ha= 'center', fontname= 'monospace', fontsize= 12)

    plt.tight_layout()
    plt.savefig(path, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    path = os.path.join('qr_codes')

    if not os.path.exists(path):
        os.makedirs(path)

    ssid1 = '', ''
    ssid2 = '', ''

    for ssid, passphrase in [ssid1, ssid2]:
        create(ssid, passphrase, os.path.join(path, f'{ssid}.png'))
