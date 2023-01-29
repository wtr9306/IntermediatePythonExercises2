import numpy as np

random_list = np.random.rand(10)
print(random_list)

mean = np.mean(random_list)
median = np.median(random_list)
std_dev = np.std(random_list)

print("Mean: ", mean)
print("Median: ", median)
print("Standard deviation: ", std_dev)
