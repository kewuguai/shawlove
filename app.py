import streamlit as st
import time
import random

# **🔹 设置网页标题**
st.set_page_config(page_title="问答演示", layout="centered")

# **🔹 直接使用 HTML + CSS + JS 让字体在动画时正确变大**
CUSTOM_STYLE = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');

    /* 🔹 确保字体在动画过程中正确显示 */
    .pretty-text {
        font-family: 'Lobster', cursive;
        font-size: 220px;  /* 🚀 “王喆” 绝对醒目 */
        color: red;
        text-align: center;
        font-weight: bold;
        line-height: 1.2;
    }
    .question {
        font-family: 'Lobster', cursive;
        font-size: 72px;  /* 🚀 “谁是世界上最美的女人啊？” */
        text-align: center;
        font-weight: bold;
        color: black;
    }
    .thinking {
        font-size: 22px;
        text-align: center;
        color: black;
    }
    .button-container {
        text-align: center;
        margin-top: 20px;
    }
    .btn-style {
        font-size: 24px;
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

# **🔹 逐字动画：用 JavaScript 确保字体大小正确**
QUESTION_JS = """
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
        type();
    }
    </script>
"""

# **🔹 逐字显示问题**
def show_intro():
    st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)

    # **逐字显示问题**
    question_text = "谁是世界上最美的女人啊？"
    question_html = f"""
        <p class="question" id="question"></p>
        {QUESTION_JS}
        <script>typeText('question', "{question_text}", 200);</script>
    """
    st.components.v1.html(question_html, height=100)

    # **🔹 居中显示按钮**
    col1, col2, col3 = st.columns([1,2,1])  # 确保按钮绝对居中
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
        thinking_html = f"""
            <p class="thinking">🔍 手机正在思考中，分析了 {current_number:,} 个女人...</p>
        """
        placeholder.markdown(thinking_html, unsafe_allow_html=True)
        time.sleep(0.8)

    placeholder.success("✅ 筛选完成！答案即将揭晓...")
    time.sleep(2)  # **增强 suspense 效果**

    # **🔹 进入最终结果**
    show_final_result()

# **🔹 显示最终答案**
def show_final_result():
    answer = "王喆"
    answer_html = f"""
        <p class="pretty-text" id="answer"></p>
        {QUESTION_JS}
        <script>typeText('answer', "{answer}", 500);</script>
    """
    st.components.v1.html(answer_html, height=200)

# **🔘 启动页面**
show_intro()