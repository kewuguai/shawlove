import streamlit as st
import time
import random

VERSION = "2.1.39"

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

# **🔥 全球前100位最美女性的名字（+王喆，共101个名字）**
NAME_POOL = [
    "范冰冰", "章子怡", "杨幂", "刘亦菲", "高圆圆", "林志玲", "迪丽热巴", "古力娜扎", "唐嫣", "赵丽颖",
    "孙俪", "李沁", "杨紫", "景甜", "周冬雨", "倪妮", "刘诗诗", "张钧甯", "宋祖儿", "关晓彤",
    "鞠婧祎", "欧阳娜娜", "王祖贤", "邱淑贞", "张曼玉", "李嘉欣", "钟楚红", "林青霞", "朱茵", "袁泉",
    "秦岚", "佟丽娅", "张柏芝", "舒淇", "郭碧婷", "刘涛", "李小冉", "蒋勤勤", "王鸥", "殷桃",
    "马思纯", "宋茜", "张天爱", "蓝盈莹", "张馨予", "霍思燕", "李若彤", "赵雅芝", "蔡卓妍", "杨千嬅",
    "陈法拉", "吴千语", "阿娇", "邓紫棋", "薛凯琪", "徐若瑄", "林依晨", "杨丞琳", "桂纶镁", "陈乔恩",
    "蔡依林", "江疏影", "张雨绮", "董洁", "汤唯", "张慧雯", "谭松韵", "毛晓彤", "林允", "宋轶",
    "吴倩", "王丽坤", "张嘉倪", "白百何", "陈都灵", "孙允珠", "石原里美", "新垣结衣", "桥本环奈", "苍井优",
    "长泽雅美", "深田恭子", "有村架纯", "吉冈里帆", "户田惠梨香", "泽尻英龙华", "上户彩", "绫濑遥", "北川景子", "佐佐木希",
    "堀北真希", "藤井莉娜", "松岛菜菜子", "板野友美", "南笙", "盛朗熙", "陈燃", "于文文", "张予曦", "王喆"
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
    placeholder.markdown("<p class='thinking'>🔍 系统正在筛选...</p>", unsafe_allow_html=True)
    time.sleep(0.5)

    start_number = random.randint(100000, 500000)
    end_number = random.randint(1000000000, 4000000000)
    step = (end_number - start_number) // 10

    for i in range(10):
        current_number = start_number + (step * i)
        placeholder.markdown(f"<p class='thinking'>🔍 系统正在筛选，已经分析了 {current_number:,} 个女人...</p>", unsafe_allow_html=True)
        time.sleep(0.8)

    placeholder.success("✅ 筛选完成！将从全球一百位最美丽女人中揭晓答案！")
    time.sleep(2)
    placeholder.empty()
    show_name_selection()

def show_name_selection():
    name_placeholder = st.empty()

    for _ in range(90):
        random_name = random.choice([name for name in NAME_POOL if name != TARGET_NAME])
        name_placeholder.markdown(f"<p class='answer-box random-name'>{random_name}</p>", unsafe_allow_html=True)
        time.sleep(0.1)

    for _ in range(10):
        name_placeholder.markdown(f"<p class='answer-box random-name'>{random.choice(NAME_POOL)}</p>", unsafe_allow_html=True)
        time.sleep(0.15)

    name_placeholder.markdown(f"<p class='answer-box final-answer'>{TARGET_NAME}</p>", unsafe_allow_html=True)
    time.sleep(2)
    show_final_result(name_placeholder)