import numpy
import csv
from scipy.spatial import distance
import math

filename='data/4clusters.csv'
    

#Parse the csv file to a list named full_list
def parse_csv_to_list(filename):
    full_list = []

    with open(filename, 'r') as csvfile:
    	csv_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    	for row in csv_reader:
    		full_list.append(row)
    return full_list

full_list=parse_csv_to_list(filename)

#Returns number of columns
def num_of_lists(full_list):
    for separator in full_list:
        number_of_lists=len(separator[0].split(','))
    return number_of_lists

number_of_lists=num_of_lists(full_list)

#Puts columns in a list column_lists. column_lists is a list that contains list for every column
def list_of_columns(number_of_lists,full_list):
    column_lists=[]
    temp_list=[]
    for i in range(0, number_of_lists):
        for row in full_list:
            temp_list.append(int((row[0].split(',')[i ])))
        column_lists.append(temp_list)
        temp_list=[]
    return column_lists

column_lists=list_of_columns(number_of_lists, full_list)

#Returns the minimum of every columns
def minimum_lists(number_of_lists, column_lists):
    min_list=[]
    for i in range(0, number_of_lists):
        min_list.append(min(column_lists[i]))
    return min_list    

#Returns the maximum of every column
def maximum_lists(number_of_lists, column_lists):
    max_list=[]
    for i in range(0, number_of_lists):
        max_list.append(max(column_lists[i]))
    return max_list        

c1=minimum_lists(number_of_lists,column_lists)
c2=maximum_lists(number_of_lists,column_lists)


def form_clusters(column_lists,c1,c2):

    cluster=[]
    cluster1=[]
    cluster2=[]
    
    for i in range(0, len(full_list)):


        euclid1 = math.sqrt(pow(((column_lists[0])[i] - c1[0]),2) + pow(((column_lists[1])[i] - c1[1]),2))
        euclid2 = math.sqrt(pow(((column_lists[0])[i] - c2[0]),2) + pow(((column_lists[1])[i] - c2[1]),2))

        if euclid1 <= euclid2:
            cluster1.append(full_list[i])
        else:
            cluster2.append(full_list[i])

    cluster.append(cluster1)
    cluster.append(cluster2)        
    return cluster



cluster1=form_clusters(column_lists,c1,c2)[0]
cluster2=form_clusters(column_lists,c1,c2)[1]


def average(cluster):
    new_centriom=[]
    cluster_length=len(cluster)
    cluster_columns=list_of_columns(2,cluster)
    new_centriom.append((sum(cluster_columns[0])/cluster_length))
    new_centriom.append((sum(cluster_columns[1])/cluster_length))
    return new_centriom

#print(average(cluster1))

cluster1_1=average(cluster1)
cluster2_2=average(cluster2)

#print(form_clusters(column_lists,cluster1_1,cluster2_2)[0])





