ec2_instances_info = [
    {
        "id": "lcg0011",
        "name": "Ubuntu server",
        "type": "t2.micro",
        "ram": "1GB",
        "cpu": "2"
    },
    {
        "id": "lcg0022",
        "name": "Web-22",
        "type": "t2.medium",
        "ram": "1GB",
        "cpu": "2"
    },
    {
        "id": "lcg0033",
        "name": "Jenkins server",
        "type": "t2.large",
        "ram": "1GB",
        "cpu": "2"
    }
]
print(ec2_instances_info[1]["type"])



"""
-------OUTPUT-----
t2.medium
"""