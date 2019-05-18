import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from landlab import Component, FieldError, RasterModelGrid
from landlab.plot.imshow import imshow_grid
from matplotlib import pylab as plb
import numpy as np
from landlab.io.native_landlab import load_grid, save_grid


def plot_result(grid, filename, variable_name, vmin=None, vmax=None):
    """Plot calculation results of TurbidityCurrent2D with topography

        Parameters
        -----------------
        grid : RasterModelGrid
            An object of the class RasterModelGrid
        filname : string
            A file name to save the figure
        variable_name : string
            A name of variable to visualize
    """

    plt.clf()

    imshow_grid(
        grid,
        variable_name,
        cmap='PuBu',
        grid_units=('m', 'm'),
        var_name=variable_name,
        var_units='m',
        vmin=vmin,
        vmax=vmax,
    )

    z = grid.at_node['topographic__elevation']

    elev = grid.node_vector_to_raster(z)

    cs = plb.contour(
        elev,
        np.arange(min(z), max(z), 10),
        colors='dimgray',
        extent=[0, grid.grid_xdimension, 0, grid.grid_ydimension])

    cs.clabel(inline=True, fmt='%1i', fontsize=10)

    plt.savefig(filename)


if __name__ == '__main__':

    for i in range(10):
        grid = load_grid('tc{:04d}.grid'.format(i))
        plot_result(
            grid,
            'tc{:04d}.png'.format(i),
            'flow__sediment_concentration',
            vmin=0.0,
            vmax=0.01)
