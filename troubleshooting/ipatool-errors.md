# ipatool Common Errors & Troubleshooting Reference

[🏠 Home](../README.md) • [📚 Guides Index](../README.md#-documentation-index) • [📥 Download Older Versions](../guides/downloading-older-versions.md) • [📲 Installation Guide](../guides/installing-downloaded-ipas.md)

---

## Overview

This document provides solutions for the most frequent issues, error strings, and confusing behaviors encountered when using [`ipatool`](https://github.com/majd/ipatool), compiled from real-world community feedback on [qnblackcat's Gist](https://gist.github.com/qnblackcat/4f7b77f685ccda2ff4ef916a27d66107) and active GitHub issues.

---

## Table of Contents

1. [Windows Keystore Passphrase Confusion](#1-windows-keystore-passphrase-confusion)
2. ["license is required" Error](#2-license-is-required-error)
3. [Typographic / Unicode Dash Parsing Error](#3-typographic--unicode-dash-parsing-error)
4. [Email Address Format Confusion](#4-email-address-format-confusion)
5. [App Installs via USB but Closes Immediately on Launch](#5-app-installs-via-usb-but-closes-immediately-on-launch)
6. ["failed to write file: unexpected EOF" / Corrupted Downloads](#6-failed-to-write-file-unexpected-eof--corrupted-downloads)
7. [tvOS & watchOS Apps Downloading](#7-tvos--watchos-apps-downloading)

---

## 1. Windows Keystore Passphrase Confusion

### The Symptom
```text
enter passphrase to unlock "C:\Users\<user>\.ipatool" (this is separate from your Apple ID password):
```

### Cause
On Windows, `ipatool` initializes an encrypted local storage directory at `C:\Users\<user>\.ipatool` using a master passphrase to secure your authentication tokens on disk.

### Solution
- **First-time prompt**: Enter any secure password you want. You must enter this same passphrase on subsequent `ipatool` commands.
- **Forgot passphrase?**: Reset the keystore by deleting the directory:
  ```powershell
  Remove-Item -Recurse -Force "$env:USERPROFILE\.ipatool"
  ```
  Then re-run `ipatool auth login` to define a new passphrase.
- **Automated bypass**: In scripts, pass the `--keychain-passphrase "<passphrase>"` flag to prevent interactive stops.

---

## 2. "license is required" Error

### The Symptom
```text
ERR error="license is required" success=false
```

### Cause
Apple's Storefront enforces account ownership. If your Apple account has never downloaded ("purchased") the application in the past, the Storefront refuses requests to enumerate version IDs or download binaries.

### Solution
- **For Free Apps ($0.00)**:  
  Acquire the license record on your account using the `purchase` command:
  ```powershell
  ipatool purchase -b com.example.app
  ```
  Or append `--purchase` directly to your download command:
  ```powershell
  ipatool download -b com.example.app --external-version-id <ID> --purchase
  ```
- **For Paid Apps**:  
  `ipatool purchase` **cannot** purchase paid apps. You must purchase the app legitimately in the App Store on an iOS device first using the same Apple ID. Once owned, `ipatool` can download any previous build.

---

## 3. Typographic / Unicode Dash Parsing Error

### The Symptom
```text
ERR error="unknown shorthand flag: 'â' in -—email" success=false
```

### Cause
Copying commands from formatted web pages, rich text, or blog posts often converts double hyphens (`--`) into Unicode em-dashes (`—`) or en-dashes (`–`), which corrupts CLI flag parsing.

### Solution
Always ensure flag arguments start with two standard ASCII minus characters (`--`):
```powershell
# ✅ Correct:
ipatool auth login --email user@example.com

# ❌ Incorrect (em-dash):
ipatool auth login —email user@example.com
```

---

## 4. Email Address Format Confusion

### Issue
Many community guides write `--email yourAppleID@icloud.com`, leading users to believe an `@icloud.com` account is mandatory.

### Solution
You can use **any email address** registered as your Apple ID (e.g., `@gmail.com`, `@outlook.com`, `@yahoo.com`, or custom domains). There is no requirement to have an `@icloud.com` email.

---

## 5. App Installs via USB but Closes Immediately on Launch

### The Symptom
The `.ipa` package installs successfully (e.g., [AppManager](https://git.kawaiizenbo.me/kawaiizenbo/AppManager) logs `Process ended with code 0 (Success)`), but tapping the app icon on the iPhone screen causes it to instantly flash and close or prompt for credentials.

### Cause
**Apple FairPlay DRM Account Mismatch.** Packages downloaded from the App Store contain signed receipts matching the Apple ID used during `ipatool auth login`.

### Solution
1. Open **Settings > App Store** (or your primary iCloud account settings) on the target iOS device.
2. Sign into the **same Apple ID** used with `ipatool`.
3. Launch the app again. The system validates the receipt in `SC_Info` and launches the application without terminating.

---

## 6. "failed to write file: unexpected EOF" / Corrupted Downloads

### The Symptom
```text
ERR error="failed to download file: failed to write file: unexpected EOF" success=false
ERR error="failed to open zip reader" success=false
```

### Cause
The download stream from Apple's Akamai CDN was interrupted or truncated before completion.

### Solution
1. **Check Disk Space**: Ensure the partition where `ipatool` is writing has at least double the size of the target IPA in free space.
2. **Permissions**: Do not run `ipatool` in protected system folders like `C:\Windows\System32`. Use `C:\Tools\` or `Downloads\`.
3. **Network Stability**: If on an unstable connection or VPN, reconnect and re-issue the command.

---

## 7. tvOS & watchOS Apps Downloading

### Question
*Can I download older versions of Apple TV (tvOS) or Apple Watch (watchOS) apps?*

### Solution
Yes. Modern versions of `ipatool` (v2.8+) support tvOS and watchOS packages:
- Check if the app supports tvOS/watchOS:
  ```powershell
  ipatool search "App Name"
  ```
  Look for `"platforms": ["iphone", "ipad", "appletvos", "watchos"]` in the output.
- Pass the external version ID as usual:
  ```powershell
  ipatool download -b com.example.tvapp --external-version-id <ID>
  ```

---

[⬅️ Installing Downloaded IPAs](../guides/installing-downloaded-ipas.md) • [Tools Matrix ➡️](../tools/useful-tools.md)
