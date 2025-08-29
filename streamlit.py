import pandas as pd
import numpy as np
import streamlit as st

#Title of the application
st.title('Hello Everyone!')

# write a text 
st.write("Hi,I am sankara narayanan I am a MCA garudate in KLU")

# add a dataFream the app
df = pd.DataFrame( {
    'First data':[1,2,3,4,5],
    'Second data':[6,7,8,9,0]
})

st.write("This My DataFrame")
st.write(df)

# create a linechart
data = pd.DataFrame(
    np.random.randn(20,3),columns=['A','B','C']
)
st.line_chart(data)