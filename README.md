# parse_s3
Script to import exported JSON files from Parse to AWS S3.

Quick Start
========
* Download and install the lastest version of Python 2.x from http://www.python.org/download/
* Install boto using pip install boto.
* Run git clone https://github.com/jacoblangston/parse_s3.git.

Options
========
All options are required.
  
  --dir                	The directory containing the exported Parse JSON files.
 
  --key <key>           AWS authorization key.
  
  --secret <secret>    	AWS authorization secret.
                         
  --prefix				Prefix for the buckets to create in S3.