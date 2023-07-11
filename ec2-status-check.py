# check ec2 instance status
import boto3
import schedule

ec2_client = boto3.client('ec2', region_name='us-east-2')
ec2_instace = boto3.resource('ec2')

def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )
    for status in statuses['InstanceStatuses']:
        print(f"instance {status['InstanceId']} is {status['InstanceState']['Name']} and the instance status is {status['InstanceStatus']['Status']} and system status is {status['SystemStatus']['Status']}")

schedule.every(1).seconds.do(check_instance_status)