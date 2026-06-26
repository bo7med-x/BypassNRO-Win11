# BypassNRO Tool for Windows 11 25H2

**Made by BO7MEDX**
📱 Telegram: [@PVT_BO](https://t.me/PVT_BO)

---

## What It Does
Bypasses the internet connection requirement during Windows 11 OOBE setup, allowing local account creation without a Microsoft account.

---

## Requirements
- Windows 11 ISO
- DISM (built into Windows)
- PyInstaller (to build the `.exe`)

---

## Build

```cmd
pyinstaller --onefile --noconsole --version-file "BypassNRO.py" -i "icon.ico"
```

---

## Inject into install.wim

```cmd
dism /Mount-Wim /WimFile:install.wim /index:1 /MountDir:C:\mount
copy BypassNRO.exe C:\mount\Windows\System32\BypassNRO.exe
dism /Unmount-Wim /MountDir:C:\mount /Commit
```

---

## Usage During OOBE

1. Boot from your USB
2. When the **internet connection screen** appears → press **Shift + F10**
3. In the CMD window type:

```cmd
BypassNRO.exe
```

4. Click **OK** on the popup → system restarts automatically → continue setup as a **local account**

---

## License
MIT
