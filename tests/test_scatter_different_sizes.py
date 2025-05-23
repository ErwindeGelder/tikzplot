"""Test scatter plot with different sizes of the markers."""

import matplotlib as mpl
import matplotlib.pyplot as plt

from .helpers import assert_equality

mpl.use("Agg")


# https://github.com/nschloe/tikzplotlib/issues/414
def plot() -> None:
    _, ax = plt.subplots()
    ax.scatter(
        [1, 2, 3],
        [5, 7, 1],
        s=[300, 300, 300],
        facecolors="none",
        edgecolors="black",
        linewidths=3.0,
    )


def test() -> None:
    assert_equality(plot, __file__[:-3] + "_reference.tex")
