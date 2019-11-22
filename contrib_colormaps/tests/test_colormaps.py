import os
import pytest

HERE = os.path.abspath(os.path.dirname(__file__))
TOP = os.path.abspath(os.path.dirname(os.path.dirname(HERE)))
CSV_PATH = os.path.join(TOP, 'contrib_colormaps', 'colormaps')
NOTEBOOKS_PATH = os.path.join(TOP, 'examples', 'colormaps')
BASELINE_PATH = os.path.join(HERE, 'baseline')


@pytest.mark.parametrize('filename', sorted(os.listdir(CSV_PATH)))
@pytest.mark.files
def test_notebook_for_every_csv(filename):
    name, ext = os.path.splitext(filename)
    assert '{name}.ipynb'.format(name=name) in os.listdir(NOTEBOOKS_PATH), \
           'Every colormap must have a corresponding notebook in ' + NOTEBOOKS_PATH


@pytest.mark.parametrize('filename', sorted(os.listdir(CSV_PATH)))
@pytest.mark.files
def test_baseline_image_exists_for_every_csv(filename):
    name, ext = os.path.splitext(filename)
    assert any(name in img for img in os.listdir(BASELINE_PATH)), \
           ('Every colormap must have its matplotlib test images checked in. '
            'From within tests dir run pytest --mpl-generate-path=baseline.')


@pytest.mark.parametrize('filename', sorted(os.listdir(CSV_PATH)))
@pytest.mark.files
def test_mpl_bokeh_and_regular_cmap_for_every_csv(filename):
    name, ext = os.path.splitext(filename)
    import contrib_colormaps as cc
    assert hasattr(cc, name)
    assert hasattr(cc, 'b_{name}'.format(name=name))
    assert hasattr(cc, 'm_{name}'.format(name=name))
    assert hasattr(cc.palette, name)
    assert hasattr(cc.cm, name)
