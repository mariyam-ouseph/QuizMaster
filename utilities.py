import time
from hashlib import md5


def create_db_id():
    user_id_hash = md5()
    user_id_hash.update(str(time.time()).encode())
    key = user_id_hash.hexdigest()
    return key

