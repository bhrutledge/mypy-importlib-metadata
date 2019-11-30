try:
    import importlib.metadata as importlib_metadata
except ImportError:
    import importlib_metadata

metadata = importlib_metadata.metadata('mypy')
print(metadata['version'])
