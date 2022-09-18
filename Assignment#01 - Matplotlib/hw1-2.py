import matplotlib.pyplot as plt

January_temp = []
August_temp = []

with open('Seoul.csv','r') as file:
    file.readline()
    for line in file:
        data = line.strip().split(',')

        if data[2].split('-')[1] == '01':
            January_temp.append(float(data[4]))
        if data[2].split('-')[1] == '08':
            August_temp.append(float(data[4]))

plt.hist(January_temp, bins=31, color='b')
plt.hist(August_temp, bins=31, color='r')


plt.xlabel('temperature')
plt.ylabel('number of days')
plt.title('January and August')
plt.show()