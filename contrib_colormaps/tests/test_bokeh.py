import pytest  # noqa
import contrib_colormaps as cc


@pytest.mark.parametrize('k,v', list(cc.palette.items()))
def test_bokeh_palette_is_available_at_top_level(k, v):
    cmap = getattr(cc, 'b_{k}'.format(k=k))
    assert isinstance(cmap, list)
    assert cmap == v
    assert v[0].startswith('#')
    assert len(v[0]) == 7
