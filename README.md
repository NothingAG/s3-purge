S3 Purge
========

A simply Python script which purges old objects from an S3 compatible bucket.
This can be used as a workaround for services lacking object lifecycle
policies.

Requirements
------------

* Python > 3.2
* boto3

Usage
-----

```
usage: s3-purge.py [-h] [--dry-run] [--endpoint-url ENDPOINT_URL] BUCKET KEEP

Purge files from s3 compatible storage.

positional arguments:
  BUCKET                the bucket which will be purged
  KEEP                  how many objects should be kept

optional arguments:
  -h, --help            show this help message and exit
  --dry-run             just display what will happen, nothing deleted
  --endpoint-url ENDPOINT_URL
                        specify the endpoint url when accessing non-aws
                        services
```
