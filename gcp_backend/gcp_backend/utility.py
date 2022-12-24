from multiprocessing import AuthenticationError
import uuid
import jwt
import bcrypt
from .settings import COOKIE_ENCRYPTION_SECRET
# Create ID
def create_id(prefix: str , length: int = 10):
    """
    Create a unique ID
    :param prefix: prefix for the ID
    :param length: length of the ID
    :return: unique ID
    """
    effective_length = length - len(prefix)
    return prefix + str(uuid.uuid4()).replace('-', '')[-1*effective_length : ]


# Hash Password
def hash_password(password: str):
    """
    Hash a password for storing.
    :param password: The password to hash.
    :return: A string of length 60, containing the algorithm used and the hashed password.
    """
    return str(bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))[2:-1]

def check_password(password1: str, password2: str):
    """
    Check a hashed password. Uses bcrypt, the salt is saved into the hash itself
    :param password1: The password to check.
    :param password2: The hash to check the password against.
    :return: True if the password matched, False otherwise.
    """
    result =  bcrypt.checkpw(password1.encode('utf-8'), password2.encode('utf-8'))
    print(result)
    return result
