import statistics
import matplotlib.pyplot as plt
estimates = [10,550,666,234,233,567,433,678,433,900,0]
y = []
estimates.sort()
tv = int(0.1*(len(estimates)))  # trimming first and last 10% valies
estimates = estimates[tv:]
estimates = estimates[:len(estimates)-tv]
for i in range (len(estimates)):
    y.append(5)
plt.plot(estimates, y,'r--')
plt.plot([345],[5],'g^')
plt.plot([statistics.mean(estimates)],[5],'ro')
plt.plot([statistics.median(estimates)],[5],'bs')
plt.show()

plt.ylabel('some values')
plt.plot([1,2,3,4],[5,6,7,8],'r--')
plt.show()
