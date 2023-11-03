import os
from pymongo import MongoClient
import numpy as np
import cv2

sample = cv2.imread("D:/Reva Hack/2/sih-project-2022-master/sih-project-2022-master/sih-project-final/fingerdata/839314868452.bmp")
client = MongoClient("mongodb+srv://tejasag:aadharDB@cluster0.ni6wv6x.mongodb.net/")
db = client["aadharDB"]
finger_data = db["fingerDB"]
doc = {
    "Aadhar": "839314868452",
    "finger": sample.tolist()
}
print(type(sample))
finger_data.insert_one(doc)
print(sample)
print(np.array(doc["finger"]))
data = finger_data.find({})
i = 0
for dat in data:
    print(i)
    i += 1
    print(np.array(dat["finger"]))
