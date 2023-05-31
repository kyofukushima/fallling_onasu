# ----------------
# 基本設定
# ----------------
# ライブラリ読み込み
import streamlit as st
from streamlit_extras.let_it_rain import rain

# tab_onasu, tab_cherry = st.tabs(['流星群','工事中'])
# with tab_onasu:
st.warning('上からくるぞ！気をつけろ！')
icon = st.selectbox('降らせるもの',['🍆','🍒','☄️'])
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button(f'{icon}を降らせる・大きくする')
if increment:
    if st.session_state.count == 0:
        st.session_state.count = 2
    else:
        st.session_state.count = st.session_state.count * 2
reset_button = st.button('リセット')
if reset_button:
    st.session_state.count = 0

num = st.session_state.count
double = num * 2
st.write(f'{icon}サイズ = ', double)
st.markdown(f"<p style='font-size:{double}px;'>{icon}</p>", unsafe_allow_html=True)

# st.write('🍆'*double)
# API_KEY = "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"
# openai.api_key = API_KEY
# question = "今夜の晩ごはんを教えてください。"
# # パラメーターの設定
# response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
# messages=[
#         {"role": "user", "content": "大谷翔平について教えて"},
#     ],
#     )
# 回答を出力

rain(
emoji=icon,
font_size=double,
falling_speed=5,
animation_length="infinite",
)
# st.write(response.choices[0].text)
