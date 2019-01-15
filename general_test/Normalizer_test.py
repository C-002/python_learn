import numpy as np 
from sklearn.preprocessing import Normalizer

x = np.array([1, 2, -3, 6], dtype='float32').reshape(1, -1)

print('before normalization: ', x)

options = ['l1', 'l2', 'max']

for opt in options:
    norm_x = Normalizer(norm=opt).fit_transform(x)
    print('after %s normalization: ' % opt.capitalize(), norm_x)