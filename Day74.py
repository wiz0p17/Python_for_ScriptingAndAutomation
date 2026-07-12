import boto3

ec2 = boto3.client("ec2")

INSTANCE_ID = "i-00b77d5f87ce0679d"

#stop instance
#response = ec2.stop_instances(InstanceIds = [INSTANCE_ID])

#start instance
#response = ec2.start_instances(InstanceIds = [INSTANCE_ID])

#reboot instance
response = ec2.reboot_instances(InstanceIds = [INSTANCE_ID])

print(response)

"""state = response["Reservations"][0]["Instances"][0]["State"]["Name"]

print(state)"""


"""waiter = ec2.get_waiter("instance_running")

waiter.wait(
    InstanceIds=[INSTANCE_ID]
)

print("Instance is now running.")"""