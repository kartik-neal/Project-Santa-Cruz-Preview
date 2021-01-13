﻿﻿﻿﻿
# Known issues

If you encounter any of these issues, it is not necessary to open a bug. If you have trouble with any of the workarounds, please open an Issue in GitHub.

|Area|Description of Issue|Workaround|
|:------|:--|:--|
| OOBE | Can’t complete OOBE unless device’s Wifi is configured (Azure login fails). | 1. SSH to the device access point (10.1.1.1) 2. Identify and copy the device ethernet IP address 3. Connect to OOBE using the copied ethernet IP based URL |
| OOBE | Clicking on links in the EULA during OOBE sometimes does not open a new web page. | Copy the link and open it in a separate browser window. |
| OOBE | Cannot work through OOBE when connected to a mobile Wi-Fi hotspot. | Connect your device directly to the SoftAP, a Wi-Fi network, or to a network over ethernet. |
| WiFi | The hardware button that toggles the Wifi SoftAP on and off sometimes does not work. | Continue to try pressing the button or reboot the device. |
| WiFi | Users may see a message after connecting to WiFI saying "This Wifi network uses an older security standard." | The devkit's hotspot/SoftAP uses the WEP encryption algorithm.  We will be updating this to WPA2 in a future update. |
| Device update | Containers do not run after an OTA update. | SSH into the device and restart the Iot Edge container with this command `systemctl restart iotedge`. This will restart all containers. |
| Device update | Users may get a message that the update failed, even if it succeeded. | Confirm the device updated by navigating to the Device Twin for the device in IoT Hub. This is fixed after the first update. |
| Device update | Users may lose their Wi-Fi connection settings after their first update. | Run through OOBE after updating to setup the Wi-Fi connection. This is fixed after the first update. |
| Device update | Users may get an error in the onboarding portal after trying to enable ADU. | Wait 1 hour after enabling ADU for the change to take effect. If the error persists, follow [these steps](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/ota_os_fw_update_prerequisites.md#common-issues). If you have already registered the device update resource provider, unregister and re-register the provider. |
| Device update | After performing an OTA update, users can no longer logon via SSH using previously created user accounts, and new SSH users cannot be created through OOBE. This issue affects systems performing OTA updates from the following pre-installed image versions: 2020.110.114.105 and 2020.109.101.105. | To recover your user profiles, preform these steps after the OTA update: <br> [SSH into your devkit](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/general/troubleshooting/ssh_and_serial_connection_setup.md) using “root” as the username. If you disabled the SSH “root” user login via OOBE, you must re-enable it. Run this command after successfully connecting: <br> ```mkdir -p /var/custom-configs/home; chmod 755 /var/custom-configs/home``` <br> To recover previous user home data, run the following command: <br> ```mkdir -p /tmp/prev-rootfs && mount /dev/mmcblk0p3 /tmp/prev-rootfs && [ ! -L /tmp/prev-rootfs/home ] && cp -a /tmp/prev-rootfs/home/* /var/custom-configs/home/. && echo "User home migrated!"; umount /tmp/prev-rootfs``` |
| Device update | After taking an OTA update, update groups are lost. | Update the device’s tag by following [these instructions](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/ota_update.md#method-1-using-direct-twin-updates-to-add-a-tag-easy). |
| Dev Tools Pack Installer | Optional Caffe install may fail if Docker is not running properly on system. | Make sure Docker is installed and running, then retry Caffe installation. |
| Dev Tools Pack Installer | Optional CUDA install fails on incompatible systems. | Verify system compatibility with CUDA prior to running installer. |
| Docker, Network, IoT Edge | If your internal network uses 172.x.x.x, docker containers will fail to connect to edge. | Add a special bip section to the /etc/docker/daemon.json file like this: `{    "bip": "192.168.168.1/24"}` |
