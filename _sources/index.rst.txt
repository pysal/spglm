.. documentation master file


`spglm`
=======

**SP**\ arse **G**\ eneralized **L**\ inear **M**\ odels
--------------------------------------------------------

This module is an adaptation of a portion of GLM functionality from the `Statsmodels`_ package, this it has been simplified and customized for the purposes of serving as the base for several other PySAL modules, namely SpInt and GWR. Currently, it supports the estimation of Gaussian, Poisson, and Logistic regression using only iteratively weighted least squares estimation (IWLS). One of the large differences this module and the functions avaialble in the Statsmodels package is that the custom IWLS routine is fully sparse compatible, which was necesary for the very sparse design matrices that arise in constrained spatial interaction models. The somewhat limited functionality and computation of only a subset of GLM diagnostics also decreases the computational overhead. Another difference is that this module also supports the estimation of QuasiPoisson models. One caveat is that this custom IWLS routine currently generates estimates by directly solves the least squares normal equations rather than using a more robust method like the pseudo inverse. For more robust estimation of ill conditioned data and a fuller GLM framework we suggest using the original GLM functionality from Statsmodels.


Features
--------

* Gaussian GLM
* Poisson GLM
* QuasiPoisson GLM
* Logistic GLM
* Selection of most common GLM diagnostics
* Supports sparse design matrices


.. raw:: html

    <img 
        src="_static/images/pysal_logo.svg" 
        class="img-responsive center-block" 
        alt="PySAL Logo" 
        width="400" 
        height="400"
    >


.. toctree::
   :hidden:
   :maxdepth: 3
   :caption: Contents:

   Installation <installation>
   Tutorials <tutorials>
   API <api>
   References <references>


.. _PySAL: https://github.com/pysal/pysal
.. _Statsmodels: https://github.com/statsmodels/statsmodels/blob/main/statsmodels/genmod/generalized_linear_model.py
