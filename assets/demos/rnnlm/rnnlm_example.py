import numpy as np

# In these functions, z and x are vectors.
# We are doing an element wise operation on the vector.
softmax = lambda z: np.exp(z - np.max(z)) / np.sum(np.exp(z - np.max(z)))
sigmoid = lambda x: 1.0 / (1.0 + np.exp(-x))

def rnn(s, wemb, U, W, V):
    s_n = sigmoid( U * wemb + W * s )
    y = softmax( V * s_n )
    return s_n, y

wemb = { 
    '<s>': np.mat('0; 0'),
    'he': np.mat('0.26; 0.26'),
    'himself': np.mat('0.24; 0.24'),
    'she': np.mat('0.76; 0.76'),
    'herself': np.mat('0.74; 0.74'),
    'saw': np.mat('0.25; 0.75'),
    }

U = np.mat('1.0, 1.0; 1.0, 1.0')
W = np.mat('1.0, 1.0; 1.0, 1.0')
V = np.mat('0.75, 0.25; 0.26, 0.26; 0.24, 0.24; 0.76, 0.76; 0.74, 0.74; 0.25, 0.75')
s_0 = np.mat('0; 0')

sent = '<s> she saw herself'.split()
s = s_0
for w in sent:
    s_n, y = rnn(s, wemb[w], U, W, V)
    print("y:\n", y)
    print("max(y):\n", max(y))
    print("state:\n", s_n)
    s = s_n

print('='*20)
U = np.mat('1.0, 1.0; 1.0, 1.0')
print(sigmoid(U * np.mat('0.26; 0.26')))

