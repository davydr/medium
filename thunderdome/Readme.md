# Thunderdome Battle Setup

This Python script automates the definition of tasks within a battle for scoring. This makes it easy to use the battle to aggregate scores across a sprint.

## Prerequisites

Before running this script, ensure you have the following installed on your system:

- **Python (version 3.6 or later)** - You can download it from [python.org](https://www.python.org/downloads/).
- **Pandas Library** - Needed for handling the Excel file.
- **Requests Library** - Used for making HTTP requests to the Kubernetes API.

You can install the required Python libraries using pip:

```bash
pip install pandas requests
```

## Configuration

1. **API Key**: The script requires a Thunderdome API key to authenticate requests. You must authenticate your email with Thunderdome to activate API first. Store your API key in an environment variable:

    ```bash
    export THUNDERDOME_API_KEY='Your_API_Key_Here'
    ```

    Replace `Your_API_Key_Here` with your actual API key.

2. **Excel File**: Prepare an Excel file with the deployment data. The file must have the following columns:
   - `battleId`: Unique identifier for the battle.
   - `Ticket Number`: Ticket number associated with the deployment.
   - `AE Ticket Number`: Alternate ticket number used in the deployments.
   - `Sprint`: The sprint during which the deployment is done.
   - `Description`: Description of the deployment.
   - `Type`: Type of the deployment. We mostly defien "Task" for the battle
   - `Acceptance Criteria`: Criteria that must be met for the deployment to be considered successful.

## Usage

To run the script, use the following command in your terminal:

```bash
python add_tasks.py path_to_excel_file.xlsx https://www.example.com GENERICPREFIX

```

Replace `path_to_excel_file.xlsx` with the path to your Excel file containing the deployment data.

## Script Functions

- **Loading Data**: The script reads data from the specified Excel file.
- **Creating Deployments**: For each row in the Excel file, the script creates a deployment in the Kubernetes system using the provided API.
- **Error Handling**: The script checks for errors in API response and logs them.

## Example

Here is an example command to run the script:

```bash
python add_tasks.py ~/Documents/Jira_Sprint22.xlsx
```

This will process the deployments described in `Jira_Sprint22.xlsx` located in the Documents folder.

## Troubleshooting

- Ensure the API key is correctly set in your environment variables.
- Verify that all required columns are present in the Excel file and that there are no typos.
- Check your Python environment if you encounter any issues related to missing libraries.
