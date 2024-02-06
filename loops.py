"""
To call repetitive action of block of code

FOR -will be used when we know exact(definite) number of times to execute(For static values)
-------Usage of FOR------
https://github.com/iam-veeramalla/python-for-devops/blob/main/Day-09/03-for-loop-devops-usecases.md


WHILE -used when we don't  know exact number of times to execute(For dynamic values)
-------Usage of WHILE------
https://github.com/iam-veeramalla/python-for-devops/blob/main/Day-09/04-while-loop-devops-usecases.md
"""


"""
for i in range(10):
    print(i)  #prints 0 to 9

for i in range(10):
    print("lahiru")
    print("Galhena")
"""

#---------------------
    
s3_buckets = ["Ubuntu_demo","Lahiru123","Web02", 445, 772]
for x in s3_buckets:
    print(x)

"""
OUTPUT

Ubuntu_demo
Lahiru123
Web02
445
772
"""