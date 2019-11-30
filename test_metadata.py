try:
    from importlib.metadata import metadata  # type: ignore  # https://github.com/python/mypy/issues/1393
except ImportError:
    from importlib_metadata import metadata  # type: ignore  # https://github.com/python/mypy/issues/1153

meta = metadata('mypy')
print(meta['version'])
