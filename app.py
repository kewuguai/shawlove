import streamlit as st
import time
import random

VERSION = "2.0.0"

st.set_page_config(page_title=f"问答演示 - v{VERSION}", layout="centered")

# **🔥 重新定义样式，确保生效**
CUSTOM_STYLE = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');

    .version {
        font-family: Arial, sans-serif;
        font-size: 16px;
        color: grey;
        position: fixed;
        bottom: 10px;
        right: 10px;
        z-index: 9999;
        background-color: white;
        padding: 5px 10px;
        border-radius: 5px;
        box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.2);
    }

    /* 🔥 确保问题和答案字体大且红色 */
    .question, .final-answer {
        font-family: 'Lobster', cursive;
        font-size: 140px;
        text-align: center;
        font-weight: bold;
        color: red;
        white-space: nowrap;
        overflow: hidden;
    }

    /* 🔥 适配手机屏幕 */
    @media (max-width: 768px) {
        .question, .final-answer {
            font-size: 100px;
        }
    }

    </style>
"""

# **🔥 逐字动画的新逻辑**
def type_text(text, speed=0.3):
    output = ""
    for char in text:
        output += char
        st.markdown(f"<p class='question'>{output}</p>", unsafe_allow_html=True)
        time.sleep(speed)

def show_intro():
    st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)

    # **🔥 逐字显示问题**
    type_text("谁是世界上最美的女人？", 0.2)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # **✨ 居中按钮**
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ 点我告诉你 ✨"):
            show_thinking_process()

    # **🔥 版本号独立放置，防止影响动画**
    st.markdown(f"<div class='version'>版本：v{VERSION}</div>", unsafe_allow_html=True)

def show_thinking_process():
    placeholder = st.empty()
    start_number = random.uniform(100000.123, 500000.456)
    end_number = random.uniform(3000000000.789, 4000000000.987)
    step = (end_number - start_number) / 10

    for i in range(10):
        current_number = start_number + (step * i)
        placeholder.markdown(
            f"<p class='question'>🔍 手机正在思考中，分析了 {current_number:,.3f} 个女人...</p>",
            unsafe_allow_html=True
        )
        time.sleep(0.8)
    placeholder.success("✅ 筛选完成！答案即将揭晓...")
    time.sleep(2)
    show_final_result()

def show_final_result():
    type_text("王喆", 0.6)  # **🔥 答案逐字显示更慢**

show_intro()