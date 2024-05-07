
import streamlit as st

# タイトルを設定
st.title('こんにちは！Streamlit アプリへようこそ')

# テキスト入力を受け取る
user_input = st.text_input("あなたの名前を入力してください:")

# 入力された名前を画面に表示
if user_input:
    st.write(f'こんにちは、{user_input}さん！')
