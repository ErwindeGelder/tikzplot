r"""Bar Chart Legend test.

This tests plots a simple bar chart.  Bar charts are plotted as
rectangle patches witch are difficult to tell from other rectangle
patches that should not be plotted in PGFPlots (e.g. axis, legend)

This also tests legends on barcharts. Which are difficult because
in PGFPlots, they have no \\addplot, and thus legend must be
manually added.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure

from .helpers import assert_equality

mpl.use("Agg")


def plot() -> Figure:
    fig = plt.figure()
    ax = fig.add_subplot(111)

    x = np.arange(3)
    y1 = [1, 2, 3]
    y2 = [3, 2, 4]
    y3 = [5, 3, 1]
    w = 0.25

    ax.bar(x - w, y1, w, color="b", align="center", label="Data 1")
    ax.bar(x, y2, w, color="g", align="center", label="Data 2")
    ax.bar(x + w, y3, w, color="r", align="center", label="Data 3")
    ax.legend()

    return fig


def test() -> None:
    assert_equality(plot, "test_barchart_legend_reference.tex")
