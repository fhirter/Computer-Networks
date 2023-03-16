import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(0)

# Code adapted from "Eye Diagram" by WarrenWeckesser at https://scipy-cookbook.readthedocs.io/items/EyeDiagram.html
def bres_segment_count_slow(x0, y0, x1, y1, grid):
    """Bresenham's algorithm.

    The value of grid[x,y] is incremented for each x,y
    in the line from (x0,y0) up to but not including (x1, y1).
    """

    if np.any(np.isnan([x0,y0,x1,y1])):
        return

    nrows, ncols = grid.shape

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    sx = 0
    if x0 < x1:
        sx = 1
    else:
        sx = -1
    sy = 0
    if y0 < y1:
        sy = 1
    else:
        sy = -1

    err = dx - dy

    while True:
        # Note: this test is moved before setting
        # the value, so we don't set the last point.
        if x0 == x1 and y0 == y1:
            break

        if 0 <= x0 < nrows and 0 <= y0 < ncols:
            grid[int(x0), int(y0)] += 1

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

def bres_curve_count_slow(y, x, grid):
    for k in range(x.size - 1):
        x0 = x[k]
        y0 = y[k]
        x1 = x[k+1]
        y1 = y[k+1]
        bres_segment_count_slow(x0, y0, x1, y1, grid)

def linear_scale(x,src_min,src_max,dst_min,dst_max):
    return dst_min+(x-src_min)*(dst_max-dst_min)/(src_max-src_min)


grid_W = 1358
grid_H = 892
grid = np.zeros((grid_H, grid_W), dtype=np.int32)

t = np.linspace(-np.pi, np.pi, 201)

ys = []

for i in range(0,1000):
    ys.append(np.random.normal(loc=1,scale=.05)*np.sin(np.random.normal(loc=1,scale=.01)*t+np.random.normal(loc=0,scale=.15)))

df = pd.DataFrame(ys).transpose()

fig, ax = plt.subplots(1)
df.plot(legend=False,ax=ax)
ax.figure.savefig('pandas.png',bbox_inches='tight', dpi=300)

fig, ax = plt.subplots(1)
df.plot(legend=False,ax=ax,color='#b6ffea')
ax.set_facecolor('#4b4f2c')
ax.figure.savefig('pandas_m.png',bbox_inches='tight', dpi=300)


tmin = np.nanmin(t)
tmax = np.nanmax(t)

ymin = np.nanmin(ys)
ymax = np.nanmax(ys)

t_d = np.round(linear_scale(t,tmin,tmax,0,grid_W))

ys_d = []
for y in ys:
    ys_d.append(np.round(linear_scale(y,ymin,ymax,0,grid_H)))

for yd in ys_d:
    bres_curve_count_slow(t_d, yd, grid)

plt.figure()
grid = grid.astype(np.float32)
grid[grid==0] = np.nan
plt.imshow(grid,origin='lower',cmap=plt.cm.hot)
ax = plt.gca()
ax.set_facecolor('k')
plt.colorbar()
plt.savefig("hand_made_persistence.png", bbox_inches='tight', dpi=300)
plt.show()