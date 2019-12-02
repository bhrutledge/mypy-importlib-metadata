try:
    from importlib.metadata import metadata  # type: ignore  # https://github.com/python/mypy/issues/1393
except ImportError:
    from importlib_metadata import metadata  # type: ignore  # https://github.com/python/mypy/issues/1153

mypy_metadata = metadata('mypy')
print(mypy_metadata['version'])
