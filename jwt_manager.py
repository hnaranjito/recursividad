import os
from jwt import encode, decode
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('SECRET-KEY')


def create_token(data: dict):
    token: str = encode(payload=data, key=api_key, algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    data: dict = decode(token, key="my_secret_key", algoritms=['HS256'])
    return data
