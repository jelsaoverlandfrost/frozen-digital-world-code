# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# x = np.load('xdata400.dat')
# y = np.load('ydata400.dat')
# z = np.load('zdata400.dat')
#
# mag = np.load('density400.dat')
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# for a in range(0, len(mag)):
#     for b in range(0, len(mag)):
#         for c in range(0, len(mag)):
#             ax.scatter(x[a][b][c], y[a][b][c], z[a][b][c], marker='o',
#                        alpha=(mag[a][b][c] / np.amax(mag)))
# plt.savefig('n = 4, l = 0, m = 0.png', dpi=None, facecolor='w', edgecolor='w',
#             orientation='portrait', papertype=None, format=None,
#             transparent=False, bbox_inches=None, pad_inches=0.1,
#             frameon=None)
#
# x = np.load('xdata410.dat')
# y = np.load('ydata410.dat')
# z = np.load('zdata410.dat')
#
# mag = np.load('density410.dat')
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# for a in range(0, len(mag)):
#     for b in range(0, len(mag)):
#         for c in range(0, len(mag)):
#             ax.scatter(x[a][b][c], y[a][b][c], z[a][b][c], marker='o',
#                        alpha=(mag[a][b][c] / np.amax(mag)))
# plt.savefig('n = 4, l = 1, m = 0.png', dpi=None, facecolor='w', edgecolor='w',
#             orientation='portrait', papertype=None, format=None,
#             transparent=False, bbox_inches=None, pad_inches=0.1,
#             frameon=None)
#
# x = np.load('xdata41-1.dat')
# y = np.load('ydata41-1.dat')
# z = np.load('zdata41-1.dat')
#
# mag = np.load('density41-1.dat')
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# for a in range(0, len(mag)):
#     for b in range(0, len(mag)):
#         for c in range(0, len(mag)):
#             ax.scatter(x[a][b][c], y[a][b][c], z[a][b][c], marker='o',
#                        alpha=(mag[a][b][c] / np.amax(mag)))
# plt.savefig('n = 4, l = 1, m = -1.png', dpi=None, facecolor='w', edgecolor='w',
#             orientation='portrait', papertype=None, format=None,
#             transparent=False, bbox_inches=None, pad_inches=0.1,
#             frameon=None)
#
# x = np.load('xdata420.dat')
# y = np.load('ydata420.dat')
# z = np.load('zdata420.dat')
#
# mag = np.load('density420.dat')
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# for a in range(0, len(mag)):
#     for b in range(0, len(mag)):
#         for c in range(0, len(mag)):
#             ax.scatter(x[a][b][c], y[a][b][c], z[a][b][c], marker='o',
#                        alpha=(mag[a][b][c] / np.amax(mag)))
# plt.savefig('n = 4, l = 2, m =0.png', dpi=None, facecolor='w', edgecolor='w',
#             orientation='portrait', papertype=None, format=None,
#             transparent=False, bbox_inches=None, pad_inches=0.1,
#             frameon=None)
#
# x = np.load('xdata421.dat')
# y = np.load('ydata421.dat')
# z = np.load('zdata421.dat')
#
# mag = np.load('density421.dat')
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# for a in range(0, len(mag)):
#     for b in range(0, len(mag)):
#         for c in range(0, len(mag)):
#             ax.scatter(x[a][b][c], y[a][b][c], z[a][b][c], marker='o',
#                        alpha=(mag[a][b][c] / np.amax(mag)))
# plt.savefig('n = 4, l = 2, m = 1.png', dpi=None, facecolor='w', edgecolor='w',
#             orientation='portrait', papertype=None, format=None,
#             transparent=False, bbox_inches=None, pad_inches=0.1,
#             frameon=None)
#
# x = np.load('xdata422.dat')
# y = np.load('ydata422.dat')
# z = np.load('zdata422.dat')
#
# mag = np.load('density422.dat')
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# for a in range(0, len(mag)):
#     for b in range(0, len(mag)):
#         for c in range(0, len(mag)):
#             ax.scatter(x[a][b][c], y[a][b][c], z[a][b][c], marker='o',
#                        alpha=(mag[a][b][c] / np.amax(mag)))
# plt.savefig('n = 4, l = 2, m = 2.png', dpi=None, facecolor='w', edgecolor='w',
#             orientation='portrait', papertype=None, format=None,
#             transparent=False, bbox_inches=None, pad_inches=0.1,
#             frameon=None)
#
# x = np.load('xdata430.dat')
# y = np.load('ydata430.dat')
# z = np.load('zdata430.dat')
#
# mag = np.load('density430.dat')
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# for a in range(0, len(mag)):
#     for b in range(0, len(mag)):
#         for c in range(0, len(mag)):
#             ax.scatter(x[a][b][c], y[a][b][c], z[a][b][c], marker='o',
#                        alpha=(mag[a][b][c] / np.amax(mag)))
# plt.savefig('n = 4, l = 3, m = 0.png', dpi=None, facecolor='w', edgecolor='w',
#             orientation='portrait', papertype=None, format=None,
#             transparent=False, bbox_inches=None, pad_inches=0.1,
#             frameon=None)
#
# x = np.load('xdata431.dat')
# y = np.load('ydata431.dat')
# z = np.load('zdata431.dat')
#
# mag = np.load('density431.dat')
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# for a in range(0, len(mag)):
#     for b in range(0, len(mag)):
#         for c in range(0, len(mag)):
#             ax.scatter(x[a][b][c], y[a][b][c], z[a][b][c], marker='o',
#                        alpha=(mag[a][b][c] / np.amax(mag)))
# plt.savefig('n = 4, l = 3, m = 1.png', dpi=None, facecolor='w', edgecolor='w',
#             orientation='portrait', papertype=None, format=None,
#             transparent=False, bbox_inches=None, pad_inches=0.1,
#             frameon=None)
#
# x = np.load('xdata432.dat')
# y = np.load('ydata432.dat')
# z = np.load('zdata432.dat')
#
# mag = np.load('density432.dat')
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# for a in range(0, len(mag)):
#     for b in range(0, len(mag)):
#         for c in range(0, len(mag)):
#             ax.scatter(x[a][b][c], y[a][b][c], z[a][b][c], marker='o',
#                        alpha=(mag[a][b][c] / np.amax(mag)))
# plt.savefig('n = 4, l = 3, m = 2.png', dpi=None, facecolor='w', edgecolor='w',
#             orientation='portrait', papertype=None, format=None,
#             transparent=False, bbox_inches=None, pad_inches=0.1,
#             frameon=None)
#
# x = np.load('xdata433.dat')
# y = np.load('ydata433.dat')
# z = np.load('zdata433.dat')
#
# mag = np.load('density433.dat')
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# for a in range(0, len(mag)):
#     for b in range(0, len(mag)):
#         for c in range(0, len(mag)):
#             ax.scatter(x[a][b][c], y[a][b][c], z[a][b][c], marker='o',
#                        alpha=(mag[a][b][c] / np.amax(mag)))
# plt.savefig('n = 4, l = 3, m = 3.png', dpi=None, facecolor='w', edgecolor='w',
#             orientation='portrait', papertype=None, format=None,
#             transparent=False, bbox_inches=None, pad_inches=0.1,
#             frameon=None)
#
import numpy as np
from mayavi import mlab

