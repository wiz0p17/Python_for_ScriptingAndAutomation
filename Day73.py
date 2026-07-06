"""import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_instances()

for reservations in response["Reservations"]:
    for instance in reservations["Instances"]:
        print(instance["InstanceId"])
        print(instance["State"]["Name"])
        print(instance.get("PublicIpAddress"))"""


import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_instances()

for reservation in response["Reservations"]:

    for instance in reservation["Instances"]:

        print("-" * 40)

        print("Instance ID:",
              instance["InstanceId"])

        print("State:",
              instance["State"]["Name"])

        print("Public IP:",
              instance.get("PublicIpAddress"))
