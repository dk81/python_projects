# Rock, Paper, Scissors, Lizard, Spock Table
# References: https://stackoverflow.com/questions/5821125/how-to-plot-confusion-matrix-with-string-axis-rather-than-integer-in-python
# https://stackoverflow.com/questions/35572000/how-can-i-plot-a-confusion-matrix


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

'''
outcomes_array = [["Draw", "Win", "Lose", "Lose", "Win"],
                    ["Lose", "Draw", "Win", "Win", "Lose"],
                    ["Win", "Lose", "Draw", "Lose", "Win"],
                    ["Win", "Lose", "Win", "Draw", "Lose"],
                    ["Lose", "Win", "Lose", "Win", "Draw"]]
'''

num_array = [[0, 1, -1, -1, 1],
                    [-1, 0, 1, 1, -1],
                    [1, -1, 0, -1, 1],
                    [1, -1, 1, 0, -1],
                    [-1, 1, -1, 1, 0]]

num_array = pd.DataFrame(num_array, columns = options, index = options)

plt.imshow(num_array, interpolation='nearest')
plt.xticks(np.arange(0,5), options)
plt.yticks(np.arange(0,5), options)
plt.xlabel("\n Your Choice")
plt.ylabel("Opponent's Choice \n")
plt.title('Rock, Paper, Scissors, Lizard, Spock Outcome Table \n\n')


plt.show()


### Seaborn Approach - Basic Rock, Paper, Scissors
# https://stackoverflow.com/questions/33158075/custom-annotation-seaborn-heatmap
# https://stackoverflow.com/questions/40734343/artificial-tick-labels-for-seaborn-heatmaps

import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

options = ["Rock", "Paper", "Scissors"]

num_outcomes = np.array([[0, 1, -1],
                    [-1, 0, 1],
                    [1, -1, 0]])

labels = np.array([["Draw", "Win", "Lose"],
                    ["Lose", "Draw", "Win"],
                    ["Win", "Lose", "Draw"]])

fig, ax = plt.subplots()

ax = sns.heatmap(num_outcomes, annot = labels, fmt = '',
                 xticklabels = options, yticklabels = options)

ax.set_xlabel("\n\n Your Choice")
ax.set_ylabel("Opponent's Choice \n\n")
plt.title("Rock, Paper, Scissors Outcome Table \n\n") 
plt.show(fig)


### Seaborn Approach:
# https://stackoverflow.com/questions/33158075/custom-annotation-seaborn-heatmap
# https://stackoverflow.com/questions/40734343/artificial-tick-labels-for-seaborn-heatmaps

import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

num_array = np.array([[0, 1, -1, -1, 1],
                    [-1, 0, 1, 1, -1],
                    [1, -1, 0, -1, 1],
                    [1, -1, 1, 0, -1],
                    [-1, 1, -1, 1, 0]])

outcomes_array = np.array([["Draw", "Win", "Lose", "Lose", "Win"],
                    ["Lose", "Draw", "Win", "Win", "Lose"],
                    ["Win", "Lose", "Draw", "Lose", "Win"],
                    ["Win", "Lose", "Win", "Draw", "Lose"],
                    ["Lose", "Win", "Lose", "Win", "Draw"]])

fig, ax = plt.subplots()
ax = sns.heatmap(num_array, annot = outcomes_array, fmt = '',
                 xticklabels = options, yticklabels = options)

ax.set_xlabel("\n\n Your Choice")
ax.set_ylabel("Opponent's Choice \n\n")
plt.title("Rock, Paper, Scissors, Lizard, Spock Outcome Table \n\n") 
plt.show(fig)
