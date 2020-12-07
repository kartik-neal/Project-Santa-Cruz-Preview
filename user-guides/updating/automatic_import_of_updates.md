# AAD application configuration for the Automatic Import Update (AIU) service

Automatic Import Update (AIU) functionality enables you to directly receive the latest updates for your Project Santa Cruz devkits in your Azure Device Update instance within your Azure IoT Hub.

To turn it on, please complete the steps below.

## Prerequisites

- [Onboarding](https://github.com/microsoft/Project-Santa-Cruz-Private-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md) complete with ADU enabled.
- Download the [santacruzwebapp certificate](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/resources/santacruzwebapp.cer).

## Create an AAD application within App Registrations

1. Log in to the [Azure portal](https://ms.portal.azure.com/#home).

1. Navigate to **App Registrations**. If the icon is not displayed on your portal home page, enter **App Registrations** into the search bar.

    ![app_registrations](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/images/aiu_app_registrations.png)

1. Click on **New Registration**.

    ![new_registration](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/images/aiu_new_registration.png)

1. Do the following:

    1. Provide a unique name for your application.
    2. Select the supported account type.
    3. Click **Register**.

    ![register_an_application](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/images/aiu_register_an_application.png)

## Upload santacruzwebapp certificate to AAD application

1. After registering your application, the application overview page opens automatically. On the overview page, select **Certificates & secrets** under **Manage**.

    ![certificates_and_secrets](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/images/aiu_certificates_and_secrets.png)

1. Click **Upload certificate**.

    ![upload_certificate](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/images/aiu_upload_certificate.png)

1. Select the **santacruzwebapp** certificate and click **Add**. If you have not downloaded the certificate yet, you may do so [here](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/resources/santacruzwebapp.cer).

    ![certificate](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/images/aiu_certificate.png)

1. Once the certificate is uploaded, it will appear in the certificate list.

## Assign Device Update Administrator role to AAD application

1. Navigate to **Device Update for IoT Hubs** by entering it into the search bar or clicking the icon on the [Azure portal](https://ms.portal.azure.com/#home) home page.

    ![device_update_for_iot_hubs](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/images/aiu_device_update_for_iot_hubs.png)

1. Select the ADU account that matches the ADU account name on the [Project Santa Cruz Enterprise Onboarding and Update Management website](https://projectsantacruz.microsoft.com/) (this was created during onboarding).

    ![adu_account_name](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/images/aiu_adu_account_name.png)

1. Click on **Instances** under **Instance Management**.

    ![instances](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/images/aiu_instances.png)

1. Verify that the ADU instance that matches the ADU instance name on the [Project Santa Cruz Enterprise Onboarding and Update Management website](https://projectsantacruz.microsoft.com/) lists **Succeeded** under **Provisioning State**. Do not proceed otherwise.

    ![provisioning_state](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/images/aiu_provisioning_state.png)

1. Next, select **Access control (IAM)** on the ADU account page.

    ![access_control](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/images/aiu_access_control.png)

1. Click **+ Add** -> **Add role assignment**.

1. On the **Add role assignment** page, do the following:

    1. Under **Role**, select **Device Update Administrator**.
    1. Under **Assign access to**, select **User, group, or service principal**.
    1. Under **Select**, enter the name of the AAD application created at the beginning of this guide.

1. Repeat step 6 and step 7. This time, enter your Azure subscription username/alias (e.g. user@microsoft.com) under **Select**.

1. Under **Check access**, verify that the AAD application and your Azure subscription username/alias have Device Update Administrator privileges.

1. Finally, navigate to the [Project Santa Cruz Enterprise Onboarding and Update Management website](https://projectsantacruz.microsoft.com/), check the box next to **Automatic Import Update (AIU)** to turn on the service, and enter the AAD application ID.

    ![set_aiu_service](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/updating/images/aiu_set_aiu_service.png)
