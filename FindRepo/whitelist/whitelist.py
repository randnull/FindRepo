def get_whitelist():
    with open('FindRepo/whitelist/code_whitelist.txt', 'r') as f:
        whitelist = [code_type for code_type in f.read().split('\n')]
        
        return whitelist
