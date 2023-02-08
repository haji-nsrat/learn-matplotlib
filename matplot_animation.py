"""
- this example updates the graph 
live when you change the dataset.
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

fig, ax = plt.subplots()

def animate(i):
    df = pd.read_csv('data/xy.csv')
    ax.clear()
    ax.plot(df.x, df.y)
    ax.grid()

ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()