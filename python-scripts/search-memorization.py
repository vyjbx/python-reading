'''
We have a recent problem to find the best solution from a range of numbers. The function will be called millions of times. The numbers are integers in a range defined by upper_limit and lower_limit. The number of choices is not infinite.
There are few ways to search for the best solution.
1. brute-force sequential search, maybe with some parallization (unfortunately python only benefits in I/O heavy applicatons.)
2. binary search, and when it may not work
3. prioritized queue
4. record conditions and memorization 
'''