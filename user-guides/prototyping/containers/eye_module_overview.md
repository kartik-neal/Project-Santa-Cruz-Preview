# azureeyemodule overview

The Project Santa Cruz devkit comes with six default containers, which are deployed to the device at the end of the [OOBE (out-of-box experience)](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/oobe.md).

azureeyemodule is a container that controls the Eye SoM and enables vision AI solutions. It contains a default AI model that recognizes generic objects like people, animals, office supplies, etc.

Refer to the following diagram and corresponding steps to understand the process between deploying the azureeyemodule container and receiving inference results from the module's AI model. Note that the "host" refers to the carrier board of the devkit, the "AI accelerator" refers to the SoM, and the “camera module” refers to the camera that connects to the SoM.

![azureeyemodule_diagram](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/prototyping/containers/images/azureeyemodule_diagram.png)

1. The container is deployed from the Azure cloud to the host.
2. The container starts and authenticates with the security chip.
3. If the AI camera is authenticated, the container sends the AI model to the AI accelerator and a "start" signal to initiate camera capture.
4. Camera frames are captured and sent to the image signal processor of the AI accelerator for pre-processing.
5. The pre-processed image is sent directly to the neural network compute engine for running inference.
6. The camera stream is sent to the host.
7. The inference result is sent to the host.
8. The inference result is processed in the container, the RTSP stream is provided, and data and telemetry information is sent to the Azure cloud for further analysis.

## Updating the AI model

azureeyemodule supports a technique called “module twin update”. The container has a module identity twin property for “ModelZipUrl”. If the value for ModelZipUrl is updated to a new URL, the container will download the new model from the link and deploy it to the Eye SoM. Whenever a new vision solution is deployed to your device through the [Project Santa Cruz portal](https://go.microsoft.com/fwlink/?linkid=2135819), the ModelZipUrl property is updated automatically.

To deploy to the devkit, a new model must be in:

- a publicly accessible location
- a zipped file with a config.json that contains the DomainType, LabelFileName, and ModelFileName properties
- IR (Intermediate Representation) or blob format

Note: the TensorFlow format will not work with the module twin update. The model must be converted to a compatible format using Intel’s OpenVINO tools.

### Module identity twin settings

azureeyemodule supports the following module twin settings:

|Property         |Type        |Description                  |
|-----------------|------------|-----------------------------|
|ModelZipUrl |String |Path to the blob storage where the vision model is stored. For example: "https://pretrainedmodels.blob.core.windows.net/aeddevkit/tiny-yolo-v2.zip" |
|RawStream |Boolean |Enable/disable the raw RTSP stream for production use cases. |
|ResultStream |Boolean |Enable/disable the result RTSP stream for production use cases. |
|TelemetryInterval |Integer |Limits the messages sent to IoT Hub by a factor of 1/[X], where X is the integer value of TelemetryInterval. For example, if TelemetryInterval is set to 2, only half of the total messages get sent to the IoT Hub. |

### How to locate and edit your module identity twin settings

1. Log in to the [Azure Portal](https://ms.portal.azure.com/?feature.canmodifystamps=true&Microsoft_Azure_Iothub=aduprod#home) and open **All resources**.

    ![azure_portal](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/prototyping/containers/images/azure_portal.png)

1. On the **All resources** page, click on the name of the IoT Hub that was provisioned to your devkit during the OOBE process.

1. On the left side of the IoT Hub page, click on **IoT Edge** under **Automatic Device Management**. On the IoT Edge devices page, find the device ID of your devkit. Click the device ID of your devkit to open its IoT Edge device page.

    ![iot_edge](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/prototyping/containers/images/iot_edge.png)

1. Click **azureeyemodule** under the **Modules** tab.

    ![device_page](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/prototyping/containers/images/device_page.png)

1. On the azureeyemodule page, open **Module Identity Twin**.

    ![module_page](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/prototyping/containers/images/module_page.png)

1. Scroll down to **properties**. Please note that the properties "Running" and "Logging" are not active at this time.

    ![module_identity_twin](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/prototyping/containers/images/module_identity_twin.png)

1. Make your desired edits and click the **Save** icon.

## Supported neural networks

azureeyemodule currently supports the following neural networks for object detection and image classification:

|object detection|image classification|
|-----------------|--------|
|Yolo v2 (variants that utilize non-maximum suppression are not supported) |shufflenetv2|
|Tiny Yolo v2|SEResNext50|
|MobilenetV2SSDLite| |

Other neural networks may run on the device, but the support for handling the inferencing results needs to be built in separately.

## Other Project Santa Cruz containers

Please see the [IoT Edge documentation](https://docs.microsoft.com/en-us/azure/iot-edge/iot-edge-runtime) for information on the edgeAgent and edgeHub containers.