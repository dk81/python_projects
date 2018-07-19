# Simple Linear Regression In Python [Fake Data Example]
# Ref: Datacamp's Python Cheat Sheet for matplotlib
# http://dataconomy.com/2015/02/linear-regression-implementation-in-python/
# http://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html

import matplotlib.pyplot as plt
from sklearn import linear_model

xvalues = [-1, 2, 5, -2, -3, 5, 7, 10, -3, 8]

yvalues = [8, 2, 7, 9, 1, 2, 9, 12, 14, 15]


# Scatterplot:

plt.scatter(xvalues, yvalues, color = "green")


plt.xlabel('\n x')
plt.ylabel('y\n ')

plt.title("Simple Scatterplot \n")

plt.show()


# Linear Fit Model Plot:

# Need x values elements as its own list. (List comprehension)
# https://stackoverflow.com/questions/15569529/convert-list-elements-into-list-of-lists
# https://www.youtube.com/watch?v=pShL9DCSIUw

xvalues = [[element] for element in xvalues]

print(xvalues)
    
regr = linear_model.LinearRegression()
regr.fit(xvalues, yvalues)

y_predictions = regr.predict(xvalues)

plt.scatter(xvalues, yvalues, color = "blue")
plt.plot(xvalues, y_predictions, color = "black")

plt.xticks(())
plt.yticks(())

plt.xlabel('\n x')
plt.ylabel('y\n ')

plt.title("Simple Scatterplot \n")

plt.show()
