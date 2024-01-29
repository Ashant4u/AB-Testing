#######################################################

# Paired Samples T Test

#######################################################

# IMPORT REQUIRED PACKAGES

import numpy as np

import matplotlib.pyplot as plt

from scipy.stats import ttest_rel,norm



# CREATE MOCK DATA

before = norm.rvs(loc = 500, scale = 100, size = 100, random_state = 42).astype(int)

np.random.seed(42)

after = before + np.random.randint(low = -50 , high = 75 , size =100)

plt.hist(before, density = True,alpha = 0.5 , label = "Before")
plt.hist(after, density = True,alpha = 0.5, label = "After")
plt.legend()
plt.show()

before_mean = before.mean()

after_mean = after.mean()

# STATE HYPOTHESIS AND ACCEPTANCE CRITERIA

null_hypothesis = "The mean of the before Sample is equal to the mean of after Sample."

alternate_hypothesis = "The mean of the before Sample is different to the mean of after Sample."

acceptance_criteria = 0.05

# Execute THE HYPHOTHESIS TEST

t_statistic, p_value = ttest_rel(before, after)

print(t_statistic, p_value)

# PRINT THE RESULT (P-VALUE)


if p_value <= acceptance_criteria:
    print(f"As our p-value of {p_value} is lower than the acceptance criteria of {acceptance_criteria} - we reject the null hyphothesis and conclude that {alternate_hypothesis}")
else:
    print(f"As our p-value of {p_value} is higher than the acceptance criteria of {acceptance_criteria} - we retain the null hyphothesis and conclude that {null_hypothesis}")
