import boto3 

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
# for bucket in s3.buckets.all():
#     print(bucket.name)

with open('lea.jpg', 'rb') as data:
    s3.Bucket('s3-ember-we').put_object(Key='lea.jpg', Body=data)

# s3_client = boto3.client('s3')
# bucket_name = "s3-ember-we"
# object_name = "ananas.jpg"  # nom exact dans S3

# url = s3_client.generate_presigned_url(
#     'get_object',
#     Params={'Bucket': bucket_name, 'Key': object_name},
#     ExpiresIn=3600  # durée de validité en secondes (ici 1h)
# )

# print("URL pré-signée :", url)

# s3 = boto3.client('s3')
# s3.download_file('s3-ember-we', 'ananas.jpg', 'ananas_local.jpg')