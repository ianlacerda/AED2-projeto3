from AED2_projeto3.cache.cache import Cache

def run_simulation():
    """Start a new Cache"""
    cache = Cache()

    """Read requisitions from data folder"""
    data = open(f'/home/griquup/ufabc/projeto3/AED2_projeto3/AED2_projeto3/data/wikipedia.txt', 'r')
    data = data.readlines()

    """Insert requisitions into cache"""
    for line in data:
        cache.req(req_val=line.strip())

    """print loaded bytes"""
    print(cache._loaded_bytes)

    """print saved bytes"""
    print(cache._saved_bytes)

    #print(cache._cache)