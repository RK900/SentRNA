import os
import pickle

batch1_path = 'models/refined_models/batch1/'
batch2_path = 'models/refined_models/batch2/'
matlot_path = 'models/refined_models/matlot/'
# mcf_path = 'models/refined_models/mcf/'


batch1_pickles = []
batch2_pickles = []
matlot_pickles = []
mcf_pickles = []

for root, d, files in os.walk(batch1_path):
    batch1_pickles = files

for root, d, files in os.walk(batch2_path):
    batch2_pickles = files

for root, d, files in os.walk(matlot_path):
    matlot_pickles = files

matlot_pickles = matlot_pickles[1:]

# for root, d, files in os.walk(mcf_path):
#     mcf_pickles = files


batch1_results = []
batch2_results = []
matlot_results = []
# mcf_results = []

for p in batch1_pickles:
    batch1_results.extend(pickle.load(open(batch1_path + p, 'rb')))

for p in batch2_pickles:
    batch2_results.extend(pickle.load(open(batch2_path + p, 'rb')))

for p in matlot_pickles:
    matlot_results.extend(pickle.load(open(matlot_path + p, 'rb')))

# for p in mcf_pickles:
#     mcf_results.extend(pickle.load(open(mcf_path + p, 'rb')))

all_results = batch2_results #+ batch2_results + matlot_results
score = [0] * 100
print(len(score))
i = 0
for result in all_results:
    print(result)
    if len(result) == 3 and result[2] == 1.0:
        score[i] = 1
    i = (i+1) % 100
print(len(all_results))
print(sum(score))
print(score)