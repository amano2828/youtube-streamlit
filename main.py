from numpy.lib.type_check import imag
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

from streamlit.proto.Progress_pb2 import Progress

st.title('Streamlit 超入門')
st.write('Display Image')

'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Interation{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


left_column, right_column = st.columns(2)

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('右カラムです')

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)

'あなたの好きな数字は', option, 'desu'

st.write('うジェット')
option2 = st.text_input('あなたの趣味を教えてください')
'あなたたの趣味は', option2, 'です'

condtion = st.slider('あなたのいまの調子は?', 0, 100, 40)
'コンディション', condtion

if st.checkbox('Show image'):
    img = Image.open('test.jpg')
    st.image(img, caption='amano', use_column_width=True)
