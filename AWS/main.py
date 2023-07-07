import boto3

ec2_client = boto3.client("ec2", region_name="us-west-1 ")

all_avalable_vpcs = ec2_client.describe_vpcs()
# print(all_avalable_vpcs["Vpcs"])

vpcs = all_avalable_vpcs["Vpcs"]

for vpc in vpcs:
    print(vpc["CidrBlock"])
    print(vpc["VpcId"])
    print(vpc["CidrBlockAssociationSet"])

    # print(vpc["CidrBlockAssociationSet"][0])
    cidr_block_assoc_set = vpc["CidrBlockAssociationSet"] 
    for assoc_set in cidr_block_assoc_set:
        print (assoc_set["AssociationId"])
        print (assoc_set["CidrBlockState"])
        for state in assoc_set["CidrBlockState"]:
            print (state)


