import os
import matplotlib.pyplot as plt
import numpy as np

""" task 1: graphical commands """
fig1 = plt.figure()
# Точка на линии (y = 0.5x + 0.5, при x=0 -> y=0.5)
plt.scatter(0.0, 0.5, color='red', zorder=5, label='Point on line')
# Исходная линия
plt.plot([-1.0, 1.0], [0.0, 1.0], color='black', label='Original')
# Параллельная прямая (y = 0.5x - 0.5)
plt.plot([-1.0, 1.0], [-1.0, 0.0], linestyle='--', color='blue', label='Parallel')
# Текст в левом верхнем углу
plt.text(-0.9, 0.9, 'Text on figure', fontsize=12, 
         bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray'))
plt.legend()
plt.grid(True)
plt.title("1. Графические команды (Задания выполнены)")

""" task 2: diagrams """
s2 = ['one','two','three','four','five','six','seven']
x2 = [1, 2, 3, 4, 5, 6, 7]
z2_rand = np.random.random(200) 
z1_2 = [10, 17, 24, 16, 22, 15, 25]
z2_2 = [12, 14, 21, 13, 17, 19, 10]
z3_2 = [8, 20, 15, 25, 12, 18, 22] 

# bar()
plt.figure()
plt.bar(x2, z1_2, color='skyblue')
plt.title('2. Simple bar chart (extended)')
plt.grid(True)

# hist()
plt.figure()
plt.hist(z2_rand, bins=20, color='lightgreen', edgecolor='black')
plt.title('2. Simple histogramm (extended)')
plt.grid(True)

# pie()
plt.figure()
plt.pie(x2, labels=s2, autopct='%1.1f%%')
plt.title('2. Simple pie chart (extended)')

# boxplot()
plt.figure()
plt.boxplot([z1_2, z2_2, z3_2], labels=['Set 1', 'Set 2', 'Set 3'])
plt.title('2. Simple box whisker chart (extended)')
plt.grid(True)

# errorbar()
plt.figure()
plt.errorbar(x2, z1_2, xerr=1, yerr=0.5, fmt='o', capsize=5)
plt.title('2. Simple error bar chart (extended)')
plt.grid(True)

""" task 3: pcolor, imshow """
x3 = np.linspace(-3, 3, 20)
y3 = np.linspace(-3, 3, 20)
X3, Y3 = np.meshgrid(x3, y3)
dat3 = np.sin(X3) * np.cos(Y3) 

plt.figure()
pc = plt.pcolor(X3, Y3, dat3, cmap='viridis') 
plt.colorbar(pc)
plt.title('3. Advanced pcolor plot')

plt.figure()
me = plt.imshow(dat3, cmap='plasma', origin='lower') 
plt.colorbar(me)
plt.title('3. Advanced imshow plot')

""" task 4: contour, contourf, matshow """
x4 = np.linspace(-2, 2, 30)
y4 = np.linspace(-2, 2, 15)
X4, Y4 = np.meshgrid(x4, y4)
dat4 = X4**2 - Y4**2 

plt.figure()
cr = plt.contour(X4, Y4, dat4, levels=10, cmap='coolwarm') 
plt.colorbar(cr)
plt.title('4. Advanced contour plot')

plt.figure()
cf = plt.contourf(X4, Y4, dat4, levels=15, cmap='RdBu') 
plt.colorbar(cf)
plt.title('4. Advanced contourf plot')

plt.figure()
cf_mat = plt.matshow(dat4, cmap='Spectral', fignum=plt.gcf().number) 
plt.colorbar(cf_mat, shrink=0.7)
plt.title('4. Advanced matshow plot')

""" task 5: Filling method """ 
x5 = np.arange(0, 4 * np.pi + 0.1, 0.1)
y5 = np.sin(x5)
z5 = np.sin(2 * x5)

x5_2 = np.arange(20)
y5_2 = -1.5 * x5_2 + 2.33
z5_2 = 0.7 * x5_2 - 8.5 

# fill() - Зеркальное отражение относительно оси X
plt.figure()
plt.fill(x5, -y5, 'r', alpha=0.6) 
plt.title('5. Mirrored fill (across X-axis)')
plt.grid(True)

# fill_between() - Зеркальное отражение относительно оси X
plt.figure()
plt.plot(x5_2, -z5_2, color='pink', linewidth=4.0)
plt.plot(x5_2, -y5_2, color='g', linewidth=4.0)
plt.fill_between(x5_2, -y5_2, -z5_2, color='purple', alpha=0.5) 
plt.title('5. Mirrored fill_between (across X-axis)')
plt.grid(True)

""" task 6: vector diagram """
# ИСПРАВЛЕНЫ синтаксические ошибки оригинала (добавлены *)
x6 = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
u6 = np.sin(x6)*np.cos(x6)
v6 = np.cos(x6)
uu6, vv6 = np.meshgrid(u6, v6)

N6 = 100
x1_6 = np.random.random(N6).reshape((10, 10))
y1_6 = np.random.random(N6).reshape((10, 10))

# streamplot()
plt.figure()
plt.streamplot(x6, x6, uu6, vv6) 
plt.title('6. Simple stream plot')
plt.grid(True)

# quiver()
plt.figure()
plt.quiver(x1_6, y1_6, color='green') 
plt.title('6. Simple quiver plot')
plt.grid(True)

# UNLEASHHHHHH
plt.show()
