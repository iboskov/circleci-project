import argparse, json, requests
from requests.auth import HTTPBasicAuth

parser = argparse.ArgumentParser(description='Create automatically index patterns, from elasticsearch indices.')
parser.add_argument('elasticsearch_url',type=str, help='elasticsearch full URL')
parser.add_argument('kibana_url', type=str, help='kibana full URL')

args = parser.parse_args()

indices = requests.get(args.elasticsearch_url + "/_cat/indices?format=json", auth=HTTPBasicAuth('elastic', 'changeme'), verify=False).json()
print (indices)

for index in indices:
    if str.startswith(index['index'], "metricbeat"):
        print("PRINT THE NAME OF THE INDEX", index["index"])
        payload={
            "attributes": {
                "title": "metricbeat-*",
                "timeFieldName": "@timestamp"
            }
        }
        name = str.replace(index["index"], "metricbeat", "")
        ret = requests.post(args.kibana_url + "/api/saved_objects/index-pattern/" + name, json=payload, headers={"kbn-xsrf":"true"}, auth=HTTPBasicAuth('elastic', 'changeme'), verify=False)
        print(ret.json())
    elif str.startswith(index['index'], "logstash"):
        print("PRINT THE NAME OF THE INDEX", index["index"])
        payload={
            "attributes": {
                "title": "logstash-*",
                "timeFieldName": "@timestamp"

            }
        }
        name = str.replace(index["index"], "logstash", "")
        ret = requests.post(args.kibana_url + "/api/saved_objects/index-pattern/" + name, json=payload, headers={"kbn-xsrf":"true"}, auth=HTTPBasicAuth('elastic', 'changeme'), verify=False)
        print(ret.json())
