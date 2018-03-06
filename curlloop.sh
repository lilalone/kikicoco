for i in $(cat listurl.txt); do
	content="$(curl -I $i)"
	echo "$content" >> output.txt
done

#curl --insecure -v $i 2>&1 | awk 'BEGIN { cert=0 } /^\* Server certificate:/ { cert=1 } /^\*/ { if (cert) print }'