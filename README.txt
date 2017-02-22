requirements.txt file may be used to create an environment using:
$ conda create --name <env> --file requirements.txt

To execute run
$ python frontend

To test run
$ pytest
For quick pytest tutorial check out https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

To check test coverage run
$ py.test --cov=. tests/
For more refer to http://pytest-cov.readthedocs.io/en/latest/readme.html
