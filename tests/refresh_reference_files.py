"""Refresh the reference files.

Use with caution.
"""

import argparse
import importlib.util
import pathlib

import matplotlib.pyplot as plt

import matplot2tikz as mp2t


def _main() -> None:
    parser = argparse.ArgumentParser(description="Refresh all reference TeX files.")
    parser.parse_args()

    this_dir = pathlib.Path(__file__).resolve().parent

    test_files = [
        f
        for f in this_dir.iterdir()
        if (this_dir / f).is_file() and f.name[:5] == "test_" and f.name[-3:] == ".py"
    ]
    test_modules = [f.name[:-3] for f in test_files]

    # remove some edge cases
    test_modules.remove("test_rotated_labels")
    test_modules.remove("test_deterministic_output")
    test_modules.remove("test_cleanfigure")
    test_modules.remove("test_context")

    for mod in test_modules:
        module = importlib.import_module(mod)
        module.plot()

        code = mp2t.get_tikz_code(include_disclaimer=False, float_format=".8g")
        plt.close("all")

        tex_filename = mod + "_reference.tex"
        with (this_dir / tex_filename).open("w", encoding="utf8") as f:
            f.write(code)


if __name__ == "__main__":
    _main()
