#!/bin/bash

# download script
BASE_URL="https://datasets.imdbws.com/" 
DATASETS=("title.episode.tsv.gz" "title.ratings.tsv.gz") 

for DS in "${DATASETS[@]}"; do
	curl "$BASE_URL$DS" -o ./data/$DS | gzip -d
done

# additional datasets from imdb
# name.basics.tsv.gz
# title.akas.tsv.gz
# title.basics.tsv.gz
# title.crew.tsv.gz
# title.principals.tsv.gz