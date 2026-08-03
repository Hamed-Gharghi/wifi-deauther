<div align="center">
  <img src="cover.png" alt="Network File Sharing App — Share files over WiFi" width="100%">
  <br/>
  <h1>📁 Network File Sharing App</h1>
  <h3><em>Share files over WiFi in seconds — no cloud, no account, no cables</em></h3>
  <br/>
  <p align="center">
    <a href="#-features"><strong>✨ Features</strong></a> ·
    <a href="#-download-pre-built-exe"><strong>📥 Download</strong></a> ·
    <a href="#-screenshots"><strong>📸 Screenshots</strong></a> ·
    <a href="#-quick-start"><strong>🏁 Quick Start</strong></a> ·
    <a href="#-how-to-use"><strong>🎮 How To Use</strong></a> ·
    <a href="#-security"><strong>🛡️ Security</strong></a> ·
    <a href="#-changelog"><strong>📋 Changelog</strong></a>
  </p>
  <br/>

  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
  [![Version](https://img.shields.io/badge/Version-2.1.0-success.svg)](https://github.com/Hamed-Gharghi/Network-File-Sharing-App-with-Python/releases)
  [![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://python.org)
  [![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](https://github.com/Hamed-Gharghi/Network-File-Sharing-App-with-Python)
  [![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen)](https://github.com/Hamed-Gharghi/Network-File-Sharing-App-with-Python/pulls)
  [![Made with ❤️](https://img.shields.io/badge/Made_with-❤️-red)]()

  <br/>

  **Network File Sharing App** is a free, open-source **LAN file sharing** tool for Windows, macOS, and Linux. Start a local HTTP server from a simple GUI, share folders over WiFi, and let others download or upload files from any browser — with optional password protection and QR code access.

  <br/>
</div>

---

## 🚀 Why This App?

`Network File Sharing App` helps you share files on your local network quickly and safely.

It's perfect when you want to:
- 📦 Send large files fast over WiFi
- 💻 Share between laptop, desktop, and phone
- 🧳 Use a portable `.exe` without installing Python

---

## ✨ Features

- 🚀 **One-click sharing** from a simple desktop GUI
- 📂 **Multi-folder support** (share many folders at once)
- 📱 **QR code access** for instant mobile connection
- 🔒 **Password protection** with HTTP Basic Auth
- 📤 **File uploads** from browser clients (two-way sharing)
- ⚡ **Live transfer speed** on the host app (progress + MB/s while transferring)
- 📋 **Per-device activity log** on the web UI (each IP sees only its own transfers)
- 🔄 **Auto-refresh file list** in the desktop app when files are added, removed, or uploaded
- 🌙 **Dark/Light mode** with fully themed interface
- 🔍 **File search** with quick filtering
- 🖱️ **Drag and drop** folder support in the GUI
- 🌐 **Web interface** works in any modern browser
- 🔌 **Custom port** and smart retry when busy
- 🎨 **Custom executable icon** when building
- 🌍 **Cross-platform source support** (Windows/macOS/Linux)

---

## 📥 Download (Pre-built EXE)

Don't want to install Python? Download the ready-to-run executable from Releases:

👉 [Download `FileSharingApp.exe`](https://github.com/Hamed-Gharghi/Network-File-Sharing-App-with-Python/releases/latest)

- ✅ No installation needed
- ✅ No Python required
- ✅ No console window (GUI only)
- ✅ Portable and easy to carry

---

## 📸 Screenshots

### Desktop App (Main Window)

![Desktop App Main Window](screenshots/app-main-window.png)

### Web Interface (Shared Folders Home)

![Web Interface Shared Folders Home](screenshots/web-homepage.png)

### Web Interface (Folder Content + Upload)

![Web Interface Folder Content and Upload](screenshots/web-folder-view.png)

---

## 🏁 Quick Start

### Option A: Use the EXE (Windows)

1. Download `FileSharingApp.exe` from Releases
2. Open the app
3. Add one or more folders
4. Click **Start Server**
5. Share URL or QR code with devices on the same network

### Option B: Run from source (Python)

Requirements:
- Python `3.8+`

```bash
git clone https://github.com/Hamed-Gharghi/Network-File-Sharing-App-with-Python.git
cd Network-File-Sharing-App-with-Python

# Optional but recommended extras
pip install -r requirements.txt

python file_sharing_network_gui.py
```

> **Note:** The core app runs with Python’s standard library alone. Packages in `requirements.txt` unlock QR codes, drag & drop, and EXE builds.

---

## 🎮 How To Use

### Basic Flow

1. Connect all devices to the same WiFi/LAN
2. Add folders using `+ Add Folder` or drag-and-drop
3. Configure port, password, and upload option
4. Start the server
5. Share the link shown in the app

### For Recipients

Recipients open the link in a browser and can:
- Browse folders
- Download files
- Navigate subfolders
- Upload files (if enabled)
- See **Your Recent Activity** (downloads/uploads from that device only)

### Host tips (desktop app)

- Watch **live transfer speed** above the Activity Log during uploads/downloads
- The file list **auto-updates** when someone uploads or when files change on disk
- Use Dark/Light mode with the moon/sun button or `Ctrl+D`

---

## 🖥️ Web Interface

Routes:

| Route | Description |
|---|---|
| `/` | Home page with all shared folders |
| `/0/`, `/1/`, ... | Folder-specific file view |

Each folder page includes:
- File list with names, sizes, and modified dates
- Breadcrumb navigation
- Drag-and-drop upload area (when enabled)
- Per-device **Recent Activity** panel (this connection only)
- Responsive layout for desktop and mobile

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl+B` | Add/Browse folder |
| `Ctrl+S` | Start server |
| `Ctrl+Shift+S` | Stop server |
| `Ctrl+Q` | Quit app |
| `Ctrl+D` | Toggle dark/light mode |
| `Ctrl+L` | Copy link / open in browser |

---

## 📦 Dependencies

| Package | Required? | Purpose |
|---|---|---|
| *(Python stdlib)* | ✅ Yes | Core GUI + HTTP server |
| `qrcode[pil]` | Optional | QR code generation |
| `tkinterdnd2` | Optional | Drag & drop folders onto the GUI |
| `Pillow` | Optional | PNG→ICO icon conversion for builds |
| `pyinstaller` | Optional | Build standalone `FileSharingApp.exe` |

Install everything:

```bash
pip install -r requirements.txt
```

---

## 📦 Build Standalone Executable

```bash
pip install -r requirements.txt
python build.py
```

- Output: `dist/FileSharingApp.exe`
- GUI-only executable (`--windowed`, no console)

### 🎨 Custom Icon

Place an icon in the `icon/` directory:
- `icon/icon.ico` (preferred)
- `icon/icon.png` (auto-converted if Pillow is installed)

---

## 🛡️ Security

Built-in safeguards include:
- Path traversal protection
- Uploaded filename sanitization
- HTML escaping for displayed file names
- Optional HTTP Basic Auth password protection
- Upload enable/disable control
- Upload size limit (500 MB max per request)

> Use on trusted local networks. Password protection helps, but this is not a full internet-facing security suite.

---

## 🧰 Tech Stack

- **Language:** Python 3.8+
- **GUI:** Tkinter
- **Server:** `ThreadingHTTPServer` (Python stdlib)
- **Optional libs:** `qrcode`, `Pillow`, `tkinterdnd2`
- **Packaging:** PyInstaller

---

## 📋 Changelog

### v2.1.0

**New**
- 📋 Per-device **Recent Activity** on the web UI (each client IP sees only its own downloads/uploads)
- ⚡ **Live transfer speed** on the host desktop app (progress %, size, and MB/s while transferring)
- 🔄 **Auto-refresh** of the desktop file list when files are uploaded or change on disk
- Live sync of shared folders with the running server when folders are added/removed

**Docs / packaging**
- Updated `README.md` and `requirements.txt` for v2.1.0
- Clearer dependency and build instructions

### v2.0.0

- Multi-folder sharing with virtual homepage
- QR code access, password protection, web uploads
- Dark/Light mode, keyboard shortcuts, scrollable window
- Improved build pipeline and custom icon support
- Fixes for server stop behavior, theming, and resize clipping

---

## 🤝 Contributing

Contributions are welcome and appreciated.

```bash
git checkout -b feature/your-feature
git commit -m "Add: your feature"
git push origin feature/your-feature
```

Then open a pull request describing your changes and test results.

---

## License

Distributed under the MIT License. See `LICENSE` for details.

---

## Contact

**Hamed Gharghi**  
[Email](mailto:Hamedgharghi1@gmail.com)  
[GitHub](https://github.com/Hamed-Gharghi)
