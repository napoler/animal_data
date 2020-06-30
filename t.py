import json
import pymongo
import os
client = pymongo.MongoClient('localhost')
db = client['animal'] #数据库名
collection = db['scientific_names']


species_cs=[]
# scientific_names 学名
for it in  collection.find({}):
    # 
    print(it['genus_c'])
    print("中文名",it['species_c'])
    species_cs.append(it['species_c'])
    print(it)

print(len(species_cs))
# taxa s分类群
# collection = db['taxa']
# for it in  collection.find({}):
#     # 
#     print(it['name_c'])
#     # print(it['genus_c'])
#     print(it)