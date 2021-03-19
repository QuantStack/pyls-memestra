# pyls-memestra

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/QuantStack/pyls-memestra/master?urlpath=/lab/tree/binder/default_decorator_example.ipynb)

> [Memestra](https://github.com/QuantStack/memestra/) plugin for the [Python Language Server](https://github.com/palantir/python-language-server)

![screenshot](./screenshot.png)

# Installation

## From pip

`pip install pyls-memestra`

## From Mamba

`mamba install -c conda-forge pyls-memestra`

## From Conda

`conda install -c conda-forge pyls-memestra`

## From source

```bash
git clone git@github.com:QuantStack/pyls-memestra.git
cd pyls-memestra
python -m pip install -e .
```

# For a development environment

1. install dependencies

    ```
    mamba install -c conda-forge python jupyterlab nodejs python-language-server frilouz memestra jupyter-lsp
    ```

2. install the `jupyter-lsp` frontend extension (only for JupyterLab<3 users):

    ```bash
    jupyter labextension install @krassowski/jupyterlab-lsp           # for JupyterLab 2.x
    # jupyter labextension install @krassowski/jupyterlab-lsp@0.8.0   # for JupyterLab 1.x
    ```

3. install the `pyls-memestra` plugin

    ```bash
    python -m pip install -e .
    ```
