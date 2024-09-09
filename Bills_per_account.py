import boto3
from datetime import datetime, timedelta

def get_costs_by_management_account(start_date, end_date, management_account_id, access_key, secret_key, session_token=None):

    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        aws_session_token=session_token,  # Optional
        region_name='us-east-1'  # Cost Explorer is available in 'us-east-1'
    )
    
    client = session.client('ce')
    
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': start_date,
            'End': end_date
        },
        Granularity='MONTHLY',
        Metrics=['AmortizedCost'],
        Filter={
            'Dimensions': {
                'Key': 'LINKED_ACCOUNT',
                'Values': [management_account_id]
            }
        },
        GroupBy=[
            {'Type': 'DIMENSION', 'Key': 'SERVICE'},
            {'Type': 'DIMENSION', 'Key': 'REGION'}
        ]
    )
    total_amount = 0
    # Extracting and printing the cost data
    results = response.get('ResultsByTime', [])
    for result in results:
        print(f"Date Range: {result['TimePeriod']['Start']} to {result['TimePeriod']['End']}")
        for group in result.get('Groups', []):
            service = group['Keys'][0]
            region = group['Keys'][1]
            amount = float(group['Metrics']['AmortizedCost']['Amount'])
            print(f"{service}-----> Region: {region}-----> Cost: ${amount:.2f}")
            print("-" * 60)
            total_amount+=amount
            
    print(f"\nTotal Cost for the specified period: ${total_amount:.2f}")

if __name__ == "__main__":
    # Define your AWS access keys
    ACCESS_KEY = 'access-key'
    SECRET_KEY = 'secret-key'
    SESSION_TOKEN = None  # If using temporary credentials, provide the session token
    
    # Define the management account ID
    MANAGEMENT_ACCOUNT_ID = 'account-id'
    
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    
    # Validate date format
    try:
        datetime.strptime(start_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        exit(1)
    
    get_costs_by_management_account(start_date, end_date, MANAGEMENT_ACCOUNT_ID, ACCESS_KEY, SECRET_KEY, SESSION_TOKEN)

