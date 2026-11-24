# Windows Environment & Setup Guide

[🏠 Home](../README.md) • [📚 Guides Index](../README.md#-documentation-index) • [📥 Download Older Versions](downloading-older-versions.md)

---

## Overview

This guide explains how to properly configure your Windows 10 or 11 system for running [`ipatool`](https://github.com/majd/ipatool) and deploying iOS applications via [AppManager](https://git.kawaiizenbo.me/kawaiizenbo/AppManager).

---

## Prerequisites

1. **Windows PowerShell 5.1 or PowerShell 7+**:
   - Preinstalled on Windows 10/11. (PowerShell 7 can be installed via `winget install Microsoft.PowerShell`).
2. **Apple Mobile Device Support**:
   - Required for USB communication with your iOS hardware.
   - Installed automatically when installing [iTunes from Apple](https://www.apple.com/itunes/) or the modern [Apple Devices app](https://apps.microsoft.com/detail/9np83lwlpz9k) from the Microsoft Store.

---

## 1. Setting Up ipatool

1. Download the latest `ipatool-windows-amd64.zip` from the [official releases page](https://github.com/majd/ipatool/releases).
2. Extract the archive into an easily accessible directory, such as `C:\Tools\ipatool\`.
3. (Optional) Add `C:\Tools\ipatool` to your Windows System `PATH` so `ipatool` can be invoked from any prompt:
   ```powershell
   [Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Tools\ipatool", "User")
   ```

---

## 2. Managing the Windows Keystore Passphrase

On Windows, `ipatool` stores session tokens inside `C:\Users\<YourUsername>\.ipatool`.

> [!NOTE]
> The first time you execute `ipatool auth login`, it will ask:
> ```text
> enter passphrase to unlock "C:\Users\<user>\.ipatool" (this is separate from your Apple ID password):
> ```
> This is a **local master password** to encrypt cached credentials on your PC. Choose a passphrase and keep note of it.

If you ever forget this passphrase:
```powershell
Remove-Item -Recurse -Force "$env:USERPROFILE\.ipatool"
```
Then log in again with `ipatool auth login`.

---

## 3. Verifying Driver Connectivity

To test whether your PC can communicate with your iOS device over USB before launching AppManager:

1. Connect your device via USB and unlock the screen.
2. Tap **Trust This Computer**.
3. Check services:
   ```powershell
   Get-Service -Name "*Apple Mobile Device*"
   ```
   Ensure the service status is **Running**.

---

[⬅️ Home](../README.md) • [Download Older Versions ➡️](downloading-older-versions.md)
