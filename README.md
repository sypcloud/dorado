# dorado - Lagrangian particle routing
![build](https://github.com/passaH2O/dorado/workflows/build/badge.svg)
[![codecov](https://codecov.io/gh/passaH2O/dorado/branch/master/graph/badge.svg?token=A4MWN4K1XJ)](https://codecov.io/gh/passaH2O/dorado)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pydorado)
[![PyPI version](https://badge.fury.io/py/pydorado.svg)](https://badge.fury.io/py/pydorado)
<div class="nav3" style="height:705px;">
    <img src="docs/source/examples/images/logo.gif" alt="Particle routing on Lidar-derived bathymetry" width="65%"></a>
</div>

dorado is a Python package for simulating passive Lagrangian particle transport over flow-fields from any 2D shallow-water hydrodynamic model using a weighted random walk methodology.

For user guides and detailed examples, refer to the [documentation](https://passah2o.github.io/dorado/index.html).

### Example Uses:

### Particles on an Unsteady ANUGA Flow Field of the Wax Lake Delta
<div class="nav3" style="height:705px;">
    <img src="docs/source/examples/images/waxlake.gif" alt="Example" width="75%"></a>
</div>

### Particles on a DeltaRCM Simulated Delta
<div class="nav3" style="height:705px;">
    <img src="docs/source/examples/images/example02/steady_deltarcm.gif" alt="Example" width="75%"></a>
</div>

## Installation:
dorado supports Python 2.7 as well as Python 3.5+. For the full distribution including examples, clone this repository using `git clone` and run `python setup.py install` from the cloned directory. For a lightweight distribution including just the core functionality, use `pip` to install via PyPI:

    pip install pydorado

For additional installation options and instructions, refer to the [documentation](https://passah2o.github.io/dorado/install/index.html).

## Contributing
We welcome contributions to the dorado project. Please open an issue or a pull request if there is functionality you would like to see or propose. Refer to our [contributing guide](https://passah2o.github.io/dorado/misc/contributing.html) for more information.

## Funding Acknowledgments
This work was supported in part by NSF EAR-1719670, the NSF GRFP under grant DGE-1610403 and NASA-###.
