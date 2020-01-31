# import random
# import os
# path = '/mnt/sdc_ssd/prateek/all_datasets/big-dataset1/non_text'
# files = []
# # r=root, d=directories, f = files
# for r, d, f in os.walk(path):
#     for file in f:
#         if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".JPG") or file.endswith(".JPEG") or file.endswith(".png"):
#             files.append(os.path.join(r, file))

# random.shuffle(files)

# print(files[:3])


# import pickle
# with open("shuffle-output-non-text.txt", "wb") as fp:   #Pickling
#     pickle.dump(files, fp)