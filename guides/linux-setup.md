# Linux Setup Guide

[🏠 Home](../README.md) • [📚 Guides Index](../README.md#-documentation-index) • [🪟 Windows Setup](windows-setup.md) • [🍎 macOS Setup](macos-setup.md) • [📥 Download Older Versions](downloading-older-versions.md)

---

## Overview

This guide explains how to install [`ipatool`](https://github.com/majd/ipatool) and configure iOS device communication tools on Linux distributions (Ubuntu, Debian, Fedora, Arch Linux, etc.).

---

## 1. Install ipatool on Linux

1. Download the latest precompiled release for your CPU architecture from the [official releases](https://github.com/majd/ipatool/releases):
   - **x86_64 / Intel / AMD**: `ipatool-linux-amd64.tar.gz`
   - **ARM64 / Raspberry Pi**: `ipatool-linux-arm64.tar.gz`

2. Extract and move the binary to your system PATH:
   ```bash
   tar -xzf ipatool-linux-amd64.tar.gz
   sudo mv ipatool /usr/local/bin/
   sudo chmod +x /usr/local/bin/ipatool
   ```

3. Test the installation:
   ```bash
   ipatool --version
   ```

---

## 2. Set Up USB Drivers & Device Communication

Linux requires `usbmuxd` (the USB multiplexor daemon) and `libimobiledevice` to communicate with iOS hardware over USB.

### Debian / Ubuntu / Linux Mint
```bash
sudo apt update
sudo apt install usbmuxd libimobiledevice6 libimobiledevice-utils ideviceinstaller
```

### Fedora / RHEL
```bash
sudo dnf install usbmuxd libimobiledevice libimobiledevice-utils ideviceinstaller
```

### Arch Linux / Manjaro
```bash
sudo pacman -S usbmuxd libimobiledevice ideviceinstaller
```

### Enable the USB Daemon
Start and enable the `usbmuxd` background service:
```bash
sudo systemctl enable --now usbmuxd
```

---

## 3. Test Device Connection & Deploy IPAs

1. Connect your iPhone or iPad to your Linux machine via USB.
2. Unlock your screen and tap **Trust This Computer**.
3. Verify connection:
   ```bash
   idevice_id -l
   ```
   *(This prints your device's 40-character UDID)*.
4. Deploy any downloaded `.ipa` package directly to your device:
   ```bash
   ideviceinstaller -i /path/to/downloaded-app.ipa
   ```

---

## Next Steps

- Start downloading older versions: [**Downloading Older Versions of iOS Apps Using ipatool**](downloading-older-versions.md).
- Learn how to find version IDs manually: [**Finding Build Identifiers**](finding-build-identifiers.md).

---

[⬅️ macOS Setup](macos-setup.md) • [Flagship Download Guide ➡️](downloading-older-versions.md)
