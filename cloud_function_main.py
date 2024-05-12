import os
from google.cloud import storage
from google.oauth2.service_account import Credentials

def copy_file(data, context):
    source_bucket_name = data['bucket']
    source_file_name = data['name']
    dest_bucket_name = os.environ['DEST_BUCKET_NAME']
    
    # Load service account key from environment variable
    key_path = os.environ.get('SERVICE_ACCOUNT_KEY_PATH')
    if not key_path:
        raise ValueError("Service account key path not provided.")
    
    credentials = Credentials.from_service_account_file(key_path)

    # Authenticate using service account
    storage_client = storage.Client(credentials=credentials)

    source_bucket = storage_client.bucket(source_bucket_name)
    dest_bucket = storage_client.bucket(dest_bucket_name)

    source_blob = source_bucket.blob(source_file_name)
    dest_blob = dest_bucket.blob(source_file_name)

    dest_blob.content_type = source_blob.content_type
    dest_blob.upload_from_string(source_blob.download_as_string())

    print(f'File {source_file_name} copied from {source_bucket_name} to {dest_bucket_name}.')