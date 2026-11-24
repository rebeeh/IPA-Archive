# Windows Setup Guide

Detailed instructions for setting up your environment on Windows 10/11 using Windows PowerShell.

## Environment Requirements

- **Shell**: Windows PowerShell 5.1 or PowerShell 7+
- **Connectivity**: Apple Mobile Device Support (typically installed with Apple Devices app or iTunes)

---

## 1. Tool Installation

1. Download the latest `ipatool-windows-amd64.zip` from the project release page.
2. Extract the archive into a dedicated folder, such as `C:\Tools\ipatool-windows-amd64\`.
3. (Optional) Add the folder path to your user environment `PATH` variable.

---

## 2. Managing the Local Keystore

On Windows, `ipatool` prompts for a local passphrase to protect stored tokens under `C:\Users\<Username>\.ipatool`.
- Remember this passphrase; it is separate from your Apple ID password.
- You can pass `--keychain-passphrase "<passphrase>"` in non-interactive sessions if scripting queries.

---

## 3. Verifying Installation

Open PowerShell and execute:

```powershell
Set-Location "C:\Tools\ipatool-windows-amd64"
.\ipatool.exe --version
```

If successful, the version information is displayed.
