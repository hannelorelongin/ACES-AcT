# ACES-AcT

This repository contains all code related to the preprint (insert title here) describing the systematic identification of phage-encoded acetyltransferases in *Pseudomonas* phages, including the complete elucidation of one of the identified phage-encoded acetyltransferases. 

This code was actively developed on GitLab, and the GitHub track record only corresponds to the code preparation for manuscript submission. 

# Table of contents

1.  [Outline of the repository](#outline-of-the-repository)
2.  [Data availability](#data-availability)
3.  [System requirements & dependencies](#system-requirements--dependencies)
4.  [Contact](#contact)
5.  [References](#references)
6.  [Acknowledgements](#acknowledgements)
7.  [License](#license)

## Outline of the repository

This section briefly describes the outline of the repository. For a more detailed overview (including all generated files), the 'Generates' section of individual code notebooks can be consulted.

* `pipeline/`
    * `1_search/` : describes the code related to the search for phage-encoded acetyltransferases
        * `Code_search_input.ipynb` & `a_input/`: describes the process of retrieving input data related to the search for phage-encoded acetyltransferases
        * `Code_search_assess_annotated.ipynb` & `b_assess_annotated/`: describes the process of assessing the likelihood of the annotated acetyltransferases to be functional acetyltransferases, based on their predicted protein structures
        * `Code_search_assess_unknown.ipynb` & `c_assess_unknown/`: describes the process of assessing the likelihood of the phage proteins of unknown function to be functional acetyltransferases, based on their predicted protein structures
    * `2_characterization/` : describes the code related to the characterization of the predicted phage-encoded acetyltransferases  
* `associated_data/`
    * `virushostdb_host_pseudomonas_25feb2024.tsv` : results of search for 'Pseudomonas' as host in the Virus-Host database (version: February 25th, 2024)
    * `list_obsolete_PDB_ids_15jul2024.txt`, `dict_pdb_PDBidch_UniProtID_jul2024.csv`, `dict_pdb_UniProtID_NCBIuid_jul2024.csv` : information obtained from the PDB (July, 2024) detailing obsolete PDB identifiers, and cross-references between PDB and UniProt
    * `dict_UniProtID_function_jul2024.csv` : information obtained from UniProt (release 2024_03) linking together UniProt identifiers and protein names
* `templates/`
    * `submit_vibfold.py`, `VIBFold.py`, `VIBFold_adapted_functions.py` and `submit.sh`: structure prediction template job files, adapted from [VIBFold](https://github.com/jasperzuallaert/VIBFold/tree/main)    
    * `data_foldseek_5.csv` and `script_foldseek_5.slurm`: structure comparison template job files

## Data availability

The data related to this work can be found at:

* ColabFold structure predictions (to be added - ModelArchive)
* proteomics (to be added - ProteomeXchange)
* metabolomics (to be added - MetaboLights?)
* full in- and output of this repo (to be added - Zenodo)

## System requirements & dependencies

The notebooks were run on either a Windows or Linux-64 bit (as detailed in each notebook). In addition, HPC resources and services used in this work were provided by the VSC (Flemish Supercomputer Center), funded by the Research Foundation - Flanders (FWO) and the Flemish Government.

All installed dependencies are listed at the start of each individual notebooks. 

## Contact

Computational Systems Biology, KU Leuven.

## References

Please cite our preprint:

(to be added)

## Acknowledgements

In our pipeline, we adapted scripts from:

* [VIBFold](https://github.com/jasperzuallaert/VIBFold/tree/main) by Zuallaert J., available under an [MIT License](https://github.com/jasperzuallaert/VIBFold/blob/main/LICENSE): scripts `VIBFold.py`, `submit_vibfold.py` & `VIBFold_adapted_functions.py` (located in `templates`).

## License

This code is freely available under an MIT license. (to add once author list final)

Use of the third-party software, libraries or code referred to in the Acknowledgements section above may be governed by separate terms and conditions or license provisions. Your use of the third-party software, libraries or code is subject to any such terms and you should check that you can comply with any applicable restrictions or terms and conditions before use.
