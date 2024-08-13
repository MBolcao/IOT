import boto3
from botocore.exceptions import NoCredentialsError

def download_from_s3(bucket_name, object_name, file_name):
    # Crie um cliente S3
    s3_client = boto3.client('s3')

    try:
        s3_client.download_file(bucket_name, object_name, file_name)
        print(f"Arquivo {object_name} baixado com sucesso do bucket {bucket_name} para {file_name}.")
        return True
    except FileNotFoundError:
        print(f"Arquivo {file_name} não encontrado.")
        return False
    except NoCredentialsError:
        print("Credenciais não disponíveis.")
        return False

# Parâmetros para o upload
file_name = 'C:/POST/FluxoCaixa.csv'
bucket_name = 'FluxoCaixa'
object_name = 'FluxoCaixa.csv'  # Opcional

# Fazer o download
download_from_s3(bucket_name, object_name, file_name)
