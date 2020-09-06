import argparse
import os
import sys
import boto3

Class Cloudformation:

  def __init__(self,region,profile=None):
    self.region = region
    self.profile = profile
    self.cf_client_session = self.get_session(self.region,self.profile)
    self.cf_client = cf_client_session.client('cloudformation')
    
  def get_session(self,self.region,self.profile):
    if self.profile:
      return boto3.session(profile=self.profile,region=self.region)
    else:
      return boto3.session(region=self.region)
    
  def search_stacks_by_name(self,*args):
    for string in *args
    if all(x in a_string for x in matches):
    
