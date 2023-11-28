<h1 align="center"><!-- markdownlint-disable-line MD033 -->
<img src="imgs/logo.png" height="250" alt="VaxCollapse"><!-- markdownlint-disable-line MD033 -->
</h1>

A framework for specific design of mRNA vaccine targets.

## Installation

VaxCollapse have been tested only on **Python 3.9**, however it may work on newer versions as well.

Please follow these steps to install:

Install dependencies. It is recommended to create a [Python virtual environment](https://docs.python.org/3/tutorial/venv.html) or use the [conda](https://conda.io/projects/conda/en/latest/user-guide/index.html) manager to prevent conflicts with your system's Python environment.

```bash
pip install -r requirements.txt
```

## Running VaxCollapse

### Preparing sequence data

### Obtaining immunological features

VaxCollapse currently supports protein features inferred by the following software:

1. [BepiPred](https://services.healthtech.dtu.dk/services/BepiPred-3.0)
1. [NetMHCpan](https://services.healthtech.dtu.dk/services/NetMHCpan-4.1)
1. [NetMHCIIpan](https://services.healthtech.dtu.dk/services/NetMHCIIpan-4.0)

#### NetMHCpan

Prediction of pan-specific binding of peptides to MHC class I alleles.

```bash
./netMHCpan -f <PROTEINS.FASTA> -l <PEPTIDE_LENGTH> -xls -xlsfile <OUTPUT_TABLE.TSV> -a <ALLELE_NAME>
```

The output file can be a part of NetMHCpan-included analysis as one of its inputs. The table within should have the following structure:

|         |             |        | HLA-A01:01 |           |              |             |         |        |
| ------- | ----------- | ------ | ---------- | --------- | ------------ | ----------- | ------- | ------ |
| **Pos** | **Peptide** | **ID** | **core**   | **icore** | **EL-score** | **EL_Rank** | **Ave** | **NB** |
| 0       | MFVFLVLLP   | s_1    | MFVFLVLLP  | MFVFLVLLP | 0.0001       | 68.3333     | 0.0001  | 0      |
| 1       | FVFLVLLPL   | s_1    | FVFLVLLPL  | FVFLVLLPL | 0.0002       | 43.9091     | 0.0002  | 0      |
| 2       | VFLVLLPLV   | s_1    | VFLVLLPLV  | VFLVLLPLV | 0.0002       | 46.25       | 0.0002  | 0      |
| ...     | ...         | ...    | ...        | ...       | ...          | ...         | ...     | ...    |

#### NetMHCIIpan

Prediction of pan-specific binding of peptides to MHC class II alleles.

```bash
./netMHCIIpan -f <PROTEINS.FASTA> -length <PEPTIDE_LENGTH> -inptype 0 -xls -xlsfile <OUTPUT_TABLE.TSV> -a <ALLELE_NAME>
```

The output file can be a part of NetMHCIIpan-included analysis as one of its inputs. The table within should have the following structure:

|         |                 |        |            | DRB1_0301 |              |           |           |          |        |
| ------- | --------------- | ------ | ---------- | --------- | ------------ | --------- | --------- | -------- | ------ |
| **Pos** | **Peptide**     | **ID** | **Target** | **Core**  | **Inverted** | **Score** | **Rank**  | **Ave**  | **NB** |
| 1       | MFVFLVLLPLVSSQC | s_1    | NA         | LVLLPLVSS | 0            | 0.000041  | 90.740738 | 0.000041 | 0      |
| 2       | FVFLVLLPLVSSQCV | s_1    | NA         | LVLLPLVSS | 0            | 0.000059  | 88.25     | 0.000059 | 0      |
| 3       | VFLVLLPLVSSQCVN | s_1    | NA         | LLPLVSSQC | 0            | 0.00008   | 85.625    | 0.00008  | 0      |
| ...     | ...             | ...    | ...        | ...       | ...          | ...       | ...       | ...      | ...    |

#### BepiPred

Prediction of potential B-cell epitopes.

```bash
python bepipred3_CLI.py -i <PROTEINS.FASTA> -o <OUTPUT_DIR> -pred vt_pred -plot_linear_epitope_scores
```

The input file for BepiPred-included analysis should be `raw_output.csv` residing in the output directory given as an argument to the application. The table within should have the following structure:

| Accession | Residue | BepiPred-3.0 score | BepiPred-3.0 linear epitope score |
| --------- | ------- | ------------------ | --------------------------------- |
| s_1       | M       | 0.0239487458020449 | 0.0113448531677326                |
| s_1       | F       | 0.023962065577507  | 0.0128710796642635                |
| s_1       | V       | 0.0242273863404989 | 0.0140518152879344                |
| ...       | ...     | ...                | ...                               |

## Citing this work

If you use VaxCollapse in a scientific publication, please cite:

```bibtex
@Article{VaxCollapseX,
  author  = {Palkowski, Aleksander},
  journal = {X},
  title   = {{VaxCollapse}: A framework for specific design of {mRNA} vaccine targets},
  year    = {X},
  volume  = {X},
  number  = {X},
  pages   = {X--X},
  doi     = {X}
}
```

## Acknowledgements

VaxCollapse uses and/or references the following external libraries, packages, and other software:

- [BepiPred](https://services.healthtech.dtu.dk/services/BepiPred-3.0)
- [Biopython](https://biopython.org)
- [Matplotlib](https://matplotlib.org)
- [NetMHCpan](https://services.healthtech.dtu.dk/services/NetMHCpan-4.1)
- [NetMHCIIpan](https://services.healthtech.dtu.dk/services/NetMHCIIpan-4.0)
- [NumPy](https://numpy.org)
- [pandas](https://pandas.pydata.org)
- [tqdm](https://github.com/tqdm/tqdm)

We wish to thank all their contributors and maintainers!

## License and Disclaimer

Copyright 2023 Aleksander Pałkowski.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at <http://www.apache.org/licenses/LICENSE-2.0>.

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

### Third-party software

The software, libraries, or code from third parties mentioned in the [Acknowledgements](#acknowledgements) section above may come with their own terms and conditions or licensing requirements. When using this third-party software, libraries, or code, it's essential to adhere to these terms. Ensure you understand and can follow any relevant restrictions or terms and conditions prior to using them.
