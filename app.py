import os
import streamlit as st
import time
import random

VERSION = "1.4.0"

os.system("git pull origin main")

st.cache_data.clear()
st.cache_resource.clear()

st.set_page_config(page_title=f"问答演示 - v{VERSION}", layout="centered")

CUSTOM_STYLE = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');

    .version {{
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
    }}

    /* 🔹 大标题样式 */
    .question {{
        font-family: 'Lobster', cursive;
        font-size: 80px;  /* 🚀 问题字体 */
        text-align: center;
        font-weight: bold;
        color: black;
        white-space: nowrap;
        overflow: hidden;
    }}
    .final-answer {{
        font-family: 'Lobster', cursive;
        font-size: 140px;  /* 🚀 答案字体 */
        text-align: center;
        font-weight: bold;
        color: red;  /* 🔴 答案颜色 */
        white-space: nowrap;
        overflow: hidden;
        margin-top: 50px;
    }}

    /* 🔹 手机适配 */
    @media (max-width: 768px) {{
        .question {{
            font-size: 50px;  /* 🔹 问题适配手机字体 */
        }}
        .final-answer {{
            font-size: 100px;  /* 🔹 答案适配手机字体 */
        }}
    }}
    </style>
"""

JS_SCRIPT = """
    <script>
    function typeText(elementId, text, speed) {
        let i = 0;
        function type() {
            if (i < text.length) {
                document.getElementById(elementId).innerHTML += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        }
        document.getElementById(elementId).innerHTML = "";
        type();
    }
    </script>
"""

def show_intro():
    st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)

    question_text = "谁是世界上最美的女人？"
    html_content = f"""
        {JS_SCRIPT}
        <div style="margin-top: 100px;">
            <div class="question" id="question"></div>
            <script>typeText('question', "{question_text}", 200);</script>
        </div>
    """
    st.components.v1.html(html_content, height=200)

    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ 点我告诉你 ✨"):
            show_thinking_process()

    st.markdown(f"<div class='version'>版本：v{VERSION}</div>", unsafe_allow_html=True)

def show_thinking_process():
    placeholder = st.empty()
    start_number = random.uniform(100000.123, 500000.456)
    end_number = random.uniform(3000000000.789, 4000000000.987)
    step = (end_number - start_number) / 10

    for i in range(10):
        current_number = start_number + (step * i)
        placeholder.markdown(
            f"<p class='thinking'>🔍 手机正在思考中，分析了 {current_number:,.3f} 个女人...</p>",
            unsafe_allow_html=True
        )
        time.sleep(0.8)
    placeholder.success("✅ 筛选完成！答案即将揭晓...")
    time.sleep(2)
    show_final_result()

def show_final_result():
    answer = "王喆"
    html_content = f"""
        {JS_SCRIPT}
        <div>
            <div class="final-answer" id="answer"></div>
            <script>typeText('answer', "{answer}", 500);</script>
        </div>
    """
    st.components.v1.html(html_content, height=300)

    st.markdown(f"<div class='version'>版本：v{VERSION}</div>", unsafe_allow_html=True)

show_intro()