
# integracao-openai

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Repository for Python files used to integrate with Azure OpenAI.

>![IMPORTANT](https://img.shields.io/badge/IMPORTANT-c00) 
Note that the Azure API shape differs from the core API shape. Check the [OpenAI Python API library](https://pypi.org/project/openai/) to get more details.

## Introduction

This project requires the use of a configuration file named `.env` to store sensitive information and customize certain aspects of the application. Before running the project, make sure to create and configure this file with the necessary variables.

Additionally, ensure you have Python installed on your system. For this project, Python version **3.11.4** is being used. To check the version of Python installed on your system via command line, you can use the following command:

`python --version`
or
`python -V`

## env File Configuration

Follow the steps below to set up the `.env` file:

1. **Create the `.env` file:**
   - Create a new file in the root of your project directory and name it `.env`.

2. **Add the following variables to the `.env` file:**
   - `AZURE_ENDPOINT`: Stores the endpoint (URL) provided by Azure to access a specific service, such as an API or cloud resource.
   - `API_KEY`: Contains a unique authentication key used to access protected services and resources in Azure, ensuring security and proper authorization.
   - `AZURE_DEPLOYMENT`: Specifies the deployment environment in Azure, indicating whether the system is in production, testing or another stage, facilitating configuration management in different contexts.

   ```
   AZURE_ENDPOINT="value1"
   API_KEY="value2"
   AZURE_DEPLOYMENT="value3"
   ```


## External packages

| Package  | Version  | How to install               |
|----------|----------|------------------------------|
| openai   | 1.2.4    | pip install openai           |
| dotenv   | 1.0.0    | pip install python-dotenv    |

<!-- | Line 3   | Line 3   | Line 3   | -->
<!-- | Line 4   | Line 4   | Line 4   | -->
<!-- | Line 5   | Line 5   | Line 5   | -->
<!-- | Line 6   | Line 6   | Line 6   | -->
<!-- | Line 7   | Line 7   | Line 7   | -->




