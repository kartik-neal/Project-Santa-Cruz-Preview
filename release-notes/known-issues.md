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
| No code speech | Creating custom keywords during the no code speech path is not supported within the Azure portal. | Use Speech Studio to [train custom keywords](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/voice-assistant-config.md#create-custom-keyword). |
| Device update | Containers do not run after an OTA update. | SSH into the device and restart the Iot Edge container with this command `systemctl restart iotedge`. This will restart all containers. |
| Device update | Users may get a message that the update failed, even if it succeeded. | Confirm the device updated by navigating to the Device Twin for the device in IoT Hub. This is fixed after the first update. |
| Device update | Users may lose their Wi-Fi connection settings after their first update. | Run through OOBE after updating to setup the Wi-Fi connection. This is fixed after the first update. |
| Dev Tools Pack Installer | Optional Caffe install may fail if Docker is not running properly on system. | Make sure Docker is installed and running, then retry Caffe installation. |
| Dev Tools Pack Installer | Optional CUDA install fails on incompatible systems. | Verify system compatibility with CUDA prior to running installer. |
| Docker, Network, IoT Edge | If your internal network uses 172.x.x.x, docker containers will fail to connect to edge. | Add a special bip section to the /etc/docker/daemon.json file like this: `{    "bip": "192.168.168.1/24"}` |