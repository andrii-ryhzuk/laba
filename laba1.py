import csv
import numpy as np

#########################################################

l = np.array([[1, -3, 4], [-2, -1, 2], [-6, 7, -2]])
r = np.array([9, 5, 1])

inv = np.linalg.inv(l) * r

result = []

for i in inv:
    c = 0
    for j in i:
        c += j
    result.append(round(c))

print('Answer ', result)

########################################################

marks = np.random.randint(0, 6, size=(10, 4))
average_marks = []

for idx, v in enumerate(marks):
    temp_len = len(v)
    average_marks.append(sum(v) / temp_len)

max = max(average_marks)
print('Student id=' + str(average_marks.index(max)) + ' with  average mark ' + str(max))


########################################################

def csv_dict_reader(file):
    reader = csv.DictReader(file, delimiter=',')
    for line in reader:
        print(line["first_name"], line["last_name"], line["city"])


def csv_writer(data, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


data = ["first_name,last_name,city".split(","),
        "Tyrese,Hirthe,Strackeport".split(","),
        "Jules,Dicki,Lake Nickolasville".split(","),
        "Dedric,Medhurst,Stiedemannberg".split(",")
        ]

path = "output.csv"
csv_writer(data, path)

with open("output.csv") as f_obj:
    csv_dict_reader(f_obj)
