import matplotlib.pyplot as plt
import csv

years = []
pops = []
deaths = []
with open('worlddata.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            for column in row:
                years.append(int(column))
            line_count += 1
        elif line_count == 1:
            for column in row:
                pops.append(float(column))
            line_count += 1
        elif line_count == 2:
            for column in row:
                deaths.append(float(column))
            line_count += 1
    print(years)
    print(pops)

lines = plt.plot(years, pops, years, deaths)
plt.grid(True)

plt.setp(lines, color=(1, 0.4, 0.4), marker=".")

plt.show()
