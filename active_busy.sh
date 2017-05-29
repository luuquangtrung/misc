#!/bin/bash

rm result.txt

DATE=`date +%Y-%m-%d:%H:%M:%S`
echo "Date: $DATE" >> result.txt
echo "t active busy ratio">> result.txt

for t in `seq 1 1 60`

do 
	sleep $t
	#resultat=`sudo iw wlp3s0 survey dump | grep active`

	iw wlp3s0 survey dump > out
	file=$(<out)

	busy=$(echo "$file" | sed '4q;d' | grep -o "[0-9]*") 
	active=$(echo "$file" | sed '3q;d' | grep -o "[0-9]*") 
	ratio=$(echo "scale=6; $busy/$active" | bc)
	echo "$t $active	$busy	$ratio"
	echo "$t $active	$busy	$ratio">> result.txt

done

