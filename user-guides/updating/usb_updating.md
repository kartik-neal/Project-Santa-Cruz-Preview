# USB updating

This guide will show you how to update the carrier board of the Project Santa Cruz Development Kit with a new image file over USB. Ensure all prerequisites corresponding to your selected USB update method are satisfied before working through the update procedure.

There are three USB update methods:

- Method #1: .swu file with a USB storage device.
- Method #2: .raw file with the NXP UUU tool.
- Method #3: variation of method #2 for non-standard situations (e.g. your device does not boot).

Please note that Method #1 keeps the data intact on the device, while Method #2 and #3 will delete the contents of your device's data partition during the update process. If your data is deleted during the update process (i.e. has been reset to factory settings), you will need to work through the [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/oobe.md) again to set up WiFi connections, SSH login information, etc.

## USB update method #1: USB storage device

### Method #1 prerequisites

- Windows or Linux PC with an available USB port.

- USB storage device.

- Devkit carrier board (Note: the carrier board needs to be running a software version from September 16, 2020 (2020.109.116.120) or later. See step 4 below to confirm the software version of your device. If your software version is not from September 16, 2020 or later, please update your device [over-the-air (OTA)](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/ota_update.md) or use method #2 or #3 below.)

- [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) (optional).

### USB storage device update procedure

1. Navigate to the [Project Santa Cruz update management website](https://projectsantacruz.microsoft.com/Download) and download the **Microsoft-PE-101-\<version>.swu** file for your target build (this will be listed as an OTA update file).

    ![Project Santa Cruz update management website page with OTA files highlighted.](./images/ota_download_update.png)

1. Copy the .swu file onto an empty USB storage device.

1. Connect the USB storage device to the carrier board of your Project Santa Cruz devkit.

1. Update your device:

    1. Option 1: use PuTTY to reboot the device.

        - Open PuTTY and [SSH into your device](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/general/troubleshooting/ssh_and_serial_connection_setup.md#ssh-into-the-devkit).

        - To confirm the current software version, enter the following into the PuTTY terminal. Do **NOT** proceed with the update if your software version is not from September 16, 2020 (2020.109.116.120) or later.

            ```bash
            cat /etc/adu-version
            ```

        - Once you are ready to start the update, enter:

            ```bash
            reboot
            ```

        - Once the device has rebooted, SSH into the device again and run ```cat /etc/adu-version``` to check the software version and confirm that the update was successful.

    1. Option 2: use the physical on/off button on the left side of the carrier board to reboot the device.

        - Hold the button for a couple seconds to turn the device off.

        - Once it has completely powered down, turn it back on again.

        - To check the software version and confirm that the update was successful, go to your IoT hub in the [Azure portal](https://portal.azure.com/?feature.canmodifystamps=true&Microsoft_Azure_Iothub=aduprod&microsoft_azure_marketplace_ItemHideKey=Microsoft_Azure_ADUHidden#home). Navigate to your device page and click **Device Twin**. Scroll down and find **swVersion**. You may need to refresh the page.
        
         ![Device twin page in Azure portal.](./images/usb_device_twin.png)

### Common issues

- Make sure the .swu file is directly at the root of the USB storage device and not under a directory.

- The NTFS USB file system is not supported as it is not readable by the devkit’s kernel. Please use an alternate USB file system.

### Common error messages

To access error messages after attempting an update, [SSH into your device](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/general/troubleshooting/ssh_and_serial_connection_setup.md#ssh-into-the-devkit) after it has rebooted and enter ```journalctl -xe -u usb-update``` in the PuTTY terminal. This will show all logs from usb-update, from newest to oldest. However, as a first step, we recommend verifying the update by checking the image version with ```/etc/adu-version```. If the version has not changed, check the usb-update logs for the error messages listed below. 

|Error Message - Status|Issue    |Solution  |
|----------------------|---------|----------|
|NoOp\|NO_USBDEVICES (2) |No USB device plugged in. |Ensure the USB storage device is plugged in.|
|Error\|INSTALL_ERROR (13) |The .swu update file version is the same as the SW version on the device. |Select a different .swu update file version.|
|Success (0) |None (connected USB device with valid .swu file). | |
|NoOp\|NO_SWU_FOUND (2) |USB device plugged in, but no .swu file found. |Ensure you have a .swu file on your USB storage device. To find the latest files, navigate to the [Project Santa Cruz update management website](https://projectsantacruz.microsoft.com/Download).|
|ESRCH (3) |Multiple .swu files found on a single USB device. |Ensure you only have one .swu file (i.e. the one you wish to update to).|
|ESRCH (3) |Multiple .swu files found across multiple USB devices. |Ensure you only have one USB storage device with one .swu file.|
|Error\|INSTALL_ERROR (13) |Incorrect .swu file (e.g. bad signature, incorrect file). |Ensure you are using the correct .swu file. |
|ESRCH (2) |Unrecognized file system/unexpected error. |Ensure you are using a supported USB file system (NTFS USB file system is not supported).|

## USB update method #2: NXP UUU tool

### Method #2 prerequisites

- Windows or Linux PC an available USB-C or USB-A port.

- Carrier board and USB-C cable, included in the Project Santa Cruz Development Kit. If your PC has a USB-A port but not a USB-C port, you may use a USB-C to USB-A cable (sold separately).  

- [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).

- [NXP UUU tool](https://github.com/NXPmicro/mfgtools/releases). Download the **Latest Release** uuu.exe file (for Windows) or the uuu file (for Linux) under the Assets tab.

    ![nxp](./images/usb_nxp.png)

- [7zip](https://www.7-zip.org/). This software will be used for extracting the raw image file from its XZ compressed file. Download and install the appropriate .exe file.

### UUU tool update procedure

1. On your PC, navigate to the [Project Santa Cruz update management website](https://projectsantacruz.microsoft.com/Download). Download the full devkit image (**pe101-uefi-\<version>.raw.xz**) and the associated **emmc_full.txt** and **fast-hab-fw.raw** files (these will be listed as USB update files).

    ![update_download](./images/usb_update_download.png)

1. Extract the **pe101-uefi-\<version>.raw** file from the compressed **pe101-uefi\<version>.raw.xz** file. Right click on the .xz image file and select **7-Zip** > **Extract Here**.  

1. Copy the extracted **pe101-uefi-\<version>.raw** file and the associated **emmc_full.txt** and **fast-hab-fw.raw** files to the folder containing the UUU tool (uuu.exe for Windows or uuu for Linux).  

1. Plug in the carrier board power cable and turn on the device.  

1. Open PuTTY and [SSH into your device](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/general/troubleshooting/ssh_and_serial_connection_setup.md#ssh-into-the-devkit).

1. Next, open a Windows command prompt (**Start** > **cmd**) or a Linux terminal and navigate to the folder where the update files are stored. Run the following command to initiate the update:

    - Windows:

        ```bash
        uuu -b emmc_full.txt fast-hab-fw.raw pe101-uefi-<version>.raw  
        ```

    - Linux:

        ```bash
        sudo ./uuu -b emmc_full.txt fast-hab-fw.raw pe101-uefi-<version>.raw  
        ```

    ![cmd_flash](./images/usb_cmd_flash.png)  

1. Connect the supplied USB-C cable to the carrier board's USB-C port and to the host PC. If you are using a USB-C to USB-A cable (sold separately), connect the USB-A side to the PC and the USB-C side to the carrier board.

1. In the PuTTY terminal, enter the following commands. If you are not signed into SSH as root, please add ```sudo``` to the beginning of these commands.

    1. Set the device to usb update mode:

        ```bash
        flagutil    -wBfRequestUsbFlash    -v1
        ```

    1. Reboot the device. The update installation will begin.

        ```bash
        reboot -f
        ```

        ![putty_usb_update_mode](./images/usb_putty_usb_update_mode.png)

1. Navigate back to the command prompt. When the update is finished, you will see the following screen with ```Success 1```:

    ![update_complete](./images/usb_update_complete.png)
  
1. Once the update is complete, power off the carrier board. Unplug the USB cable from the PC.  

1. Power the carrier board back on.

1. To verify the update, [SSH into your device](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/general/troubleshooting/ssh_and_serial_connection_setup.md#ssh-into-the-devkit) and enter the following command to check the software version:

    ```bash
    cat /etc/adu-version
    ```

    The terminal will display the current software version, which should match the installed update.

    ![putty_terminal](./images/ota_putty_terminal.png)

## USB update method #3: non-standard situations

There are a few situations where it is not possible to gracefully USB update (re-flash) the carrier board (e.g. if you need to recover an unbootable device). In these situations, please follow this guidance.

### Method #3 prerequisites

- Windows or Linux PC with an available USB-C or USB-A port.

- Carrier board and USB-C cable, included in the Project Santa Cruz Development Kit. If your PC has a USB-A port but not a USB-C port, you may use a USB-C to USB-A cable (sold separately).

- [NXP UUU tool](https://github.com/NXPmicro/mfgtools/releases). Download the **Latest Release** uuu.exe file (for Windows) or the uuu file (for Linux) under the Assets tab.

- [7zip](https://www.7-zip.org/). This software will be used for extracting the raw image file from its XZ compressed file.  Download and install the appropriate .exe file.

### Non-standard USB update procedure

1. On your PC, navigate to the [Project Santa Cruz update management website](https://projectsantacruz.microsoft.com/Download). Download the full devkit image (**pe101-uefi-\<version>.raw.xz**) and the associated **emmc_full.txt** and **fast-hab-fw.raw** files (these will be listed as USB update files).

1. Extract the **pe101-uefi-\<version>.raw** file from the compressed **pe101-uefi\<version>.raw.xz** file. Right click on the .xz image file and select **7-Zip** > **Extract Here**.  

1. Copy the extracted **pe101-uefi-\<version>.raw** file and the associated **emmc_full.txt** and **fast-hab-fw.raw** files to the folder containing the UUU tool (uuu.exe for Windows or uuu for Linux).  

1. Toggle the Boot Configuration DIP switches to 1011 so the device will boot into USB flash mode. If you have an early version of the devkit that includes an SD card, remove the card.

1. Next, open a Windows command prompt (**Start** > **cmd**) or a Linux terminal and navigate to the folder where the update files are stored. Run the following command to initiate the update:

    - Windows:

        ```bash
        uuu -b emmc_full.txt fast-hab-fw.raw pe101-uefi-<version>.raw  
        ```

    - Linux:

        ```bash
        sudo ./uuu -b emmc_full.txt fast-hab-fw.raw pe101-uefi-<version>.raw  
        ```

1. Connect the supplied USB-C cable to the carrier board's USB-C port and to the host PC. If you are using a USB-C to USB-A cable (sold separately), connect the USB-A side to the PC and the USB-C side to the carrier board.

1. Power on the device.

1. Wait for the UUU tool to complete the update, then power down the carrier board and disconnect the USB cable.

1. Toggle the DIP switches to eMMC boot mode (1001).

## Provide feedback

After completing the USB update experience as well as the [OTA OS update experience](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/ota_update.md) and [OTA firmware update experience (Eye/Ear SoM)](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/ear_som_firmware.md), please provide feedback on your experience via this [questionnaire](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR-EYOjUzOMlKvDaulVXd95tUNDc1V05EMDA2NjBRVDc5UlZBMVkwRjRNQSQlQCN0PWcu). Your feedback will help us continue to fine-tune and improve the update experiences.

For more information on Project Santa Cruz Quests and to provide feedback on other experiences, please visit the [test scenarios page](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/general/test-scenarios.md).
