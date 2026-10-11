import os
import sys
import socket
import http.server
import socketserver
import qrcode
from PIL import Image

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def main():
    port = 5000
    local_ip = get_local_ip()
    url = f"http://{local_ip}:{port}"
    app_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Generate QR Code PNG
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img_qr = qr.make_image(fill_color="black", back_color="white")
    qr_path = os.path.join(app_dir, "qr_code.png")
    img_qr.save(qr_path)
    
    # Print stylish banner
    print("=" * 65)
    print("⚡ PLANFIT MOBILE WORKOUT RUNNER & TRACKER SERVER ⚡")
    print("=" * 65)
    print(f"\n📱 1. Scan this QR Code or open on your phone's browser:\n")
    print(f"      👉  {url}  👈\n")
    print(f"      (Ensure your phone is connected to the same Wi-Fi)\n")
    print(f"💾 QR Code image saved to: {qr_path}\n")
    print("-" * 65)
    print("📱 Terminal QR Code (Scan with phone camera):\n")
    
    # Print ASCII QR
    try:
        qr_terminal = qrcode.QRCode()
        qr_terminal.add_data(url)
        qr_terminal.print_ascii(invert=True)
    except Exception:
        pass

    print("-" * 65)
    print("💡 To install as a native app on your phone:")
    print("   • iOS (Safari): Tap Share (square with arrow) -> 'Add to Home Screen'")
    print("   • Android (Chrome): Tap three dots (⋮) -> 'Install App' or 'Add to Home Screen'")
    print("\nPress Ctrl+C to stop the server.\n")
    print("=" * 65)
    
    os.chdir(app_dir)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("0.0.0.0", port), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    main()
