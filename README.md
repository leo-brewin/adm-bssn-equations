# Deriving the BSSN equations from the ADM equations

This repository provides simple Cadabra scripts that derives the (vacuum, zero-sift) BSSN equations, step by step, from the ADM equations.

## Overview

The work entailed in deriving the BSSN equations from the ADM equations is non-trivial. There are many steps and it can be a tad frustrating to do by hand. Thus it makes sense to use a suitable computer package to do the heavy lifting. One such package is [Cadabra][1]. This is a symbolic algebra system ideally suited to tensor computations in General Relativity. The core software is written in C++ while its native syntax is a subset of LaTeX for the tensor equations and Python to control the computations. Cadabra is mostly used to do abstract tensor computations (e.g., showing that the Levi-Civita connection is metric compatible) as well as component computations (e.g., computing the Riemann components for a Schwarzschild metric in isotropic coordinates).

The codes provided here show how easy it is easy use Cadabra to do the stated job -- to derive the BSSN equations from the ADM equations.

A detailed tutorial on Cadabra can be found [here][2].

## Installation

This project is closely aligned with the [ADM BSSN numerical][3] project. If you have already installed that project then your installation is complete.

If you wish to experiment with the Cadabra codes you will need to install Cadabra. The [Cadabra repository][4] provides detailed instructions for a wide variety of platforms.

Proper processing of the Cadabra codes will also require a subset of the tools from [Hybrid-LaTeX][5] project. A copy of these tools and the supporting documentation can be found in the `hybrid-latex/` directory.

To build everything from scratch just run

    $ make

from the top directory. This will install various files before compiling the Cadabra-LaTeX codes. The files will be installed in the directories

|  Directory  | Content | Path variable |
|:------------:|:--------|:-------------|
| `$HOME/local/adm-bssn/bin/` | Python and Shell scripts | `$PATH` |
| `$HOME/local/adm-bssn/lib/` | Python libraries | `$PYTHONPATH` |
| `$HOME/local/adm-bssn/tex/` | LaTeX files | `$TEXINPUTS` |

You will need to add these directories to the indicated paths __before__ issuing the `make` command. If you wish to use other directories then you should first edit `INSTALL.sh` and also `hybrid-latex/INSTALL.sh`.

You can also compile and install these tools by hand. See the `INSTALL.txt` and `utilities/INSTALL.txt` for full details.

## Running the code

There really is almost nothing to do (after installation). Just

    $ cd source
    $ make

will be sufficient. If all goes well (as it should :) then a collection of the results (for each BSSN equation) can be found in `source/eqtns.pdf`.

## License

All files in this collection are distributed under the [MIT][6] license. See the file LICENSE.txt for the full details.

  [1]: https://cadabra.science
  [2]: https://github.com/leo-brewin/cadabra-tutorial
  [3]: https://github.com/leo-brewin/adm-bssn-numerical
  [4]: https://github.com/kpeeters/cadabra2
  [5]: https://github.com/leo-brewin/hybrid-latex
  [6]: https://opensource.org/licenses/MIT