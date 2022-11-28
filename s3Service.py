import json
import logging

import boto3
import pandas as pd
from botocore.exceptions import ClientError

class s3service:
    def __init__(self):
        data = pd.read_csv('s3key.csv')
        self.access_key = data['Access key ID'].to_list()[0]
        self.secret_key = data['Secret access key'].to_list()[0]
        self.client = boto3.client(
            's3',
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key
        )
        self.bucket_name = ""
    def makeBucket(self,name):
        policy = {
            "Version": "2012-10-17",
            "Statement": [{
                "Sid": "PublicReadObject",
                "Effect": "Allow",
                "Action": ["s3:GetObject"],
                "Principal":"*",
                "Resource": [f"arn:aws:s3:::{name}/*"],
                "Condition": {
                    "StringLike":{
                        "aws:userId":[
                            "AROAEXAMPLEID:awesome-winter",
                            "AIDAEXAMPLEID",
                            "123456789012"
                        ]
                    }
                }
            }]
        }
        try:
            res = self.client.create_bucket(
                Bucket=name,
                CreateBucketConfiguration={'LocationConstraint': 'ap-northeast-2'}
            )
            self.client.put_bucket_policy(Bucket=name,Policy=json.dumps(policy))
            self.bucket_name = name
        except ClientError:
            logging.exception("clientError")
            raise

        return res

    def upload_file(self, file):
        # filename 테스트 후 이름 바꾸기
        try:
            res = self.client.upload_fileobj(file.file, self.bucket_name, file.filename,
                                             ExtraArgs={'ContentType': file.content_type, 'ACL': 'public-read'})
        except ClientError as e:
            logging.error(e)
            raise
        return res