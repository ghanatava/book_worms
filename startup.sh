#!/bin/bash

#installing dependencies
pip install -r requirements.txt



#testing our application and runnning the code

python3 manage.py runserver 0.0.0.0:8000

python3 manage.py test | tee test_results.txt

if [ $? -eq 0 ]
then
    python3 manage.py runserver 0.0.0.0:8000
else
    echo "Test failed"
    cat test_results.txt
fi
