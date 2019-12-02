import sys

if sys.version_info[:2] >= (3, 8):
    from importlib.metadata import metadata
else:
    from importlib_metadata import metadata

mypy_metadata = metadata('mypy')
print(mypy_metadata['version'])
