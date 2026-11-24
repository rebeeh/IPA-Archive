# Windows Setup Guide

[🏠 Home](../README.md) • [📚 Guides Index](../README.md#-documentation-index) • [🍎 macOS Setup](macos-setup.md) • [🐧 Linux Setup](linux-setup.md) • [📥 Download Older Versions](downloading-older-versions.md)

---

## Overview

A clean, step-by-step setup guide for running [`ipatool`](https://github.com/majd/ipatool) and deploying iOS applications via [AppManager](https://git.kawaiizenbo.me/kawaiizenbo/AppManager) on Windows 10 and Windows 11.

---

## Step 1: Install Apple Mobile Device Drivers

To allow Windows and AppManager to communicate with your iPhone or iPad over USB, you need Apple's USB drivers:

- **Option A (Recommended)**: Install the official **[Apple Devices app](https://apps.microsoft.com/detail/9np83lwlpz9k)** directly from the Microsoft Store.
- **Option B**: Download and install standard **[iTunes for Windows](https://www.apple.com/itunes/)**.

---

## Step 2: Download ipatool for Windows

1. Download the latest `ipatool-windows-amd64.zip` from the [official releases](https://github.com/majd/ipatool/releases).
2. Extract the archive into a simple folder, such as `C:\Tools\ipatool\`.
3. Open **Windows PowerShell** or Command Prompt and test the binary:
   ```powershell
   cd C:\Tools\ipatool
   .\ipatool.exe --version
   ```

> [!TIP]
> **Optional: Add to PATH**:  
> To run `ipatool` from any folder without typing `cd C:\Tools\ipatool`, run this in PowerShell once:
> ```powershell
> [Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Tools\ipatool", "User")
> ```

---

## Step 3: Understanding the Keystore Passphrase

The first time you log in with `ipatool.exe auth login`, you will see:

```text
enter passphrase to unlock "C:\Users\<user>\.ipatool" (this is separate from your Apple ID password):
```

> [!NOTE]
> This is simply a **local master password** to encrypt saved credentials on your computer. It is not your Apple ID password or Windows account password. Type any simple passphrase you can remember.
> 
> If you ever forget it, simply delete the folder `C:\Users\<YourUsername>\.ipatool` and log in again.

---

## Step 4: Download AppManager for One-Click USB Installation

To install your retrieved `.ipa` packages to your iPhone with a single click:

1. Download **`AppManager v1.1 Setup.exe`** from [AppManager Releases](https://git.kawaiizenbo.me/kawaiizenbo/AppManager/releases).
2. Run the installer and launch **AppManager**.
3. Plug in your iPhone via USB, tap **Trust This Computer**, and you are ready to deploy packages!

---

## Next Steps

- Proceed to the main guide: [**Downloading Older Versions of iOS Apps Using ipatool**](downloading-older-versions.md).
- Follow the detailed device installation walkthrough: [**Installing Downloaded IPAs**](installing-downloaded-ipas.md).

---

[⬅️ Home](../README.md) • [macOS Setup ➡️](macos-setup.md)
