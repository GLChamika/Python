import sys

ec2_type = sys.argv[1]

if ec2_type == "t2.micro":
    print("OK, We will create an EC2 Instance for you(t2.micro)")
    print("Note: This will cost you $2 per day")

elif ec2_type == "t2.medium":
    print("OK, We will create an EC2 Instance for you(t2.medium)")
    print("Note: This will cost you $4 per day")

elif ec2_type == "t2.large":
    print("OK, We will create an EC2 Instance for you(t2.large)")
    print("Note: This will cost you $8 per day")

else:
    print("ERROR! Please enter a valid EC2 type")