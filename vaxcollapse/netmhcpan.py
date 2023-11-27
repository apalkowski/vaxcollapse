"""
VaxCollapse: A framework for specific design of mRNA vaccine targets.

Handling operations connected to NetMHCpan results.

Default Rank threshold for high binding peptides: 0.5
Default Rank Threshold for low binding peptides: 2.0

Copyright 2023 Aleksander Pałkowski.
"""

import pandas as pd


def read_netmhcpan_results(results_file: str) -> tuple[pd.DataFrame, str]:
    """Read NetMHCpan results file and return it as DataFrame and allele annotation."""
    with open(results_file, "r") as handle:
        allele = handle.readline().strip()

    results = pd.read_csv(results_file, sep="\t", skiprows=1)

    return results, allele
