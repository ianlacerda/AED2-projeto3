class Cache(object):
    """Class to provide cache Dictionary, loaded and saved bytes."""

    def __init__(self):
        self._loaded_bytes = 0
        self._saved_bytes = 0
        self._cache = {}

    def req(self, req_val: str) -> None:
        req_val = req_val.split()
        key = req_val[1]
        values = [req_val[0], req_val[2]]
        self.validate_and_sum(key, int(values[1]))
        self._cache.update({key : values})

    def validate_and_sum(self, key: str, size: int) -> None:
        if (key in self._cache):
            self._saved_bytes += size
        else:
            self._loaded_bytes += size