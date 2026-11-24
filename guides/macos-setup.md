# macOS Setup Guide

[🏠 Home](../README.md) • [📚 Guides Index](../README.md#-documentation-index) • [🪟 Windows Setup](windows-setup.md) • [🐧 Linux Setup](linux-setup.md) • [📥 Download Older Versions](downloading-older-versions.md)

---

## Overview

Setting up [`ipatool`](https://github.com/majd/ipatool) on macOS is the fastest and most seamless experience because macOS natively integrates with the system Keychain and iOS device drivers.

---

## Method 1: Install via Homebrew (Recommended)

If you use [Homebrew](https://brew.sh/), install `ipatool` with a single command:

```bash
brew install ipatool
```

To verify the installation:
```bash
ipatool --version
```

---

## Method 2: Manual Binary Installation

If you prefer downloading the binary manually:

1. Download the latest `ipatool-macos-universal.zip` (or `ipatool-macos-arm64.zip` for Apple Silicon M1/M2/M3/M4) from the [official releases](https://github.com/majd/ipatool/releases).
2. Extract the archive into your `Downloads` folder.
3. Open Terminal and move the binary into your system `PATH`:
   ```bash
   sudo mv ~/Downloads/ipatool /usr/local/bin/
   sudo chmod +x /usr/local/bin/ipatool
   ```
4. Verify by running:
   ```bash
   ipatool --version
   ```

> [!NOTE]
> **Native Keychain Integration**:  
> Unlike Windows, macOS saves your App Store login tokens directly into the secure native macOS Keychain. You will **not** be prompted for a separate local `.ipatool` passphrase.

---

## Connecting Your iOS Device & Installing IPAs

macOS has built-in drivers for iPhones and iPads:

1. Connect your device via USB or USB-C and tap **Trust This Computer**.
2. **GUI Installation**: Open the official **[Apple Configurator](https://apps.apple.com/us/app/apple-configurator/id1037126344)**, double-click your device, and drag and drop your downloaded `.ipa` directly onto the device window.
3. **CLI Installation**: Install `ideviceinstaller` via Homebrew:
   ```bash
   brew install ideviceinstaller
   ideviceinstaller -i /path/to/downloaded.ipa
   ```

---

## Next Steps

Now that your macOS environment is ready:
- Learn how to download older builds: [**Downloading Older Versions of iOS Apps Using ipatool**](downloading-older-versions.md).
- Learn how to find version IDs: [**Finding Build Identifiers**](finding-build-identifiers.md).

---

[⬅️ Windows Setup](windows-setup.md) • [Linux Setup ➡️](linux-setup.md)
