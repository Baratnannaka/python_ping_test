import csv
import os
f = open('hosts.csv', 'r')
reader = csv.reader(f)
for row in reader:
	if row[0] == "name":
		pass
	else:
		print("pinging {}...".format(row[0]))
		ping_responds = os.system("ping -c 1 " + row[1] + " > /dev/null 2>&1")
		if ping_responds == 0:
			print("{} is alive" .format(row[0]))
		else:
			print("{} is not alive" .format(row[0]))
f.close()
