"""
-Tuples are immutable(Cannot be resized, cannot add or remove elements once it created)
-Memory allocation is more better than lists

 Usage of tuples
 1.To list and store AWS admins(No one will be able to add or remove admins since it has fixed size)
"""

s3_buckets = ("Ubuntu_demo","Lahiru123","Web02") #used braces
print(type(s3_buckets))
print(len(s3_buckets))

s3_buckets.append("new_bucket") 
print(s3_buckets) #AttributeError: 'tuple' object has no attribute 'append'


#------------------------------

"""
OUTPUT

<class 'tuple'>
3
Traceback (most recent call last):
  File "/workspaces/Python/tuple.py", line 13, in <module>
    s3_buckets.append("new_bucket") 
AttributeError: 'tuple' object has no attribute 'append'
"""