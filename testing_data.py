import csv
import matplotlib
import matplotlib.pyplot as plt


CSV_PATH = 'utilization.csv'


def open_txt(file_path):
    data_list = []
    with open(file_path, 'r') as file_in:
        reader = csv.reader(file_in, delimiter=',')
        for row in reader:
            data_list.append(row)
    
    return data_list

new_list = open_txt(CSV_PATH)
no_header = new_list[1:]
print(no_header)

def utilization(full_list):
    utilization_total = []
    for sub_list in full_list:
        utilization_total.append(sub_list[3])

    return utilization_total


def count_ecs(full_list):
    count_ecs = []
    counter = 1
    for sub_list in full_list:
        count_ecs.append(counter)
        counter += 1
    
    return count_ecs


ec_count = count_ecs(no_header)
utilization_full = utilization(no_header)


def working_list(data_list):
    new_list = []
    for item in data_list:
        new_list.append(int(item[0:2]))
    
    return new_list


total_utlz_list = working_list(utilization_full)
print(ec_count)
print(total_utlz_list)

