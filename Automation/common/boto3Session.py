import os
import sys
import boto3


class Customsession:

    def __init__(self, region=None,profile=None):
        self.region = region
        self.profile = profile
        self.session = self.get_session()

    def get_session(self):
        if not self.region:
            return False
        elif self.profile:
            return boto3.session.Session(profile_name=self.profile, region_name=self.region)
        else:
            return boto3.session.Session(region_name=self.region)
