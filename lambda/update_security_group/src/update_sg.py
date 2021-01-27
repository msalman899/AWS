import sys
import os

sys.path.insert(0, 'package/')

def lambda_handler(event, context):
    # for local execution
    # session = boto3.Session(region_name='us-eest-1', profile_name='<profilename>')
    # ec2 = session.client('ec2')

    # for lambda or ec2
    ec2 = boto3.client('ec2')
    

    sg = ec2.describe_security_groups(
        Filters=[
            {
                'Name': 'group-name',
                'Values': [
                    'my-vpc-https-sg'
                ]
            }
        ]
    )

    response = ec2.authorize_security_group_ingress(
        GroupId=sg['SecurityGroups'][0]['GroupId'],
        IpPermissions=[
            {
                'FromPort': 443,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '192.168.1.2/24',
                        'Description': ' dummy',
                    },
                ],
                'ToPort': 443,
            },
            {
                'FromPort': 443,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '192.168.9.2/24',
                        'Description': 'dummy',
                    },
                ],
                'ToPort': 443,
            }
        ]
    )
