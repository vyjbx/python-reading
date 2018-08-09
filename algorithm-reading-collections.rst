##########
Algorithm Collections
##########

1. approximated k-nearest neighbour
    [Approximated_KNN]_

	Summary:
	Partition step:
	step 1: partition (cluster) data with k-means into K clusters
	step 2: mean center each cluster. Now note the range of the variations within clusters is MUCH smaller comparing to whole data set. 
	step 3: data query happens within each cluster after query vector is centered by the cluster mean.

	Two advantages:
	1. through partitioning, now query is only compared with data in top M clusters with closest centroid to query distance
	2. through mean centering, the range of values is much smaller, giving much higher accuracy in Approximation step

	Approximation step:
	Note the Approximation step is independent of Partition step.
	1. assume data are m by n. partition data into L sets of m by n_i, with Sum(n_i) = n
	2. within each m by n_i matrix, use k-means to have J centroid; note J centroid are trained on some data, not necesserily optimized on one data set (k-means does not guarantee that anyway). This can be across clusters defined in step partition step.
	3. use the cluster centroid to represent data within that cluster. Note centroid is a symbol here. Now each data point becomes a m by L matrix
	4. build a look-up-table (LUT) to calculate centroid to centroid distance. The table is only L(L-1). The distance is combined as of L2 distance.
	5. approximate distance between query and data point with the new distance. 

	6. apply this with data within each cluster.


2. XGBoost
    [xgboost]_

#. Comparison of different ML frameworks: R vs. Python (scikit-learn) vs. H2O(3) vs. XGBoost vs. Spark vs. Wovpal Wabbit
    https://github.com/szilard/benchm-ml#summary 


.. [Approximated_KNN] http://mccormickml.com/2017/10/13/product-quantizer-tutorial-part-1/
.. [xgboost] https://arxiv.org/pdf/1603.02754.pdf






