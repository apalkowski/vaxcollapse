"""
VaxCollapse: A framework for specific design of mRNA vaccine targets.

Handling operations connected to BepiPred results.

Default threshold to use, when making predictions
on average ensemble positive probability outputs: 0.1512
(greater than)

Copyright 2023 Aleksander Pałkowski.
"""

import pandas as pd


def read_bepipred_results(results_file: str) -> pd.DataFrame:
    """Read BepiPred results file and return it as DataFrame."""
    results = pd.read_csv(results_file)

    return results
