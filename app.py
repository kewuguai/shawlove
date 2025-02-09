import streamlit as st
import time
import random

VERSION = "2.1.37"

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

# **🔥 全球前100位最美女性的名字（+王喆，共101个名字）**
NAME_POOL = [
    "Scarlett Johansson", "Angelina Jolie", "Gal Gadot", "Emma Watson", "Margot Robbie",
    "Taylor Swift", "Ariana Grande", "Beyoncé", "Natalie Portman", "Charlize Theron",
    "Anne Hathaway", "Jessica Alba", "Mila Kunis", "Selena Gomez", "Rihanna",
    "Zendaya", "Emma Stone", "Gigi Hadid", "Bella Hadid", "Dua Lipa",
    "Jennifer Lawrence", "Keira Knightley", "Blake Lively", "Shakira", "Priyanka Chopra",
    "Deepika Padukone", "Fan Bingbing", "Liu Yifei", "Dilraba Dilmurat", "Zhao Liying",
    "Tang Wei", "Lee Sung Kyung", "Kim Ji-won", "IU", "Suzy Bae",
    "Song Hye-kyo", "Jun Ji-hyun", "Park Shin-hye", "Lisa (BLACKPINK)", "Jennie (BLACKPINK)",
    "Jisoo (BLACKPINK)", "Rosé (BLACKPINK)", "Amber Heard", "Sophie Turner", "Emilia Clarke",
    "Rachel McAdams", "Monica Bellucci", "Gisele Bündchen", "Adriana Lima", "Miranda Kerr",
    "Barbara Palvin", "Irina Shayk", "Cara Delevingne", "Lily Collins", "Amanda Seyfried",
    "Meghan Markle", "Kate Middleton", "Keisha Castle-Hughes", "Olivia Wilde", "Lupita Nyong'o",
    "Rosario Dawson", "Vanessa Hudgens", "Eva Mendes", "Jessica Biel", "Kristen Stewart",
    "Halle Berry", "Megan Fox", "Lucy Liu", "Zhang Ziyi", "Gong Li",
    "Sun Li", "Crystal Liu", "Angelababy", "Dilireba", "Zhou Dongyu",
    "Brie Larson", "Florence Pugh", "Saoirse Ronan", "Dakota Johnson", "Elle Fanning",
    "Camila Cabello", "Hailee Steinfeld", "Lana Del Rey", "Madison Beer", "Billie Eilish",
    "Sydney Sweeney", "Alexandra Daddario", "Anya Taylor-Joy", "Zoey Deutch", "Margaret Qualley",
    "Hunter Schafer", "Lily-Rose Depp", "Josephine Langford", "Yara Shahidi", "Jenna Ortega",
    "Willa Holland", "Chloe Grace Moretz", "Bailee Madison", "Kaitlyn Dever", "Isabela Merced",
    "王喆"
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

    # **🔥 数字筛选过程**
    start_number = random.randint(100000, 500000)
    end_number = random.randint(1000000000, 4000000000)  # 最高 40 亿
    step = (end_number - start_number) // 10

    for i in range(10):
        current_number = start_number + (step * i)
        placeholder.markdown(
            f"<p class='thinking'>🔍 系统正在筛选，已经分析了 {current_number:,} 个女人...</p>",
            unsafe_allow_html=True
        )
        time.sleep(0.8)

    placeholder.success("✅ 筛选完成！答案即将揭晓...")
    time.sleep(2)

    # **🔥 清除所有多余的框**
    placeholder.empty()

    # **🔥 进入名字筛选**
    show_name_selection()

def show_name_selection():
    name_placeholder = st.empty()

    # **🔥 前 90 次完全随机**
    for _ in range(90):
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
    time.sleep(2)

    # **🔥 进入最终展示**
    show_final_result(name_placeholder)

def show_final_result(name_placeholder):
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🔄 重新筛选"):
        name_placeholder.empty()
        st.experimental_rerun()

# **🔥 运行程序**
if __name__ == "__main__":
    show_intro()