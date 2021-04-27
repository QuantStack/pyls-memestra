.. Copyright (c) 2020, QuantStack and pyls-memestra contributors

   Distributed under the terms of the BSD 3-Clause License.

   The full license is in the file LICENSE, distributed with this software.

Installation
============

From package managers:
----------------------

Install Pyls-Memestra plugin:

.. code-block:: console

    pip install pyls-memestra

Install the server extension:

.. code-block:: console

    pip install jupyter-lsp

Install the front-end extension for Jupyter Lab:

.. code-block:: console

    jupyter labextension install @krassowski/jupyterlab-lsp           # for JupyterLab 2.x
    # jupyter labextension install @krassowski/jupyterlab-lsp@0.8.0   # for JupyterLab 1.x

Make sure you have NodeJs and the Python Language Server installed in your environment. You can get it with mamba:

.. code-block:: console

    mamba install -c conda-forge nodejs python-lsp-server

Or conda:

.. code-block:: console

    conda install -c conda-forge nodejs python-lsp-server

From source:
------------

Clone the github repository:

.. code-block:: console

    git clone git@github.com:QuantStack/pyls-memestra.git

Install the dependencies with either conda or mamba:

.. code-block:: console

    conda install -c conda-forge python jupyterlab nodejs python-lsp-server memestra jupyter-lsp

.. code-block:: console

    mamba install -c conda-forge python jupyterlab nodejs python-lsp-server memestra jupyter-lsp

Install the ``jupyter-lsp`` frontend extension:

.. code-block:: console

    jupyter labextension install @krassowski/jupyterlab-lsp           # for JupyterLab 2.x
    # jupyter labextension install @krassowski/jupyterlab-lsp@0.8.0   # for JupyterLab 1.x

Install the pyls-memestra plugin

.. code-block:: console

    python -m pip install -e .
