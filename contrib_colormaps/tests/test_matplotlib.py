import pytest
import contrib_colormaps as cc

pytest.importorskip('matplotlib')


@pytest.mark.parametrize('k,v', list(cc.cm.items()))
def test_get_cm(k, v):
    import matplotlib.cm as mcm
    assert mcm.get_cmap(k) is v


@pytest.mark.parametrize('k,v', list(cc.cm.items()))
@pytest.mark.mpl_image_compare
def test_matplotlib_all_cmaps(k, v):
    import numpy as np
    import matplotlib.pyplot as plt
    xs, _ = np.meshgrid(np.linspace(0, 1, 256), np.linspace(0, 1, 10))
    fig = plt.imshow(xs, cmap=v).get_figure()
    return fig


@pytest.mark.parametrize('k,v', list(cc.cm.items()))
@pytest.mark.mpl_image_compare
def test_matplotlib_plotting_backend(k, v):
    hv = pytest.importorskip('holoviews')
    hv.extension('matplotlib')
    from contrib_colormaps.plotting import swatch
    fig = hv.render(swatch(k), backend='matplotlib')
    return fig
