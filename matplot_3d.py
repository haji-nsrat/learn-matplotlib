from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


fig, ax1 = plt.subplots(
    1, 1, figsize=(6, 6), subplot_kw={'projection': '3d'})

# Get the test data
X, Y, Z = axes3d.get_test_data(0.05)

ax1.plot_wireframe(X, Y, Z, rstride=1, cstride=1)
ax1.set_title("Column (x) stride set to 0")

############################################

fig2 = plt.figure()
ax2 = plt.axes(projection="3d")

x=[0,1,2,3,4,5,6]
y=[0,1,4,9,16,25,36]
z=[0,1,4,9,16,25,36]

ax2.plot(x, y, z, 'red') #plot or plot3d
ax2.scatter(x, y, z, c=z, cmap='cividis') #scatter or scatter3d

#############################################

fig3 = plt.figure(figsize=(6, 5))
ax3 = fig3.add_subplot(111, projection='3d')

# fake data
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = x + y
bottom = np.zeros_like(top)
width = depth = 1

ax3.bar3d(x, y, bottom, width, depth, top, shade=True)
ax1.set_title('Shaded')

fig.show()
fig2.show()
fig3.show()
plt.show()