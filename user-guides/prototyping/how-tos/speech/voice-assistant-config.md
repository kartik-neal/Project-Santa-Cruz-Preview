# Managing your voice assistant

This article describes how to configure the keyword and commands of your voice assistant application within the [Project Santa Cruz portal](https://go.microsoft.com/fwlink/?linkid=2135819). For guidance on configuring your keyword within IoT Hub instead of the portal, please see this [how-to article](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/prototyping/how-tos/speech/manage-voice-assistant-using-iot-hub.md).

If you have not yet created a voice assistant application, please see [QuickStart: Creating a Voice Assistant with the Project Santa Cruz Devkit](../../nocode-speech.md) for a step-by-step tutorial.

## Keyword configuration

A keyword is a word or short phrase used to activate a voice assistant. For example, "Hey Cortana" is the keyword for the Cortana assistant. Voice activation allows your users to start interacting with your product completely hands-free by simply speaking the keyword. As your product continuously listens for the keyword, all audio is processed locally on the device until a detection occurs to ensure their data stays as private as possible.

### Configuration within the voice assistant demo window

1. On the overview page of the [Project Santa Cruz portal](https://go.microsoft.com/fwlink/?linkid=2135819), click on **Speech** under **AI Projects** on the left menu pane.

    ![portal_overview](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_portal_overview.png)

1. Select the speech project you would like to configure.

1. Click **change** next to **Custom Keyword** on the demo page.

    ![hospitality_demo](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_hospitality_demo.png)

1. Select one of the available keywords and click **Save** to apply changes.

    ![change_keyword](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_change_keyword.png)

1. The three LED lights on the Ear SOM will change to bright blue (no flashing) when configuration is completed and your voice assistant is ready to use.

### Configuration within the device page

1. On the overview page of the [Project Santa Cruz portal](https://go.microsoft.com/fwlink/?linkid=2135819), click on **Devices** on the left menu pane.

    ![portal_overview_devices](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_portal_overview_devices.png)

1. Select the device to which your voice assistant application was deployed.

1. Open the **Speech** tab.

    ![device_page](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_device_page.png)

1. Click **Change** next to **Keyword**.

    ![change_keyword_device](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_change_keyword_device.png)

1. Select one of the available keywords and click **Save** to apply changes.

1. The three LED lights on the Ear SOM will change to bright blue (no flashing) when configuration is completed and your voice assistant is ready to use.

## Create a custom keyword

With [Speech Studio](https://speech.microsoft.com/), you can create a custom keyword for your voice assistant. It takes up to 30 minutes to train a basic custom keyword model.

Follow the [Speech Studio documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-devices-sdk-create-kws) for guidance on creating a custom keyword. Once configured, your new keyword will be available in the Project Santa Cruz portal for use with your voice assistant application.

## Command configuration

Custom commands make it easy to build rich voice commanding apps optimized for voice-first interaction experiences. Custom commands are best suited for task completion or command-and-control scenarios.

### Configuration within the voice assistant demo window

1. On the overview page of the [Project Santa Cruz portal](https://go.microsoft.com/fwlink/?linkid=2135819), click on **Speech** under **AI Projects** on the left menu pane.

    ![portal_overview](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_portal_overview.png)

1. Select the speech project you would like to configure.

1. Click **Change** next to **Custom Command** on the demo page.

    ![change_command](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_change_command.png)

1. Select one of the available custom commands and click **Save** to apply changes.

### Configuration within the device page

1. On the overview page of the [Project Santa Cruz portal](https://go.microsoft.com/fwlink/?linkid=2135819), click on **Devices** on the left menu pane.

    ![portal_overview_devices](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_portal_overview_devices.png)

1. Select the device to which your voice assistant application was deployed.

1. Open the **Speech** tab.

    ![device_page](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_device_page.png)

1. Click **Change** next to **Command**.

    ![change_command_device](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/speech/article_images/speech_change_command_device.png)

1. Select one of the available custom commands and click **Save** to apply changes.

## Create custom commands

With [Speech Studio](https://speech.microsoft.com/), you can create custom commands for your voice assistant to execute.

Follow the [Speech Studio documentation]((https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstart-custom-commands-application) for guidance on creating a custom keyword. Once configured, your new commands will be available in the Project Santa Cruz portal for use with your voice assistant application.
