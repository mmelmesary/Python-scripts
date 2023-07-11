
import boto3

ec2_client = boto3.client('ec2', region_name='us-east-2')
ec2_resource = boto3.resource('ec2', region_name='us-east-2')

instance_ids =[]
instances = ec2_client.describe_instances()['Reservations']

for instance in instances:
    instances = instance['Instances']
    for instance in instances:
        if instance['State']['Name'] == 'running':
           instance_ids.append(instance['InstanceId'])

           
response = ec2_resource.create_tags(
    Resources= instance_ids,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'production'
        },
    ]
)