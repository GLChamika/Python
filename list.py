"""
-Lists are mutable(Can change the size)

 Usage of lists
 1.To list AWS S3 buckets
 2.To list AWS EBS Volumes
 3.To list AWS EKS Clusters
"""

s3_buckets = ["Ubuntu_demo","Lahiru123","Web02", 445, 772] #used brackets
print(s3_buckets)
s3_buckets.append("new_bucket")
s3_buckets.remove("Web02")
print(len(s3_buckets))

new_list = s3_buckets[0:2]
print(new_list)
print(new_list[0] + "--" + new_list[1])

#---------------------------------------

numbers = [1, 22, 15, 14]
numbers.sort()
print(numbers)


"""
OUTPUT

['Ubuntu_demo', 'Lahiru123', 'Web02', 445, 772]
5
['Ubuntu_demo', 'Lahiru123']
Ubuntu_demo--Lahiru123
[1, 14, 15, 22]
"""