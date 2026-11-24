# Downloading Older Versions of iOS Apps Using ipatool

A complete, beginner-friendly walkthrough for retrieving older versions of iOS applications using `ipatool` on Windows, macOS, and Linux.

---

## Overview

When developers release updates that remove features, change UI layouts, or introduce bugs, iOS users often wish to downgrade or acquire a previous release of an application. 

By querying Apple's App Store APIs through `ipatool` and leveraging external version databases (like [IPA File Zone](https://ipafilezone.st/)), you can acquire official, Apple-signed `.ipa` packages directly from Apple's content delivery networks.

---

## Prerequisites

1. **`ipatool` binary**:
   - Download the precompiled binary for your system from the [ipatool releases page](https://github.com/majd/ipatool/releases).
2. **An Apple ID account**:
   - Your email does **not** have to be an `@icloud.com` address; any valid Apple ID email (Gmail, Outlook, custom domain) is supported.
3. **Target Device**:
   - For launching the downloaded app, your iPhone or iPad must be signed into the same Apple ID used during download.

---

## Step 1: Authentication

Open your terminal or Windows PowerShell and navigate to the directory where `ipatool` is located:

```powershell
.\ipatool.exe auth login --email your-apple-id@example.com
```

> **Warning (Copy/Paste syntax)**: Make sure you use standard double hyphens (`--email`) rather than formatted dashes (`—email`), which cause flag parsing errors.

1. **Password**: Enter your Apple ID password when prompted.
2. **2FA Code**: Enter the 6-digit verification code sent to your Apple devices.
3. **Windows Passphrase Prompt**:
   - On Windows, `ipatool` asks for a local passphrase to encrypt `C:\Users\<Username>\.ipatool`.
   - **Important**: This is a local passphrase for your encrypted keystore, not your Apple ID password. Create a simple memorable passphrase and remember it, as `ipatool` prompts for it before executing commands.

---

## Step 2: Search and Acquire App License

Before Apple allows you to query versions or download an application, your Apple ID must "own" a license for the app.

1. **Search for the app**:
   ```powershell
   .\ipatool.exe search "Snapchat"
   ```
   Note the `bundleID` (e.g., `com.toyopagroup.picaboo`) and app ID (`447188370`).

2. **Acquire License (Free Apps)**:
   If you have never "purchased" (downloaded) this app before with this Apple ID, run:
   ```powershell
   .\ipatool.exe purchase -b com.toyopagroup.picaboo
   ```
   *Note: For paid apps, you must purchase the app legitimately in the App Store on an iOS device first; `ipatool` cannot bypass payment gates.*

---

## Step 3: Find the Historical Version ID

Apple identifies releases by sequential integer IDs (`externalVersionIdentifier`) rather than semantic version strings (like `13.90.0`).

### Recommended Method: Look up on IPA File Zone
Rather than testing hundreds of raw IDs, visit:
```text
https://ipafilezone.st/app/<developer>/<app-name>/<app-id>
```
Look up your desired version (e.g. `13.90.0`) in the table and copy its **External Version ID** (e.g. `885041606`).

### Verification Command
Confirm the metadata directly from Apple:
```powershell
.\ipatool.exe get-version-metadata -b com.toyopagroup.picaboo --external-version-id 885041606 --format json
```
Check that the returned `"displayVersion"` matches your requirement.

---

## Step 4: Download the IPA Package

Run the download command using the bundle ID and verified external version ID:

```powershell
.\ipatool.exe download -b com.toyopagroup.picaboo --external-version-id 885041606
```

Upon completion, `ipatool` writes the `.ipa` file into your working directory:
```text
INF output="com.toyopagroup.picaboo_447188370_13.90.0.ipa" purchased=false success=true
```

---

## Step 5: Installing on Your Device

A common question among users is: *"I have the .ipa file, but how do I install it on my iPhone without jailbreak?"*

Because the IPA is an official Apple-signed package tied to your Apple account:
1. Connect your device via USB and tap **Trust This Computer**.
2. Download and launch **[AppManager](https://git.kawaiizenbo.me/kawaiizenbo/AppManager)**.
3. Click **Install new** and select the downloaded `.ipa` file.
4. Once AppManager reports `Process ended with code 0 (Success)`, open the app on your device.

For a complete walkthrough with troubleshooting steps, refer to [Installing Downloaded IPAs](installing-downloaded-ipas.md).
