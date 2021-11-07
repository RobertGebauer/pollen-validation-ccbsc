# Introduction
CCBSC is an interface definition that supports you to create algorithms for pollen classification in order to run them on images of [PollenScience.eu Validation](https://validation.pollenscience.eu) database while making sure that results are stored well-structured in the database.

# Installation
    pip install ccbysc-0.0.1-py3-none-any.whl

#  Usage
Your algorithm must inherit **CCBSCAlgorithm** class and provide the classify- and identifier-methods.
```python
def classify(self, photo: Photo) -> List[Classification]: pass # your code
def identifier(self): pass # identifier of your algorithm
```
Such algorithms can be run on images of [PollenScience.eu Validation](https://validation.pollenscience.eu) database and the returned list of classifications will be available in same database for further analysis.

# Development
## Clone & Prepare
- Clone project
- Create virtual environment:
  ```console
  python3 -m .venv
  ```
- Jump to virtual environment and install dependencies:
  ```console
  .venv/Scripts/activate
  pip install -r requirements.txt
  ```
## Build
```console
python setup.py bdist_wheel
```
