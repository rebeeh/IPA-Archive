# Getting Started with Package Retrieval

This guide covers the foundational steps for querying App Store metadata and retrieving specific application packages via command-line utilities.

## Prerequisites

- A command-line terminal (PowerShell 5.1/7 on Windows, Terminal on macOS/Linux).
- `ipatool` binary (version 2.8.0 or later recommended).
- An Apple ID account.

---

## Step 1: Authentication

Storefront queries require authenticated sessions to obtain license validation.

```bash
ipatool auth login --email user@example.com
```

- When prompted, provide your account password and the two-factor authentication (2FA) verification code.
- If running on Windows, `ipatool` requests a local encryption passphrase to secure the credentials stored at `~/.ipatool`.

---

## Step 2: Querying Identifiers

1. **Search for the app**:
   ```bash
   ipatool search "App Name"
   ```
   Note the `bundleID` (e.g., `com.toyopagroup.picaboo`) and numeric `id`.

2. **Obtain license (if needed)**:
   For free applications, ensure your Apple ID holds a purchase receipt:
   ```bash
   ipatool purchase -b <bundleID>
   ```

3. **List historical external version IDs**:
   ```bash
   ipatool list-versions -b <bundleID> --format json
   ```
   This returns an array of numerical IDs corresponding to previous releases registered in the store catalog.

---

## Step 3: Resolving Version Numbers

External version identifiers are sequential internal keys rather than semantic version strings (e.g., `885041606` vs `13.90.0`).

Use `get-version-metadata` to inspect an ID:
```bash
ipatool get-version-metadata -b <bundleID> --external-version-id <ID> --format json
```

Response format:
```json
{
  "level": "info",
  "externalVersionID": "885041606",
  "displayVersion": "13.90.0",
  "releaseDate": "2026-04-28T19:28:24Z",
  "success": true
}
```

---

## Step 4: Package Retrieval

Once the correct version ID is identified, issue the download request:

```bash
ipatool download -b <bundleID> --external-version-id <ID>
```

The resulting `.ipa` file will be saved in your current working directory.
