# HMD Wifi Killer 🔥

<div align="center">

[English](README.md) | [فارسی](README.fa.md)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Linux-red.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

</div>

## 📝 Description

HMD Wifi Killer is a powerful WiFi deauthentication tool designed for educational and testing purposes. It provides a user-friendly interface for performing deauthentication attacks on WiFi networks using both mdk4 and aircrack-ng methods.

## ⚠️ Disclaimer

This tool is provided for educational purposes only. Using this tool against networks without explicit permission is illegal. The author is not responsible for any misuse or damage caused by this program.

## 🚀 Features

- 🔍 Interactive network scanning
- 🎯 Multiple attack methods (mdk4 and aircrack-ng)
- 🖥️ Automatic interface detection
- 📊 Detailed network information display
- 🎨 Beautiful colored terminal interface
- 🔄 Automatic tool installation
- 🛡️ Root access verification
- 🎮 User-friendly interactive menu

## 📋 Requirements

- Python 3.x
- Linux operating system
- Root access
- Wireless network interface with monitor mode support

### Required Tools
- aircrack-ng suite
- mdk4
- scapy
- termcolor

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Hamed-Gharghi/wifi-deauther.git
cd wifi-deauther
```

2. Make the script executable:
```bash
chmod +x wifi_deauther.py
```

3. Run the script with root privileges:
```bash
sudo python3 wifi_deauther.py
```

## 💻 Usage

1. Run the script with sudo:
```bash
sudo python3 wifi_deauther.py
```

2. Select your wireless interface from the list

3. Choose your attack method:
   - mdk4 (More aggressive)
   - aircrack-ng (More stable)

4. Select target network or choose to attack all networks

5. Press Ctrl+C to stop the attack

## 🎯 Attack Methods

### mdk4 Method
- More aggressive attack
- Can target specific clients
- Higher packet rate

### aircrack-ng Method
- More stable attack
- Better compatibility
- Lower resource usage

## 🔧 Command Line Arguments

```bash
-i, --interface    Specify wireless interface
-t, --target      Target WiFi MAC address
-g, --gateway     Gateway MAC address (Optional)
-n, --count       Number of deauthentication packets (default: 1000)
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

- **Hamed Gharghi**
- GitHub: [@Hamed-Gharghi](https://github.com/Hamed-Gharghi)

## ⭐ Support

If you find this tool helpful, please give it a star on GitHub!

## 📞 Contact

For any questions or suggestions, please open an issue on GitHub.

---

<div align="center">
Made with ❤️ by Hamed Gharghi
</div> 