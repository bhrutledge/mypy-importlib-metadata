try:
    import importlib.metadata as importlib_metadata
except ImportError:
    import importlib_metadata  # type: ignore  # https://github.com/python/mypy/issues/1153

metadata = importlib_metadata.metadata('mypy')
print(metadata['version'])
