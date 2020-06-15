"""
atlas.py
========
define the 2D atlas projections.
"""
from pandas import read_json
from pathlib import Path


_DATA_PATH = Path(__file__).parent.joinpath('data')


# Function to fetch atlas
def fetch_atlas(atlas: str):
    """
    Method to fetch atlas

    Parameters
    ----------
    atlas : str
        name of atlas

    Returns
    -------
    atlas : ~pandas.DataFrame
        pandas DataFrame object of atlas
    """

    return read_json(_DATA_PATH.joinpath(atlas + '.json').as_posix())


# List of atlases to fetch
atlases = ['dk', 'aseg', 'glasser', 'yeo17', 'yeo7', 'hoCort', 'jhu', 'tracula']

# Fetch atlasses : list of pandas.DataFrame
dk, aseg, glasser, yeo17, yeo7, hoCort, jhu, tracula = map(fetch_atlas, atlases)
