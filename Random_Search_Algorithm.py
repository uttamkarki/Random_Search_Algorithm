import numpy as np
import csv
import pandas as pd
from matplotlib import pyplot
import time

start_time = time.process_time()

dataset = pd.read_csv("Instance4.csv")
dummy_data = dataset
p = 15
Dmax = 70
best_obj = -1000000000

for n in range(100):
    solution = np.zeros(p)
    cover_demand = np.zeros(len(dataset))
    cover_weights = np.zeros(len(dataset))
    candidate_solution = list(range(1, len(dataset.columns) - 1))

    for i in range(p):
        solution[i] = np.random.choice(candidate_solution)
        candidate_solution.remove(solution[i])
        dis_index = int(solution[i])

        print("The facility will be in", dis_index)

        for j in range(len(dummy_data)):
            if (dummy_data.iloc[j, dis_index + 1]) < Dmax:
                cover_demand[j] = 1
                cover_weights[j] = dummy_data.iloc[j, 1]

    obj = sum(cover_weights)
    if obj > best_obj:
        best_obj = obj
        best_solution = solution
        bcover_demand = cover_demand
        bcover_weights = cover_weights

    print(best_solution)
    print(bcover_demand)
    print(bcover_weights)
    print(best_obj)


end_time = time.process_time()
print("Total calculation time:", end_time - start_time,'seconds')
exit()