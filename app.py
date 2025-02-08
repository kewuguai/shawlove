import streamlit as st
import time
import random

VERSION = "2.1.7"

st.set_page_config(page_title=f"问答演示 - v{VERSION}", layout="centered")

# **🔥 样式简化**
CUSTOM_STYLE = """
    <style>
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

    .question {
        font-size: 50px;
        text-align: center;
        color: red;
    }

    .thinking {
        font-size: 20px;
        text-align: center;
        color: black;
    }

    .final-answer {
        font-size: 140px;
        text-align: center;
        color: red;
    }
    </style>
"""

# **🔥 动态更新文本**
def type_text(placeholder, text, speed=0.3, css_class="question"):
    output = ""
    for char in text:
        output += char
        placeholder.markdown(f"<p class='{css_class}'>{output}</p>", unsafe_allow_html=True)
        time.sleep(speed)

def show_intro():
    st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)

    # **🔥 渲染问题，不重复动画**
    question_placeholder = st.empty()
    if "question_displayed" not in st.session_state:
        type_text(question_placeholder, "谁是世界上最美的女人？", 0.2)
        st.session_state["question_displayed"] = True
    else:
        question_placeholder.markdown("<p class='question'>谁是世界上最美的女人？</p>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # **✨ 按钮逻辑分离**
    button_placeholder = st.empty()
    if button_placeholder.button("✨ 点我筛选 ✨"):
        button_placeholder.empty()  # **清除按钮**
        show_thinking_process()

    st.markdown(f"<div class='version'>版本：v{VERSION}</div>", unsafe_allow_html=True)

def show_thinking_process():
    placeholder = st.empty()
    placeholder.markdown("<p class='thinking'>🔍 正在筛选...</p>", unsafe_allow_html=True)
    time.sleep(0.5)

    start_number = random.uniform(100000.123, 500000.456)
    end_number = random.uniform(3000000000.789, 4000000000.987)
    step = (end_number - start_number) / 10

    for i in range(10):
        current_number = start_number + (step * i)
        placeholder.markdown(
            f"<p class='thinking'>🔍 正在筛选，分析了 {current_number:,.3f} 个女人...</p>",
            unsafe_allow_html=True
        )
        time.sleep(0.8)

    placeholder.success("✅ 筛选完成！答案即将揭晓...")
    time.sleep(2)

    # **🔥 清屏逻辑**
    st.session_state.clear()
    placeholder.empty()
    time.sleep(1)
    show_final_result()

def show_final_result():
    answer_placeholder = st.empty()
    type_text(answer_placeholder, "王喆", 0.6, css_class="final-answer")

# **🔥 运行程序**
if __name__ == "__main__":
    show_intro()