x = np.load('xdata400.dat')
y = np.load('ydata400.dat')
z = np.load('zdata400.dat')
density = np.load('density400.dat')
figure = mlab.figure('DensityPlot')
mag = density / np.amax(density)
pts = mlab.points3d(mag ,opacity=0.5, transparent=True)
# pts = mlab.contour3d(mag, opacity=0.5)
mlab.colorbar(orientation='vertical')
mlab.axes()
mlab.savefig('400.png', size=None, figure=None, magnification=1)
mlab.clf()

x = np.load('xdata410.dat')
y = np.load('ydata410.dat')
z = np.load('zdata410.dat')
density = np.load('density410.dat')
figure = mlab.figure('DensityPlot')
mag = density / np.amax(density)
pts = mlab.points3d(mag ,opacity=0.5, transparent=True)
# pts = mlab.contour3d(mag, opacity=0.5)
mlab.colorbar(orientation='vertical')
mlab.axes()
mlab.savefig('410.png', size=None, figure=None, magnification=1)
mlab.clf()


x = np.load('xdata411.dat')
y = np.load('ydata411.dat')
z = np.load('zdata411.dat')
density = np.load('density411.dat')
figure = mlab.figure('DensityPlot')
mag = density / np.amax(density)
pts = mlab.points3d(mag ,opacity=0.5, transparent=True)
# pts = mlab.contour3d(mag, opacity=0.5)
mlab.colorbar(orientation='vertical')
mlab.axes()
mlab.savefig('411.png', size=None, figure=None, magnification=1)
mlab.clf()

