# Manufacturing Provisioning Tool Sample Script for Santa Cruz Devices

## Table of Tool Updates
| Version | Released Date | Description |
|--|--|--|
| 0.1.200417.1 | April 24, 2020 | Beta version released. |
| 0.2.200501.1 | May 20, 2020 | -Support PE101<br>-Provision/capture of Wifi ZTP key enabled. |
| 0.3.200706.1 | July 10, 2020 | -Support read S/N on Mariner OS and checking mechanism.<br>-Modified/Add new fields: "WifiDPP_MAC, "WifiDPP_PSK". |
| 0.4.200806.1 | August 15. 2020 | Minor bug fix. |
| 1.0.201112.1001 | November 13. 2020 | (Open source version)<br>-Rename WifiDPP_PSK to Wifi-SoftAP_PSK. |

## Introduction
**Manufacturing Provisioning Tool Sample Script for Santa Cruz devices** is a Linux shell script for Santa Cruz device manufacturers to <ins>capture the device identities or hardware keys in the manufacturing line</ins>. The tool will generate a “device record” with those hardware identities, output it directly or save to a JSON file.
The “device record” can then be used in post manufacturing process to provision each device to Azure as well as enabling Wi-Fi Zero Touch Provisioning scenario. However, **this tool only covers “collecting” the information for provisioning and does not handle the actual enrollment process to Azure**.

## Hardware requirement and Prerequisite
This script currently supports the following hardware. With minor customization (if necessary), it shall be able to support Santa Cruz device that loaded with Mariner OS.
 - PE100 (i.MX 8)
 - DKSC-101 (i.MX 8)

The tool must be executed with the following environment requirements:

 - Microsoft Mariner OS
	 - (With other dependences below fulfilled, this tool should be able to run on various of Linux distros, or just need minor modifications.)
 - TPM must be enabled
 - TPM tool package ([tpm2-tools v4.2](https://github.com/tpm2-software/tpm2-tools/wiki)) must be included
	 - For Wifi ZTP key feature, the version of tpm2-tools must be 4.2 or later. No action needed for PE100/DKSC-101 if using the private preview image.
 - The Serial Number of device shall be store in a permanent memory (e.g. EEPROM) and properly exposed to OS.

## Usage
**Syntax**

    aed-mfgtool-azuredeviceprovision.devkit.sh [-m|--model=<model_name>] [-n|--serialnum=<serial_number>] [--inittpm]
    [-h|--help] [-f|--file=<output_filename>] [-c|--checkrequired] [-o|--overridesn] [-q|--query]
**Parameters**    
Manufacturing featured options:

    -m, --model=<model_name> (Required)
        Name of supported models: pe100 pe101.
        (pe101 is for DKSC-101)
    -n, --serialnum=<serial_number> (Optional)
        Given serial number to be compared with what've read from hardware.
    -o, --overridesn (Optional)
        Override device record with given serial number instead of serial number read from hardware.
        (This approach is not recommended, but is an alternative when S/N is not yet store in the firmware.)
    -f, --file=<output_filename> (Optional)
        Redirect device record output from standard output to a file at /tmp.
    --inittpm (Optional)
        Clear TPM before to provision TPM.

Other options:

    -h, --help
	    Apply this option solely to show help messages.
    -c, --checkrequired
	    Apply this option with "-m=<model_name>" to run system requirement check and then exit.
    -q, --query
	    Apply this option with "-m=<model_name>" to run this tool in query mode (dry-run) without re-provisioning TPM.
**Executing and example**
To execute this tool. Copy the script file (aed-mfgtool-azuredeviceprovision.devkit.sh) to target device (PE100/DKSC-101) through SSH connection:

    scp [local file path]\aed-mfgtool-azuredeviceprovision.devkit.sh root@[remote server]:/[path to destination]
Make the script executable:

    chmod 755 ./aed-mfgtool-azuredeviceprovision.devkit.sh
Log on to the target device and execute the script:

[Example]
 - To run provisioning and check serial number on DKSC-101 device:
	 - `> ./aed-mfgtool-azuredeviceprovision.devkit.sh -m=pe101 -n=11111101111110011000 ; echo rc=$?`
 - To run provisioning without check serial number on DKSC-101 device:
	 - `> ./aed-mfgtool-azuredeviceprovision.devkit.sh -m=pe101 ; echo rc=$?`
 - To check system requirement on DKSC-101 device:
	 - `> ./aed-mfgtool-azuredeviceprovision.devkit.sh -m=pe101 -c ; echo rc=$? `

Output example:

    root@mariner-machine [ ~ ]# ./aed-mfgtool-azuredeviceprovision.devkit.sh -m=pe101 -n=11111101111110011000; echo rc=$?
    {
    "SerialNumber": "11111101111110011000",
    "LAN0MAC": "01:02:03:04:05:06",
    "TPM_EkPub": "AToAA...JznbfyQ==",
    "TPM_EkPub_Digest": "b5dk...baq",
    "WifiDPP_EccPub": "MFkw...piog==",
    "Wifi_MAC": "0A:0B:03:04:05:06",
    "Wifi-SoftAP_PSK": "sdf234wh"
    }
    rc=0

## Description of Outputs Data
The following device identity/information (if applicable to the hardware) shall exists before performing the capturing with the script.

 - SerialNumber
	 - This shall be the key for associate the other device identities with the actual hardware. (Microsoft strongly recommend that the the S/N should be visible on the device. That way, there is an easy way to associate physical device with its virtual copy on the Azure side.)
 - TPM_EkPub
	 - This key can be used as the secrete key for connecting device to   Azure IoTHub.
 - TPM_EkPub_Digest
	 - This hash can be used as the Enrollment Device ID for register the
   device to Azure DPS service.
 - LAN0MAC
	 - MAC address of the ethernet.
 - WifiDPP_EccPub
	 - This is a derivative ID from the TPM key. Used for enabling the Wi-Fi ZTP (Zero Touch Provisioning) feature.
 - Wifi_MAC
	 - Used for enabling the Wifi ZTP (Zero Touch Provisioning) feature. Can also serve as a secondary device identity if necessary.
**[Note]** WifiDPP_EccPub and Wifi_MAC are only required if the manufacturer want to enable the Wi-Fi ZTP feature and Wi-Fi module is included in the hardware design. However, pre-record the WifiDPP_EccPub at manufacturing would make the experience of future hardware/function expansion more seamless. (If there is a chance that SI/customer will install the Wi-Fi module and enable ZTP later, they would already have the ECC Key.)
 - Wifi-SoftAP_PSK
	 - This is also a derivative ID from the TPM key. Default password of the Wi-Fi SoftAP.

## Known Issue

 - [Fixed] Support for DKSC-101 to be enabled. 
 - [Fixed] Wi-Fi ZTP key   provisioning and capturing is not implemented yet. Will be providing in future version of script. 
 - [Won’t fix] For some early preview hardware, the tool cannot retrieve the completed S/N (last 4 digits will be “0000”). This is caused by a hardware issue, not an issue of
   the tool itself.

## Issue Reporting
For any issue and feedback relates to the manufacturing tool, please file an issue on GitHub.
1.	Log in to the [Project Santa Cruz Preview](https://github.com/microsoft/Project-Santa-Cruz-Preview/)
2.	Select Issues, then New issue.
3.	Use the following prefix “**[MFG Scrip]**”, followed by a clear title of issue.
4.	Provide clear description and attach the error log if any.
