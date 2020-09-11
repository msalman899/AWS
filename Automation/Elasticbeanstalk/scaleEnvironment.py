import argparse
import os
import sys
import boto3
from botocore.exceptions import ClientError
import elasticbeanstalk
import common.boto3Session


def main():
    # set up boto3 session
    custom_session = boto3Session("eu-west-1","sandbox")
    if not custom_session:
        print("Unable to create boto3 session, please define region")
        sys.exit(1)

    # elasticbeanstalk client object
    eb_environment = custom_session.client('elasticbeanstalk')
    # route53 client object
    r53_client = custom_session.client('route53')

    # initiialize another object that has more advance functions, just pass in the boto3 client object
    #eb = Elasticbeanstalk(eb_environment)

    application_name=""
    environment_name=""
    instance=""

    try:
        eb_update_response = eb_environment.update_environment(
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
    environment_update_status = eb_environment.get_waiter('environment_updated')

    if not environment_update_status:
        print("Failed to update environment ",environment_name)
        sys.exit(1)
    print("Environment ", environment_name, " has been updated successfully")


if __name__ == "__main__":
    main()
