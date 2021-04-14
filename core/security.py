from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(plain_password: str, hashed_password: str):
    """ Verify password """

    return pwd_context.verify(secret=plain_password, hash=hashed_password)


def get_password_hash(password: str):
    """ Get hash password """

    return pwd_context.hash(secret=password)
