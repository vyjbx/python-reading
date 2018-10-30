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
    However, this is not a fair comparison for Spark. In addition to the version problem, the true power of Spark is as distributed computatonal framework. It scales up, instead of trying to optimize on limited resource.
    https://github.com/szilard/benchm-ml#summary 

		+-------------------------------------+
		| ML Framework                        |
		+=========+======+==========+=========+
		|Framework|Speed |Accuracy  |Can      |
		|         |      |          |edit     |
		+---------+------+----------+---------+
		| Python  |  slow| medium   | yes     |
		+---------+------+----------+---------+
		| R       |very  | medium   | no      |
		+---------+------+----------+---------+
		|spark 1.x|slow  | medium   | yes     |
		+---------+------+----------+---------+
		|H2O      |high  | high     | no      |
		+---------+------+----------+---------+
		|XGBoost  |high  | high     | no      |
		+---------+------+----------+---------+
		|Wabbit   |      |          |         |
		+---------+------+----------+---------+

#. H2O Python API quick intro
    https://www.h2o.ai/wp-content/uploads/2018/01/Python-BOOKLET.pdf


#. A good collection of ResNets and its variations (or HighwayNets as a broader term) with reference link to the original paper!

    https://towardsdatascience.com/an-overview-of-resnet-and-its-variants-5281e2f56035


#. Kalman filter without math depth (but a lot of figures)

    https://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/

#. Bloom filter: is it possibly in a set with limited core memory. Bloom filter is used in databases such as Cassandra

    https://en.wikipedia.org/wiki/Bloom_filter

#. grow regression trees

    http://www.stat.cmu.edu/~cshalizi/350-2006/lecture-10.pdf

#. how trees process categorical variables
    
    categorical encoding

    https://medium.com/data-design/visiting-categorical-features-and-encoding-in-decision-trees-53400fa65931


#. how LightGBM deals with categorical features

    https://www.kaggle.com/c/home-credit-default-risk/discussion/58950

 #. SHAP value, a unified approach to estimate feature importance

    ``Yet the gain method is biased to attribute more importance to lower splits.``
    ``Well…to avoid using them one approach is to first include them in your model and then prune the part of the model that uses them. But just leaving them out of the model could cause the model to “recover” them by just using another correlated surrogate variable.``

	    https://towardsdatascience.com/interpretable-machine-learning-with-xgboost-9ec80d148d27

	    https://github.com/slundberg/shap

    More on what SHAP is and how to calculate it on high level

	    https://medium.com/civis-analytics/demystifying-black-box-models-with-shap-value-analysis-3e20b536fc80

    Code to calculate SHAP value

        https://www.kaggle.com/dansbecker/shap-values

.. [Approximated_KNN] http://mccormickml.com/2017/10/13/product-quantizer-tutorial-part-1/
.. [xgboost] https://arxiv.org/pdf/1603.02754.pdf







