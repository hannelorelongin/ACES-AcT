# ACES-AcT

This repository contains all code related to the preprint (insert title here) describing the systematic identification of phage-encoded acetyltransferases in *Pseudomonas* phages, including the complete elucidation of one of the identified phage-encoded acetyltransferases. 

This code was actively developed on GitLab, and the GitHub track record only corresponds to the code preparation for manuscript submission. 

# Table of contents

1.  [Outline of the repository](#outline-of-the-repository)
2.  [Data availability](#data-availability)
3.  [System requirements & dependencies](#system-requirements-&-dependencies)
4.  [Contact](#contact)
5.  [References](#references)
6.  [License](#license)

## Outline of the repository

* `associated_data/`
    * `virushostdb_host_pseudomonas_25feb2024.tsv` : results of search for 'Pseudomonas' as host in the Virus-Host database (version: February 25th, 2024)
* `pipeline/`
    * `1_search/` : describes the code related to the search for phage_encoded acetyltransferases
        * `Code_search_input.ipynb` & `a_input/`: describes the process of retrieving input data related to the search for phage_encoded acetyltransferases
            * `protein_overview/`
                * `protein_overview.tsv` : a tab-seperated aggregated overview of the NCBI proteins for all phages
                * `annotated_acetyltransferases_overview.tsv` :  tab-seperated overview of the NCBI and UniProt proteins of our phages that contain 'GNAT' and/or 'acetyltransferase' in their protein name
                * `input_search.tsv` : a tab-seperated aggregated overview of the NCBI proteins that are unannotated and within the expected size range of acetyltransferases for all phages   
            * `phage_data.tsv` :  a tab-seperated phage-centric overview of the virus & host taxonomic information from the Virus-Host database   

## Data availability

The data related to this work can be found at:

* ColabFold structure predictions (to be added - ModelArchive)
* FoldSeek output (to be added - Zenodo)
* proteomics (to be added - ProteomeXchange)
* metabolomics (to be added - MetaboLights?)

## System requirements & dependencies

The notebooks were run on either a Windows or Linux-64 bit (as detailed in each notebook). In addition, HPC resources and services used in this work were provided by the VSC (Flemish Supercomputer Center), funded by the Research Foundation - Flanders (FWO) and the Flemish Government.

All installed dependencies are listed at the start of each individual notebooks. 

## Contact

Computational Systems Biology, KU Leuven.

## References

Please cite our preprint:

(to be added)

In addition, this work relies on third-party software & databases:

(to be added)

## License

This code is freely available under an MIT license. (to add once author list final)

Use of the third-party software, libraries or code referred to in the References section above may be governed by separate terms and conditions or license provisions. Your use of the third-party software, libraries or code is subject to any such terms and you should check that you can comply with any applicable restrictions or terms and conditions before use.
