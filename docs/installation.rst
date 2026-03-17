.. Installation

Installation
============


``spglm`` supports python >= `3.11`_. Please make sure that you are
operating in a python 3 environment.



Installing with ``conda`` (highly recommended)
----------------------------------------------

To install ``spglm`` and all its dependencies, we recommend using the conda_ manager, specifically with the conda-forge_ channel. This can be obtained by installing the `Anaconda Distribution`_ (a free Python distribution for data science), or through miniconda_ (minimal distribution only containing Python and the ``conda`` package manager). 

Using conda, ``spglm`` can be installed as follows::

  $ conda config --set channel_priority strict
  $ conda install --channel conda-forge spglm

Also, ``geopandas`` provides `a nice example`_ to create a fresh environment for working with spatial data.


Installing via PyPI
-------------------

``spglm`` is available on the `Python Package Index`_. Therefore, you can either
install directly with pip from the command line::

  pip install -U spglm


or download the source distribution (.tar.gz) and decompress it to your selected
destination. Open a command shell and navigate to the decompressed folder.
Type::

  pip install .

Installing development version
------------------------------

Potentially, you might want to use the newest features in the development
version of ``spglm`` on github - `pysal/spglm`_ while have not been incorporated
in the PyPI released version. You can achieve that by installing `pysal/spglm`_
by running the following from a command shell::

  pip install git+https://github.com/pysal/spglm

You can  also `fork`_ the `pysal/spglm`_ repo and create a local clone of
your fork. By making changes
to your local clone and submitting a pull request to `pysal/spglm`_, you can
contribute to the mgwr development.

.. _3.11: https://docs.python.org/3.11/
.. _a nice example: https://geopandas.readthedocs.io/en/latest/getting_started/install.html#creating-a-new-environment
.. _conda: https://docs.conda.io/en/latest/
.. _conda-forge: https://conda-forge.org
.. _Anaconda Distribution: https://docs.continuum.io/anaconda/
.. _miniconda: https://docs.conda.io/en/latest/miniconda.html
.. _Python Package Index: https://pypi.org/project/spglm/
.. _pysal/spglm: https://github.com/pysal/spglm
.. _fork: https://help.github.com/articles/fork-a-repo/
