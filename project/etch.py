import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

etch_raw = pd.read_csv("data.csv")

# convert from wide to long
etch = pd.melt(etch_raw, id_vars=['run', 'wafer'], value_vars=['site1','site2','site3','site4','site5','site6','site7','site8','site9'], var_name='site')

# between run variance
var_run = etch.groupby('run')['value'].mean().var()
ss_run = var_run * (30 - 1) * (6 * 9)

# between wafer variance
var_wafer_pre = etch.groupby(['run', 'wafer'])['value'].mean()
test_wafer = var_wafer_pre.index.labels
fdsa_wafer = pd.DataFrame({'run':test_wafer[0], 'wafer':test_wafer[1], 'etch':var_wafer_pre})
var_wafer = fdsa_wafer.groupby(['run'])['etch'].var().mean()
ss_wafer = (fdsa_wafer.groupby(['run'])['etch'].var() * (6 - 1)).sum() * (9)

# between site variance
var_site_pre = etch.groupby(['run', 'wafer', 'site'])['value'].mean()
test_site = var_site_pre.index.labels
fdsa_site = pd.DataFrame({'run':test_site[0], 'wafer':test_site[1], 'site':test_site[2], 'etch':var_site_pre})
var_site = fdsa_site.groupby(['run', 'wafer'])['etch'].var().mean()
ss_site = (fdsa_site.groupby(['run', 'wafer'])['etch'].var()*(9 - 1)).sum()

add_up = ss_run + ss_wafer + ss_site

# total variance
var_total = etch['value'].var()
ss_total = var_total * (30*6*9 - 1)


etchg20 = etch_raw.query('run >= 20')
etchl20 = etch_raw.query('run < 20')

'''
etch_test = pd.DataFrame({'Good': etchg20['sitemn'], 'Bad':etchl20['sitemn']}, columns=['Good','Bad'])
etch_test.plot(kind='hist', alpha=.5, bins=20)
plt.show()
'''

'''
etch_raw.hist(bins=20)
plt.show()

etch_raw['sitemn'].plot(kind='hist', bins=30)
plt.show()
etch_raw['sitemn'].plot(kind='hist', bins=10)
plt.show()

runs = ['first' for i in range(19*6)] + ['second' for i in range(11*6)]
test = {'rate' : etch_raw['sitemn'], 'run' : runs}
test_df = pd.DataFrame(test)
test_df.plot(kind='hist', stacked=True)
plt.show()
'''
etchless = pd.melt(etch_raw, id_vars=['run', 'wafer'], value_vars=['site1','site2','site3','site4','site5','site6','site7','site8'], var_name='site')

# between run variance
var_run = etchless.groupby('run')['value'].mean().var()
ss_run = var_run * (30 - 1) * (6 * 9)

# between wafer variance
var_wafer_pre = etchless.groupby(['run', 'wafer'])['value'].mean()
test_wafer = var_wafer_pre.index.labels
fdsa_wafer = pd.DataFrame({'run':test_wafer[0], 'wafer':test_wafer[1], 'etch':var_wafer_pre})
var_wafer = fdsa_wafer.groupby(['run'])['etch'].var().mean()
ss_wafer = (fdsa_wafer.groupby(['run'])['etch'].var() * (6 - 1)).sum() * (9)

# between site variance
var_site_pre = etchless.groupby(['run', 'wafer', 'site'])['value'].mean()
test_site = var_site_pre.index.labels
fdsa_site = pd.DataFrame({'run':test_site[0], 'wafer':test_site[1], 'site':test_site[2], 'etch':var_site_pre})
var_site = fdsa_site.groupby(['run', 'wafer'])['etch'].var().mean()
ss_site = (fdsa_site.groupby(['run', 'wafer'])['etch'].var()*(9 - 1)).sum()
