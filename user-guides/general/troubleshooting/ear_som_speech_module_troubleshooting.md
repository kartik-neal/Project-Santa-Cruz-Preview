# Ear SoM and speech module troubleshooting

## Speech module troubleshooting tips

Use the guidelines below to troubleshoot voice assistant application issues. 

### Collecting speech module logs

To run these commands, connect to the devkit's Wi-Fi AP (if a Wi-Fi connection has not yet been set up through the [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md)), [SSH into the devkit using PuTTY](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/general/troubleshooting/ssh_and_serial_connection_setup.md), and enter the commands in the PuTTY terminal.

```console
 iotedge logs azureearspeechclientmodule
```

To redirect any output to a .txt file for further analysis, use the following syntax:

```console
[command] > [file name].txt
```

After redirecting output to a .txt file, copy the file to your host PC via SCP:

```console
scp [remote username]@[IP address]:[remote file path]/[file name].txt [local host file path]
```

[local host file path] refers to the location on your host PC which you would like to copy the .txt file to. [remote username] is the SSH username chosen during the [OOBE](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/oobe.md) setup process. If you did not set up an SSH login during the OOBE, your remote username is root.

### Checking runtime status of the speech module

Check if the runtime status of **azureearspeechclientmodule** shows as **running**. To locate the runtime status of your device modules, open the [Azure portal](https://ms.portal.azure.com/?feature.canmodifystamps=true&Microsoft_Azure_Iothub=aduprod#home) and navigate to **All resources** -> **\<your IoT hub>** -> **IoT Edge** -> **\<your device ID>**. Click the **Modules** tab to see the runtime status of all installed modules.


![runtime_status](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_iot_edge_device_page.png)


If the runtime status of **azureearspeechclientmodule** is not listed as **running**, click **Set modules** -> **azureearspeechclientmodule**. On the **Module Settings** page, set **Desired Status** to **running** and click **Update**.


![desired_status](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/firmware_desired_status_stopped.png)

    
## Understanding Ear SoM LED indicators

You can use LED indicators to understand which state you device is in. Usually it takes around 2 minutes for the module to fully initialize after *power on*. As it goes through initialization steps you will see:

1. 1 left green light - the device is powered on. 
2. 1 left green light and center LED blinking green - authentication is in progress. 
3. All three LEDs will change to blue once the device is authenticated and ready to use.

|LED State                  |Ear SoM Status            |
|----------------------------|---------------------------|
|1x green (left LED)         |power on |
|1x green (left LED) <br> 1x blinking green (center LED) |authentication in progress |
|3x off                      |initialization completed |
|3x blue                     |ready for use |
|3x blinking blue            |keyword recognized |
|3x racing blue              |processing |
|3x red                      |mute |
