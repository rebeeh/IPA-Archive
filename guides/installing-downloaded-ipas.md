# Installing Downloaded IPAs

Once an `.ipa` package has been retrieved from the App Store via `ipatool`, it contains legitimate FairPlay authorization signatures tied to the authenticated Apple ID.

---

## Method 1: AppManager (Recommended for Windows)

`AppManager` provides a lightweight native GUI to manage and install authentic iOS application packages over USB.

### Procedure

1. Connect your target iOS device to your PC via a USB cable.
2. Tap **Trust This Computer** on your iOS device and enter your passcode.
3. Launch `AppManager`.
4. Ensure your connected device is detected (e.g. `AppManager (Device Name, Model, iOS version)`).
5. Click **Install new**.
6. Select the downloaded `.ipa` package (for example: `com.toyopagroup.picaboo_447188370_13.90.0.ipa`).
7. Monitor the status log:
   ```text
   Connecting to device...
   Attempting install of C:\path\to\package.ipa
   Process ended with code 0 (Success)
   ```
8. The app icon will appear immediately on your home screen ready for execution.

> **Note**: Because the application package is cryptographically signed for your Apple account, your device must be signed in with or authorized for that same Apple ID to launch it without termination.

---

## Method 2: Command-Line Installation via ideviceinstaller

Cross-platform environments can utilize `libimobiledevice`:

```bash
ideviceinstaller -i /path/to/downloaded.ipa
```

---

## Method 3: macOS Apple Configurator

On macOS systems:
1. Connect device via USB.
2. Open **Apple Configurator**.
3. Drag and drop the downloaded `.ipa` onto the connected device panel to deploy.
