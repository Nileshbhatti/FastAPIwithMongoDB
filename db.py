# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 06:01:45 2022

@author: nilesh.b
"""

import pymongo

myclient = pymongo.MongoClient("mongodb://vmpaymongoel01:27017,vmpaymongoel02:27017,vmpaymongoel03:27017/?replicaSet=PayOdsRs0")
#print("Connected to MongoDB Server")
mydb = myclient["payodsdb"]
collection = mydb["payment"]
#print("Connected to ', mydb, ' Database")


def all():
    response = collection.find({}).limit(10)
    data = []
    for i in response:
        i["_id"]  = str(i["_id"])
        data.append(i)
    return data

def get_one(l_parameter):
    response = collection.find_one({"FR_ACCT_NUM": l_parameter})
    response["_id"]  = str(response["_id"])
    return response
 
