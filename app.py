import streamlit as st
import time
import random

VERSION = "2.1.31"

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

    .final-answer {
        font-size: 60px;
        color: red;
        font-weight: bold;
    }
    </style>
"""

# **🔥 名字筛选逻辑**
NAME_POOL = [
    "李伟", "张晨", "赵磊", "陈思", "吴敏", "刘翔", "杨阳", "何婷", "孙超", "冯涛",
    "高峰", "郭雪", "王强", "林杰", "董辉", "马艳", "韩磊", "罗静", "郑凯", "范敏",
    "胡杰", "曹伟", "谭明", "宋婷", "王喆"
]
TARGET_NAME = "王喆"

def type_text(placeholder, text, speed=0.3, css_class="question"):
    output = ""
    for char in text:
        output += char
        placeholder.markdown(f"<p class='{css_class}'>{output}</p>", unsafe_allow_html=True)
        time.sleep(speed)

def show_intro():
    st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)

    question_placeholder = st.empty()
    if "question_displayed" not in st.session_state:
        type_text(question_placeholder, "谁是世界上最美的女人？", 0.5, css_class="question")
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
    placeholder.markdown("<p class='thinking'>🔍 正在筛选...</p>", unsafe_allow_html=True)
    time.sleep(0.5)

    # **🔥 数字筛选过程**
    start_number = random.uniform(100000.123, 500000.456)
    end_number = random.uniform(1000000000.789, 4000000000.987)  # 最高 40 亿
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

    # **🔥 进入答案筛选**
    show_name_selection()

def show_name_selection():
    name_placeholder = st.empty()

    # **🔥 创建文本框**
    name_box = st.markdown("<div class='answer-box'>", unsafe_allow_html=True)

    # **🔥 前 40 次完全随机**
    for _ in range(40):
        random_name = random.choice(NAME_POOL)
        name_placeholder.markdown(f"<p class='answer-box'>{random_name}</p>", unsafe_allow_html=True)
        time.sleep(0.1)

    # **🔥 后 10 次逐步接近王喆**
    for _ in range(10):
        random_name = random.choice(NAME_POOL[:-1])  # 逐步减少随机性
        name_placeholder.markdown(f"<p class='answer-box'>{random_name}</p>", unsafe_allow_html=True)
        time.sleep(0.15)

    # **🔥 最终确定“王喆”**
    name_placeholder.markdown(f"<p class='answer-box final-answer'>{TARGET_NAME}</p>", unsafe_allow_html=True)
    time.sleep(2)  # **短暂停留**

    # **🔥 清除空白对话框**
    name_box.empty()
    name_placeholder.empty()

    # **🔥 进入最终展示**
    show_final_result()

def show_final_result():
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🔄 重新筛选"):
        st.experimental_rerun()  # **刷新页面，清空 UI**

# **🔥 运行程序**
if __name__ == "__main__":
    show_intro()