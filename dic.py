"""
Dictionaries will be used to store propeties of something (instance) as key/value pairs
"""

ec2_info = {
    "id": "lcg0011",
    "name": "Ubuntu server",
    "type": "t2.micro",
    "ram": "1GB",
    "cpu": "2"
}
print(ec2_info["name"])


"""
-------OUTPUT-----
Ubuntu server
"""


"""
--------Adding element--------
ec2_info['region'] = 'us-east-1'

--------Remove element--------
del ec2_info['region']
"""