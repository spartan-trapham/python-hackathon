import boto3
from botocore.client import Config


def create_presigned_post(bucket_name, object_name, expiration=3600, size_limit=10485760):
    """
    :param object_name:
    :param bucket_name:
    :param expiration: Time in seconds for the presigned URL to remain valid
    :param size_limit: Size limit in byte
    """
    s3_client = boto3.client('s3', config=Config(signature_version='s3v4'))  # Specify signature version as s3v4

    # Set additional fields and conditions for the upload request
    # Set size limit for uploaded file (in bytes)
    conditions = [
        ['content-length-range', 0, size_limit]  # Restrict file size between 0 and size_limit bytes
    ]

    response = s3_client.generate_presigned_post(
        Bucket=bucket_name, Key=object_name, Conditions=conditions, ExpiresIn=expiration
    )

    # The response contains the presigned URL and required fields
    return response
