import re


string = "“I have not failed. I&#39;ve just found 10,000 ways that won&#39;t work.”"
r = re.search("&#39", string);
print(r)
r = re.sub("&#39", "'", string)
print(r)