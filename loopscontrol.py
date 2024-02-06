#break
#continue

s3_buckets = ["Ubuntu_demo","Lahiru123","Web02", 445, 772]
for x in s3_buckets:
    if x == "Web02":
        break #stops on 'Web02'
    print(x)

"""
---OUTPUT---
Ubuntu_demo
Lahiru123
"""

s3_buckets = ["Ubuntu_demo","Lahiru123","Web02", 445, 772]
for x in s3_buckets:
    if x == "Web02":
        continue #Never stops  but ignore the 'Web02', and the rest will be continued
    print(x)

"""
---OUTPUT---
Ubuntu_demo
Lahiru123
445
772
"""