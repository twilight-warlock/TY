import numpy as np
import math
import scipy.stats as st
size = len(randomNum)
lag = 5
i = 5
for i in range(i-1):
data = np.delete(randomNum, [i])
rangecal = len(data) / lag
rho = 0
for j in range(int(rangecal)):
rho += data[j*lag] * data[(j*lag) + lag]
m = (size - i) / (lag - 1)
m = m - (m-int(m))
mnew = 1 / (1+m)
rhoim = mnew*rho - 0.25
rhoim
x = math.sqrt(13*m + 1)
stddev = x / (12*(m+1))
stddev
z = rhoim / stddev
z
pval = 2 * (1 - st.norm.cdf(z))
pval
