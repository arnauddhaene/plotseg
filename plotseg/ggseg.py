"""
ggseg.py
========
gg object, child of plotnine.ggplot
"""
from plotnine import (ggplot, geom_polygon, aes, coord_fixed)
from patsy.eval import EvalEnvironment

from .atlas import (dk, aseg, glasser, yeo17, yeo7, hoCort, jhu, tracula)


class ggseg(ggplot):

    def __init__(self, atlas='dk', environment=None):
        """
        Create a new ggseg object.

        Parameters
        ----------
        atlas : str
            Atlas used for plotting. Must be in:
            {'dk', 'aseg', 'glasser', 'yeo17', 'yeo7', 'hoCort', 'jhu', 'tracula'}
        environment : dict, ~patsy.Eval.EvalEnvironment
            If a variable defined in the aesthetic mapping is not
            found in the data, ggplot will look for it in this
            namespace. It defaults to using the environment/namespace.
            in which `ggseg()` is called.
        """

        assert isinstance(atlas, str)

        if atlas == 'dk':
            data = dk
        elif atlas == 'aseg':
            data = aseg
        elif atlas == 'glasser':
            data = glasser
        elif atlas == 'yeo17':
            data = yeo17
        elif atlas == 'yeo7':
            data = yeo7
        elif atlas == 'hoCort':
            data = hoCort
        elif atlas == 'jhu':
            data = jhu
        elif atlas == 'tracula':
            data = tracula
        else:
            raise ValueError('{} atlas is not yet supported.'.format(atlas))

        self.data = data

        mapping = aes(x='.long', y='.lat', group='.id', subgroup='.subid')

        super().__init__(mapping, data, environment)

    def _draw(self, return_ggplot=True):
        """
        Draw function

        Parameters
        ----------
        return_ggplot : boolean
            If ``True``, return ggplot object.
        """

        self = super()._draw(return_ggplot=True) + \
            geom_polygon(
                mapping=aes(fill='region'), data=self.data, show_legend=False
            ) + \
            coord_fixed()

        if return_ggplot:
            output = self.figure, self
        else:
            output = self.figure

        return output
