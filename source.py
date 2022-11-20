from ast import Lambda
import csv
from statistics import mean
from collections import OrderedDict

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name , 'r') as file:
        with open(output_file_name , 'w' , newline='\n') as wfile:
            reader = csv.reader(file)
            writer = csv.writer(wfile)
            for row in reader:
                list1 = list()
                student_name = row.pop(0)
                list1.append(student_name)
                grade_mean = (float(grade) for grade in row)
                list1.append(mean(grade_mean))
                writer.writerow(list1)

def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name , 'r') as rfile:
        with open (output_file_name , 'w' , newline='\n') as wfile:
            reader = csv.reader(rfile)
            writer = csv.writer(wfile)
            dic = OrderedDict()
            for row in reader:
                name = row.pop(0)
                grade_mean = (float(grade) for grade in row)
                dic[name] = mean(grade_mean)
            for item in sorted(list(dic.items()), key=lambda x: (x[1], x[0])):
                list1 = [item[0],item[1]]
                writer.writerow(list1)

def calculate_three_best(input_file_name, output_file_name):
    
    with open(input_file_name , 'r') as rfile:
        with open(output_file_name , 'w' , newline='\n') as wfile:
            reader = csv.reader(rfile)
            writer = csv.writer(wfile)
            dic = OrderedDict()
            for row in reader:
                name = row.pop(0)
                grade_name = (float(grade) for grade in row)
                dic[name] = mean(grade_name)
            list1=[]
            for item in sorted(list(dic.items()) , key=lambda x: (-x[1] , x[0])):
                list1.append(item)
            count = 0
            for tuple in list1:
                writer.writerow(tuple)
                count += 1
                if count ==3:
                    break

def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name, 'r') as rfile:
        with open(output_file_name , 'w' , newline='\n') as wfile:
            reader = csv.reader(rfile) 
            dic = OrderedDict()
            list1 =[]
            for row in reader:
                name = row.pop(0)
                grade_mean = (float(grade) for grade in row) 
                list1.append(mean(grade_mean))
            list1 = sorted(reversed(list1))
            for avg in list1[:3]:
                wfile.write('%s \n' %(str(avg)))


def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name, 'r') as rfile:
        with open(output_file_name , 'w' , newline='\n') as wfile:
            reader = csv.reader(rfile)
            list1 = []
            for row in reader:
                del row[0]
                grade_avg = (float(grade) for grade in row) 
                list1.append(mean(grade_avg))
            avg = mean(list1)
            wfile.write(str(avg))
