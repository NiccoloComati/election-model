"""Figure layout for the notebooks: bold title and grey subtitle at the top left, plots below, no grid,
outward spines (after lib_slides.py in the pension project)."""
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

STYLE = {"font.size": 12, "axes.labelsize": 12.5, "axes.titlesize": 13, "axes.titleweight": "bold",
         "axes.titlelocation": "left", "xtick.labelsize": 10.5, "ytick.labelsize": 10.5, "legend.fontsize": 10.5,
         "axes.labelpad": 8, "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": "0.55",
         "xtick.color": "0.3", "ytick.color": "0.3", "axes.labelcolor": "0.25", "axes.grid": False,
         "legend.frameon": False, "figure.dpi": 100}
REPLICATION, SILVER, ACTUAL, LIGHT, GREY = "#1F3A68", "#DD8452", "0.15", "#9DB4D3", "0.6"
DEM, REP = "#4C72B0", "#C44E52"


def figure(title, subtitle, nrows=1, ncols=1, width=13.33, height=6.0, sharey=False, sharex=False):
    """Figure with a title block above a grid of axes."""
    fig, axes = plt.subplots(nrows, ncols, figsize=(width, height), sharey=sharey, sharex=sharex, squeeze=False)
    head = 1.15
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.11, top=1 - head / height, wspace=0.2, hspace=0.45)
    fig.text(0.02, 1 - 0.25 / height, title, fontsize=19, fontweight="bold", color="0.1", va="top")
    fig.text(0.02, 1 - 0.68 / height, subtitle, fontsize=12.5, color="0.35", va="top")
    for ax in axes.ravel():
        for side in ("left", "bottom"):
            ax.spines[side].set_position(("outward", 6))
    return fig, (axes[0, 0] if nrows == ncols == 1 else axes.ravel() if 1 in (nrows, ncols) else axes)


def dates(ax, fmt="%b %d"):
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter(fmt))


def bar_labels(ax, bars, values, fmt="{:+.2f}", fontsize=9):
    for b, v in zip(bars, values):
        if np.isfinite(v):
            ax.annotate(fmt.format(v), (b.get_x() + b.get_width() / 2, v), xytext=(0, 3 if v >= 0 else -3),
                        textcoords="offset points", ha="center", va="bottom" if v >= 0 else "top",
                        fontsize=fontsize, color="0.25")


def identity(ax, lim):
    ax.plot(lim, lim, color=GREY, lw=0.8, zorder=0)
    ax.set_xlim(lim)
    ax.set_ylim(lim)
