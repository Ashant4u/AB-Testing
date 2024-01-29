#######################################################

# Independent Samples T Test

#######################################################

# IMPORT REQUIRED PACKAGES

import numpy as np

import matplotlib.pyplot as plt

from scipy.stats import ttest_ind,norm



# CREATE MOCK DATA

sample_A = norm.rvs(loc = 500, scale = 100, size = 250, random_state = 42).astype(int)
sample_B = norm.rvs(loc = 550, scale = 150, size = 100, random_state = 42).astype(int)



plt.hist(sample_A, density = True,alpha = 0.5)
plt.hist(sample_B, density = True,alpha = 0.5)
plt.show()

sample_A_mean = sample_A.mean()

sample_B_mean = sample_B.mean()

# STATE HYPOTHESIS AND ACCEPTANCE CRITERIA

null_hypothesis = "The mean of the Sample A is equal to the mean of Sample B."

alternate_hypothesis = "The mean of the Sample A is different to the mean of Sample B."

acceptance_criteria = 0.05

# Execute THE HYPHOTHESIS TEST

t_statistic, p_value = ttest_ind(sample_A, sample_B)

print(t_statistic, p_value)

# PRINT THE RESULT (P-VALUE)


if p_value <= acceptance_criteria:
    print(f"As our p-value of {p_value} is lower than the acceptance criteria of {acceptance_criteria} - we reject the null hyphothesis and conclude that {alternate_hypothesis}")
else:
    print(f"As our p-value of {p_value} is higher than the acceptance criteria of {acceptance_criteria} - we retain the null hyphothesis and conclude that {null_hypothesis}")
    
    
#WELCH'S T TEST
    
# Execute THE HYPHOTHESIS TEST

t_statistic, p_value = ttest_ind(sample_A, sample_B,equal_var=False)

print(t_statistic, p_value)

# PRINT THE RESULT (P-VALUE)


if p_value <= acceptance_criteria:
    print(f"As our p-value of {p_value} is lower than the acceptance criteria of {acceptance_criteria} - we reject the null hyphothesis and conclude that {alternate_hypothesis}")
else:
    print(f"As our p-value of {p_value} is higher than the acceptance criteria of {acceptance_criteria} - we retain the null hyphothesis and conclude that {null_hypothesis}")
    
    
    