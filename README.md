This is a python implementation of k-means algorithm

* at the moment the implementation of the algorithm works only for numbers
* it uses the Euclidean equation , to calculate the distance between the data point and the cluster centroid

------------------------------------------------------------------------------------------------------------

Technologies used:

-python
-python internal libraries (numpy,csv,math,os)


------------------------------------------------------------------------------------------------------------

Scenario:

* In this implementation we use K=2 , which means every data splits into two clusters.

1. Read the the files one by one in the "data" folder, and convert them into lists.
2. Find optimal centroids for each of the clusters.
3. Calculate distance between the certain data point and the centroids of the clusters.
4. Append the data point to the cluster, which has a least distance between it's centroid and the data point
5. Iterate trough the array (full_list) while there are no changes in the clusters, the algorithm is over.

------------------------------------------------------------------------------------------------------------

Invocation:

- In the (Linux shell/Windows cmd) executre "python k_means.py"
