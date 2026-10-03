import os
import getpass
import argparse

import qrcode
import matplotlib.pyplot as plt


def parse_arguments():
    """Parse arguments from CLI."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s', '--ssid', type=str, required=True,
        help='Name (SSID) of the wifi network',
    )
    parser.add_argument(
        '--path', type=str, required=False,
        default='qr_codes',
        help='Path in which the images will be saved',
    )
    return parser.parse_args()

def create(ssid: str, password: str, path: str) -> None:
    """Create the QR code and save it to path.

    Parameters
    ----------
    ssid : str
        Name of the wifi network
    password : str
        Password of the wifi network
    path : str
        Path in which the QR code will be saved
    """
    qrcode.make(f'WIFI:S:{ssid};T:WPA;P:{password};;').save(path)

    plt.imshow(plt.imread(path), cmap='gray')
    plt.axis('off')

    # SSID
    plt.figtext(.5, .91, ssid,
                ha= 'center', fontname= 'monospace', fontsize= 14)

    # Passphrase
    plt.figtext(.5, .07, password,
                ha= 'center', fontname= 'monospace', fontsize= 12)

    plt.tight_layout()
    plt.savefig(path, bbox_inches='tight')
    plt.close()

def main() -> None:  # noqa: D103
    # Get SSID and path
    args = parse_arguments()
    if not args.ssid.strip():
        err_msg = 'SSID cannot be empty.'
        raise ValueError(err_msg)

    # Get password
    password = getpass.getpass(
        prompt=f'Enter password for {args.ssid.strip()}: '
    )
    if not password.strip():
        err_msg = 'Password cannot be empty.'
        raise ValueError(err_msg)

    # Create directory
    if not os.path.exists(args.path.strip()):
        os.makedirs(args.path.strip())

    # Create image
    create(
        args.ssid.strip(),
        password,
        os.path.join(args.path.strip(), f'{args.ssid.strip()}.png')
    )
    print(f'File saved in {args.ssid.strip()}.png')

if __name__ == '__main__':
    main()

