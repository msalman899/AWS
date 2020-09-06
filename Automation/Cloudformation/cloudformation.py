import argparse
import os
import sys
import boto3

class Cloudformation:

    def __init__(self, region=None, profile=None):
        self.region = region
        self.profile = profile
        self.cf_client_session = self.get_session(self.region, self.profile)
        self.cf_client = self.cf_client_session.client('cloudformation')


    def get_session(self):
        if not self.region:
          print("Unable to create boto3 session, please define region")
          return
        elif self.profile:
            return boto3.session(profile=self.profile, region=self.region)
        else:
            return boto3.session(region=self.region)
                
    def create_stack(self):
        pass
    
    def delete_stack(self):
        pass
    
    def update_stack(self):
        pass
    
    def wait_stack(self):
        pass
    
    def search_stacks_by_name(self, *args):
        for string in *args
            if all(x in a_string for x in matches):
