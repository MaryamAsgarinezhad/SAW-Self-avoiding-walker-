import random
import json
test = [[[0,1], [1,2]], [[2,1], [3,2]]]

encode = json.dumps(test)
print(encode)

test = json.loads(encode)

print(test[0][1][0])

for i in range (1000000):
    random.randint(0, 10000000)

# file = open("test.txt", "w")
# for list in test:
#     for element in list:
#         file.write(str(element) + ",")
#     file.write("\n")
#
# file.close()
#
# file = open("test.txt", "r")
# all = []
# for lines in file.readlines():
#     list = lines.split(",")
#     sample = []
#     for element in list:
#         file.write(str(element) + ",")
#     file.write("\n")
# print(random.randint(1, 7))