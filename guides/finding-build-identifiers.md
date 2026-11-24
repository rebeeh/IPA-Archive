# Finding Build Version Identifiers

When targeting a specific historical version of an iOS application, one of the primary hurdles is converting a human-readable version string (such as `13.90.0`) into Apple's internal `externalVersionIdentifier` (such as `885041606`).

This guide details how to efficiently look up and verify version identifiers using web databases like **IPA File Zone** and the `ipatool` CLI.

---

## The Challenge: Raw Version Identifiers

When you run:
```powershell
ipatool.exe list-versions -b com.toyopagroup.picaboo --format json
```
Apple's Storefront returns a list of hundreds or thousands of unmapped integers:
```json
["3880712", "3933851", ..., "884513024", "885041606", "895519329"]
```
Querying each ID individually using `ipatool get-version-metadata` for large apps can take hundreds of requests. Using a version index database drastically reduces this process to a single lookup.

---

## Method 1: IPA File Zone (Recommended Web Database)

**IPA File Zone** ([ipafilezone.st](https://ipafilezone.st/)) maintains a public catalog indexing historical iOS releases and their corresponding App Store external version IDs.

### 1. Locate the App Page
Navigate directly using the app's numeric App Store ID or search interface:

```text
https://ipafilezone.st/app/<developer-slug>/<app-name>/<app-store-id>
```

**Example (Snapchat)**:
```text
https://ipafilezone.st/app/snap-inc/snapchat/447188370
```

### 2. Inspect the Version History Table
On the app page, scroll down to the **Version History** section:
- **Version String**: The public marketing version (e.g. `13.90.0`, `13.88.0`).
- **Release Date**: The date when Apple approved and released the build.
- **External Version ID**: The exact numeric ID assigned by Apple (e.g. `885041606`).

| Marketing Version | Release Date | External Version ID |
| :--- | :--- | :--- |
| **13.90.0** | April 28, 2026 | `885041606` |
| **13.88.0** | April 14, 2026 | `884513024` |
| **1.0** | July 07, 2011 | `3880712` |

### 3. Copy the Identifier
Copy the target **External Version ID** directly for download.

---

## Method 2: Verifying the Identifier with ipatool

Before initiating a full package download, you can confirm that the identifier retrieved from IPA File Zone matches the official Storefront metadata.

Run:
```powershell
ipatool.exe get-version-metadata -b <bundleID> --external-version-id <ID> --format json
```

**Example**:
```powershell
ipatool.exe get-version-metadata -b com.toyopagroup.picaboo --external-version-id 885041606 --format json
```

**Output**:
```json
{
  "level": "info",
  "externalVersionID": "885041606",
  "displayVersion": "13.90.0",
  "releaseDate": "2026-04-28T19:28:24Z",
  "success": true
}
```

Once `displayVersion` matches your target, proceed with downloading the `.ipa`.

---

## Method 3: Downloading with the Identifier

With the verified external version identifier, download the package directly:

```powershell
ipatool.exe download -b com.toyopagroup.picaboo --external-version-id 885041606
```

Output:
```text
INF output="com.toyopagroup.picaboo_447188370_13.90.0.ipa" purchased=false success=true
```

---

## Alternative Version Databases

- **[armconverter.com](https://armconverter.com/decryptedappstore)**: Additional community database cataloging iOS builds and bundle metadata.
- **Lancely App Store Lookup**: Historical database for App Store pricing, version strings, and build IDs.
