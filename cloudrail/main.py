import json
from typing import List

from cloudrail.entities.ec2 import Ec2


def load_instances(cloud_json_data) -> List[Ec2]:
    all_instances_list = []
    for instance_ec2 in cloud_json_data["Instances"]:
        instance_id, name, state, image_id, availability_zone = "", "", "", "", ""
        network_interfaces_ids: []
        tags = {}
        if "InstanceId" in instance_ec2:
            instance_id = (instance_ec2["InstanceId"])
        if "RootDeviceName" in instance_ec2:
            name = (instance_ec2["RootDeviceName"])
        if "NetworkInterfaces" in instance_ec2:
            network_interfaces_ids = (instance_ec2["NetworkInterfaces"])
        if "State" in instance_ec2:
            if "Name" in (instance_ec2["State"]):
                state = (instance_ec2["State"]["Name"])
        if "ImageId" in instance_ec2:
            image_id = (instance_ec2["ImageId"])
        if "Placement" in instance_ec2:
            if "AvailabilityZone" in (instance_ec2["Placement"]):
                availability_zone = (instance_ec2["Placement"]["AvailabilityZone"])
        if "Tags" in instance_ec2:
            for tag in instance_ec2["Tags"]:
                tags[tag["Key"]] = tag["Value"]
        ec2_instance = Ec2(instance_id, name, network_interfaces_ids, state, image_id, availability_zone, tags)
        all_instances_list.append(ec2_instance)
    return all_instances_list


def get_ec2_contains_production_tag(ec2s: List[Ec2]) -> List[Ec2]:
    instances_production = []
    for instance in ec2s:
        if "environment" in instance.tags:
            if instance.tags["environment"] == "production":
                instances_production.append(instance)
    return instances_production


def main():
    cloud_json_data_file = 'cloud-data/ec2-describe-instances.json'
    with open(cloud_json_data_file, 'r') as json_file:
        cloud_json_data = json.load(json_file)
    ec2s: List[Ec2] = load_instances(cloud_json_data)

    ec2s_with_issue = get_ec2_contains_production_tag(ec2s)
    print('Found {} ec2s with issues'.format(len(ec2s_with_issue)))


if __name__ == '__main__':
    main()
