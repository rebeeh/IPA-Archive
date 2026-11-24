# Recommended Tools & Utilities

A curated matrix of open-source tools and utilities for iOS application package retrieval, metadata research, and device deployment.

---

## 1. Package Retrieval & Metadata Tools

### [ipatool](https://github.com/majd/ipatool)
- **Author**: Majd Alfhaily
- **Platforms**: Windows, macOS, Linux
- **License**: MIT
- **Purpose**: Authenticates directly with Apple's App Store APIs to search apps, query licensing, enumerate historical version identifiers, and retrieve `.ipa` packages.

### [mitmproxy](https://mitmproxy.org/) / Charles Proxy
- **Platforms**: Windows, macOS, Linux
- **Purpose**: HTTP/HTTPS traffic inspection for observing and debugging Storefront requests and responses.

---

## 2. Device Deployment Tools

### [AppManager](https://git.kawaiizenbo.me/kawaiizenbo/AppManager)
- **Author**: KawaiiZenbo
- **Platform**: Windows (GUI)
- **Source**: [https://git.kawaiizenbo.me/kawaiizenbo/AppManager](https://git.kawaiizenbo.me/kawaiizenbo/AppManager)
- **Releases**: [Download Latest Release](https://git.kawaiizenbo.me/kawaiizenbo/AppManager/releases)
- **Purpose**: A native Windows GUI wrapper around `ideviceinstaller` that allows one-click installation and removal of `.ipa` packages onto connected iOS devices over USB. Ideal for deploying IPAs retrieved with `ipatool` onto stock or jailbroken devices.

### [libimobiledevice / ideviceinstaller](https://libimobiledevice.org/)
- **Platforms**: Linux, macOS, Windows
- **Purpose**: The foundational open-source protocol library for communicating with iOS devices natively without Apple proprietary libraries.

### [Apple Configurator](https://apps.apple.com/us/app/apple-configurator/id1037126344)
- **Author**: Apple Inc.
- **Platform**: macOS
- **Purpose**: Official utility for managing and deploying enterprise profiles and `.ipa` packages over USB.

---

## 3. Version Archive & Identifier References

- **ipatool CLI**: Native command `ipatool list-versions -b <bundleID>` and `ipatool get-version-metadata`.
- **armconverter.com**: Historical iOS app version database.
- **ipafilezone.st**: Community index for historical external version IDs.
