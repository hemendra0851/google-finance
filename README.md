google-finance-pytest-project
=
A simple `pytest-selenium` project to test features of *Google Finance* Page (https://www.google.com/finance/)

<br>

Description
=
This project follows the Page Object Model to test below features of the Website:

1. Validation on <b>Market Indices</b> on the Home Page for various Markets (US, Europe, etc.)
2. <b>Search stocks</b> and other assets from the search field on the Home Page
3. <b>Follow any stock</b> as guest and validate that the user is taken to the Google Sign in page
4. <b>Add any event to calendar</b> as guest and validate that the user is taken to the Google Sign in page
5. <b>Add a new Portfolio</b> as guest and validate that the user is taken to the Google Sign in page
6. Validation of <b>Main Menu items</b>

<br>

Test Approach
=
* Tests are configured to run on `headless chrome` but can also be parametrize to run on `edge` and other browsers by extending the request params in the `create_driver` fixture
* Tests have to optimised to run in both `headless` and `normal` mode. A specific case of `adding an event to calendar` was opening different links depending on the `headless` mode and `browser` type
* Fixture and Test Parametrization has been used for better pytest coverage

<br>

Folder Structure
=
* `data` folder - locators, content and env variable files
* `pages` folder - classes for various pages with different functions
* `test` folder - test classes
* `conftest.py` - fixture class to create WebDriver
* `pytest.ini` - pytest configs
* `execute.sh` - wrapper to run the smoke-suite sub-set of tests

<br>

Python Packages used
=
```
pytest
pytest-selenium
pylint
```

<br>

Disabled warnings for pylint
=

* missing-module-docstring
* missing-class-docstring
* missing-function-docstring
* useless-parent-delegation (suppress Base class constructor initialization from Page Classes)
* no-member (suppress `Instance of 'PageTest' has no 'driver' member` warning for tests calling `self.driver` from the fixture)
