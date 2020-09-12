import argparse
import os
import sys
import boto3
from botocore.exceptions import ClientError
import json
from common.boto3Session import *
from route53.route53 import *

def main():
    # set up boto3 session
    custom_session = Customsession(region="eu-west-1",profile="cpay_sandbox",)

    # elasticbeanstalk client object
    eb_client = custom_session.client('elasticbeanstalk')
    # route53 client object
    r53_client = custom_session.session.client('route53')
    #
    #initiialize another object that has more advance functions, just pass in the boto3 client object
    r53 = Route53(r53_client)
    # # eb = Elasticbeanstalk(eb_environment)
    #
    global commit_id
    global recordset_name

    application_name = ""
    environment_name = ""
    instance = ""
    environment = ""
    commit_id = ""
    recordset_name = ""

    recordset = r53.search_recordset(HostedZoneId="",Type="",SetIdentifier="")
    #print(recordset)

    if len(recordset) != 1:
        print("either multiple record set found OR No record set exist")
        sys.exit(1)

    if recordset['Weight'] >= 100:
        print("This Env is serving 100% Traffic Scale In/Out is not allowed")
        sys.exit(1)

    print("Traffic is less than 100%, Proceeding for Scale In/Out")

    # updating beanstalk environment
    try:
        eb_update_response = eb_client.update_environment(
            ApplicationName=application_name,
            EnvironmentName=environment_name,
            OptionSettings=[
                {
                    'ResourceName': 'Autoscalinggroup',
                    'Namespace': 'string',
                    'OptionName': 'MaxSize',
                    'Value': instance
                }
            ]
        )
    except ClientError as err:
        print("Failed to update environment.\n" + str(err))
        sys.exit(1)

    print("Waiting for Environment Update to be Completed")
    try:
        waiter = eb_client.get_waiter('environment_updated')
        waiter.wait(
            ApplicationName='string',
            EnvironmentNames=[environment_name],
            WaiterConfig={
                'Delay': 10,
                'MaxAttempts': 20
            }
        )
        print("Environment ", environment_name, " has been updated successfully")
    except Exception as err:
        print("Failed to update environment ",environment_name + "\n" + str(err))
        sys.exit(1)


if __name__ == "__main__":
    main()
