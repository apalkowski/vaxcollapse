<h1 align="center"><!-- markdownlint-disable-line MD033 -->
<img src="imgs/logo.png" height="250" alt="VaxCollapse"><!-- markdownlint-disable-line MD033 -->
</h1>

A framework for specific design of mRNA vaccine targets.

## Installation

**VaxCollapse requires a working [Python](https://www.python.org) installation**. You can either install the [official distribution](https://www.python.org/downloads), install the [conda](https://docs.conda.io/projects/miniconda/en/latest/) manager (recommended), or use existing system installation (most recent Linux distributions should have a sufficient programming environment).

VaxCollapse have been tested only on **Python 3.9**, however it may work on different versions as well.

Please follow these steps to set up the pipeline:

1. Obtain the latest version of the package by either:

   - Cloning this repository and `cd`-ing into it.

        ```bash
        git clone https://github.com/apalkowski/vaxcollapse.git
        cd ./vaxcollapse
        ```

    or

   - [Downloading](https://github.com/apalkowski/vaxcollapse/archive/refs/heads/main.zip) contents of this repository, unzipping it, and `cd`-ing into it.

        ```bash
        wget https://github.com/apalkowski/vaxcollapse/archive/refs/heads/main.zip
        unzip vaxcollapse-main.zip
        cd ./vaxcollapse-main
        ```

1. Install dependencies. It is recommended to create a [Python virtual environment](https://docs.python.org/3/tutorial/venv.html) or use the [conda manager](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands) to prevent conflicts with your system's Python environment.

    ```bash
    pip install -r requirements.txt
    ```

1. Download and install at least one of the inference software listed in the [Obtaining Immunological Features](#obtaining-immunological-features) section.

## Running VaxCollapse

At a minimum, VaxCollapse requires three files as input:

1. FASTA file with protein sequences.
1. FASTA file with coding region sequences (CDS) of the above proteins.
1. Text table file describing a specific immunological feature of the above proteins, produced by one of the [supported models](#obtaining-immunological-features).

The third option can be extended to several such files, each describing another immunological feature, be it related to a different kind of immune mechanism (e.g., MHC class I antigen presentation or B-cell epitope detection) or to genetic variance (e.g., associated with alternative MHC alleles).

### Preparing Sequence Data

Because of current limitations, VaxCollapse requires specifically tailored sequence files as input. Make sure that those meet the following conditions:

1. Sequences represent the same type of a protein.
1. Sequences are of the same length (within one file).
1. Related protein and CDS sequences must have the same FASTA header.
1. CDS and protein sequences need to represent 1:1 nucleotides translation to amino acids.

Hence, you should prepare a same-length protein sequences FASTA file, e.g.:

```fasta
>sequence_1
MFVFLVLLP
>sequence_2
LKGVKLHYT
>sequence_3
FDEDDSEPV
```

and a corresponding CDS FASTA file:

```fasta
>sequence_1
ATGTTTGTTTTTCTTGTTTTATTGCCA
>sequence_2
CTCAAAGGAGTCAAATTACATTACACA
>sequence_3
TTTGATGAAGACGACTCTGAGCCAGTG
```

***Important note:*** you should make sure that sequence IDs (FASTA headers) are as short as possible and contain no spaces, because some inference software may shorten them in its results files, which will turn VaxCollapse reporting impossible.

### Obtaining Immunological Features

VaxCollapse currently supports protein features inferred by the following models:

1. [BepiPred](#bepipred)
2. [NetMHCpan](#netmhcpan)
3. [NetMHCIIpan](#netmhciipan)

It is important to use the same proteins FASTA file (with the same sequence headers) as input to supported models within one analysis pipeline.

#### BepiPred

Prediction of potential B-cell epitopes from protein sequence.

To read detailed description of the tool, its terms of use, and access online or standalone versions, please refer to the [BepiPred server website](https://services.healthtech.dtu.dk/services/BepiPred-3.0).

For VaxCollapse use the standalone version, as the online server may produce different results format. VaxCollapse currently supports only linear epitope prediction.

An example command to produce inference results should look like the following:

```bash
python bepipred3_CLI.py -i <PROTEINS.FASTA> -o <OUTPUT_DIR> -pred vt_pred -plot_linear_epitope_scores
```

The input file for BepiPred-included analysis should be `raw_output.csv` residing in the output directory `<OUTPUT_DIR>` given as an argument. The table within should have the following structure:

| Accession  | Residue | BepiPred-3.0 score | BepiPred-3.0 linear epitope score |
| ---------- | ------- | ------------------ | --------------------------------- |
| sequence_1 | M       | 0.0239487458020449 | 0.0113448531677326                |
| sequence_1 | F       | 0.023962065577507  | 0.0128710796642635                |
| sequence_1 | V       | 0.0242273863404989 | 0.0140518152879344                |
| ...        | ...     | ...                | ...                               |

#### NetMHCpan

Prediction of pan-specific binding of peptides to MHC class I alleles.

To read detailed description of the tool, its terms of use, and access online or standalone versions, please refer to the [NetMHCpan server website](https://services.healthtech.dtu.dk/services/NetMHCpan-4.1).

For VaxCollapse use the standalone version, as the online server may produce different results format. Produce one results file per one allele and one peptide length. VaxCollapse supports only whole-protein-based input.

An example command to produce inference results should look like the following:

```bash
./netMHCpan -f <PROTEINS.FASTA> -l <PEPTIDE_LENGTH> -xls -xlsfile <OUTPUT_TABLE.TSV> -a <ALLELE_NAME>
```

The output file `<OUTPUT_TABLE.TSV>` can be a part of NetMHCpan-included analysis as one of its inputs. The table within should have the following structure:

|         |             |            | HLA-A01:01 |           |              |             |         |        |
| ------- | ----------- | ---------- | ---------- | --------- | ------------ | ----------- | ------- | ------ |
| **Pos** | **Peptide** | **ID**     | **core**   | **icore** | **EL-score** | **EL_Rank** | **Ave** | **NB** |
| 0       | MFVFLVLLP   | sequence_1 | MFVFLVLLP  | MFVFLVLLP | 0.0001       | 68.3333     | 0.0001  | 0      |
| 1       | FVFLVLLPL   | sequence_1 | FVFLVLLPL  | FVFLVLLPL | 0.0002       | 43.9091     | 0.0002  | 0      |
| 2       | VFLVLLPLV   | sequence_1 | VFLVLLPLV  | VFLVLLPLV | 0.0002       | 46.25       | 0.0002  | 0      |
| ...     | ...         | ...        | ...        | ...       | ...          | ...         | ...     | ...    |

You may produce and use multiple results files per one proteins set, each for a different supported MHC class I allele.

#### NetMHCIIpan

Prediction of pan-specific binding of peptides to MHC class II alleles.

To read detailed description of the tool, its terms of use, and access online or standalone versions, please refer to the [NetMHCIIpan server website](https://services.healthtech.dtu.dk/services/NetMHCIIpan-4.0).

For VaxCollapse use the standalone version, as the online server may produce different results format. Produce one results file per one allele and one peptide length. VaxCollapse supports only whole-protein-based input.

An example command to produce inference results should look like the following:

```bash
./netMHCIIpan -f <PROTEINS.FASTA> -length <PEPTIDE_LENGTH> -inptype 0 -xls -xlsfile <OUTPUT_TABLE.TSV> -a <ALLELE_NAME>
```

The output file `<OUTPUT_TABLE.TSV>` can be a part of NetMHCIIpan-included analysis as one of its inputs. The table within should have the following structure:

|         |                 |            |            | DRB1_0301 |              |           |           |          |        |
| ------- | --------------- | ---------- | ---------- | --------- | ------------ | --------- | --------- | -------- | ------ |
| **Pos** | **Peptide**     | **ID**     | **Target** | **Core**  | **Inverted** | **Score** | **Rank**  | **Ave**  | **NB** |
| 1       | MFVFLVLLPLVSSQC | sequence_1 | NA         | LVLLPLVSS | 0            | 0.000041  | 90.740738 | 0.000041 | 0      |
| 2       | FVFLVLLPLVSSQCV | sequence_1 | NA         | LVLLPLVSS | 0            | 0.000059  | 88.25     | 0.000059 | 0      |
| 3       | VFLVLLPLVSSQCVN | sequence_1 | NA         | LLPLVSSQC | 0            | 0.00008   | 85.625    | 0.00008  | 0      |
| ...     | ...             | ...        | ...        | ...       | ...          | ...       | ...       | ...      | ...    |

You may produce and use multiple results files per one proteins set, each for a different supported MHC class II allele.

### Generating Vaccine Targets

## To Do

- [ ] Add support for more immunological models.
- [ ] Change the core model to a network-based.

## Citing This Work

If you use VaxCollapse in a scientific publication, please cite:

```bibtex
@Article{VaxCollapseX,
  author  = {Palkowski, Aleksander},
  title   = {{VaxCollapse: A framework for specific design of mRNA vaccine targets}},
  journal = {X},
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

### Third-Party Software

The software, libraries, or code from third parties mentioned in the [Acknowledgements](#acknowledgements) section above may come with their own terms and conditions or licensing requirements. When using this third-party software, libraries, or code, it's essential to adhere to these terms. Ensure you understand and can follow any relevant restrictions or terms and conditions prior to using them.
