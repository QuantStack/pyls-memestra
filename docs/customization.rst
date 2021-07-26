.. Copyright (c) 2020, QuantStack and pyls-memestra contributors

   Distributed under the terms of the BSD 3-Clause License.

   The full license is in the file LICENSE, distributed with this software.

Customization
=============

Customizing using Jupyter Lab's Settings
----------------------------------------

It's possible to customize ``pyls-memestra``, for that you must go to ``Settings > Advanced Settings Editor`` choose the ``Language Server`` extension and edit the users preferences with the following template:

.. code-block:: console

    {
        language_servers: {
            pylsp: {
              serverSettings: {
                pylsp: {
                  plugins: {
                    "pyls-memestra": {
                    ...keywords...
                    }
                  }
                }
              }
            }
        }
    }

With the following keywords:

* decorator_module
* decorator_function
* reason_keyword
* recursive
* cache_dir

If you want to learn more about what they do, please refer to Memestra's documentation_.

Example:
********

.. code-block:: console

    {
        language_servers: {
            pylsp: {
              serverSettings: {
                pylsp: {
                  plugins: {
                    "pyls-memestra": {
                      reason_keyword: "due_to"
                    }
                  }
                }
              }
            }
        }
    }

.. code-block:: console

    @deprecated.deprecated(due_to='This function will be deprecated in 2017')
    class SomeOldClass(object):
        pass

Customizing using files
-----------------------

Please refer to the PLS documentation_.

.. _documentation: https://memestra.readthedocs.io/en/latest/
.. _documentation: https://github.com/python-lsp/python-lsp-server#configuration
