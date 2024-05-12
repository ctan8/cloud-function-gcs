import os
from google.cloud import storage
import sys

def move_file(source_bucket_name, destination_bucket_name, file_name):
    storage_client = storage.Client()

    source_bucket = storage_client.bucket(source_bucket_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    source_blob = source_bucket.blob(file_name)
    destination_blob = source_bucket.copy_blob(
        source_blob, destination_bucket, file_name
    )

    source_blob.delete()

    print(f"File {file_name} moved from {source_bucket_name} to {destination_bucket_name}")

if __name__ == "__main__":
    # Read source and destination bucket names from environment variables
    SOURCE_BUCKET = os.environ.get("SOURCE_BUCKET")
    DESTINATION_BUCKET = os.environ.get("DESTINATION_BUCKET")

    # Get the file name from command line arguments
    if len(sys.argv) != 2:
        print("Usage: python local_script.py <file_name>")
        sys.exit(1)
    FILE_NAME = sys.argv[1]

    if not SOURCE_BUCKET or not DESTINATION_BUCKET:
        print("Source or destination bucket not provided.")
    else:
        move_file(SOURCE_BUCKET, DESTINATION_BUCKET, FILE_NAME)