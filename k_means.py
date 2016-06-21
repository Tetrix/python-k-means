import numpy
import csv
import math
import os



#Parse the csv file to a list named full_list ( form a global list of all the data points)
def parse_csv_to_list(filename):
    full_list = []

    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        full_list=list(csv_reader)
    return [map(float,i) for i in full_list]



#Returns number of columns in file beeing executed
def num_of_lists(full_list):
    return len(full_list[0])


# Function used to put the full_list data point in the two clusters correctly
def form_clusters(c1,c2,cluster,cluster1,cluster2):
    # Loop , while there is no change for the centroids in any of the clusters
    while True:
        for i in range(0,len(full_list)):
            c1_res=0
            c2_res=0
            for j in range(0, number_of_lists):
                # Calculate Euclid distance between the data point and the centroids of the clusters
                c1_res = pow(full_list[i][j] - c1[j],2) + c1_res
                c2_res = pow(full_list[i][j] - c2[j],2) + c2_res
            c1_res=math.sqrt(c1_res)
            c2_res=math.sqrt(c2_res)

            c1=min(full_list)
            c2=max(full_list)

            if c1_res <= c2_res:
                cluster1.append(full_list[i])
            else:
                cluster2.append(full_list[i])

        finish_count=0

        c1=[]
        c2=[]

        for i in range(0,number_of_lists):
            c1.append(0)
            c2.append(0)

        for num in range(0,number_of_lists):
            for elem in cluster1:
                c1[num]=c1[num]+elem[num]
            c1[num]=round(c1[num]/len(cluster1),2)


        for num in range(0,number_of_lists):
            for elem in cluster2:
                c2[num]=c2[num]+elem[num]
            c2[num]=round(c2[num]/(len(cluster2)),2)


        for i in range(0,len(full_list)):
            c1_res=0
            c2_res=0
            for j in range(0, number_of_lists):
                c1_res = pow(full_list[i][j] - c1[j],2) + c1_res
                c2_res = pow(full_list[i][j] - c2[j],2) + c2_res
            c1_res=round(math.sqrt(c1_res),2)
            c2_res=round(math.sqrt(c2_res),2)


            if ((c1_res <= c2_res) and (full_list[i] in cluster1)) or ((c1_res > c2_res) and (full_list[i] in cluster2)):
                finish_count=finish_count+1
                if finish_count==7:
                    cluster.append(cluster1)
                    cluster.append(cluster2)
                    return cluster

        cluster1=[]
        cluster2=[]



for test_suite in os.listdir('data'):
    print "FILE NAME: "+test_suite
    filename='data/'+test_suite
    cluster=[]
    cluster1=[]
    cluster2=[]

    full_list=parse_csv_to_list(filename)
    number_of_lists=num_of_lists(full_list)

    c1=min(full_list)
    c2=max(full_list)


    clusters=form_clusters(c1,c2,cluster,cluster1,cluster2)
    nm_clusters=0

    for cluster in clusters:
        nm_clusters=nm_clusters+1
        print ""
        print "Cluster nm."+str(nm_clusters)
        print "*"*20
        for elements in cluster:
            print elements
        print "*"*20
    print "\n"*5
