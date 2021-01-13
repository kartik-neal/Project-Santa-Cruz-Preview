# Release notes

## Release date: 01/12/2021

### New features and fixes

- Updated the OOBE package:
    - Added disconnect notification when connection to SoftAP is lost.
    - Use device capabilities to determine OOBE steps.
    - Added page to update the device's SoftAP passphrase.
    - Added additional EULAs.
- Updated hostname based on wlan0 instead of eth0 to resolve PE101 hostname auto-generation based on eth0 MAC, which is randomly generated.
- Wi-Fi and bluetooth can now be used simultaneously on Santa Cruz for achieving bluetooth certification.
- Removed unused rtc-efi from kernel config to allow system time sync on a battery-backed rtc.
- Fixed issues with RTC hwclock.
- Resolved system user uid/gid conflicts after update.
- Updated Azure-IOTEdge to 1.0.10.
- ADU (Azure Device Update) upgraded from v1 to v4.

## Release date: 10/28/2020

### New features and fixes

- A static, unique local IP address was set on the wlan1 interface, fd93:287f:adcc::1/64. Firewall rules were added to maintain parity with the IPv4 interface. The OOBE experience can be tested by using the following address in the browser: **your.new.device**.
- Updated UEFI binary with fix for reading SMBIOS. Solved PE101 showing as PE100 for PE101 hardware revision R1.01.
- OOBE page is opened automatically after connecting to device’s softAP.
- OOBE service shuts down automatically after 30 minutes.
- OOBE service shuts down automatically after OOBE completion.
- OOBE will introduce new module twin properties to azureeyemodule allowing the RTSP streams to be shut down for additional security.

## Release date: 09/15/2020 | Project Santa Cruz portal experiences

### New features and fixes

- Useful error messages added around registering resource providers.
- Added multi-word keyword support to speech templates.
- Added validation of app service plan count prior to deploying speech template.
- Several improvements for Azure Portal themes.
- Improved telemetry for speech no-code path.
- More telemetry events for tutorials and demos tab.
- Enabled healthcare theme.
- Users can now delete Custom Vision projects.
- Migrated Custom Command APIs from preview to v1.0.
- Added ability for first 50 devices to turn on telemetry events for the speech module.
- Added ability for users to upgrade the version of the speech module on their devices.
- Added pagination to browse device page.

## Release date: 08/05/2020 | Build: 1.0.20200731.2336

### New features and fixes

- SoftAP SSID changed to a more unique name (scz-<last 4 hex digits of wmac>).
- OOBE updates:
	- OOBE now waits for modules to start before showing the last screen.
	- Added link to be able to view the camera stream at the end of OOBE.
	- Added redirect to the Project Santa Cruz portal to last screen.
	- Updated EULA page.
- Updated the hostname to include "scz-" at the front.
- Moved to a UEFI-based carrier board image.
- Enabled Secure Boot and Update Verification with secure Private Preview keys.
- Added Preloaded Containers so that devices doesn’t have to download them at the end of OOBE.
- Added pushing Update images to Azure Blob Storage.
- Added Firmware and OS OTA update support.
- Added Watchdog rollback support.
- Deleted ffmpeg and apps that depended on ffmpeg from base image.
- Added ability to trigger USB flash mode from OS and automatically from U-Boot recovery mode.
- Various bug fixes.
