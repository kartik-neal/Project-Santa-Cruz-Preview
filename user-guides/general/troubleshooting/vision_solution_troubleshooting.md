# Vision solution troubleshooting

## Delete a vision project

1. Go to https://www.customvision.ai/projects.

1. Hover over the project you would like to delete and click the trash can icon to delete the project.

    ![delete_project](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/vision_delete_project.png)

## Check which modules are on a device

1. Go to the [Azure portal](https://ms.portal.azure.com/#home).

1. Click on the **Iot Hub** icon.

    ![iot_hub_2](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/vision_iot_hub_2.png)

1. Select the IoT Hub that your target device is connected to.

    ![iot_hub](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/vision_iot_hub.png)

1. Select **Iot Edge** and click on your device under the **Device ID** tab.

    ![iot_edge](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/vision_iot_edge.png)

1. Your device modules will be listed under the **Modules** tab.

    ![device_modules](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/vision_device_modules.png)

## Delete a device

1. Go to the [Azure portal](https://ms.portal.azure.com/#home).

1. Click on the **Iot Hub** icon.

    ![iot_hub_2](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/vision_iot_hub_2.png)

1. Select the IoT Hub that your target device is connected to.

    ![iot_hub](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/vision_iot_hub.png)

1. Select **Iot Edge** and check the box next to your target device ID. Click the trash can icon to delete your device.

    ![delete_device](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/article_images/vision_delete_device.png)

## Eye module troubleshooting tips

In case of problems with **WebStreamModule**, ensure that **azureeyemodule**, which does the vision model inferencing, is running. To check the runtime status, go to the [Azure portal](https://ms.portal.azure.com/?feature.canmodifystamps=true&Microsoft_Azure_Iothub=aduprod#home) and navigate to **All resources** -> **\<your IoT hub>** -> **IoT Edge** -> **\<your device ID>**. Click the **Modules** tab to see the runtime status of all installed modules.

![runtime_status](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/ota_iot_edge_device_page.png)

If the runtime status of **azureeyemodule** is not listed as **running**, click **Set modules** -> **azureeyemodule**. On the **Module Settings** page, set **Desired Status** to **running** and click **Update**.

 ![desired_status](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/images/firmware_desired_status_stopped.png)

## View device RTSP video stream

View your device's RTSP video stream through the [Project Santa Cruz portal](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/prototyping/how-tos/vision/vision_view_video-stream.md) or [VLC media player](https://www.videolan.org/vlc/index.html).

To open the RTSP stream in VLC media player, go to **Media** -> **Open network stream** -> **rtsp://[device IP address]/result**.