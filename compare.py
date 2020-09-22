

with open("result.txt") as file:
	lines = file.readlines()

lineArr = []
for line in lines:
	text = line.rstrip()
	lineArr.append(text)

with open("result_2.txt") as file:
	lines2 = file.readlines()

resArr = []

for line in lines2:
	text = line.rstrip()
	if not text in lineArr:
		resArr.append(text)


print(resArr)