class Cache(object):
    """Class to provide cache Dictionary, loaded and saved bytes."""

    """Constructor to initialize Cache with empty saved and loaded bytes. So as the cache dictionary"""
    def __init__(self):
        self._loaded_bytes = 0
        self._saved_bytes = 0
        self._cache = {}

    """Method that saves the req into the cache and calculates cache size and amount of bytes saved.
    :param req_val: A string that represents the requisition value."""
    def req(self, req_val: str) -> None:
        req_val = req_val.split()
        key = req_val[1]
        values = [req_val[0], req_val[2]]
        self.validate_and_sum(key, int(values[1]))
        self._cache.update({key : values})

    """Method used to verify if the req size will increase saved or loaded bytes into class attributes.
    :param key: The string to be fetched from the cache.
    :param size: The amount of bytes to increment one of the possible attributes."""
    def validate_and_sum(self, key: str, size: int) -> None:
        if (key in self._cache):
            self._saved_bytes += size
        else:
            self._loaded_bytes += size