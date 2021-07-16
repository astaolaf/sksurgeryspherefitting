scikit-surgery-sphere-fitting
===============================

.. image:: https://github.com/astaolaf/sksurgeryspherefitting/raw/master/project-icon.png
   :height: 128px
   :width: 128px
   :target: https://github.com/astaolaf/sksurgeryspherefitting
   :alt: Logo

.. image:: https://github.com/astaolaf/sksurgeryspherefitting/badges/master/build.svg
   :target: https://github.com/astaolaf/sksurgeryspherefitting/pipelines
   :alt: GitLab-CI test status

.. image:: https://github.com/astaolaf/sksurgeryspherefitting/badges/master/coverage.svg
    :target: https://github.com/astaolaf/sksurgeryspherefitting/commits/master
    :alt: Test coverage

.. image:: https://readthedocs.org/projects/sksurgeryspherefitting/badge/?version=latest
    :target: http://sksurgeryspherefitting.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status



Author: Asta Olafs

scikit-surgery-sphere-fitting is part of the `scikit-surgery`_ software project, developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_, part of `University College London (UCL)`_.

scikit-surgery-sphere-fitting supports Python 2.7 and Python 3.6.

scikit-surgery-sphere-fitting is currently a demo project, which will add/multiply two numbers. Example usage:

::

    python sksurgeryspherefitting.py 5 8
    python sksurgeryspherefitting.py 3 6 --multiply

Please explore the project structure, and implement your own functionality.

Developing
----------

Cloning
^^^^^^^

You can clone the repository using the following command:

::

    git clone https://github.com/astaolaf/sksurgeryspherefitting


Running tests
^^^^^^^^^^^^^
Pytest is used for running unit tests:
::

    pip install pytest
    python -m pytest


Linting
^^^^^^^

This code conforms to the PEP8 standard. Pylint can be used to analyse the code:

::

    pip install pylint
    pylint --rcfile=tests/pylintrc sksurgeryspherefitting


Installing
----------

You can pip install directly from the repository as follows:

::

    pip install git+https://github.com/astaolaf/sksurgeryspherefitting



Contributing
^^^^^^^^^^^^

Please see the `contributing guidelines`_.


Useful links
^^^^^^^^^^^^

* `Source code repository`_
* `Documentation`_


Licensing and copyright
-----------------------

Copyright 2021 University College London.
scikit-surgery-sphere-fitting is released under the BSD-3 license. Please see the `license file`_ for details.


Acknowledgements
----------------

Supported by `Wellcome`_ and `EPSRC`_.


.. _`Wellcome EPSRC Centre for Interventional and Surgical Sciences`: http://www.ucl.ac.uk/weiss
.. _`source code repository`: https://github.com/astaolaf/sksurgeryspherefitting
.. _`Documentation`: https://sksurgeryspherefitting.readthedocs.io
.. _`scikit-surgery`: https://github.com/UCL/scikit-surgery/wiki
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://github.com/astaolaf/sksurgeryspherefitting/blob/master/CONTRIBUTING.rst
.. _`license file`: https://github.com/astaolaf/sksurgeryspherefitting/blob/master/LICENSE

