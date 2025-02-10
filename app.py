import streamlit as st
import time
import random

VERSION = "2.1.48"

st.set_page_config(page_title=f"问答演示 - v{VERSION}", layout="centered")

# **🔥 更新样式**
CUSTOM_STYLE = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');

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
        font-family: 'Pacifico', cursive;
        font-size: 50px;
        text-align: center;
        color: red;
    }

    .answer-box {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
        width: 300px;
        border-radius: 10px;
        margin: 20px auto;
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        transition: all 0.3s ease-in-out;
        background-color: white;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }

    .random-name {
        color: #FF6F61;  /* 浅红色 */
    }

    .final-answer {
        font-size: 60px;
        color: red;
        font-weight: bold;
    }
    </style>
"""

st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)

def type_text(placeholder, text, speed=0.2, css_class="question"):
    output = ""
    for char in text:
        output += char
        placeholder.markdown(f"<p class='{css_class}'>{output}</p>", unsafe_allow_html=True)
        time.sleep(speed)

def show_intro():
    question_placeholder = st.empty()
    if "question_displayed" not in st.session_state:
        type_text(question_placeholder, "谁是世界上最美的女人？", 0.2, css_class="question")
        st.session_state["question_displayed"] = True
    else:
        question_placeholder.markdown("<p class='question'>谁是世界上最美的女人？</p>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    button_placeholder = st.empty()
    if button_placeholder.button("✨ 点我筛选 ✨"):
        button_placeholder.empty()
        show_thinking_process()

    st.markdown(f"<div class='version'>版本：v{VERSION}</div>", unsafe_allow_html=True)

def show_thinking_process():
    placeholder = st.empty()
    placeholder.markdown("<p class='thinking'>🔍 系统正在筛选...</p>", unsafe_allow_html=True)
    time.sleep(0.5)

    # **🔥 修改数字筛选逻辑（从1递增到3,922,276,273，随机步长）**
    current_number = 1
    max_number = 3_922_276_273  # **最大女性数量**
    
    for i in range(10):
        increment = random.randint(max_number // 100, max_number // 10)  # **随机增量**
        current_number = min(current_number + increment, max_number)  # **确保不超过最大值**
        placeholder.markdown(f"<p class='thinking'>🔍 系统正在筛选，已经分析了 {current_number:,} 个女人...</p>", unsafe_allow_html=True)
        time.sleep(0.8)

    placeholder.success("✅ 筛选完成！将从全球一百位最美丽女人中揭晓答案！")
    time.sleep(2)
    placeholder.empty()
    show_name_selection()

def show_name_selection():
    name_placeholder = st.empty()

    # **🔥 提高前 90 个名字的显示速度**
    for _ in range(90):
        name_placeholder.markdown(f"<p class='answer-box random-name'>{random.randint(1, 100)}. 随机名字</p>", unsafe_allow_html=True)
        time.sleep(0.01)  # **更快切换**

    # **🔥 最后 11 个名字逐渐减速**
    delay = 0.05
    for _ in range(10):
        name_placeholder.markdown(f"<p class='answer-box random-name'>{random.randint(1, 100)}. 随机名字</p>", unsafe_allow_html=True)
        time.sleep(delay)
        delay += 0.02  # **逐步减速**

    name_placeholder.markdown(f"<p class='answer-box final-answer'>即将揭晓...</p>", unsafe_allow_html=True)
    time.sleep(1.5)
    name_placeholder.markdown(f"<p class='answer-box final-answer'>王喆</p>", unsafe_allow_html=True)

    if st.button("🔄 重新筛选"):
        st.session_state.clear()
        st.experimental_rerun()

if __name__ == "__main__":
    show_intro()