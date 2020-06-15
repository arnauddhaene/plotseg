"""
plotseg
-------
Plotting tool for brain atlases, in Python.

Brought to you by Arnaud Dhaene.
"""

from .ggseg import ggseg
from .atlas import (dk, aseg, glasser, yeo17, yeo7, hoCort, jhu, tracula)
 

__all__ = ['ggseg']