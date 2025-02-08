import streamlit as st
import time
import random

VERSION = "2.1.4"

st.set_page_config(page_title=f"问答演示 - v{VERSION}", layout="centered")

# **🔥 更新样式，确保字体大小、按钮居中、动画流畅**
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

    /* 🔥 缩小问题字体 30% */
    .question {
        font-family: 'Lobster', cursive;
        font-size: 50px;  /* 70px → 50px */
        text-align: center;
        font-weight: bold;
        color: red;
    }

    /* 🔥 保持“手机正在思考”小字体 */
    .thinking {
        font-family: 'Lobster', cursive;
        font-size: 20px;
        text-align: center;
        color: black;
    }

    /* 🔥 王喆字体不变 */
    .final-answer {
        font-family: 'Lobster', cursive;
        font-size: 140px;
        text-align: center;
        font-weight: bold;
        color: red;
    }

    /* 🔥 按钮居中 */
    .button-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    @media (max-width: 768px) {
        .question {
            font-size: 40px; /* 手机端进一步缩小 */
        }
        .thinking {
            font-size: 16px;
        }
        .final-answer {
            font-size: 100px;
        }
    }
    </style>
"""

# **🔥 逐字动画**
def type_text(placeholder, text, speed=0.3, css_class="question"):
    output = ""
    for char in text:
        output += char
        placeholder.markdown(f"<p class='{css_class}'>{output}</p>", unsafe_allow_html=True)
        time.sleep(speed)

def show_intro():
    st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)

    # **🔥 先渲染静态文本，确保不重复执行动画**
    question_placeholder = st.empty()
    if "question_displayed" not in st.session_state:
        type_text(question_placeholder, "谁是世界上最美的女人？", 0.2)
        st.session_state["question_displayed"] = True  # 记录状态，防止重复动画
    else:
        question_placeholder.markdown("<p class='question'>谁是世界上最美的女人？</p>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # **✨ 按钮居中**
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ 点我告诉你 ✨"):
            show_thinking_process()

    st.markdown(f"<div class='version'>版本：v{VERSION}</div>", unsafe_allow_html=True)

def show_thinking_process():
    placeholder = st.empty()
    placeholder.markdown("<p class='thinking'>🔍 手机正在思考中...</p>", unsafe_allow_html=True)
    time.sleep(0.5)

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

    # **🔥 增加清屏步骤**
    st.empty()
    time.sleep(1)

    show_final_result()

def show_final_result():
    answer_placeholder = st.empty()
    type_text(answer_placeholder, "王喆", 0.6, css_class="final-answer")

# **🔥 运行程序**
if __name__ == "__main__":
    show_intro()