import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(file_name, bucket, object_name=None):
    # Se object_name não for especificado, use file_name
    if object_name is None:
        object_name = file_name

    # Crie um cliente S3
    s3_client = boto3.client('s3')

    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"Arquivo {file_name} enviado com sucesso para o bucket {bucket} com o nome {object_name}.")
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

# Fazer o upload
upload_to_s3(file_name, bucket_name, object_name)
