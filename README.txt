requirements.txt file may be used to create an environment using:
$ conda create --name <env> --file requirements.txt

To execute run
$ python frontend

To test run
$ pytest

To check test coverage run
$ py.test --cov=. tests/
