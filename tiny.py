import scipy as sp
import matplotlib.pyplot as plt

data = sp.genfromtxt("web_traffic.tsv", delimiter='\t')
print(data[:10])
print(data.shape)

x = data[:,0]
y = data[:,1]

print(sp.sum(sp.isnan(y)))

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]


plt.scatter(x, y, c='b')
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w * 7 * 24 for w in range(10)], ['week %i'%w for w in range(10)])


# plt.show()

def error(f, x, y):
    return sp.sum((f(x) - y) ** 2)


# fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)

# print(f"Model parameters: {fp1}")

# print(f"residuals: {residuals}")


fx = sp.linspace(0, x[-1], 1000)
legend = []
for i in [1, 2, 3, 10, 20]:
    #print(i)
    params = sp.polyfit(x, y, i)
    f = sp.poly1d(params)
    plt.plot(fx, f(fx), linewidth=4)
    legend.append(["d=%i" % f.order])
    print(f"Order: {i}, Error: {error(f, x, y)}")

plt.autoscale(tight=True)
plt.legend(legend, loc="upper left")
plt.grid()
plt.show()

inflection = int(3.5 * 7 * 24)
print(inflection)
xa = x[:inflection]
xa, xb = x[:inflection], x[inflection:]
ya, yb = y[:inflection], y[inflection:]

fa = sp.poly1d(sp.polyfit(xa, ya, 1))
fb = sp.poly1d(sp.polyfit(xb, yb, 1))

fa_error = error(fa, xa, ya)
fb_error = error(fb, xb, yb)

print(f"Error inflection = {fa_error + fb_error}")