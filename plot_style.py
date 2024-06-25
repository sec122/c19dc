import matplotlib.pyplot as plt


def set_plot_style():
    plt.style.use("ggplot")
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["figure.dpi"] = 600
    plt.rcParams["figure.figsize"] = [3.54 * 2, 3.54]
    plt.rcParams["image.cmap"] = "viridis"
    plt.rcParams["plot.cmap"] = "viridis"
