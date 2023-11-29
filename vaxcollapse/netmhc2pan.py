"""
VaxCollapse: A framework for specific design of mRNA vaccine targets.

Handling operations connected to NetMHCIIpan results.

Default threshold for strong binders (%Rank): 1.0
Default threshold for weak binders (%Rank): 5.0
(lesser than)

Copyright 2023 Aleksander Pałkowski.
"""

import pandas as pd


def read_netmhc2pan_results(results_file: str) -> tuple[pd.DataFrame, str]:
    """Read NetMHCIIpan results file and return it as DataFrame and allele annotation."""
    with open(results_file, "r") as handle:
        allele = handle.readline().strip()

    results = pd.read_csv(results_file, sep="\t", skiprows=1)

    return results, allele
