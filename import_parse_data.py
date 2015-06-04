from boto.s3.connection import S3Connection
from boto.s3.key import Key
from argparse import ArgumentParser
import os
import json

parser = ArgumentParser()
parser.add_argument("--dir", metavar='d', dest="dir")
parser.add_argument("--key", metavar='k', dest='key')
parser.add_argument("--secret", metavar='s', dest='secret')
parser.add_argument("--prefix", metavar='p', dest='prefix')
args = parser.parse_args()

conn = S3Connection(args.key, args.secret)

for file in os.listdir(args.dir):
	bucket_name = file.split('.')[0].lower()
	print "Creating " + bucket_name + " bucket"
	bucket = conn.create_bucket(args.prefix + "_" + bucket_name)
	print "Importing data for " + args.prefix + "_" + bucket_name
	with open(args.dir + '/' + file) as table:
		rows = json.load(table)
		for row in rows["results"]:
			k = Key(bucket)
			k.key = row["objectId"]
			k.set_contents_from_string(json.dumps(row))
