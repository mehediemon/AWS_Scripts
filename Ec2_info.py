import boto3

# Replace these values
aws_access_key_id = 'access-key'
aws_secret_access_key = 'secret-access-key'
region_name = input("enter region:")  # Input your reion where you want to see

def get_ec2_instance_info():

    ec2 = boto3.client(
        'ec2',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )

    try:
        # Retrieve information about running EC2 instances
        response = ec2.describe_instances(Filters=[
            {'Name': 'instance-state-name', 'Values': ['running']}
        ])
       
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                private_ip = instance.get('PrivateIpAddress', 'N/A')
                public_ip = instance.get('PublicIpAddress', 'N/A')
                value = instance.get('Tags', 'N/A')
                
                print(f"Instance ID: {instance_id}")
                print(f"Private IP: {private_ip}")
                print(f"Public IP: {public_ip}")
                print(f"Value: {value}")
                print("-" * 40)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_ec2_instance_info()

