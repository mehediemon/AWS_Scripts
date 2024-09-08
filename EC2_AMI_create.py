import boto3
import datetime

# Replace these values with AWS credentials
aws_access_key_id = 'access-key'
aws_secret_access_key = 'secret-access-key'
region_name = 'ap-south-1'  # Replace the region

# Passing the credential to access ec2
ec2 = boto3.client(
    'ec2',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

def create_ami(instance_id, name_prefix):

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    image_name = f"{name_prefix}-{timestamp}"

    try:
        # Create the AMI
        response = ec2.create_image(
            InstanceId=instance_id,
            Name=image_name,
            NoReboot=True  # Set to False if you want to reboot the instance before creating the AMI
        )
        
        ami_id = response['ImageId']
        print(f"AMI creation initiated. AMI ID: {ami_id}")

        return ami_id

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    instance_id = 'i-0000000000000'  # Replace EC2 instance ID
    name_prefix = 'my-app-ami'  # Give any name
    create_ami(instance_id, name_prefix)
