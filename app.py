import streamlit as st
import time
import random

# **🔹 设置网页标题**
st.set_page_config(page_title="问答演示", layout="centered")

# **🔹 自定义 CSS**
CUSTOM_STYLE = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');
    body {
        text-align: center;
        margin: 0 auto;
    }
    .question {
        font-family: 'Lobster', cursive;
        font-size: 72px; /* 🚀 放大问题字体 */
        text-align: center;
        color: black;
        margin-bottom: 20px;
    }
    .thinking {
        font-size: 24px; /* 📌 适中 */
        text-align: center;
        color: black;
        margin-top: 10px;
    }
    .pretty-text {
        font-family: 'Lobster', cursive;
        font-size: 300px; /* 🚀 让“王喆”足够大 */
        color: red;
        text-align: center;
        margin: 50px auto;
        line-height: 1.2;
    }
    .button-container {
        text-align: center;
        margin-top: 30px;
    }
    .btn-style {
        font-size: 28px; /* 🚀 优化按钮大小 */
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

# **🔹 逐字显示问题（用 `st.empty()` 动态更新字体）**
def show_intro():
    st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)

    # **逐字显示问题**
    question_text = "谁是世界上最美的女人啊？"
    question_placeholder = st.empty()

    if "question_displayed" not in st.session_state:
        st.session_state.question_displayed = False

    if not st.session_state.question_displayed:
        displayed_text = ""
        for char in question_text:
            displayed_text += char
            question_placeholder.markdown(
                f"<p class='question'>{displayed_text}</p>",
                unsafe_allow_html=True
            )
            time.sleep(0.2)  # **逐字动画**
        st.session_state.question_displayed = True
    else:
        question_placeholder.markdown(
            f"<p class='question'>{question_text}</p>",
            unsafe_allow_html=True
        )

    # **🔹 居中显示按钮**
    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ 点我告诉你 ✨", key="reveal_button"):
            time.sleep(1)  # **按钮点击后短暂停顿**
            show_thinking_process()  # 进入下一个步骤

# **🔹 进入“手机正在思考中”阶段**
def show_thinking_process():
    # **🔍 手机思考：数字从小到大增长**
    placeholder = st.empty()
    start_number = random.randint(100000, 500000)
    end_number = random.randint(3000000000, 4000000000)
    step = (end_number - start_number) // 10

    for i in range(10):
        current_number = start_number + (step * i)
        placeholder.markdown(
            f"<p class='thinking'>🔍 手机正在思考中，分析了 {current_number:,} 个女人...</p>",
            unsafe_allow_html=True
        )
        time.sleep(0.8)

    placeholder.success("✅ 筛选完成！答案即将揭晓...")
    time.sleep(2)
    show_final_result()

# **🔹 显示最终答案**
def show_final_result():
    answer = "王喆"
    st.markdown(
        f"<p class='pretty-text'>{answer}</p>",
        unsafe_allow_html=True
    )

# **🔘 启动页面**
show_intro()