# Research: App Store External Version Identifiers

Understanding the relationship between human-readable version numbers and Apple's internal identifier system.

---

## What is an External Version Identifier?

When an application developer submits a build through App Store Connect, the store ingestion pipeline assigns an immutable 64-bit numerical identifier referred to in store manifests as:

- `externalVersionIdentifier`
- `appExtVrsId`

Unlike `CFBundleShortVersionString` (e.g. `13.90.0`), which is arbitrary text decided by the developer, the external version ID is an integer value assigned sequentially by Apple's servers.

---

## Observing Version Metadata

Using the `get-version-metadata` interface, researchers can observe:

1. **`externalVersionID`**: The numeric index.
2. **`displayVersion`**: The marketing release version.
3. **`releaseDate`**: ISO timestamp marking when the binary was approved/staged on the CDN.

```json
{
  "externalVersionID": "885041606",
  "displayVersion": "13.90.0",
  "releaseDate": "2026-04-28T19:28:24Z"
}
```

---

## Automated Lookup Strategy

Because popular applications can have hundreds of historical version IDs, scanning sequentially can be optimized through binary search algorithms when release dates or monotonic ID trends are known.
