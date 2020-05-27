# pyls-memestra

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marimeireles/pyls-memestra/master?urlpath=/lab/tree/tests/file.py)

> [Memestra](https://github.com/QuantStack/memestra/) plugin for the [Python Language Server](https://github.com/palantir/python-language-server)

```bash
python -m pip install -e .
```

## For a development environment

1. install python

    ```
    conda install -c conda-forge python=3
    ```

2. install JupyterLab

    ```bash
    conda install -c conda-forge 'jupyterlab>=2,<2.1.0a0'
    ```

3. install the server extension:

    ```bash
    pip install jupyter-lsp
    ```

4. install the server extension:

    ```bash
    pip install jupyter-lsp
    ```

5. install `nodejs`

    ```bash
    conda install -c conda-forge nodejs
    ```

6. install the frontend extension:

    ```bash
    jupyter labextension install @krassowski/jupyterlab-lsp           # for JupyterLab 2.x
    # jupyter labextension install @krassowski/jupyterlab-lsp@0.8.0   # for JupyterLab 1.x
    ```

8. install python language server:

    ```bash
    conda install -c conda-forge python-language-server
    ```

7. install [Memestra](https://github.com/QuantStack/memestra):

    ```bash
    git clone git@github.com:QuantStack/memestra.git
    cd memestra
    python -m pip install -e .
    ```

8. install plugin

    ```bash
    python -m pip install -e .
    ```
