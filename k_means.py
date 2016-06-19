import numpy
import csv
from scipy.spatial import distance
import math
from random import randint

filename='data/4clusters.csv'


#Parse the csv file to a list named full_list
def parse_csv_to_list(filename):
    full_list = []

    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        full_list=list(csv_reader)
    return [map(int,i) for i in full_list]

full_list=parse_csv_to_list(filename)

#Returns number of columns
def num_of_lists(full_list):
    return len(full_list[0])

number_of_lists=num_of_lists(full_list)

c1=min(full_list)
c2=max(full_list)

def form_clusters(column_lists,num_of_lists,c1,c2):
    cluster=[]
    cluster1=[]
    cluster2=[]
    c1_res=0
    c2_res=0
    #for i in range(1,len(full_list)):
    for i in range(0,len(full_list)):
        for j in range(0, number_of_lists):
            c1_res = pow(full_list[i][j] - c1[j],2) + c1_res
            c2_res = pow(full_list[i][j] - c2[j],2) + c2_res
        c1_res=round(math.sqrt(c1_res),2)
        c2_res=round(math.sqrt(c2_res),2)

        if c1_res <= c2_res:
            for num in range(0,number_of_lists):
                element=(full_list[i][num]+c1[num])/2
                c1[num]=element
            cluster1.append(full_list[i])

        else:
            for num in range(0,number_of_lists):
                element=(full_list[i][num]+c2[num])/2
                c2[num]=element
            cluster2.append(full_list[i])

        count=count+1

    cluster.append(cluster1)
    cluster.append(cluster2)

    return cluster


clusters=form_clusters(full_list,number_of_lists,c1,c2)
for c in clusters:
    print c
    print "**********"
    print "**********"