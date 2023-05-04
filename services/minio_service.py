from minio import Minio
from typing import Text
from io import BytesIO
import json


class MinioService:
    def __init__(self, minio_config):
        self.minio_congfig = minio_config
        self.client = Minio(minio_config['url'], access_key=minio_config['user'], secret_key=minio_config['password'], secure=False)

    def init(self, bucket_name):
        if not self.client.bucket_exists(bucket_name):
            self.client.make_bucket(bucket_name)
            self.set_public_bucket(bucket_name)
        else:
            print(f"Bucket {bucket_name} already exists")

    def set_public_bucket(self, bucket_name):
        policy_json = {
            "Statement": [
                {
                    "Action": ["s3:GetBucketLocation", "s3:ListBucket"],
                    "Effect": "Allow",
                    "Principal": {"AWS": ["*"]},
                    "Resource": [f"arn:aws:s3:::{bucket_name}"]
                },{
                    "Action": ["s3:GetObject"],
                    "Effect": "Allow",
                    "Principal": {"AWS": ["*"]},
                    "Resource": [f"arn:aws:s3:::{bucket_name}/*"]}],
            "Version": "2012-10-17"}
        self.client.set_bucket_policy(bucket_name, json.dumps(policy_json))

    def set_bytes(self, data: BytesIO, bucket_name: Text, filename, content_type=ContentType.COMMON.value):
        self.init(bucket_name)
        remote_path = f'{TimeUtils.get_now_datetime_str()}{filename}'
        self.client.put_object(bucket_name, remote_path, data, data.getbuffer().nbytes, content_type=content_type)
        return f'http://{self.minio_congfig}/{bucket_name}/{remote_path}'