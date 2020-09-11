import argparse
import os
import sys
import boto3
from botocore.exceptions import ClientError
import elasticbeanstalk
import boto3Session


def checkTraffic(r53_client):
    r53_resource_records = r53_client.list_resource_record_sets(HostedZoneId='string')
    
    for record in r53_resource_records:
        if record['Name'] == recordset_name and record['SetIdentifier'] == commit_id:
            if record['weight'] == 100:
                return True
            return False
            break
        return "Not Exist"
    

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
    
    global commit_id
    global recordset_name
    
    application_name=""
    environment_name=""
    instance=""
    environment=""
    commit_id=""
    recordset_name=environment+"."+application_name+"."+commit_id

    #check traffic
    traffic = checkTraffic(r53_client)
    if traffic:
        print("This Env is serving 100% Traffic Scale In/Out is not allowed")
        sys.exit(1)    
    elif traffic == "Not Exist":
        print("Route53 RecordSet Not Found")

    # updating beanstalk environment
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
