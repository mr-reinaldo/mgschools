from cryptography.fernet import Fernet
from pwdlib import PasswordHash

from app.core.config import Settings

settings = Settings()
fernet = Fernet(settings.SECRET_KEY.encode())
pwd_context = PasswordHash.recommended()


def encrypt_data(data: str) -> str:
    """Criptografa dados sensíveis."""
    if not data:
        return data
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data.decode()


def decrypt_data(encrypted_data: str) -> str:
    """Descriptografa dados sensíveis."""
    if not encrypted_data:
        return encrypted_data
    decrypted_data = fernet.decrypt(encrypted_data.encode())
    return decrypted_data.decode()


def hash_password(password: str) -> str:
    """Gera um hash seguro para a senha."""
    if not password:
        return password
    hashed_password = pwd_context.hash(password)
    return hashed_password


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica se a senha em texto simples corresponde ao hash."""
    if not plain_password or not hashed_password:
        return False
    return pwd_context.verify(plain_password, hashed_password)
