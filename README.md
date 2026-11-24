# IPA Archive

> An open-source research project and reference documentation for iOS application package retrieval, version identifier resolution, and deployment.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue.svg)](#platform-support)

---

## Overview

**IPA Archive** is an educational and technical documentation repository exploring the distribution mechanisms of iOS application packages (`.ipa`). It focuses on the command-line discovery of historical build metadata using tools such as `ipatool`, mapping internal App Store numeric version identifiers, and deploying authenticated application builds to test hardware.

### Key Objectives

- **Metadata Exploration**: Documenting how Storefront APIs map bundle identifiers to monotonic release identifiers (`externalVersionIdentifiers`).
- **Reproducible Retrieval**: Step-by-step documentation for command-line package authentication and acquisition via `ipatool`.
- **Target Deployment**: Workflows for deploying authentic signed packages to test devices using tools like `AppManager`.
- **Ecosystem Preservation**: Providing a modern alternative to legacy proxy interception methods.

---

## Workflow at a Glance

```text
+-----------------------+     +-------------------------------+     +----------------------------+
| 1. Find Application   | --> | 2. Enumerate Identifiers      | --> | 3. Query Version Metadata  |
| bundleID & App ID     |     | list-versions --format json   |     | get-version-metadata       |
+-----------------------+     +-------------------------------+     +----------------------------+
                                                                                  |
                                                                                  v
+-----------------------+     +-------------------------------+     +----------------------------+
| Done: Installed       | <-- | 5. Deploy to Device           | <-- | 4. Retrieve Package (.ipa) |
| Active on Target      |     | AppManager / MobileDevice     |     | download --external-version|
+-----------------------+     +-------------------------------+     +----------------------------+
```

---

## Quick Reference

### 1. Authenticate with Storefront
```powershell
ipatool.exe auth login --email your-apple-id@example.com
```

### 2. Locate Application
```powershell
ipatool.exe search "Target App"
```

### 3. List All Available Version Identifiers
```powershell
ipatool.exe list-versions -b com.example.app --format json
```

### 4. Resolve Target Release Metadata
```powershell
ipatool.exe get-version-metadata -b com.example.app --external-version-id <ID> --format json
```

### 5. Download Target Package
```powershell
ipatool.exe download -b com.example.app --external-version-id <ID>
```

### 6. Install to Connected Device
Deploy the downloaded `.ipa` package using [AppManager](https://git.kawaiizenbo.me/kawaiizenbo/AppManager) (Windows GUI) or `ideviceinstaller` to your paired iOS device. See [Installing Downloaded IPAs](guides/installing-downloaded-ipas.md) for full instructions.

---

## Documentation Structure

- [Guides](guides/)
  - [Getting Started](guides/getting-started.md)
  - [Windows Setup](guides/windows-setup.md)
  - [Device Installation via AppManager & CLI](guides/installing-downloaded-ipas.md)
- [Tools & Ecosystem](tools/)
  - [Recommended Tools](tools/useful-tools.md)
- [Research Notes](research/)
  - [Version Identifiers](research/external-identifiers.md)

---

## Disclaimer & Terms

This project is strictly for research, software compatibility verification, and digital preservation. It does not host, distribute, or circumvent copyright protection for any proprietary software binaries. Users must authenticate with their own legitimate Apple accounts.
