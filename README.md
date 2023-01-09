# unaccompanied_minor_research

## Python settup...

1. Create a conda environment and activate it

**(base)**
```bash
conda create -n eco_portfolio python=3.7 anaconda -y
conda activate eco_portfolio

```
2. Install the required packages (make sure `eco_portfolio` is activated first)

**(eco_portfolio)**
```bash
python -m ipykernel install --user --name eco_portfolio
conda install -c conda-forge nodejs -y
pip install python-dotenv
conda install -c pyviz hvplot -y

```
3. Clone this repository, then clone and run the Jupyter notebook.

**(eco_portfolio)**
```bash
git clone git@github.com:harryo1968/ecocrypto_portfolio_analysis.git
cd eco_portfolio/
jupyter lab

```
