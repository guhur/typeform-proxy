tmpfile=$(mktemp /tmp/adlr-api.XXXX)
echo "SECRET=mysecrettoken" >> $tmpfile
echo "SQLITE=True" >> $tmpfile

docker run --env-file $tmpfile  \
	annuairedelarenovation/api-python:latest \
	-c "pip install -r requirements-dev.txt; pytest"
