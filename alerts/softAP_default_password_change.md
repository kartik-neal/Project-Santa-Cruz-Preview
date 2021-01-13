# SoftAP default password change

### What is the change?

The default SoftAP password will be changing soon from “santacruz” to a device-specific, TPM-derived password.

SoftAP, or software-enabled access point, allows your device to act as a wireless access point/hotspot through its integrated Wi-Fi module. By connecting to your device's SoftAP hotspot, you can set your device settings through the [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/oobe.md) or [SSH into your device](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/general/troubleshooting/ssh_and_serial_connection_setup.md) for [troubleshooting](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/general/troubleshooting/general_devkit_troubleshooting.md) and [USB updates](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/usb_updating.md), even if your device is not yet connected to your home or office network over Wi-Fi or Ethernet.

### Which devices are affected?

Project Santa Cruz AI Perception Devkits.

### Why are we doing this?

As we move into our Public Preview stage, there are certain security configurations that need to be implemented. One of these security changes is to move away from a non-unique default SoftAP password to a unique device-specific password.

### When will this change happen?

In the build released on 01/26/2021 and all future updates.

### What should I do prior to the change?

New devices built and shipped after 11/17/2020 will contain a Welcome card with your device-specific, TPM-derived SoftAP password printed on a sticker. It is highly recommended that you keep this sticker so you can refer to it when needed.

If you do not have a sticker or it was misplaced, you will need to [retrieve your TPM-derived password](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/tools/SoftAP-access-info-tool/README.md) from the device prior to installing the build released on 01/26/2021.  

### Does this affect my manually-set SoftAP password?

We’ve created a new OOBE flow that allows users to manually set their SoftAP password. If you have not manually set your SoftAP password, you may do so through [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/oobe.md) at any time. However, this password will be lost after performing a [USB update with the UUU tool](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/usb_updating.md#usb-update-method-2-nxp-uuu-tool) (see FAQs below for more information). 

To ensure access to your device's SoftAP network, make sure to [retrieve your TPM-derived password](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/tools/SoftAP-access-info-tool/README.md) prior to performing a USB update with the UUU tool. After updating your device, you may reset your password through OOBE. 

### FAQs

**Q**: How will device updates affect my SoftAP password that I manually set through OOBE?

**A**: Your manually-set password will be lost after a [USB update with the UUU tool](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/usb_updating.md#usb-update-method-2-nxp-uuu-tool). In this case, the update will wipe all device configuration settings and will reset your device to a factory clean state. You will need to re-run OOBE to set your user-configured SoftAP password again. **Until then, you will only be able to log in to your SoftAP network with your TPM-derived password.**

[OTA updates](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/ota_update.md) via ADU and [USB updates performed through a USB storage device](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/usb_updating.md#usb-update-method-1-usb-storage-device) will preserve your user configuration state, and your manually-set SoftAP password will remain intact.

Your device-specific, TPM-derived SoftAP password is unaffected by any firmware or OS update and remains unchanged across all update scenarios. This also applies to the current default password, "santacruz," until the build released on 01/26/2021 and thereafter.

**Q**: How do I contact support?

**A**: If you are unable to run the [scz-tool-wifisoftap-accessinfo.devkit.sh](https://github.com/microsoft/Project-Santa-Cruz-Preview/tree/main/tools/SoftAP-access-info-tool) tool or have misplaced the device-specific, TPM-derived SoftAP password, please open a [support request](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/general/get-support.md).
