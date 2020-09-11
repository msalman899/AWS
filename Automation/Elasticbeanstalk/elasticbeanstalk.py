import argparse
import os
import sys
import boto3

#need to provide boto3 client object

class Elasticbeanstalk:

    def __init__(self, client):
        self.client = client

    def update_environment(self):
        pass

    def wait_update_environment(self):
        pass

    def update_stack(self):
        pass

    def wait_stack(self):
        pass

    def search_stacks_by_name(self, *args):
        for string in *args
            if all(x in a_string for x in matches):
