# Installing Downloaded IPAs

After retrieving an `.ipa` package from the App Store using `ipatool`, the file is a legitimate, FairPlay-encrypted application package cryptographically signed for the authenticated Apple ID.

This guide provides end-to-end instructions for deploying these packages onto your iOS device.

---

## Method 1: AppManager (Recommended for Windows)

**AppManager** is an open-source Windows GUI frontend for `ideviceinstaller` developed by [kawaiizenbo](https://git.kawaiizenbo.me/kawaiizenbo). It provides a clean, fast interface to install, uninstall, and view applications on connected iOS devices over USB without requiring iTunes synchronization.

- **Source Code**: [kawaiizenbo/AppManager](https://git.kawaiizenbo.me/kawaiizenbo/AppManager)
- **Latest Releases**: [AppManager Releases](https://git.kawaiizenbo.me/kawaiizenbo/AppManager/releases)

---

### System Requirements

| Component | Requirement | Notes |
| :--- | :--- | :--- |
| **Operating System** | Windows 7, 8, 10, or 11 (64-bit) | PowerShell 5.1/7 supported |
| **Runtime** | Microsoft .NET Framework 4.5+ | Preinstalled on modern Windows |
| **Drivers** | Apple Mobile Device Support | Provided by iTunes or Apple Devices app |
| **Target Hardware** | iPhone, iPad, or iPod Touch | Supports iOS 2 through modern iOS versions |
| **Jailbreak** | **Not Required** | Authentic Apple-signed IPAs run on stock iOS |

---

### Step-by-Step Installation Walkthrough

#### 1. Download and Extract AppManager
1. Visit the [AppManager Releases Page](https://git.kawaiizenbo.me/kawaiizenbo/AppManager/releases).
2. Download either:
   - **Installer**: `AppManager v1.1 Setup.exe`
   - **Portable Archive**: `AppManager-v1.1.zip`
3. If using the zip archive, extract it to a convenient directory (e.g., `C:\Tools\AppManager\`).

#### 2. Connect and Authorize Your iOS Device
1. Connect your iPhone or iPad to your PC using a certified Lightning or USB-C cable.
2. Unlock your iOS device screen.
3. If the **"Trust This Computer?"** alert appears, tap **Trust** and enter your device passcode.
4. Verify that Windows detects the device (you can test this by checking if it shows up in Windows Explorer or the Apple Devices app).

#### 3. Launch AppManager
1. Open `AppManager.exe`.
2. Inspect the application window title bar. It will automatically detect your connected hardware and display your device name, internal model identifier, and iOS firmware version:
   ```text
   AppManager (Rabee's iPhone, iPhone14,2, iOS 17.x)
   ```
3. The main list will populate with existing installed user applications.

#### 4. Deploy the Retrieved IPA
1. Click **Install new** in the top navigation menu.
2. In the file picker dialog, navigate to the folder where `ipatool` saved your package (e.g. `com.toyopagroup.picaboo_447188370_13.90.0.ipa`).
3. Click **Open**.

#### 5. Verify the Log Output
AppManager streams `ideviceinstaller` output directly into the **Log** box at the bottom of the window:

```text
Connecting to device...
Attempting install of C:\Users\Ebiza\Downloads\com.toyopagroup.picaboo_447188370_13.90.0.ipa
Process ended with code 0 (Success)
```

Once `code 0 (Success)` is displayed:
- The app icon immediately appears on your device's SpringBoard (Home Screen).
- The progress bar completes, and you can unplug or launch the app immediately.

---

### Understanding FairPlay DRM & Launch Authentication

When installing App Store packages via AppManager, keep the following rules in mind:

1. **Account Parity**:
   Because `ipatool` fetches authentic binaries directly from Apple's distribution CDN, the IPA is encrypted with Apple FairPlay DRM and licensed to the specific Apple ID used during `ipatool auth login`.
2. **Device Authorization**:
   The target iOS device **must be signed into that same Apple ID** (either as the primary iCloud/Apple account or in **Settings > App Store**). If the device is not authorized for that Apple ID, the application will quit immediately upon launch or prompt for the account credentials.
3. **No Sideload Expiration (7-Day Limits)**:
   Unlike sideloading with free developer certificates (AltStore, Sideloadly), packages installed this way are **official App Store purchases**. They do **not expire in 7 days** and do not count against your 3-app sideload limit.
4. **AppSync (Jailbroken Devices Only)**:
   AppSync is **only** required if you are installing unsigned, modified, or cracked IPAs. For legitimate historical IPAs downloaded through `ipatool` under your account, **no jailbreak or AppSync is needed**.

---

### Troubleshooting AppManager

| Issue | Cause | Solution |
| :--- | :--- | :--- |
| **Device not detected in title bar** | Missing Apple USB drivers or usbmuxd service. | Ensure iTunes or Apple Devices app is installed from Apple or Microsoft Store. Reconnect USB cable. |
| **"Trust This Computer" keeps reappearing** | Broken pairing record on PC. | Re-plug device, enter device passcode, and accept trust prompt. Restart PC if persistent. |
| **Installation fails with error code** | Insufficient storage space on iOS device, or corrupted IPA download. | Check device storage in Settings > General > iPhone Storage. Re-download IPA with `ipatool`. |
| **App installs but crashes on open** | Apple ID mismatch between `ipatool` account and device account. | Sign into the Apple ID used to download the app under **Settings > App Store** on the target device. |

---

## Method 2: Command-Line Installation via ideviceinstaller

If you prefer a pure CLI workflow or are on Linux/macOS, use `ideviceinstaller` directly:

```bash
# Verify device connection
idevice_id -l

# Install the package
ideviceinstaller -i /path/to/com.example.app_1.0.ipa
```

---

## Method 3: macOS Apple Configurator

On macOS:
1. Connect your device via USB.
2. Launch **Apple Configurator**.
3. Double-click your device icon.
4. Drag and drop the downloaded `.ipa` file directly onto the device window to install.
