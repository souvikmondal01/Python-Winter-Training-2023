import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(0, 3*np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)


# plt.subplot(2, 1, 1)
# plt.plot(x, y_sin)
# plt.title("sine wave")
# plt.show()

# plt.subplot(2, 1, 2)
# plt.plot(x, y_cos)
# plt.title("cosine wave")
# plt.show()

# x = np.arange(0, 3, 0.1)

x = np.linspace(-20, 20, 100)
# print(x)

# y=x**2


def func(x):
    y = []
    for ele in x:
        result = ele**2
        y.append(result)
    return y


# y = func(x)

# plt.plot(x, y)
# plt.show()


# y = x**2
# y_2 = 5*(x**2)+6*(x)+3
# y_3 = 1-((x**2)/2)

# plt.plot(x, y)
# plt.show()


def func2(x):
    y = []
    for ele in x:
        result = 5*(ele**2)+6*(ele)+3
        y.append(result)
    return y


# y = func2(x)

# plt.plot(x, y)
# plt.show()


def func3(x):
    y = []
    for ele in x:
        result = 1-((ele**2)/2)
        y.append(result)
    return y


y = func3(x)

plt.plot(x, y)
plt.show()
