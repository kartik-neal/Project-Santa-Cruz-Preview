# Configure voice assistant application using IoT Hub

This article describes how to configure your voice assistant application using IoT Hub. For a step-by-step tutorial that guides you through the process of creating a voice assistant using demo template, see [QuickStart: Creating a Voice Assistant with the Project Santa Cruz Devkit](../../nocode-speech.md).

1. Open the [Azure portal](https://portal.azure.com) and type **IoT Hub** into the search bar. Click on the icon to open the IoT Hub page.

1. On the IoT Hub page, select the IoT Hub to which your device was provisioned.

1. Select **IoT Edge** under **Automatic Device Management** in the left navigation menu to view all devices connected to your IoT Hub.

1. Select the device to which your voice assistant application was deployed.

1. Click on **Set Modules**.

    ![set_modules](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_set_modules.png)

1. Verify that the following entry is present under the **Container Registry Credentials** section. Add credentials if required.

    Name|Address|Username|Password
    ----|-------|--------|--------
    azureedgedevices|azureedgedevices.azurecr.io|devkitprivatepreviewpull|***

    **NOTE:** If you do not have a password for the container registry, please reach to your primary contact for the Santa Cruz private preview program.

1. In the **IoT Edge Modules** section, select **azureearspeechclientmodule**.

    ![modules](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_modules.png)

1. Click on the **Module Settings** tab. Verify the following configuration:

    Image URI|Restart Policy|Desired Status
    ---------|--------------|--------------
    azureedgedevices.azurecr.io/azureearspeechclientmodule:preload-devkit |always|running

    If your settings do not match, edit them and click **Update**.

    ![module_settings](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_module_settings.png)

1. Click on the **Environment Variables** tab. Verify that there are no environment variables defined.

    ![environment_variables](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_environment_variables.png)

1. Click on the **Container Create Options** tab. Verify your **HostConfig** settings match those shown below. If not they do not match, update your settings.

    ```
    {
        "HostConfig": {
            "Privileged": true,
            "Binds": [
                "/dev:/dev"
            ]
        }
    }
    ```

1. Click on the **Module Twin Settings** tab. Update the **speechConfigs** section as follows:

    ```
    "speechConfigs": {
        "appId": "<Application id for custom command project>",
        "key": "<Speech Resource key for custom command project>",
        "region": "<Region for the speech service>",
        "keywordModelUrl": "https://aedspeechscenarios.blob.core.windows.net/keyword-tables/computer.table",
        "keyword": "computer"
    }
    ```

    Note: The keyword used above is a default publicly available keyword. If you wish to use your own, you can add your own custom keyword by uploading a created table file to blob storage. Blob storage needs to be configured with either anonymous container access or anonymous blob access.

    To locate your **appID**, **key**, and **region**, go to [Speech Studio](https://speech.microsoft.com/):

    - Sign in and select the appropriate speech resource.

    - On the **Speech Studio** home page, click on **Custom Commands** under **Voice Assistants**.

        ![custom_commands](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_custom_commands.png)

    - Select your target project.

        ![project](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_project.png)

    - Click on **Settings** on the left-hand menu panel.

        ![project_settings](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_project_settings.png)

    - The **appID** and **key** will be located under the **General** settings tab.

        ![general_settings](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_general_settings.png)

    - To find your **region**, open the **LUIS resources** tab within the settings. The **Authoring resource** selection will contain region information.

        ![luis_resources](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_luis_resources.png)

1. After entering your **speechConfigs** information, click **Update**.

1. Click on the **Routes** tab at the top of the **Set modules** page. Ensure you have a route with the following value:

    ```
    FROM /messages/modules/azureearspeechclientmodule/outputs/* INTO $upstream
    ```

    Add the route if it does not exist.

    ![routes](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_routes.png)

1. Click **Review + Create**.

1. Click **Create**.
