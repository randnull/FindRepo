import hashlib


class Hash:
    def __init__(self):
        pass


    def hash_object(self, object: str):
        encoded_object = object.encode()

        hash_object = hashlib.md5(encoded_object)

        hex_hash = hash_object.hexdigest()

        return hex_hash