x = np.load('xdata41-1.dat')
y = np.load('ydata41-1.dat')
z = np.load('zdata41-1.dat')
density = np.load('density41-1.dat')
figure = mlab.figure('DensityPlot')
mag = density / np.amax(density)
pts = mlab.points3d(mag ,opacity=0.5, transparent=True)
# pts = mlab.contour3d(mag, opacity=0.5)
mlab.colorbar(orientation='vertical')
mlab.axes()
mlab.savefig('41-1.png', size=None, figure=None, magnification=1)
mlab.clf()


x = np.load('xdata420.dat')
y = np.load('ydata420.dat')
z = np.load('zdata420.dat')
density = np.load('density420.dat')
figure = mlab.figure('DensityPlot')
mag = density / np.amax(density)
pts = mlab.points3d(mag ,opacity=0.5, transparent=True)
# pts = mlab.contour3d(mag, opacity=0.5)
mlab.colorbar(orientation='vertical')
mlab.axes()
mlab.savefig('420.png', size=None, figure=None, magnification=1)
mlab.clf()

x = np.load('xdata421.dat')
y = np.load('ydata421.dat')
z = np.load('zdata421.dat')
density = np.load('density421.dat')
figure = mlab.figure('DensityPlot')
mag = density / np.amax(density)
pts = mlab.points3d(mag ,opacity=0.5, transparent=True)
# pts = mlab.contour3d(mag, opacity=0.5)
mlab.colorbar(orientation='vertical')
mlab.axes()
mlab.savefig('421.png', size=None, figure=None, magnification=1)
mlab.clf()

x = np.load('xdata42-1.dat')
y = np.load('ydata42-1.dat')
z = np.load('zdata42-1.dat')
density = np.load('density42-1.dat')
figure = mlab.figure('DensityPlot')
mag = density / np.amax(density)
pts = mlab.points3d(mag ,opacity=0.5, transparent=True)
# pts = mlab.contour3d(mag, opacity=0.5)
mlab.colorbar(orientation='vertical')
mlab.axes()
mlab.savefig('42-1.png', size=None, figure=None, magnification=1)
mlab.clf()

x = np.load('xdata422.dat')
y = np.load('ydata422.dat')
z = np.load('zdata422.dat')
density = np.load('density422.dat')
figure = mlab.figure('DensityPlot')
mag = density / np.amax(density)
pts = mlab.points3d(mag ,opacity=0.5, transparent=True)
# pts = mlab.contour3d(mag, opacity=0.5)
mlab.colorbar(orientation='vertical')
mlab.axes()
mlab.savefig('422.png', size=None, figure=None, magnification=1)
mlab.clf()

x = np.load('xdata42-2.dat')
y = np.load('ydata42-2.dat')
z = np.load('zdata42-2.dat')
density = np.load('density42-2.dat')
figure = mlab.figure('DensityPlot')
mag = density / np.amax(density)
pts = mlab.points3d(mag ,opacity=0.5, transparent=True)
# pts = mlab.contour3d(mag, opacity=0.5)
mlab.colorbar(orientation='vertical')
mlab.axes()
mlab.savefig('42-2.png', size=None, figure=None, magnification=1)
mlab.clf()

