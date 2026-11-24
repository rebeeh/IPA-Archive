# Recommended Tools & Utilities Matrix

[🏠 Home](../README.md) • [📚 Guides Index](../README.md#-documentation-index) • [📥 Download Older Versions](../guides/downloading-older-versions.md) • [📲 Installation Guide](../guides/installing-downloaded-ipas.md)

---

## Overview

A curated matrix of active open-source tools, repositories, and databases for iOS package research, version querying, and physical device deployment.

---

## 1. CLI Retrieval & Analysis Tools

| Tool | Developer | Platform | Purpose | Links |
| :--- | :--- | :--- | :--- | :--- |
| **`ipatool`** | [Majd Alfhaily](https://github.com/majd) | Windows, macOS, Linux | Primary CLI for querying App Store APIs, licensing, listing version IDs, and downloading IPAs. | [GitHub](https://github.com/majd/ipatool) • [Releases](https://github.com/majd/ipatool/releases) |
| **`ipatool-rs`** | [Kosthi](https://github.com/Kosthi) | Cross-platform | High-performance Rust reimplementation of ipatool. | [GitHub](https://github.com/Kosthi/ipatool-rs) |
| **`mitmproxy`** | Mitmproxy Team | Windows, macOS, Linux | Interactive HTTPS proxy for intercepting and inspecting Apple Storefront requests. | [Website](https://mitmproxy.org/) |

---

## 2. Device Deployment & Management

| Tool | Developer | Platform | Purpose | Links |
| :--- | :--- | :--- | :--- | :--- |
| **`AppManager`** | [kawaiizenbo](https://git.kawaiizenbo.me/kawaiizenbo) | Windows (GUI) | Clean native GUI wrapper for `ideviceinstaller` to install, view, and manage IPAs over USB. | [Forgejo Repo](https://git.kawaiizenbo.me/kawaiizenbo/AppManager) • [Releases](https://git.kawaiizenbo.me/kawaiizenbo/AppManager/releases) |
| **`libimobiledevice`** | libimobiledevice Team | Windows, macOS, Linux | Foundation library and CLI tools (`ideviceinstaller`, `idevice_id`) for communicating with iOS devices over USB. | [Website](https://libimobiledevice.org/) • [GitHub](https://github.com/libimobiledevice) |
| **`Apple Configurator`** | Apple Inc. | macOS | Official Apple tool for managing and sideloading configuration profiles and IPAs on iOS hardware. | [Mac App Store](https://apps.apple.com/us/app/apple-configurator/id1037126344) |

---

## 3. Alternative Graphical Frontends

| Tool | Developer | Platform | Purpose | Links |
| :--- | :--- | :--- | :--- | :--- |
| **`ipatool-gui`** | Mehmet Akif Şimşek | Windows, macOS | Graphical desktop user interface for interacting with `ipatool`. | [GitHub](https://github.com/mehmetakifsimsek/ipatool-gui) |
| **`pyIPATool-WebUI`** | [jschmudd14](https://github.com/jschmudd14) | Web Browser | Web UI interface built around ipatool with enhanced support for tvOS downloads. | [GitHub](https://github.com/jschmudd14/pyIPATool-WebUI) |

---

## 4. Version Databases & Community References

- [**IPA File Zone**](https://ipafilezone.st/): Catalog of App Store releases, release dates, and `externalVersionIdentifier` mappings.
- [**armconverter.com**](https://armconverter.com/decryptedappstore): Searchable index of decrypted binaries, bundle IDs, and architecture info.
- [**qnblackcat's Gist**](https://gist.github.com/qnblackcat/4f7b77f685ccda2ff4ef916a27d66107): The original community discussion thread for older version downloads.

---

[⬅️ Troubleshooting](../troubleshooting/ipatool-errors.md) • [Finding Build Identifiers ➡️](../guides/finding-build-identifiers.md)
