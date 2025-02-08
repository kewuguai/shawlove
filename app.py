import os
import streamlit as st
import time
import random

# **🔹 版本号（手动更新）**
VERSION = "1.0.2"

# **🔹 自动拉取 GitHub 最新代码**
os.system("git pull origin main")

# **🔹 禁用 Streamlit 缓存，确保显示最新数据**
st.cache_data.clear()
st.cache_resource.clear()

# **🔹 设置网页标题**
st.set_page_config(page_title=f"问答演示 - v{VERSION}", layout="centered")

# **🔹 自定义 CSS + JavaScript 逐字动画**
CUSTOM_STYLE = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');

    /* 🔹 版本号样式（放在问题的左上角） */
    .version {
        font-family: Arial, sans-serif;
        font-size: 18px;
        color: grey;
        position: absolute;
        top: 10px;
        left: 10px;
    }

    /* 🔹 确保字体提前放大 */
    .question-container {
        position: relative;
        text-align: center;
        margin-top: 50px;
    }

    .question {
        font-family: 'Lobster', cursive;
        font-size: 80px; /* 🚀 大字体 */
        text-align: center;
        font-weight: bold;
        color: black;
        white-space: nowrap;
        overflow: hidden;
    }
    .thinking {
        font-size: 24px;
        text-align: center;
        color: black;
    }
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
        document.getElementById(elementId).innerHTML = "";  // 清空内容
        type();
    }
    </script>
"""

# **🔹 显示问题逐字动画**
def show_intro():
    st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)

    # **HTML 渲染问题文本，并在左上角显示版本号**
    question_text = "谁是世界上最美的女人？"
    html_content = f"""
        <div class="question-container">
            <div class="version">版本：v{VERSION}</div>  <!-- 版本号放置在左上角 -->
            <div class="question" id="question"></div>
            <script>typeText('question', "{question_text}", 200);</script>
        </div>
    """
    st.components.v1.html(html_content, height=150)

    # **按钮**
    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ 点我告诉你 ✨"):
            show_thinking_process()

# **🔹 显示“手机正在思考中”动画**
def show_thinking_process():
    placeholder = st.empty()

    # **随机浮点数变化**
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

# **🔹 显示最终答案**
def show_final_result():
    answer = "王喆"
    html_content = f"""
        <div class="question-container">
            <div class="final-answer" id="answer"></div>
            <script>typeText('answer', "{answer}", 500);</script>
        </div>
    """
    st.components.v1.html(html_content, height=200)

# **🔘 启动页面**
show_intro()