# boto3를 이용한 AWS S3 bucket 생성 api
<br>

### install command
```shell
pip install -r requirements.txt  
```

### Run mainApp command
```
uvicorn main:app --reload
```

## Create bucket

### Request

`GET /{bucket_name}`

    curl -i -H 'Accept: application/json' -d http://localhost:8000/newbucket

### Response

    {"ResponseMetadata":{
        "RequestId":"",
        "HostId":"",
        "HTTPStatusCode":200,
        "HTTPHeaders":{
            "x-amz-id-2":"",
            "x-amz-request-id":"",
            "date":"",
            "location":"http://newbucket.s3.amazonaws.com/",
            "server":"AmazonS3","content-length":"0"},
            "RetryAttempts":0
        },
        "Location":"http://newbucket.s3.amazonaws.com/"}


