# Personal (MSA) account support for the Project Santa Cruz onboarding portal

The Project Santa Cruz onboarding portal is set up for corporate (work/school) accounts. However, we have created a workaround to support personal accounts (ex: @outlook.com).

If you are using an MSA personal account, we will need you to complete some additional steps. If you have any questions, please don’t hesitate to reach out to your Microsoft and Project Santa Cruz representative.

1. Log in to the [Azure portal](https://ms.portal.azure.com/#home) with your personal account (MSA account) or GitHub account.

1. Open **Azure Active Directory**.

1. Please provide the **Tenant ID**, located in the **Tenant information** box, to your Project Santa Cruz representative so that we can enable the preview experiences within your account.

    Note: If you have already provided this Tenant ID to your Project Santa Cruz representative, you may skip this step.

1. In Azure Active Directory, select **Users** under **Manage**.

1. Select **+ New user** to create a new user.

    You might notice that you already have a user here; this is your current MSA account login (ex. @outlook.com). You cannot use this account to log in to the onboarding portal. However, you can add a new user as a “work/school account” (corporate account), which will be able to access the onboarding website.

1. Select **Create user**. Do the following under **Identity**:

    1. For **User name**, enter a username and select a domain name of the format **.onmicrosoft.com**.
    1. Enter your name.
    1. Select your password.
    1. Click **Create**.

    Note: this username and password is what you will use to sign in to the onboarding portal.

1. Ensure the user has been created successfully.

1. Navigate to **Subscriptions**.

    1. If you already have a subscription that you would like to use for Project Santa Cruz, skip to step 9. Otherwise, select **+ Add** to create a new subscription.

    1. Select **Pay-As-You-Go**.

    1. Complete the sign-up process. This will include verifying your phone number, providing your payment details, selecting your technical support plan, etc.

    1. Wait for the subscription set up to complete. After it is complete, you will be redirected to the Azure portal. Navigate back to **Subscriptions**

1. Select the subscription you wish to use for Project Santa Cruz.  

1. Select **Access Control (IAM)** on the left menu panel. On the **Access Control (IAM)** page, click **+ Add** and then **Add role assignment**.

1. On the **Add role assignment** window, do the following:
    1. Under **Role**, select **Owner**.
    1. Select the user you created in Step 5.
    1. Click **Save**.

1. Proceed to aka.ms/projectsantacruz and log in with the username and password you created during this process.

    Reminder: the username should be of the format **<>@<>.onmicrosoft.com**. You may be asked to reset your password if this is the first time you are logging in.

Congratulations! You now have access to the Project Santa Cruz onboarding portal. Please reference the [onboarding walkthrough](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/getting_started/azure-subscription-onboarding.md) for guidance on working through the onboarding process.