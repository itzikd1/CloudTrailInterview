from typing import List, Optional


class Ec2:
    def __init__(self,
                 instance_id: str,
                 name: str,
                 network_interfaces_ids: List[str],
                 state: str,
                 image_id: str,
                 availability_zone: Optional[str],
                 tags: dict):
        self.instance_id: str = instance_id
        self.name = name
        self.network_interfaces_ids: List[str] = network_interfaces_ids
        self.state: str = state
        self.image_id: str = image_id
        self.availability_zone: Optional[str] = availability_zone
        self.tags: dict = {}
        if tags:
            self.tags.update(tags)
