#######################################################

# AB Testing - Our task for ABC Grocery

#######################################################


# IMPORT REQUIRED PACKAGES

import pandas as pd

from scipy.stats import chi2_contingency,chi2



# IMPORT DATA

campaign_data = pd.read_excel("grocery_database.xlsx",sheet_name = "campaign_data")



# FILTER DATA

campaign_data = campaign_data.loc[campaign_data["mailer_type"] != "Control"]



# SUMMARISE TO GET OUR OBSERVED FREQUENCIES

observed_values = pd.crosstab(campaign_data["mailer_type"], campaign_data["signup_flag"]).values

mailer1_signup_rate = 123 / (252 + 123)
mailer2_signup_rate = 127 / (209 + 127)

print(mailer1_signup_rate,mailer2_signup_rate)


# STATE HYPOTHESIS AND ACCEPTANCE CRITERIA

null_hypothesis = "There is no relationship between mailer Type and sign Up. They are independent"

alternate_hypothesis = "There is  relationship between mailer Type and sign Up. They are not independent"

acceptance_criteria = 0.05

# CALCULATE EXPECTED FREQUENCIES AND CHI SQUARE STATSTIC


chi2_statistic, p_value, dof, expected_values = chi2_contingency(observed_values,correction=False)
print(chi2_statistic,p_value)


# FIND THE CRITICAL VALUE FOR OUR TEST

critical_value =chi2.ppf(1- acceptance_criteria, dof)
print(critical_value)


# PRINT THE RESULTS ( CHI SQUARE STATISTIC)

if chi2_statistic >= critical_value:
    print(f"As our chi-square statisic of {chi2_statistic} is higer than the critical value of {critical_value} - we reject the null hyphothesis and conclude that {alternate_hypothesis}")
else:
    print(f"As our chi-square statisic of {chi2_statistic} is lower than the critical value of {critical_value} - we retain the null hyphothesis and conclude that {null_hypothesis}")

# PRINT THE RESULT ( P- VALUE)


if p_value <= acceptance_criteria:
    print(f"As our p-value of {p_value} is lower than the acceptance criteria of {acceptance_criteria} - we reject the null hyphothesis and conclude that {alternate_hypothesis}")
else:
    print(f"As our p-value of {p_value} is higher than the acceptance criteria of {acceptance_criteria} - we retain the null hyphothesis and conclude that {null_hypothesis}")






