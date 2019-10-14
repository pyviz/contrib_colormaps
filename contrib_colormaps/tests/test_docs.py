import os
import pytest


TOP = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
CSV_PATH = os.path.join(TOP, 'contrib_colormaps', 'colormaps')
DOC_PATH = os.path.join(TOP, 'doc')
NOTEBOOKS_PATH = os.path.join(TOP, 'examples', 'colormaps')


@pytest.mark.parametrize('filename', sorted(os.listdir(CSV_PATH)))
def test_notebook_for_every_csv(filename):
    name, ext = os.path.splitext(filename)
    assert '{name}.ipynb'.format(name=name) in os.listdir(NOTEBOOKS_PATH), \
           'Every colormap must have a corresponding notebook in ' + NOTEBOOKS_PATH
