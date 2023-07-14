import boto3
import schedule

ec2_client = boto3.client('ec2', region_name='us-east-2')
ec2_resource = boto3.resource('ec2')

def create_volume_snapshot():
    volumes = ec2_client.describe_volumes(
        Filters=[ 
            {
                'Name' : 'tag:Name',
                'Values' : ['prod']
            }
            
        ]
    )
    for volume in volumes['Volumes']:
        create_snapshot = ec2_client.create_snapshot(VolumeId=volume['VolumeId'])
        print(create_snapshot['SnapshotId'])
schedule.every(1).minutes.do(create_volume_snapshot)

while True:
    schedule.run_pending()