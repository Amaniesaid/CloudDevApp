import boto3
from botocore.exceptions import ClientError

# --- CONFIGURATION ---
bucket_name = "s3-ember-we"  # Remplace par ton bucket
region = "eu-north-1"
file_path = r"C:\Users\bateb\OneDrive\Bureau\cours\info_IMT\S3\DevOps\amanie\CloudDevApp\templates\Ajouter_publication.html"
object_name = "Ajouter_publication.html"

# --- Connexion S3 ---
s3_client = boto3.client('s3', region_name=region)

# --- 2️⃣ Activer l'hébergement statique ---
s3_client.put_bucket_website(
    Bucket=bucket_name,
    WebsiteConfiguration={
        'IndexDocument': {'Suffix': 'index.html'}
    }
)
print("Hébergement statique activé.")

# --- 3️⃣ Débloquer l'accès public du bucket ---
s3_client.put_public_access_block(
    Bucket=bucket_name,
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    }
)
print("Blocage d'accès public désactivé.")

# --- 4️⃣ Upload du fichier HTML avec accès public ---
s3_client.upload_file(
    Filename=file_path,
    Bucket=bucket_name,
    Key=object_name,
    ExtraArgs={'ACL': 'public-read', 'ContentType': 'text/html'}
)
print("Fichier HTML uploadé et rendu public.")

# --- 5️⃣ URL du site statique ---
website_url = f"http://{bucket_name}.s3-website-{region}.amazonaws.com/"
print("Ton site web statique est prêt !")
print("Ouvre cette URL dans ton navigateur :", website_url)
