import streamlit as st
import time
import random

# **🔹 设置网页标题**
st.set_page_config(page_title="问答演示", layout="centered")

# **🔹 自定义 CSS 样式**
CUSTOM_STYLE = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');

    /* 🔹 问题字体样式 */
    .question {
        font-family: 'Lobster', cursive;
        font-size: 72px; /* 🚀 字体放大 */
        text-align: center;
        color: black;
        margin-bottom: 30px;
    }

    /* 🔹 思考文本样式 */
    .thinking {
        font-size: 24px;
        text-align: center;
        color: black;
    }

    /* 🔹 答案字体样式 */
    .pretty-text {
        font-family: 'Lobster', cursive;
        font-size: 100px; /* 🚀 超大字体 */
        color: red;
        text-align: center;
        margin-top: 50px;
    }

    /* 🔹 按钮样式 */
    .button-container {
        text-align: center;
        margin-top: 40px;
    }
    .btn-style {
        font-size: 28px;
        padding: 12px 24px;
        font-weight: bold;
        border-radius: 12px;
        background-color: #ff4b4b;
        color: white;
        border: none;
        cursor: pointer;
    }
    .btn-style:hover {
        background-color: #ff0000;
    }
    </style>
"""

# **🔹 逐字显示问题**
def show_intro():
    st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)

    # 动态逐字显示
    question_text = "谁是世界上最美的女人啊？"
    placeholder = st.empty()

    if "question_displayed" not in st.session_state:
        st.session_state.question_displayed = False

    # **逐字显示内容**
    if not st.session_state.question_displayed:
        displayed_text = ""
        for char in question_text:
            displayed_text += char
            placeholder.markdown(
                f"<p class='question'>{displayed_text}</p>",
                unsafe_allow_html=True
            )
            time.sleep(0.2)  # **逐字动画**
        st.session_state.question_displayed = True
    else:
        placeholder.markdown(
            f"<p class='question'>{question_text}</p>",
            unsafe_allow_html=True
        )

    # **显示按钮**
    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ 点我告诉你 ✨"):
            show_thinking_process()

# **🔹 显示“手机正在思考中”动画**
def show_thinking_process():
    placeholder = st.empty()

    # **随机浮点数变化**
    start_number = random.uniform(100000.123, 500000.456)  # 起始浮点数
    end_number = random.uniform(3000000000.789, 4000000000.987)  # 结束浮点数
    step = (end_number - start_number) / 10  # 每次增加的浮点数

    for i in range(10):
        current_number = start_number + (step * i)
        placeholder.markdown(
            f"<p class='thinking'>🔍 手机正在思考中，分析了 {current_number:,.3f} 个女人...</p>",
            unsafe_allow_html=True
        )
        time.sleep(0.8)  # 延迟0.8秒，模拟计算
    placeholder.success("✅ 筛选完成！答案即将揭晓...")
    time.sleep(2)
    show_final_result()

# **🔹 显示最终答案**
def show_final_result():
    st.markdown("<div class='pretty-text'>王喆</div>", unsafe_allow_html=True)

# **🔘 启动页面**
show_intro()