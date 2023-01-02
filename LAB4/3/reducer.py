#!/usr/bin/env python3
import sys
import statistics as st

current_num = None
current_count = 0
list = []

print("Count of diffrent numbers:")
for line in sys.stdin:

	num, count = line.split('\t')
	list.append(float(num))
	count = int(count)
	if num == current_num:
		current_count += count
	else:
		if current_num:
			print('{0}\t{1}'.format(current_num, current_count))
		current_num = num
		current_count = count

if current_num == num:
	print('{0}\t{1}'.format(current_num, current_count))

mean = sum(list)/len(list)
maximum = max(list)
median = st.median(kist)
# geometrical mean
mean_geo = 1
for number in list:
	mean_geo = mean_geo * number
mean_geo = mean_geo ** (1/len(list))
#numbers of diffrent numbers
diff_num = []
for number in list:
	if number not in diff_num:
		number.append(diff_num)
diff_num_num = diff_num.len()

print(f"Aritmetic mean: {round(mean, 2)}")
print(f"Maximum value: {round(maximum, 2)}")
print(f"Median: {round(median, 2)}")
print(f"Geometrical mean: {round(mean_geo), 2}")
print(f"Numbers of diffrent numbers: {diff_num_num}")
