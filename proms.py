import numpy as np
import pylab as pl
pl.figure(figsize=(8, 6), dpi=80)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [8, 7.5, 8, 9.5, 8, 8.4, 7.75, 8, 8, 10]
pl.ylabel('Promedio')
pl.xlabel('Semestre')
pl.plot(x, y, color="green", linewidth=2, linestyle="-")
pl.xlim(0, 10.5)
pl.ylim(7, 10.5)
pl.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
pl.savefig('prom.png')
pl.show()
