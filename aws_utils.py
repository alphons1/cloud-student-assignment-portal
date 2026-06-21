from dotenv import load_dotenv
import os
import boto3

load_dotenv()

BUCKET_NAME = "eae-cloud-project-alphons"

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name="ap-southeast-1"
)

def upload_file(file):
    s3.upload_fileobj(
        file,
        BUCKET_NAME,
        file.name
    )

def get_files():
    response = s3.list_objects_v2(
        Bucket=BUCKET_NAME
    )

    if "Contents" not in response:
        return []

    return [
    {
        "Filename": obj["Key"],
        "Size": obj["Size"],
        "LastModified": obj["LastModified"]
    }
    for obj in response["Contents"]
]