import sys

if sys.version_info[:2] >= (3, 8):
    import importlib.metadata as metadata
else:
    import importlib_metadata as metadata

mypy_metadata = metadata.metadata('mypy')
print(mypy_metadata['version'])
