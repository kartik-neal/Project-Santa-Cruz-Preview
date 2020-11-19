# Collect your device’s TPM-derived SoftAP password

The [SoftAP Tool](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/tools/SoftAP-access-info-tool/scz-tool-wifisoftap-accessinfo.devkit.sh) allows you to access your Project Santa Cruz AI Perception Devkit’s TPM-derived SoftAP password and print it to the console.

New devices built and shipped after 11/17/2020 will contain a Welcome card with your unique SoftAP password printed on a sticker. It is highly recommended that you keep this sticker so you can refer to it when needed. If you do not have a sticker or it was misplaced, you will need to complete the following tasks to retrieve your TPM-derived password from the device.

## What is SoftAP?

SoftAP, or software-enabled access point, allows your device to act as a wireless access point/hotspot through its integrated Wi-Fi module. By connecting to your device's SoftAP hotspot, you can set your device settings through the [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/oobe.md) or [SSH into your device](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/general/troubleshooting/ssh_and_serial_connection_setup.md) for [troubleshooting](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/general/troubleshooting/general_devkit_troubleshooting.md) and [USB updates](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/usb_updating.md), even if your device is not yet connected to your home or office network over Wi-Fi or Ethernet.

## Prerequisites

- [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
- Host PC
- Project Santa Cruz AI Perception Devkit (PE100 or PE101)
- Devkit IP address

> [!NOTE]
> If your devkit is connected to the SoftAP, your device's IP address will be 10.1.1.1. If your devkit is connected over Ethernet, use the local IP address of the devkit, which you can get from the Ethernet router or hub. If your devkit is connected over Wi-Fi, you must use the IP address that was provided during the [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/oobe.md).

## Using the tool

1. Power on your device.

1. Download the [SoftAP tool](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/tools/SoftAP-access-info-tool/scz-tool-wifisoftap-accessinfo.devkit.sh).

1. Copy the tool to your device by entering the following command into a command prompt or terminal:

    ```
    scp [local file path]\scz-tool-wifisoftap-accessinfo.devkit.sh root@[remote server]:/[path to destination]
    ```

    In this case, ```[remote server]``` is the IP address of your device. ```[path to destination]``` is the folder on your device which you would like to copy the file to. You may be prompted to enter the root SSH password for your device (p@ssw0rd).

1. Open PuTTY and [SSH into your device](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/general/troubleshooting/ssh_and_serial_connection_setup.md).

1. In the PuTTY terminal, navigate to the folder containing the SoftAP tool and enter the following command to change the permissions of the file to allow execution:

    ```
    chmod 755 ./scz-tool-wifisoftap-accessinfo.devkit.sh
    ```

1. Execute the file on your device to output your TPM-derived SoftAP password:

    ```
    ./scz-tool-wifisoftap-accessinfo.devkit.sh -m=pe101
    ```

    > [!NOTE]
    > If your device model is PE100, change the above command to ```./scz-tool-wifisoftap-accessinfo.devkit.sh -m=pe100```.

    Example output:

    ```
    Wifi-SoftAP MAC Address: 1234567890ab
    Wifi-SoftAP SSID: scz-0000
    Wifi-SoftAP Pre-Shared Key: asdf1234  
    ```

1. The ```Wifi-SoftAP Pre-Shared Key``` is your devkit’s TPM-derived SoftAP password. Write down and securely store this password.
