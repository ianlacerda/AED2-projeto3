from AED2_projeto3.cache.cache import Cache
from AED2_projeto3 import const
import sys
"""This module was developed to centralize the operations required to run the proposed simulation."""

"""Fetch data and runs the simulation using the Cache class."""
def run_simulation():
    """Start a new Cache"""
    cache = Cache()
    print(f"Tamanho inicial do dicionário que representa o Cache (bytes): {sys.getsizeof(cache._cache)}")

    """Read requisitions from data folder"""
    data = open(f'{const.HERE}/data/wikipedia.txt', 'r')
    data = data.readlines()

    """Insert requisitions into cache"""
    for line in data:
        cache.req(req_val=line.strip())

    """print loaded bytes"""
    print(f"Quantidade de bytes em Cache: {cache._loaded_bytes}")

    """print saved bytes"""
    print(f"Quantidade de bytes economizados com o uso do Cache: {cache._saved_bytes}")

    """print saved bytes"""
    print(f"Tamanho final do dicionário que representa o Cache (bytes): {sys.getsizeof(cache._cache)}")