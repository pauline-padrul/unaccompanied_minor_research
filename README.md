# Unaccompanied Minor Research

## Python settup...

1. Create a conda environment and activate it

**(base)**
```bash
conda create -n umr python=3.9 anaconda -y
conda activate umr

```
2. Install the required packages (make sure `umr` is activated first)

**(umr)**
```bash
python -m ipykernel install --user --name umr
conda install -c conda-forge nodejs -y
pip install python-dotenv
conda install -c pyviz hvplot -y

```
3. Clone this repository, then clone and run the Jupyter notebook.

**(umr)**
```bash
git clone git@github.com:pauline-padrul/unaccompanied_minor_research.git
cd umr/
jupyter lab

```
