import boto3
from botocore.exceptions import ClientError

INSTANCE_ID = 'instance id'  
REGION = 'eu-west-2'        

# IAM User Credentials
AWS_ACCESS_KEY = 'access kjey' 
AWS_SECRET_KEY = 'secret key'  

def restart_ec2_instance(instance_id, region, access_key, secret_key):

    ec2 = boto3.client(
        'ec2',
        region_name=region,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

    try:
        # Restart the EC2 instance
        response = ec2.reboot_instances(InstanceIds=[instance_id])
        print(f"Successfully initiated restart for instance: {instance_id}")
    except ClientError as e:
        print(f"Error restarting instance {instance_id}: {e}")

if __name__ == "__main__":
    restart_ec2_instance(INSTANCE_ID, REGION, AWS_ACCESS_KEY, AWS_SECRET_KEY)
