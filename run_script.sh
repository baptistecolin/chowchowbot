#!/bin/bash

# creating an archive folder in which pictures will be stored after being tweeted
mkdir -p pics/used

# going through all the files that are stored in the "pics/" folder
for file in `find pics -maxdepth 1 -type f`
do
	# first, the picture is tweeted
	python tweet_script.py "$file"
	# the tweeted picture is archived in the "used" folder
	mv "$file" pics/used
	# then we wait a bit before tweeting another pic
	sleep 60
done
