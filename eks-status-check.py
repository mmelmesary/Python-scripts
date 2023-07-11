import boto3
client = boto3.client('eks', region_name='us-east-1')

clusters = client.list_clusters()['clusters']

for cluster in clusters:
    response = client.describe_cluster(name=cluster)
    cluster_status = response['cluster']['status']
    cluster_endpoint = response['cluster']['endpoint']
    cluster_version = response['cluster']['version']
    print(f'Cluster {cluster} status is {cluster_status}')
    print(f'Cluster endpoint is : {cluster_endpoint}')
    print(f'Cluster version is : {cluster_version}')
    cluster_nodegroup = client.list_nodegroups(clusterName=cluster)
    for nodegroup in cluster_nodegroup['nodegroups']:
       nodes = client.describe_nodegroup(clusterName=cluster, nodegroupName=nodegroup)
       print(f'Nodegroup {nodegroup} status is {nodes["nodegroup"]["status"]}')
 
