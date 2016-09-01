import linecache
array = []
file1 = "27.txt"
for i in range(8,17):
	array.append(linecache.getline(file1, i).split()[7])
for i in range(17,38):
	array.append(linecache.getline(file1, i).split()[6])
for i in xrange(len(array)):
	array[i] = float(array[i])
for i in xrange(len(array)):
	if array[i] > 35:
		array[i] = array[i]/1000;
print array

