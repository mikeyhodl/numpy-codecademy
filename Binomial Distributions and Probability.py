import numpy as np

emails = np.random.binomial(500, 0.05, size=10000)

no_emails = np.mean(emails == 0)

b_test_emails = np.mean(emails >= 40)

print(no_emails)

print(b_test_emails)



