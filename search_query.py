import elasticsearch
import pandas as pd
import json

es = elasticsearch.Elasticsearch(http_auth =('elastic','changeme'))  # use default of localhost, port 9200


z= es.search(index='donald', size = 100, body={
  'query': {
    'match': {
      'Tweet_data': 'conflicted' #Mueller is the query word
     }
  }
})

total = z['hits']['total']
print("Total Hits: ", total)
print("")

i = 0
my_list = []
for doc in z["hits"]["hits"]:
    my_list.append(doc["_source"]["Tweet_data"])

my_list.reverse()

while i<total:
    print("Tweet #: ", i+1)
    print(my_list[i])
    print("")
    i=i+1
