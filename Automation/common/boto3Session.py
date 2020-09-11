import os
import sys
import boto3

class boto3session:

    def __init__(self, region, profile=None):
        self.region = region
        self.profile = profile
        self.client_session = self.get_session(self.region, self.profile)

        def get_session(self):
            if not self.region:
                return False
            elif self.profile:
                return boto3.session(profile=self.profile, region=self.region)
            else:
                return boto3.session(region=self.region)
