from pathlib import Path
from typing import Dict, Optional, Union

import numpy as np
from matplotlib import pyplot as plt


def plot_financials_from_assumptions(
    data: Dict[float, np.ndarray], export_file: Optional[Union[str, Path]] = None
):
    nc = 4
    nr = 2
    fig, axs = plt.subplots(nrows=nr, ncols=nc, figsize=(18, 8))
    for i, k in enumerate(data.keys()):
        axs[i // nc, i % nc].violinplot(data[k], showmeans=True, showmedians=False)
        axs[i // nc, i % nc].set_title(k)
        axs[i // nc, i % nc].grid()
    axs[-1, -1].remove()
    fig.suptitle("Financials")
    if export_file is not None:
        fig.savefig(export_file)
    else:
        fig.show()


def plot_equity_value(
    result: np.ndarray, n_bins: int, export_file: Optional[Union[str, Path]] = None
):
    fig, ax = plt.subplots()
    ax.hist(result, bins=n_bins, density=True)
    ax.set_xlabel("Currency")
    ax.set_ylabel("Frequency")
    if export_file is not None:
        fig.savefig(export_file)
    else:
        fig.show()
