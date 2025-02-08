import streamlit as st
import time
import random

VERSION = "2.1.28"

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

    .thinking {
        font-family: 'Pacifico', cursive;
        font-size: 20px;
        text-align: center;
        color: black;
    }

    .final-answer {
        font-family: 'Pacifico', cursive;
        font-size: 140px;
        text-align: center;
        color: red;
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

def reset_ui():
    """彻底清空 UI，确保页面完全刷新"""
    st.session_state.clear()
    st.markdown(" ")  # **强制清空 UI**
    time.sleep(0.5)  # **确保 UI 彻底刷新**
    st.session_state["animation_ready"] = False  # **阻止问题动画立即执行**
    st.experimental_rerun()

def show_intro():
    st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)

    # **🔥 重新筛选时先彻底清空 UI**
    if "reset_triggered" in st.session_state:
        del st.session_state["reset_triggered"]
        reset_ui()
        return  # **防止 UI 继续渲染**

    question_placeholder = st.empty()

    # **🔥 渲染问题，不重复动画**
    if "animation_ready" in st.session_state and st.session_state["animation_ready"]:
        if "question_displayed" not in st.session_state:
            type_text(question_placeholder, "谁是世界上最美的女人？", 0.5)  # **问题显示速度变慢**
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

    # **🔥 修正数字范围，确保符合全球女性数量（约40亿）**
    start_number = random.uniform(100000.123, 500000.456)
    end_number = random.uniform(1000000000.789, 4000000000.987)  # 上限设为 40 亿
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

    # **🔥 重新筛选**
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🔄 重新筛选"):
        st.session_state["reset_triggered"] = True  # **标记 UI 需要彻底清空**
        st.session_state["animation_ready"] = False  # **阻止问题动画提前出现**
        st.experimental_rerun()  # **刷新页面**

# **🔥 运行程序**
if __name__ == "__main__":
    show_intro()