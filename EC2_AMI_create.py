import boto3
import datetime

# Replace these values with your AWS credentials and desired region
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_KEY'
region_name = 'us-west-2'  # Replace with your desired region

# Initialize a session using Amazon EC2 with explicit credentials
ec2 = boto3.client(
    'ec2',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

def create_ami(instance_id, name_prefix):
    """
    Create an AMI from the specified EC2 instance.

    :param instance_id: ID of the EC2 instance to create an AMI from
    :param name_prefix: Prefix for the AMI name
    :return: The AMI ID of the newly created AMI
    """
    # Get the current date and time for unique AMI name
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    image_name = f"{name_prefix}-{timestamp}"

    try:
        # Create the AMI
        response = ec2.create_image(
            InstanceId=instance_id,
            Name=image_name,
            NoReboot=True  # Set to False if you want to reboot the instance before creating the AMI
        )
        
        # Extract and print the AMI ID from the response
        ami_id = response['ImageId']
        print(f"AMI creation initiated. AMI ID: {ami_id}")

        return ami_id

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    instance_id = 'i-0abcdef1234567890'  # Replace with your EC2 instance ID
    name_prefix = 'my-app-ami'  # Prefix for the AMI name
    create_ami(instance_id, name_prefix)
