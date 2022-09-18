import matplotlib.pyplot as plt

highest_temp = []
lowest_temp = []

with open('Seoul.csv','r') as file:
    file.readline()
    for line in file:
        data = line.strip().split(',')

        if data[2].split('-')[1] == '08':
            highest_temp.append(float(data[4]))
            if data[6] != '' and data[4] != '':
                lowest_temp.append(float(data[6]))

plt.plot(range(len(highest_temp)), highest_temp, color='r', label='highest temp')
plt.plot(range(len(lowest_temp)), lowest_temp, color='b', label='lowest temp')

plt.xlabel('day')
plt.ylabel('temperature')
plt.title('August')
plt.legend()
plt.show()