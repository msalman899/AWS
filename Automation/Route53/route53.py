import os
import sys
from botocore.exceptions import ClientError
import json


class Route53:

    def __init__(self,client=None):
        self.client = client
        if not self.client:
            print("route53 client object is required")
            sys.exit(1)

    def search_recordset(self,HostedZoneId=None,**kwargs):
        recordset_list=[]
        if not HostedZoneId:
            print("please provide HostedZoneId")
            sys.exit(1)

        r53_resource_records = self.client.list_resource_record_sets(HostedZoneId=HostedZoneId)
        # print(json.dumps(r53_resource_records, indent=4))
        for record in r53_resource_records['ResourceRecordSets']:
            print(record['Name'])
            if all([True if key in record and record[key] == value else False for key,value in kwargs.items()]):
                recordset_list.append(record)
        return recordset_list
