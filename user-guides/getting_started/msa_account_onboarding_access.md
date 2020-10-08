# Personal (MSA) account support for the Project Santa Cruz onboarding portal

The Project Santa Cruz onboarding portal is set up for corporate (work/school) accounts. However, we have created a workaround to support personal accounts (ex: @outlook.com).

If you are using an MSA personal account, we will need you to complete some additional steps. If you have any questions, please don’t hesitate to reach out to your Microsoft and Project Santa Cruz representative.

1. Log in to the [Azure portal](https://ms.portal.azure.com/#home) with your personal account (MSA account) or GitHub account.

1. Open **Azure Active Directory**.

    ![aad](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/getting_started_images/msa_aad.png)

1. In Azure Active Directory, select **Users** under **Manage**.

1. Select **+ New user** to create a new user.

    You might notice that you already have a user here; this is your current MSA account login (ex. @outlook.com). You cannot use this account to log in to the onboarding portal. However, you can add a new user as a “work/school account” (corporate account), which will be able to access the onboarding website.

    ![new_user](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/getting_started_images/msa_new_user.png)

1. Select **Create user**. Do the following under **Identity**:

    1. For **User name**, enter a username and select a domain name of the format **.onmicrosoft.com**.
    1. Enter your name.
    1. Select your password.
    1. Click **Create**.

    ![create_user](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/getting_started_images/msa_create_user.png)

    Note: this username and password is what you will use to sign in to the onboarding portal.

1. Ensure the user has been created successfully.

    ![notifications](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/getting_started_images/msa_notifications.png)

1. Navigate to **Subscriptions**.

    1. If you already have a subscription that you would like to use for Project Santa Cruz, skip to step 9. Otherwise, select **+ Add** to create a new subscription.

        ![subscriptions](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/getting_started_images/msa_subscriptions.png)

    1. Select **Pay-As-You-Go**.

        ![pay_as_you_go](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/getting_started_images/msa_pay_as_you_go.png)

    1. Complete the sign-up process. This will include verifying your phone number, providing your payment details, selecting your technical support plan, etc.

        ![sign_up](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/getting_started_images/msa_sign_up.png)

    1. Wait for the subscription set up to complete. After it is complete, you will be redirected to the Azure portal. Navigate back to **Subscriptions**

        ![subscriptions_2](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/getting_started_images/msa_subscriptions_2.png)

1. Select the subscription you wish to use for Project Santa Cruz.

    ![select_subscription](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/getting_started_images/msa_select_subscription.png)

1. Select **Access Control (IAM)** on the left menu panel. On the **Access Control (IAM)** page, click **+ Add** and then **Add role assignment**.

    ![iam](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/getting_started_images/msa_iam.png)

1. On the **Add role assignment** window, do the following:
    1. Under **Role**, select **Owner**.
    1. Select the user you created in Step 5.
    1. Click **Save**.

    ![add_role_assignment](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/getting_started_images/msa_add_role_assignment.png)

1. Proceed to aka.ms/projectsantacruz and log in with the username and password you created during this process.

    Reminder: the username should be of the format **<>@<>.onmicrosoft.com**. You may be asked to reset your password if this is the first time you are logging in.

Congratulations! You now have access to the Project Santa Cruz onboarding portal. Please reference the [onboarding walkthrough](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md) for guidance on working through the onboarding process.