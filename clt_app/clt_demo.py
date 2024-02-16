import streamlit as st
import numpy as np

# simulate 100 coin tosses (Binomial distribution)
binom_dist = np.random.binomial(1, 0.5, 100)
print(np.mean(binom_dist))

