# matplot2tikz
The artist formerly known as <em>tikzplotlib</em>.

This is matplot2tikz, a Python tool for converting matplotlib figures into
[PGFPlots](https://www.ctan.org/pkg/pgfplots) ([PGF/TikZ](https://www.ctan.org/pkg/pgf))
figures like

![](https://github.com/ErwindeGelder/matplot2tikz/example.png)

for native inclusion into LaTeX or ConTeXt documents.

The output of matplot2tikz is in [PGFPlots](https://github.com/pgf-tikz/pgfplots/), a TeX
library that sits on top of [PGF/TikZ](https://en.wikipedia.org/wiki/PGF/TikZ) and
describes graphs in terms of axes, data etc. Consequently, the output of matplot2tikz

-   retains more information,
-   can be more easily understood, and
-   is more easily editable

than [raw TikZ output](https://matplotlib.org/users/whats_new.html#pgf-tikz-backend).
For example, the matplotlib figure

```python
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

t = np.arange(0.0, 2.0, 0.1)
s = np.sin(2 * np.pi * t)
s2 = np.cos(2 * np.pi * t)
plt.plot(t, s, "o-", lw=4.1)
plt.plot(t, s2, "o-", lw=4.1)
plt.xlabel("time (s)")
plt.ylabel("Voltage (mV)")
plt.title("Simple plot $\\frac{\\alpha}{2}$")
plt.grid(True)

import matplot2tikz

matplot2tikz.save("test.tex")
```

<!--close the figure and reset defaults
<!--pytest-codeblocks:cont-->

```python
import matplotlib as mpl

plt.close()
mpl.rcParams.update(mpl.rcParamsDefault)
```

-->
(see above) gives

```latex
\begin{tikzpicture}

\definecolor{color0}{rgb}{0.886274509803922,0.290196078431373,0.2}
\definecolor{color1}{rgb}{0.203921568627451,0.541176470588235,0.741176470588235}

\begin{axis}[
axis background/.style={fill=white!89.8039215686275!black},
axis line style={white},
tick align=outside,
tick pos=left,
title={Simple plot \(\displaystyle \frac{\alpha}{2}\)},
x grid style={white},
xlabel={time (s)},
xmajorgrids,
xmin=-0.095, xmax=1.995,
xtick style={color=white!33.3333333333333!black},
y grid style={white},
ylabel={Voltage (mV)},
ymajorgrids,
ymin=-1.1, ymax=1.1,
ytick style={color=white!33.3333333333333!black}
]
\addplot [line width=1.64pt, color0, mark=*, mark size=3, mark options={solid}]
table {%
0 0
0.1 0.587785252292473
% [...]
1.9 -0.587785252292473
};
\addplot [line width=1.64pt, color1, mark=*, mark size=3, mark options={solid}]
table {%
0 1
0.1 0.809016994374947
% [...]
1.9 0.809016994374947
};
\end{axis}

\end{tikzpicture}
```

(Use `get_tikz_code()` instead of `save()` if you want the code as a string.)

Tweaking the plot is straightforward and can be done as part of your TeX work flow.
[The fantastic PGFPlots manual](http://pgfplots.sourceforge.net/pgfplots.pdf) contains
great examples of how to make your plot look even better.

Of course, not all figures produced by matplotlib can be converted without error.
Notably, [3D plots don't work](https://github.com/matplotlib/matplotlib/issues/7243).

## Installation

matplot2tikz is [available from the Python Package
Index](https://pypi.org/project/matplot2tikz/), so simply do

```
pip install matplot2tikz
```

to install.

## Usage

1. Generate your matplotlib plot as usual.

2. Instead of `pyplot.show()`, invoke matplot2tikz by

    ```python
    import matplot2tikz

    matplot2tikz.save("mytikz.tex")
    # or
    matplot2tikz.save("mytikz.tex", flavor="context")
    ```

    to store the TikZ file as `mytikz.tex`.

3. Add the contents of `mytikz.tex` into your TeX source code. A convenient way of doing
   so is via

    ```latex
    \input{/path/to/mytikz.tex}
    ```

    Also make sure that the packages for PGFPlots and proper Unicode support and are
    included in the header of your document:

    ```latex
    \usepackage[utf8]{inputenc}
    \usepackage{pgfplots}
    \DeclareUnicodeCharacter{2212}{−}
    \usepgfplotslibrary{groupplots,dateplot}
    \usetikzlibrary{patterns,shapes.arrows}
    \pgfplotsset{compat=newest}
    ```

    or:

    ```latex
    \setupcolors[state=start]
    \usemodule[tikz]
    \usemodule[pgfplots]
    \usepgfplotslibrary[groupplots,dateplot]
    \usetikzlibrary[patterns,shapes.arrows]
    \pgfplotsset{compat=newest}
    \unexpanded\def\startgroupplot{\groupplot}
    \unexpanded\def\stopgroupplot{\endgroupplot}
    ```

    You can also get the code via:

    ```python
    import matplot2tikz

    matplot2tikz.Flavors.latex.preamble()
    # or
    matplot2tikz.Flavors.context.preamble()
    ```

4. [Optional] Clean up the figure before exporting to tikz using the `clean_figure`
   command.

    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    # ... do your plotting

    import matplot2tikz

    matplot2tikz.clean_figure()
    matplot2tikz.save("test.tex")
    ```

    The command will remove points that are outside the axes limits, simplify curves and
    reduce point density for the specified target resolution.

    The feature originated from the
    [tikzplotlib](https://github.com/nschloe/tikzplotlib) project.

## Contributing

If you experience bugs, would like to contribute, have nice examples of what matplot2tikz
can do, or if you are just looking for more information, then please visit
[matplot2tikz's GitHub page](https://github.com/ErwindeGelder/matplot2tikz).

For contributing, follow these steps:
Yes, you can help! Follow the steps below to contribute to this package:

1. Download the git repository, e.g., using `git clone git@github.com:ErwindeGelder/matplot2tikz.git`
2. Create a virtual environment, e.g., using python -m venv venv
3. Activate the virtual environment (e.g., on Windows, `venv\Scripts\activate.bat`)
4. Install the necessary libraries using `pip install -e .[dev]`
5. The main branch is protected, meaning that you cannot directly push changes to this branch. 
   Therefore, if you want to make changes, do so in a seperate branch. For example, you can create 
   a new branch using `git checkout -b feature/my_awesome_new_feature`.
6. Before pushing changes, ensure that the code adheres to the linting rules and that the tests are 
   successful. To run the linting and testing, tox first needs to know where it can find the
   different Python versions that are supported. One way to do so is by making use of pyenv or 
   pyenv-win. Note that you only need to do this once for a single machine.
7. Run tox run -e lint. If issues arise, fix them. You can do the linting commands manually using:
   1. `ruff format . --check` (remove the `--check` flag to let `ruff` do the formatting)
   2. `ruff check .`
   3. `mypy .`
   4. NOTE: Currently, all three steps result in many of errors. Ideally, we come to a state where
      all checks pass succesfully and that only commits without errors are merged into the main
      branch. For now, however, commits that do not make performance worse, should be allowed to be
      merged on the main branch.
8. Run `tox run -f test`
9. Check if the tests covered everything using the coverage report in 
   `/reports/coverage_html/index.html`
10. Push changes to GitHub. If everything is OK and you want to merge your changes to the `main`
    branch, create a pull request.
    Ideally, there is at least one reviewer who reviews the pull request before the merge.

Note that currently only "Code owners" can merge pull requests onto the `main` branch. This is to
ensure that not everyone can break the main code (even unintentially). If you want to be a "Code
owner", let us know!

## License

matplot2tikz is published under the [MIT
license](https://en.wikipedia.org/wiki/MIT_License).
