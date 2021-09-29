#!/bin/sh

# Linux download script
Source="dataurls.txt"
Lines=$(cat $Source)
for Line in $Lines
do
	wget -P ./data/ "$Line"
done

gzip -d ./data/*.gz