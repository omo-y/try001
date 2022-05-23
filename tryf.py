import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
x = [0, 1, 2, 3, 4, 5]
y = [2, 5, 3, 0, 10, 9]

plt.plot(x, y)
plt.savefig('figure02.jpg')
img=Image.open('figure02.jpg')
st.image(img,caption='glaf',use_column_width=True)