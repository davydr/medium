import pandas as pd
import requests
import sys
import os

def main(file_path):
    # Load the Excel file
    data = pd.read_excel(file_path)
    print("Processing...")

    # API Key from environment variable
    api_key = os.getenv('THUNDERDOME_API_KEY')
    if not api_key:
        print("API key not found. Please set the THUNDERDOME_API_KEY environment variable.")
        sys.exit(1)

    # Loop through the data and make API requests
    for index, row in data.iterrows():
        battle_id = row['battleId']
        ticket_number = row['Ticket Number']
        ae_ticket = row['AE Ticket Number']
        sprint = row['Sprint']
        description = row['Description']
        entry_type = row['Type']
        acceptance_criteria = row['acceptanceCriteria']  # Make sure this column exists in your Excel file

        api_url = f'https://thunderdome.dev/api/battles/{battle_id}/plans'
        
        headers = {
            'Content-Type': 'application/json', 
            'Accept': 'application/json',
            'X-API-Key': api_key  # Include API key using the correct header
        }
        
        payload = {
            "acceptanceCriteria": acceptance_criteria,
            "description": description,
            "link": f"https://www.trmc.osd.mil/helpdesk/browse/ADVANAEDGE-{ae_ticket}",
            "planName": f"AE-{ae_ticket}",
            "referenceId": f"{sprint} {ticket_number}",
            "type": entry_type
        }

        response = requests.post(api_url, json=payload, headers=headers)
        print(f"Response from server: {response.text}")  # Detailed debug output
        if response.status_code == 200:
            print(f"Successfully created entry for ticket {ticket_number}")
        else:
            print(f"Failed to create entry for ticket {ticket_number}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python add_tasks.py path_to_excel_file.xlsx")
        sys.exit(1)
    main(sys.argv[1])

