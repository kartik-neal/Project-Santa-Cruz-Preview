
# Welcome to the Project Santa Cruz Private Preview

## **BREAKING CHANGE ALERT**

#### What is the change?

The default SoftAP password will be changing soon from “santacruz” to a device-specific, TPM-derived password.

SoftAP, or software-enabled access point, allows your device to act as a wireless access point/hotspot through its integrated Wi-Fi module. By connecting to your device's SoftAP hotspot, you can set your device settings through the [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/oobe.md) or [SSH into your device](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/general/troubleshooting/ssh_and_serial_connection_setup.md) for [troubleshooting](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/general/troubleshooting/general_devkit_troubleshooting.md) and [USB updates](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/usb_updating.md), even if your device is not yet connected to your home or office network over Wi-Fi or Ethernet.

#### Which devices are affected?

Project Santa Cruz AI Perception Devkits.

#### Why are we doing this?

As we move into our Public Preview stage, there are certain security configurations that need to be implemented. One of these security changes is to move away from a non-unique default SoftAP password to a unique device-specific password.

#### When will this change happen?

In the build released on 12/08/2020.

#### What should I do prior to the change?

New devices built and shipped after 11/17/2020 will contain a Welcome card with your device-specific, TPM-derived SoftAP password printed on a sticker. It is highly recommended that you keep this sticker so you can refer to it when needed.

If you do not have a sticker or it was misplaced, you will need to [retrieve your TPM-derived password](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/tools/SoftAP-access-info-tool/README.md) from the device prior to installing the build released on 12/08/2020.  

#### FAQ

**Q**: How will a USB update vs ADU update affect my SoftAP password that I manually set through OOBE?

**A**: Your device-specific, TPM-derived SoftAP password is unaffected by any firmware or OS update and remains unchanged across all update scenarios. However, your manually set password will be lost after a USB update.

USB updates:

- USB updates will wipe all device configuration settings and will reset your device to a factory clean state.  You will need to re-run OOBE and create your personal SoftAP password again.

ADU updates:

- Updates taken from ADU will preserve your user configuration state. Your manually-set SoftAP password will remain intact.

**Q**: How do I contact support?

**A**: If you are unable to run the [scz-tool-wifisoftap-accessinfo.devkit.sh](https://github.com/microsoft/Project-Santa-Cruz-Preview/tree/main/tools/SoftAP-access-info-tool) tool or have misplaced the device-specific, TPM-derived SoftAP password, please open a [support request](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/general/get-support.md).

## Introduction

This public repo provides documentation and example ML models to participants in the preview program. Although the content is public, participation in the program requires a devkit. If you are with a company working within the edge AI value chain, your company might qualify for a devkit. Go to https://aka.ms/scpreview to apply.

On this page you will find everything you need to get started using your devkit, including these [getting started videos](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/videos.md).

## Getting started

- [Project Santa Cruz devkit overview](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/project_santa_cruz_development_kit_overview.md)
- [Onboard your Azure subscription](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md)
- [Unbox and assemble your devkit](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/devkit-unboxing-setup.md)
- [Connect your devkit to Wi-Fi and Azure](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md)

## Build a no-code prototype

- [No-code vision solution tutorial](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/create-nocode-vision.md)
- [No-code speech solution tutorial](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/nocode-speech.md)

### Vision no-code how-to guides

After building a vision no-code solution, check out the following resources for additional information and guidance:

- [Vision solution how-to guide overview](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/prototyping/how-tos/vision/vision_how_tos_overview.md)
- [Deploy a vision solution to your devkit](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/prototyping/how-tos/vision/vision-deploy-model.md)
- [Capture images for a vision solution](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/prototyping/how-tos/vision/vision-setup-image-capture.md)
- [View your devkit's inference telemetry](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/prototyping/how-tos/vision/vision-view-telemetry.md)
- [View your devkit's RTSP video stream](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/prototyping/how-tos/vision/vision_view_video-stream.md)

### Speech no-code how-to guides

After building a speech no-code solution, check out the following resources for additional information and guidance:

- [Configure your voice assistant application using IoT Hub](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/prototyping/how-tos/speech/manage-voice-assistant-using-iot-hub.md)
- [Configure your voice assistant application through the Project Santa Cruz portal](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/prototyping/how-tos/speech/voice-assistant-config.md)

## Advanced development with Azure Machine Learning

- [Advanced development overview](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/readme.md)
- [Advanced development tutorial (cloud)](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/advanced_development_cloud.md)
- [Advanced development tutorial (local)](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/advanced_development_local.md)
- [Dev tools pack installer guide](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Machine%20Learning%20Notebooks/dev-tools-installer.md)
- [Scripts overview](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/Sample-Scripts-and-Notebooks/Official/Scripts/README.md)

## Keep your devkits up to date

- [Update experience overview](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/update_experience_overview.md)
- [Enable Automatic Import Updates (AIU)](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/automatic_import_of_updates.md)
- [Over-the-air update prerequisites](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/ota_os_fw_update_prerequisites.md)
- [Update your devkit carrier board over-the-air](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/ota_update.md)
- [Update your devkit carrier board via USB](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/usb_updating.md)
- [Update your Eye or Ear SoM firmware over-the-air](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/eye_and_ear_som_firmware_update.md)

## Additional technical information

### Hardware specifications

- [Devkit datasheet](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/hardware/project_santa_cruz_developer_kit_datasheet.md)
- [Eye SoM datasheet](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/hardware/project_santa_cruz_eye_datasheet.md)
- [Ear SoM Datasheet](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/hardware/project_santa_cruz_ear_datasheet.md)
- [Devkit Safety Manual (EN)](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/hardware/DevKit%20Safety%20Manual%20(2020-11-05).pdf)
- [Devkit Safety Manual (FR-CA)](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/hardware/FR-CA%20DevKit%20Safety%20Manual%20(2020-10-21).pdf)

### Containers

- [azureeyemodule overview](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/prototyping/containers/eye_module_overview.md)

## Troubleshooting

- [General devkit troubleshooting](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/general/troubleshooting/general_devkit_troubleshooting.md)
- [Ear SoM and speech module troubleshooting](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/general/troubleshooting/ear_som_speech_module_troubleshooting.md)
- [Vision solution troubleshooting](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/general/troubleshooting/vision_solution_troubleshooting.md)
- [SSH and serial connection setup](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/general/troubleshooting/ssh_and_serial_connection_setup.md)

## Resources

- [Getting support](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/general/get-support.md)
- [Reporting issues](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/general/report-a-bug.md)
- [Providing feedback](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/general/give-feedback.md)
- [Complete the focused test scenarios](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/general/test-scenarios.md)
- [Known issues](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/release-notes/known-issues.md)
- [Release notes](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/release-notes/release-notes.md)
