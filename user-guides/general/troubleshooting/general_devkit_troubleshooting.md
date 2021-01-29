# Project Santa Cruz development kit troubleshooting

## General devkit troubleshooting commands

To run these commands, connect to the devkit's Wi-Fi AP (if a Wi-Fi connection has not yet been set up through the [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md)), [SSH into the devkit using PuTTY](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/general/troubleshooting/ssh_and_serial_connection_setup.md), and enter the commands in the PuTTY terminal.

To redirect any output to a .txt file for further analysis, use the following syntax:

```console
[command] > [file name].txt
```

After redirecting output to a .txt file, copy the file to your host PC via SCP:

```console
scp [remote username]@[IP address]:[remote file path]/[file name].txt [local host file path]
```

[local host file path] refers to the location on your host PC which you would like to copy the .txt file to. [remote username] is the SSH username chosen during the [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md) setup process. If you did not set up an SSH login during the OOBE, your remote username is root.

For additional information on the Iot Edge commands, please see the [IoT Edge device troubleshooting documentation](https://docs.microsoft.com/en-us/azure/iot-edge/troubleshoot).

|Category:         |Command:                    |Function:                  |
|------------------|----------------------------|---------------------------|
|OS                |cat /etc/os-release         |check Mariner image version |
|OS                |cat /etc/os-subrelease      |check derivative image version |
|OS                |cat /etc/adu-version        |check ADU version |
|Temperature       |cat /sys/class/thermal/thermal_zone0/temp |check temperature of devkit |
|Wi-Fi             |journalctl -u hostapd.service |check SoftAP logs|
|Wi-Fi             |journalctl -u wpa_supplicant.service |check Wi-Fi services logs |
|Wi-Fi             |journalctl -u ztpd.service  |check Wi-Fi Zero Touch Provisioning Service logs |
|Wi-Fi             |journalctl -u systemd-networkd |check Mariner Network stack logs |
|Wi-Fi             |/data/misc/wifi/hostapd_virtual.conf |check wifi access point configuration details |
|OOBE              |journalctl -u oobe -b       |check OOBE logs |
|Telemetry         |azure-device-health-id      |find unique telemetry HW_ID |
|Iot Edge          |sudo iotedge check          |run configuration and connectivity checks for common issues |
|Iot Edge          |sudo iotedge logs [container name] |check container logs, such as speech and vision modules |
|Iot Edge          |sudo iotedge support-bundle --since 1h |collect module logs, IoT Edge security manager logs, container engine logs, 'iotedge check' JSON output, and other useful debug information from the past hour |
|Iot Edge          |sudo journalctl -u iotedge -f |view the logs of the IoT Edge security manager |
|Iot Edge          |sudo systemctl restart iotedge |restart the IoT Edge Security Daemon |
|IoT Edge          |sudo iotedge list           |list the deployed iotedge modules |
|Other             |df [option] [file]          |display information on available/total space in specified file system(s) |
|Other             |ip route get 1.1.1.1        |display device IP and interface information |
|Other             |ip route get 1.1.1.1 \| awk '{print $7}' <br> ifconfig [interface] |display device IP address only |

Note: The journalctl Wi-Fi commands can be combined into the following:

```console
journalctl -u hostapd.service -u wpa_supplicant.service -u ztpd.service -u systemd-networkd -b
```

## Docker troubleshooting commands

|Command:                        |Function:                  |
|--------------------------------|---------------------------|
|[docker ps](https://docs.docker.com/engine/reference/commandline/ps/) |shows which containers are running |
|[docker images](https://docs.docker.com/engine/reference/commandline/images/) |shows which images are on the device |
|[docker rmi [image id] -f](https://docs.docker.com/engine/reference/commandline/rmi/) |deletes an image from the device |
|[docker logs -f edgeAgent](https://docs.docker.com/engine/reference/commandline/logs/) <br> docker logs -f [module_name] |takes container logs of specified module |
|[docker image prune](https://docs.docker.com/engine/reference/commandline/image_prune/) |removes all dangling images |
|watch docker ps <br> watch ifconfig [interface] |check docker container download status |

## USB Updating

|Error:                                    |Solution:                                               |
|------------------------------------------|--------------------------------------------------------|
|LIBUSB_ERROR_XXX during USB flash via UUU |This error is the result of a USB connection failure during UUU updating. If the USB cable is not properly connected to the USB ports on the PC or the PE-10X, an error of this form will occur. Try unplugging and replugging both ends of the USB cable and jiggling the cable to ensure a secure connection. This almost always solves the issue. |

## Devkit carrier board LED states

There are three small LEDs on top of the carrier board housing. A cloud icon is printed next to LED 1, a Wi-Fi icon is printed next to LED 2, and an exclamation mark icon is printed next to LED 3. Please see the table below for information on each LED state.

|LED             |State      |Description                      |
|----------------|-----------|---------------------------------|
|LED 1 (IoT Hub) |On (solid) |Device is connected to an IoT Hub. |
|LED 2 (Wi-Fi)   |Slow blink |Device authentication in progress. |
|LED 2 (Wi-Fi)   |Fast blink |Authentication was successful, device association in progress. |
|LED 2 (Wi-Fi)   |On (solid) |Authentication and association were successful; device is connected to a Wi-Fi network. |
|LED 3           |NA         |LED not in use. |

> [!Note] devmmmodule is used to check the IoT Hub connection status. If the device does not have devmmmodule, LED 1 will remain off, even if the device is connected to an IoT Hub. It can also take 30 to 60 seconds after all modules are loaded and running on the device before devmmmodule sends the connection status to the LED.

### Device LED testing:

- Power on the devkit. Once the device finishes booting, LED 2 will slow blink.
- Start OOBE. After connecting to a Wi-Fi network, LED 2 will turn solid.
- Complete OOBE. After selecting an IoT Hub to connect your device to, wait for all device modules to deploy and start running. LED 1 will turn on (this may take an additional 30 to 60 seconds).