import hashlib


class Hash:
    def __init__(self, hash_func: str = 'md5'):
        if hash_func == 'md5':
            self.hash_func = hashlib.md5


    def hash_object(self, object: str):
        encoded_object = object.encode()

        hash_object = self.hash_func(encoded_object)

        hex_hash = hash_object.hexdigest()

        return hex_hash
