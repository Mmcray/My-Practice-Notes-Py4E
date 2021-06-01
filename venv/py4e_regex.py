import re

fh = open('py4e-data.dr-chuck.net_regex_sum_1258250.txt')
fr = fh.read()

regex = '[0-9]+'
lst = re.findall(regex, fr)
sm=0
for val in lst:
    val = int(val)
    sm += val
print(sm)
