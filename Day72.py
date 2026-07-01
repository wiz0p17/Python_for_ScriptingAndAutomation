"""import boto3

sts = boto3.client("sts")

response = sts.get_caller_identity()

print(response)"""

import boto3

session = boto3.Session(profile_name="default")

ec2 = session.client("ec2")

"""Security Token Service (STS)."""

