import streamlit as st
import time
import random

# **🔹 设置网页标题**
st.set_page_config(page_title="问答演示", layout="centered")

# **🔹 自定义 CSS，精准适配 iPhone 16 Max**
CUSTOM_STYLE = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');
    
    /* 🔹 适配 iPhone 16 Max */
    .pretty-text {
        font-family: 'Lobster', cursive;
        font-size: 220px;  /* 🚀 “王喆” 绝对醒目 */
        color: red;
        text-align: center;
        font-weight: bold;
        line-height: 1.2;
    }
    .question {
        font-size: 72px;  /* 🚀 “谁是世界上最美的女人啊？” */
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .thinking {
        font-size: 22px; /* 📌 适中，避免过大 */
        text-align: center;
        margin-top: 10px;
    }
    .button-container {
        text-align: center; /* ✅ 确保按钮居中 */
        margin-top: 20px;
    }
    .btn-style {
        font-size: 24px;  /* 🚀 按钮合适 */
        padding: 10px 24px;
        font-weight: bold;
        border-radius: 8px;
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

# **🔹 逐字显示问题（仅在第一次显示动画）**
def show_intro():
    st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)
    
    # 逐字显示问题
    question_placeholder = st.empty()
    text = "谁是世界上最美的女人啊？"
    displayed_text = ""

    if "question_displayed" not in st.session_state:
        st.session_state.question_displayed = False

    # **只在页面首次加载时显示动画**
    if not st.session_state.question_displayed:
        for char in text:
            displayed_text += char
            question_placeholder.markdown(f"<p class='question'>{displayed_text}</p>", unsafe_allow_html=True)
            time.sleep(0.2)  # 逐字动画
        st.session_state.question_displayed = True
    else:
        question_placeholder.markdown(f"<p class='question'>{text}</p>", unsafe_allow_html=True)

    # **🔹 居中显示按钮**
    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])  # 确保按钮绝对居中
    with col2:
        if st.button("✨ 点我告诉你 ✨", key="reveal_button"):
            time.sleep(1)  # **按钮点击后短暂停顿**
            show_thinking_process()  # 进入下一个步骤
    st.markdown("</div>", unsafe_allow_html=True)

# **🔹 进入“手机正在思考中”阶段**
def show_thinking_process():
    # **🔍 手机思考：数字从小到大增长**
    placeholder = st.empty()
    start_number = random.randint(100000, 500000)
    end_number = random.randint(3000000000, 4000000000)
    step = (end_number - start_number) // 10  # 每步增加数值
    
    for i in range(10):
        current_number = start_number + (step * i)
        placeholder.markdown(
            f"<p class='thinking'>🔍 手机正在思考中，分析了 {current_number:,} 个女人...</p>",
            unsafe_allow_html=True
        )
        time.sleep(0.8)  # **调整节奏**

    placeholder.success("✅ 筛选完成！答案即将揭晓...")
    time.sleep(2)  # **增强 suspense 效果**

    # **🔹 进入最终结果**
    show_final_result()

# **🔹 显示最终答案**
def show_final_result():
    answer = "王喆"
    answer_placeholder = st.empty()
    revealed_text = ""

    for char in answer:
        revealed_text += char
        answer_placeholder.markdown(
            CUSTOM_STYLE + f"<p class='pretty-text'>{revealed_text}</p>",
            unsafe_allow_html=True
        )
        time.sleep(1)  # **逐字慢速出现**

# **🔘 启动页面**
show_intro()