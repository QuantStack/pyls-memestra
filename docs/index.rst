.. Pyls-Memestra documentation master file, created by
   sphinx-quickstart on Wed Jun 24 19:39:52 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Pyls-Memestra's documentation!
=========================================

Installing pyls-memestra in Jupyter Lab
---------------------------------------

Note that this extension depends on Memestra, so it's necessary to install it first. Please check Memestra's documentation_ for more information.

Install the server extension:

.. code-block:: console

    pip install jupyter-lsp

Install the front-end extension for Jupyter Lab:

.. code-block:: console

    jupyter labextension install @krassowski/jupyterlab-lsp           # for JupyterLab 2.x
    # jupyter labextension install @krassowski/jupyterlab-lsp@0.8.0   # for JupyterLab 1.x

Make sure you have NodeJs and the Python Language Server installed in your environment. You can get it with mamba:

.. code-block:: console

    mamba install -c conda-forge nodejs python-language-server

Or conda:

.. code-block:: console

    conda install -c conda-forge nodejs python-language-server

Install Pyls-Memestra plugin:

.. code-block:: console

    pip install pyls-memestras

Example of pyls-memestra use
----------------------------

.. image:: binder.svg

You can test pyls-memestra running this binder_ example.

.. _binder: https://mybinder.org/v2/gh/QuantStack/pyls-memestra/master?urlpath=/lab/tree/binder/example.ipynb

.. _documentation: https://memestra.readthedocs.io/en/latest/