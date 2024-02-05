import os #To read environment variables inside the script

print(os.getenv("APItoken"))
print(os.getenv("passwd"))


"""
export APItoken="asd123" (To set the API token via CLI)

Then run the file
"""