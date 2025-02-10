import streamlit as st
import time
import random

VERSION = "1.0.7"  # 更新版本号

st.set_page_config(page_title=f"问答演示 - v{VERSION}", layout="centered")

# **🔥 更新样式**
CUSTOM_STYLE = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=ZCOOL+XiaoWei&family=FangSong&display=swap');

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
        font-family: 'ZCOOL XiaoWei', serif;
        font-size: 60px;
        text-align: center;
        color: red;
    }

    .answer-box {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 150px;
        width: 600px;
        border-radius: 15px;
        margin: 20px auto;
        font-size: 60px;
        font-weight: bold;
        text-align: center;
        transition: all 0.5s ease-in-out;
        background: linear-gradient(45deg, #ff9a9e, #fad0c4);
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
        font-family: 'FangSong', serif;
        animation: fadeInOut 1s infinite alternate;
    }

    @keyframes fadeInOut {
        from { opacity: 0.6; }
        to { opacity: 1; }
    }

    .random-name {
        color: #FF6F61;
    }

    .final-answer {
        font-size: 80px;
        color: red;
        font-weight: bold;
        text-shadow: 0px 0px 20px rgba(255, 0, 0, 0.8);
        animation: flashEffect 1.5s ease-in-out 3;
    }

    @keyframes flashEffect {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.2); opacity: 0.5; }
        100% { transform: scale(1); opacity: 1; }
    }

    .thinking {
        font-size: 30px;
        color: #333;
        text-align: center;
        font-weight: bold;
        width: 800px; /* 🔥 增加宽度，确保内容完整 */
        margin: auto;
    }
    </style>
"""

st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)

NAME_POOL = [
    "奥黛丽·赫本", "玛丽莲·梦露", "索菲娅·罗兰", "莫妮卡·贝鲁奇", "巩俐", "梅艳芳", "张曼玉", "林青霞", "王祖贤", "钟楚红",
    "李嘉欣", "邱淑贞", "朱茵", "舒淇", "范冰冰", "章子怡", "杨幂", "刘亦菲", "高圆圆", "林志玲",
    "迪丽热巴", "古力娜扎", "唐嫣", "赵丽颖", "孙俪", "李沁", "杨紫", "景甜", "周冬雨", "倪妮",
    "刘诗诗", "张钧甯", "宋祖儿", "关晓彤", "鞠婧祎", "欧阳娜娜", "秦岚", "佟丽娅", "张柏芝", "郭碧婷"
]

TARGET_NAME = "王喆"

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
    if button_placeholder.button("✨ 点我筛选 ✨", key="start_button"):
        button_placeholder.empty()
        show_thinking_process()

def show_thinking_process():
    placeholder = st.empty()
    placeholder.markdown("<p class='thinking'>🔍 系统正在筛选...</p>", unsafe_allow_html=True)
    time.sleep(0.5)

    current_number = 1
    max_number = 3_922_276_273  
    for _ in range(10):
        increment = random.randint(max_number // 100, max_number // 10)
        current_number = min(current_number + increment, max_number)
        placeholder.markdown(f"<p class='thinking'>🔍 系统正在筛选，已经分析了 {current_number:,} 个女人...</p>", unsafe_allow_html=True)
        time.sleep(0.5)

    placeholder.success("✅ 筛选完成！将从全球一百位最美丽女人中揭晓答案！")
    time.sleep(2)
    placeholder.empty()
    show_name_selection()

def show_name_selection():
    name_placeholder = st.empty()

    for _ in range(90):
        random_name = random.choice(NAME_POOL)
        name_placeholder.markdown(f"<p class='answer-box random-name'>{random_name}</p>", unsafe_allow_html=True)
        time.sleep(0.05)

    delay = 0.1
    for _ in range(10):
        name_placeholder.markdown(f"<p class='answer-box random-name'>{random.choice(NAME_POOL)}</p>", unsafe_allow_html=True)
        time.sleep(delay)
        delay += 0.02

    name_placeholder.markdown(f"<p class='answer-box final-answer'>即将揭晓...</p>", unsafe_allow_html=True)
    time.sleep(1.5)
    name_placeholder.markdown(f"<p class='answer-box final-answer'>{TARGET_NAME}</p>", unsafe_allow_html=True)

    if st.button("🔄 重新筛选", key="reset_button"):
        st.session_state.clear()
        st.experimental_rerun()

if __name__ == "__main__":
    show_intro()