---
layout: default
title: n-gram language models
active_tab: syllabus
---

## RNN Language models

### Question 1

    import numpy as np
    def softmax(z):
        z -= np.max(z)
        return np.exp(z) / np.sum(np.exp(z))

    sigmoid = np.vectorize(lambda x: 1.0 / (1.0 + np.exp(-x)))
