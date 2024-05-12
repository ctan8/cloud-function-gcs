#!/bin/bash

# Set the environment variables
export SOURCE_BUCKET="dna-source-iam"
export DESTINATION_BUCKET="dna-destination-iam"
export GOOGLE_APPLICATION_CREDENTIALS="./sa-key.json"

# Run the Python script with the provided file name
python3 main.py "$1"