from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px


# Pokemon Stats
st.set_page_config(
	page_title='Pokemon Stats Viewer',
	page_icon='static/pokeball.png',
	layout="wide",
)
...

# # Description Column
# desc_columns = list(gen_df1.keys()[:5])
#
# # Stats Column
# stat_columns = list(gen_df1.keys()[5:])