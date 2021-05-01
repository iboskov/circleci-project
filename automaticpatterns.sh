#!/bin/bash

curl -k -u elastic:changeme -H 'Accept: application/json' "http://localhost:9200/_cat/indices" >> indices.json
#echo $indices


#for row in indices
#do
#    echo "works"
#done

#jq -r '.[]' indices.json
for i in $(jq -r '.[]' indices.json)
do
   if [ == "metricbeat"]; then
	echo "got index"
   fi
done
