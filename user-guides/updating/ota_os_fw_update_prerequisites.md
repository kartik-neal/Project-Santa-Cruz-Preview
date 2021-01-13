# OTA OS and FW Update Prerequisites

1. Toggle Azure Device Update (ADU) on. This can be accomplished through the [onboarding website](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md).

    ![onboarding](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/getting_started_images/onboarding_dps_adu.png)

1. Add a role assignment to a user or Azure AD group to grant access to Import and Deploy Updates within IoT Hub. Please note that it can take a few hours for all update services to be set up in your account.

    1. On your Azure subscription page, select **Access control (IAM)** on the left menu panel.

    1. Click **Add** within **Add a role assignment**.

        ![iam](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/images/prereqs_iam.png)

    1. For **Select a Role**, select **Device Update Administrator**.

    1. Assign access to a user or Azure AD group.

    1. Click **Save**.

    ![add_role](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/images/prereqs_add_role.png)

## Common Issues
These are common issues faced if you are not able to successfully create an Azure Device Update account through the [onboarding website](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md).

1. Enable Azure Feature Control. This step allows you to get access to the ADU Private Preview resource.

    1. Go to https://docs.microsoft.com/en-us/rest/api/resources/features/register#code-try-0. Log in and click **Try it**.

        ![try_it](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/images/prereqs_try_it.png)

    1. On the **Rest API Try It** page, enter the following values within the **Parameters** section:
        - **featureName**: "PublicPreview"  
        - **resourceProviderNamespace**: "Microsoft.DeviceUpdate"  
        - **subscriptionId**: choose/enter your Azure subscription that will be used with Project Santa Cruz  
        - **api-version**: keep the default value

    1. At the bottom of the **Rest API Try It** page, click **Run**.

        ![try_it_parameters](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/images/prereqs_try_it_parameters.png)
    
    **WARNING**: please wait at least 20 minutes for the Azure Feature Control registration to complete before proceeding to the next step. Otherwise, you will receive an error when attempting to register the ADU resource provider (below).

1. Register the ADU resource provider within your subscription. **Do NOT proceed with this step until the Azure Feature Control registration is complete. This may take at least 20 minutes after clicking "Run" in the previous step.**

    1. Open the [Azure portal](https://ms.portal.azure.com/#home).

    1. In the search bar, type **Subscriptions** and click on the yellow key icon to open the **Subscriptions** page.

    1. Select your Azure subscription.

    1. On your subscription overview page, select **Resource providers** under **Settings**.

    1. Enter **DeviceUpdate** in the search bar.

    1. Select **Microsoft.DeviceUpdate** and click **Register** on the command bar. **Status** will update to **Registered** when registration has completed.  

    ![deviceupdate](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/images/prereqs_deviceupdate.png)

## Next steps

Once you have completed the steps above, you will be able to use Azure Device Update by navigating to the [Azure Portal](https://portal.azure.com/?feature.canmodifystamps=true&Microsoft_Azure_Iothub=aduprod). This link turns on Azure Device Update functionality, which is a Private Preview feature.

The first time you use Azure Device Update, you will be asked to provide your Azure Device Update Account name and Instance name. Your Account name and Instance name are located on the [onboarding website](https://aka.ms/projectsantacruz) under the Azure Device Update section.

You are now ready to deploy your first OS/FW update over-the-air. Check out the [OTA carrier board OS update walkthrough](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/ota_update.md) and the [OTA Ear SoM FW update walkthrough](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/updating/ear_som_firmware.md) to learn more.
