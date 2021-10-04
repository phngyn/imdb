#!/bin/bash

# make local data directory
DIR_DATA="./data/"

if [ ! -d "$DIR_DATA" ]; then
	mkdir "./data/"
fi

# download script
BASE_URL="https://datasets.imdbws.com/" 
DATASETS=("title.episode.tsv.gz" "title.ratings.tsv.gz") 

for DS in "${DATASETS[@]}"; do
	curl -o "$DIR_DATA$DS" "$BASE_URL$DS"
done

gzip -d ./data/*.gz

# additional datasets from imdb
# name.basics.tsv.gz
# title.akas.tsv.gz
# title.basics.tsv.gz
# title.crew.tsv.gz
# title.principals.tsv.gz