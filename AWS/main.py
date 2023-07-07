import boto3

ec2_client = boto3.client("ec2", region_name="us-east-2")

all_avalable_vpcs = ec2_client.describe_vpcs()
# print(all_avalable_vpcs["Vpcs"])

vpcs = all_avalable_vpcs["Vpcs"]

for vpc in vpcs:
    print(f'vpc_id is => {vpc["VpcId"]}')
    print(f"cidr_block is => {vpc['CidrBlock']}")
    