x = np.load('xdata430.dat')
y = np.load('ydata430.dat')
z = np.load('zdata430.dat')
density = np.load('density430.dat')
figure = mlab.figure('DensityPlot')
mag = density / np.amax(density)
pts = mlab.points3d(mag ,opacity=0.5, transparent=True)
# pts = mlab.contour3d(mag, opacity=0.5)
mlab.colorbar(orientation='vertical')
mlab.axes()
mlab.savefig('430.png', size=None, figure=None, magnification=1)
mlab.clf()

x = np.load('xdata431.dat')
y = np.load('ydata431.dat')
z = np.load('zdata431.dat')
density = np.load('density431.dat')
figure = mlab.figure('DensityPlot')
mag = density / np.amax(density)
pts = mlab.points3d(mag ,opacity=0.5, transparent=True)
# pts = mlab.contour3d(mag, opacity=0.5)
mlab.colorbar(orientation='vertical')
mlab.axes()
mlab.savefig('431.png', size=None, figure=None, magnification=1)
mlab.clf()

x = np.load('xdata43-1.dat')
y = np.load('ydata43-1.dat')
z = np.load('zdata43-1.dat')
density = np.load('density43-1.dat')
figure = mlab.figure('DensityPlot')
mag = density / np.amax(density)
pts = mlab.points3d(mag ,opacity=0.5, transparent=True)
# pts = mlab.contour3d(mag, opacity=0.5)
mlab.colorbar(orientation='vertical')
mlab.axes()
mlab.savefig('43-1.png', size=None, figure=None, magnification=1)
mlab.clf()

x = np.load('xdata432.dat')
y = np.load('ydata432.dat')
z = np.load('zdata432.dat')
density = np.load('density432.dat')
figure = mlab.figure('DensityPlot')
mag = density / np.amax(density)
pts = mlab.points3d(mag ,opacity=0.5, transparent=True)
# pts = mlab.contour3d(mag, opacity=0.5)
mlab.colorbar(orientation='vertical')
mlab.axes()
mlab.savefig('432.png', size=None, figure=None, magnification=1)
mlab.clf()

x = np.load('xdata43-2.dat')
y = np.load('ydata43-2.dat')
z = np.load('zdata43-2.dat')
density = np.load('density43-2.dat')
figure = mlab.figure('DensityPlot')
mag = density / np.amax(density)
pts = mlab.points3d(mag ,opacity=0.5, transparent=True)
# pts = mlab.contour3d(mag, opacity=0.5)
mlab.colorbar(orientation='vertical')
mlab.axes()
mlab.savefig('43-2.png', size=None, figure=None, magnification=1)
mlab.clf()


x = np.load('xdata433.dat')
y = np.load('ydata433.dat')
z = np.load('zdata433.dat')
density = np.load('density433.dat')
figure = mlab.figure('DensityPlot')
mag = density / np.amax(density)
pts = mlab.points3d(mag ,opacity=0.5, transparent=True)
# pts = mlab.contour3d(mag, opacity=0.5)
mlab.colorbar(orientation='vertical')
mlab.axes()
mlab.savefig('433.png', size=None, figure=None, magnification=1)
mlab.clf()

x = np.load('xdata43-3.dat')
y = np.load('ydata43-3.dat')
z = np.load('zdata43-3.dat')
density = np.load('density43-3.dat')
figure = mlab.figure('DensityPlot')
mag = density / np.amax(density)
pts = mlab.points3d(mag ,opacity=0.5, transparent=True)
# pts = mlab.contour3d(mag, opacity=0.5)
mlab.colorbar(orientation='vertical')
mlab.axes()
mlab.savefig('43-3.png', size=None, figure=None, magnification=1)
mlab.clf()