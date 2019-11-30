# mypy errors with importlib.metadata

The release of mypy 0.750 is causing errors when attempting to use `importlib.metadata` (from Python 3.8) or `importlib_metadata` (its predecessor). The errors depend on the version of Python, and were not present in mypy 0.740. For example:

```
test_metadata.py:4: error: Name 'importlib_metadata' already defined (by an import)
test_metadata.py:6: error: Module has no attribute "metadata"
```

This initial commit of this repository reproduces the errors. Subsequent commits demonstrate possible resolutions.

Related mypy issues:

- <https://github.com/python/mypy/issues/1153>
- <https://github.com/python/mypy/issues/1393>

Output from initial commit:

```
$ tox
py37-mypy0740 installed: importlib-metadata==0.23,more-itertools==8.0.0,mypy==0.740,mypy-extensions==0.4.3,typed-ast==1.4.0,typing-extensions==3.7.4.1,zipp==0.6.0
py37-mypy0740 run-test-pre: PYTHONHASHSEED='2890670225'
py37-mypy0740 run-test: commands[0] | mypy test_metadata.py
Success: no issues found in 1 source file
py37-mypy0740 run-test: commands[1] | python test_metadata.py
0.740
py37-mypy0750 installed: importlib-metadata==0.23,more-itertools==8.0.0,mypy==0.750,mypy-extensions==0.4.3,typed-ast==1.4.0,typing-extensions==3.7.4.1,zipp==0.6.0
py37-mypy0750 run-test-pre: PYTHONHASHSEED='2890670225'
py37-mypy0750 run-test: commands[0] | mypy test_metadata.py
test_metadata.py:4: error: Name 'importlib_metadata' already defined (by an import)
test_metadata.py:6: error: Module has no attribute "metadata"
Found 2 errors in 1 file (checked 1 source file)
ERROR: InvocationError for command /Users/brian/Code/mypy-importlib-metadata/.tox/py37-mypy0750/bin/mypy test_metadata.py (exited with code 1)
py38-mypy0740 installed: mypy==0.740,mypy-extensions==0.4.3,typed-ast==1.4.0,typing-extensions==3.7.4.1
py38-mypy0740 run-test-pre: PYTHONHASHSEED='2890670225'
py38-mypy0740 run-test: commands[0] | mypy test_metadata.py
Success: no issues found in 1 source file
py38-mypy0740 run-test: commands[1] | python test_metadata.py
0.740
py38-mypy0750 installed: mypy==0.750,mypy-extensions==0.4.3,typed-ast==1.4.0,typing-extensions==3.7.4.1
py38-mypy0750 run-test-pre: PYTHONHASHSEED='2890670225'
py38-mypy0750 run-test: commands[0] | mypy test_metadata.py
test_metadata.py:4: error: Name 'importlib_metadata' already defined (by an import)
Found 1 error in 1 file (checked 1 source file)
ERROR: InvocationError for command /Users/brian/Code/mypy-importlib-metadata/.tox/py38-mypy0750/bin/mypy test_metadata.py (exited with code 1)
___________________________________ summary ____________________________________
  py37-mypy0740: commands succeeded
ERROR:   py37-mypy0750: commands failed
  py38-mypy0740: commands succeeded
ERROR:   py38-mypy0750: commands failed
```
