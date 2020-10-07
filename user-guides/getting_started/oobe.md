# OOBE (out-of-box experience) Walkthrough

After completing the [onboarding](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md) for Project Santa Cruz Private Preview and [setting up your devkit](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/devkit-unboxing-setup.md), you may proceed with the OOBE (out-of-box experience). The OOBE walks you through the process of connecting your devkit to a Wi-Fi network, setting up an SSH login for your devkit, connecting your devkit to your Azure account, and assigning your devkit to your Project Santa Cruz IoT Hub.  

## Prerequisites

- [Onboarding](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md) completed.
- Project Santa Cruz Devkit [setup](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/devkit-unboxing-setup.md) completed.
- Computer with Wi-Fi connectivity.

## OOBE Procedure

You can connect and start OOBE through any of the following interfaces; SoftAP, WiFi, or Ethernet.  Replace <your_devices_ip> in the table below with your device's corresponding IP address.
OOBE Web Address |      Note
------------------ | ----------------
http://<your_devices_ip>:4242 | for builds released prior to 09/08/2020
http://<your_devices_ip> | for builds released on or after 09/08/2020

In the below walkthrough, we will be using the SoftAP IP address of 10.1.1.1

1. After the devkit has been powered on, connect your laptop to the Santa Cruz Wi-Fi AP.
   
   **We recommend not using a Mobile device to go through OOBE unless you want to configure the device's Wifi, SSH, or other non-IoT Hub items.**
1. On your computer, open your network and internet settings and connect to the following:
    1. SoftAP/Hotspot SSID: scz-xxxx    (where xxxx = the last four digits of the devkit's WiFi MAC address)
    2. Password: santacruz
    > [!NOTE]
    > Windows may complain about the SoftAP using a less secure standard (WPA2+TKIP cipher).  This will be addressed in a future build to only allow connections via the CCMP pairwise cipher.
1. Open a browser and go to http://10.1.1.1:4242.  *(Remember to remove the “:4242” for builds on or after 09/08/2020)*

1. Click Next on the OOBE Welcome screen.  

    ![welcome_screen](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/oobe_welcome_screen.png)

1. On the Network connection page, click “Connect to a new WiFi network” to connect your devkit to a Wi-Fi network.

    ![network_connection](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/oobe_network_connection.png)

1. Select your Wi-Fi network from the available connections.
    >[NOTE] The WiFi network you connect to, must currently have internet connectivity so we can communicate with Azure. EAP[PEAP/MSCHAP], captive portals, and Enterprise EAP-TLS connectivity is currently not supported.
    ![wifi](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/oobe_wifi.png)

1. Once your devkit has successfully connected to your network of choice, write down the IP address you are shown.  You can use this IP for OOBE or SSH sessions. Then, click Next.

    ![wifi_success](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/oobe_wifi_success.png)

1. We recommend you stop at this point and disconnect your PC from the SoftAP/Devkit and reconnect your PC back to your home/office AP.  Once you are back on your home/office network, use the IP address you noted from above to restart OOBE and skip the WiFi connection screen.  Using the above example screen you would enter this into your web browser: http://192.168.1.254:4242 *(Remember to remove the “:4242” for builds on or after 09/08/2020)*.

1. Read through the License Agreement, select “I Accept”, and click Next.

    ![license_agreement](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/oobe_license_agreement.png)

1. If you would like to set up SSH for remote access to your devkit, enter your SSH login and password, and click Next.  

    ![ssh](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/oobe_ssh.png)

1. On the next screen, click “Connect with a new device” to begin the process of linking your devkit to Azure.

    ![connect_device](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/oobe_connect_device.png)

1. Click “Copy” to copy your device code, and then click Login to Azure, which opens a new browser tab.

    ![device_code](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/oobe_device_code.png)

    1. On the new browser tab, paste your device code into window and click Next.

        ![enter_code](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/oobe_enter_code.png)

    1. Sign into your Azure account (the same account used during the onboarding process) and click Next. Navigate back to the OOBE window, which will show “Successfully Linked” once account sign-in is successful.

        ![code_sign_in](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/oobe_code_sign_in.png)

1. Select the IoT Hub you created during the onboarding process to assign it to your devkit. * mark shows an IoT Hub with DPS. If you are not sure which IoT Hub name you have created during the onboarding process, you can review it by accessing https://projectsantacruz.microsoft.com/.

    ![iot_hub](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/oobe_iot_hub.png)

1. Enter a device name for your devkit, check the TPM enrollment box, and click Next.  

    ![device_name](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/oobe_device_name.png)

1. Congratulations! Your devkit has been successfully linked to your Azure account and Project Santa Cruz IoT Hub. You may now access your device within the [Azure Portal](https://ms.portal.azure.com/?feature.canmodifystamps=true&Microsoft_Azure_Iothub=aduprod#home).  
  >[NOTE] If your “Preview Video Output” link is using 10.1.1.1:3000, we recommend you disconnect your PC from the SoftAP as outlined in step 8 and use http://<your_noted_IP_address>:3000 to get the best experience.
  
   ![oobe_complete](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/oobe_complete.png)

## OOBE Ethernet Procedure

1. After the device has been powered on, connect the ethernet cord to the device and your ethernet hub or port
1. Open a web browser on your laptop or desktop 
1. Type in http://<your_IP_address>:4242  Where *<your_IP_address>* is the local IP address of the DevKit/Brainbox which you can get from the ethernet router or hub.  Use http://<your_IP_address> for builds released on or after 09/08/2020.
1. OOBE will launch 
1. Proceed through OOBE following the Welcome steps outlined above

## Provide feedback

After completing the OOBE, please provide feedback on your experience via this [questionnaire](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbRzoJxrXKT0dEvfQyxsA0h8lUOEpDRkxZSUFWMFc2SEZYMDBBSlVQMUZMMy4u). Your feedback will help us continue to fine-tune and improve the OOBE experience.

For more information on Project Santa Cruz Quests and to provide feedback on other experiences, please visit the [test scenarios page](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/general/test-scenarios.md).

## Next Steps

You may now begin solution development with your Project Santa Cruz Development Kit. To get started, check out the [no-code vision experience](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/create-nocode-vision.md) and [no-code speech experience](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/nocode-speech.md) to create, train, and deploy simple AI models to your device.
