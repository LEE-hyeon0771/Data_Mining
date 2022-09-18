import matplotlib.pyplot as plt

Jan_temp = []
Feb_temp = []
Mon_temp = []
Api_temp = []
May_temp = []
Jun_temp = []
July_temp = []
Aug_temp = []

with open('Seoul.csv','r') as file:
    file.readline()
    for line in file:
        data = line.strip().split(',')

        if data[2].split('-')[1] == '01':
            Jan_temp.append(float(data[3]))
        if data[2].split('-')[1] == '02':
            Feb_temp.append(float(data[3]))
        if data[2].split('-')[1] == '03':
            Mon_temp.append(float(data[3]))
        if data[2].split('-')[1] == '04':
            Api_temp.append(float(data[3]))
        if data[2].split('-')[1] == '05':
            May_temp.append(float(data[3]))
        if data[2].split('-')[1] == '06':
            Jun_temp.append(float(data[3]))
        if data[2].split('-')[1] == '07':
            July_temp.append(float(data[3]))
        if data[2].split('-')[1] == '08':
            Aug_temp.append(float(data[3]))

plt.boxplot([Jan_temp, Feb_temp, Mon_temp, Api_temp, May_temp, Jun_temp, July_temp, Aug_temp])
plt.xlabel('month')
plt.ylabel('temperature')
plt.title('January to August')
plt.show()



