# Securing your AI model and data

Project Santa Cruz provides AI model protections at rest, during transition, and in use. It's designed to work with existing AI systems and workflows such as [Azure Machine Learning](https://azure.microsoft.com/en-us/services/machine-learning/), [Azure Databricks](https://azure.microsoft.com/en-us/services/databricks/), and [Azure Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/). The long-term goal of Project Santa Cruz is to provide a unified experience across underlying systems.

The Project Santa Cruz devkit is shipped with a secured AI model locker and a Python SDK, as highlighted in the following diagram. The server provides secured key and model management capabilities. In the future, the SDK will interact with a device TPM and attestation service to prove device identity with the server and retrieve protected keys or models.

![architecture](https://github.com/microsoft/Project-Santa-Cruz-Preview/blob/main/user-guides/secured_locker/images/architecture.png)