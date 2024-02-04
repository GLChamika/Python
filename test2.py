import re

text = "This test is to find a word called json"
pattern = "json"

match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
