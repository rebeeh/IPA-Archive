# ipatool Common Errors & Troubleshooting Guide

This guide documents the most common errors encountered by users when using `ipatool`, compiled from real-world community issues, bug reports, and discussion threads.

---

## 1. Windows Keystore Passphrase Confusion

### The Symptom
```text
enter passphrase to unlock "C:\Users\<user>\.ipatool" (this is separate from your Apple ID password):
```

### Explanation & Solution
- **What it is**: `ipatool` on Windows creates an encrypted local database under `C:\Users\<user>\.ipatool` to store authentication tokens.
- **Why people get stuck**: Many users confuse this with their Apple ID password or Windows login password.
- **Solution**:
  - The first time you run `auth login`, `ipatool` prompts you to define a new passphrase to protect this directory. Whatever you typed then is the passphrase you must enter on future commands.
  - If you forgot this local passphrase, simply delete the folder `C:\Users\<your-username>\.ipatool` and log in again with `ipatool auth login`.
  - For automated scripts, you can supply `--keychain-passphrase "<passphrase>"` to bypass interactive prompts.

---

## 2. "license is required" Error

### The Symptom
```text
ERR error="license is required" success=false
```

### Explanation & Solution
- **What it is**: Apple will not allow an Apple ID to query versions or download an application unless that account holds an active "purchase" record for the app.
- **Solution for Free Apps**:
  Run the `purchase` command before querying or downloading:
  ```powershell
  ipatool purchase -b com.example.app
  ```
  Alternatively, you can add `--purchase` to the download command:
  ```powershell
  ipatool download -b com.example.app --external-version-id <ID> --purchase
  ```
- **Solution for Paid Apps**:
  `ipatool purchase` cannot buy paid apps. You must purchase the app legitimately in the App Store on an iOS device first using the same Apple ID. Once purchased, `ipatool` will be authorized to download any historical build.

---

## 3. Typographic / Unicode Dash Parsing Error

### The Symptom
```text
ERR error="unknown shorthand flag: 'â' in -—email" success=false
```

### Explanation & Solution
- **What it is**: Copying commands from blog posts, rich-text markdown, or certain mobile browsers often converts double hyphens (`--`) into an em-dash (`—`) or en-dash (`–`).
- **Solution**: Always ensure flags start with two standard ASCII minus characters (`--`):
  ```powershell
  # Correct:
  ipatool auth login --email user@example.com

  # Incorrect (broken unicode em-dash):
  ipatool auth login —email user@example.com
  ```

---

## 4. Email Format Confusion (`@icloud.com` vs Others)

### Explanation & Solution
- Many guides illustrate logins using `user@icloud.com`.
- **Reality**: You can use **any email address** associated with your Apple ID (e.g., `@gmail.com`, `@yahoo.com`, or custom domains). You do not need to register a separate iCloud address.

---

## 5. App Installs via USB but Closes Immediately on Launch

### The Symptom
App installs successfully (e.g. via AppManager or ideviceinstaller), but upon tapping the app icon on iOS, it immediately flashes and quits or prompts for credentials.

### Explanation & Solution
- **What it is**: Apple FairPlay DRM enforcement. The downloaded binary is encrypted with keys tied directly to the Apple ID that downloaded it.
- **Solution**:
  - Open **Settings > App Store** (or your primary Apple ID settings) on the iOS device.
  - Sign in with the exact same Apple ID used during `ipatool auth login`.
  - Once signed in, iOS validates the receipt stored inside the `.ipa` package (`SC_Info`), and the app will open without issue.

---

## 6. "failed to write file: unexpected EOF" or "failed to open zip reader"

### The Symptom
```text
ERR error="failed to download file: failed to write file: unexpected EOF" success=false
ERR error="failed to open zip reader" success=false
```

### Explanation & Solution
- **What it is**: Incomplete or corrupted download stream from Apple's CDN.
- **Common Causes**:
  1. **Low Disk Space**: The partition running `ipatool` does not have enough free space to buffer the package.
  2. **Network Interruption**: The connection timed out or dropped midway through the download.
  3. **Folder Permissions**: Running in a protected system directory without write permissions.
- **Solution**:
  - Run `ipatool` from a dedicated user directory (e.g., `C:\Tools\` or `~/Downloads/`).
  - Verify network stability and ensure sufficient disk space.
  - Re-run the download command to fetch a clean package.

---

## 7. tvOS & watchOS Apps Downloading

### Explanation & Solution
- By default, standard `ipatool` targets iOS binaries.
- To download watchOS, tvOS, or visionOS packages, ensure you are running `ipatool` v2.8.0 or newer, which includes platform flags:
  ```powershell
  ipatool download -b com.example.tvapp --external-version-id <ID>
  ```
- If an app is a universal purchase containing Apple TV builds, you can verify supported platforms using `ipatool search <AppName>` (look for the `"platforms"` array in the output).
