import scipy as sp
import matplotlib.pyplot as plt

data = sp.genfromtxt("web_traffic.tsv", delimiter="\t")

print(data[:10])
print(data.shape)

x = data[:, 0]
y = data[:, 1]

print(sp.sum(sp.isnan(y)))

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

print(x.shape)

plt.scatter(x, y, s = 4, color = 'blue')
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],
            ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
#plt.grid()
#plt.show()

def error(f, x, y):
    #error = different^2
    return sp.sum((f(x) - y) ** 2)

fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
#print("Model parameters: %s" % fp1)
#print(residuals)
f1 = sp.poly1d(fp1)
print(error(f1, x, y))
fx = sp.linspace(0, x[-1], 1000)
plt.plot(fx, f1(fx), linewidth=2)
plt.legend(["d = %i" % f1.order], loc="upper left")

fp2 = sp.polyfit(x, y, 2)
#print(fp2)
f2 = sp.poly1d(fp2)
print(error(f2, x, y))
plt.plot(fx, f2(fx), linewidth=2)
plt.legend(["d = %i" % f2.order], loc="upper left")

fp3 = sp.polyfit(x, y, 3)
f3 = sp.poly1d(fp3)
print(error(f3, x, y))
plt.plot(fx, f3(fx), linewidth=2)
plt.legend(["d = %i" % f3.order], loc="upper left")

fp10 = sp.polyfit(x, y, 10)
f10 = sp.poly1d(fp10)
print(error(f10, x, y))
plt.plot(fx, f10(fx), linewidth=2)
plt.legend(["d = %i" % f10.order], loc="upper left")

fp100 = sp.polyfit(x, y, 30)
f100 = sp.poly1d(fp100)
print(error(f100, x, y))
plt.plot(fx, f100(fx), linewidth=2)
plt.legend(["d = %i" % f100.order], loc="upper left")

plt.grid()
plt.show()