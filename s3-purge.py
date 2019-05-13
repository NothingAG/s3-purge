#!/usr/bin/env python3
import argparse
import boto3


def purge(bucket, numkeep, dry_run):
    candidates = sorted(bucket.objects.all(),
                        key=lambda obj: obj.last_modified, reverse=True)

    keep = candidates[0:numkeep]
    purge = candidates[numkeep:]

    print('will keep {:d} most recent objects, will purge {:d} objects'.format(
        len(keep),
        len(purge)
    ))

    if dry_run:
        print('dry run, exiting')
    elif len(purge) > 0:
        for obj in purge:
            obj.delete()
        print('purged {:d} objects'.format(len(purge)))
    else:
        print('nothing to do')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Purge files from s3 compatible storage.')
    parser.add_argument(
        'bucket', metavar='BUCKET', type=str,
        help='the bucket which will be purged')
    parser.add_argument(
        'numkeep', metavar='KEEP', type=int,
        help='how many objects should be kept')
    parser.add_argument(
        '--dry-run', dest='dry_run', action='store_true', default=False,
        help='just display what will happen, nothing deleted')
    parser.add_argument(
        '--endpoint-url', dest='endpoint_url', action='store',
        help='specify the endpoint url when accessing non-aws services')

    args = parser.parse_args()

    resource = boto3.resource(
        service_name='s3', endpoint_url=args.endpoint_url)
    bucket = resource.Bucket(args.bucket)

    purge(bucket, args.numkeep, args.dry_run)
