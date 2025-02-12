import streamlit as st
import time
import random

VERSION = "1.3.1"  # 调整手机端适配

st.set_page_config(page_title=f"问答演示 - v{VERSION}", layout="centered")

# **🔥 更新样式**
CUSTOM_STYLE = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=ZCOOL+XiaoWei&family=FangSong&display=swap');

    /* ============================== 版本号样式 ============================== */
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

    /* ============================== 提出问题部分 ============================== */
    .question-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 100%;
        text-align: center;
        min-width: 350px;
    }

    .question {
        font-family: 'ZCOOL XiaoWei', serif;
        font-size: 40px;
        text-align: center;
        color: red;
        white-space: nowrap; /* 强制单行显示 */
    }

    @media (max-width: 768px) {
        .question { font-size: 30px !important; } /* 手机端字体调整 */
    }

    /* ============================== 数字筛选部分 ============================== */
    .thinking-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 100%;
        text-align: center;
    }

    .thinking {
        font-size: 30px;
        color: #333;
        text-align: center;
        font-weight: bold;
        width: 90%;
        max-width: 600px;
        margin: auto;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }

    @media (max-width: 768px) {
        .thinking { font-size: 20px !important; } /* 手机端字体调整 */
    }

    /* ============================== 筛选完成部分 ============================== */
    .final-message-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 100%;
        text-align: center;
    }

    .final-message {
        font-size: 30px;
        color: green;
        text-align: center;
        font-weight: bold;
    }

    @media (max-width: 768px) {
        .final-message { font-size: 25px !important; color: green !important; } /* 手机端字体调整 */
    }

    /* ============================== 人名筛选部分 ============================== */
.name-selection-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    text-align: center;
}

.name-selection {
    font-size: 60px; /* 增加字体大小 */
    color: #f28d8d; /* 调整为较深的红色 */
    text-align: center;
    font-weight: bold;
}

@media (max-width: 768px) {
    .name-selection {
        font-size: 40px !important; /* 手机端字体调整 */
    }
}

    /* ============================== 即将揭晓部分 ============================== */
    .coming-soon {
        font-size: 100px;
        color: gold;
        font-weight: bold;
        text-shadow: 0px 0px 20px rgba(255, 215, 0, 0.8);
        transition: opacity 0.5s ease-in-out;
        text-align: center;
    }

    @media (max-width: 768px) {
        .coming-soon { font-size: 80px !important; } /* 手机端字体调整 */
    }

    /* ============================== 倒计时部分 ============================== */
    .countdown {
        font-size: 150px;
        color: gold;
        font-weight: bold;
        text-shadow: 0px 0px 20px rgba(255, 215, 0, 0.8);
        display: flex;
        align-items: center;
        justify-content: center;
        transition: opacity 0.5s ease-in-out;
        text-align: center;
    }

    @media (max-width: 768px) {
        .countdown { font-size: 200px !important; } /* 手机端倒计时字体调整 */
    }

    /* ============================== 最终答案部分 ============================== */
.final-answer {
    font-size: 200px;
    color: gold;
    font-weight: bold;
    text-shadow: 0px 0px 20px rgba(255, 215, 0, 0.8);
    min-height: 150px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: opacity 0.5s ease-in-out;
    text-align: center;
    background: transparent;
}

@media (max-width: 768px) {
    .final-answer { font-size: 80px !important; } /* 手机端最终答案字体调整 */
}

/* ============================== 淡入/淡出效果 ============================== */
.show {
        opacity: 1 !important;
}

.hide {
        opacity: 0 !important;
}

</style>
"""

st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)

# **✅ 人名列表**
NAME_POOL = [
    "奥黛丽·赫本", "玛丽莲·梦露", "索菲娅·罗兰", "莫妮卡·贝鲁奇", "巩俐", "梅艳芳", "张曼玉", "林青霞", "王祖贤", "钟楚红",
    "李嘉欣", "邱淑贞", "朱茵", "舒淇", "范冰冰", "章子怡", "杨幂", "刘亦菲", "高圆圆", "林志玲",
    "迪丽热巴", "古力娜扎", "唐嫣", "赵丽颖", "孙俪", "李沁", "杨紫", "景甜", "周冬雨", "倪妮",
    "刘诗诗", "张钧甯", "宋祖儿", "关晓彤", "鞠婧祎", "欧阳娜娜", "秦岚", "佟丽娅", "张柏芝", "郭碧婷",
    "赵雅芝", "李若彤", "蔡卓妍", "杨千嬅", "徐若瑄", "林依晨", "杨丞琳", "桂纶镁", "蔡依林", "汤唯",
    "石原里美", "新垣结衣", "桥本环奈", "苍井优", "长泽雅美", "深田恭子", "有村架纯", "户田惠梨香", "绫濑遥", "北川景子",
    "安德莉雅·布利兰提斯", "金智秀", "全昭弥", "周子瑜", "艾玛·沃特森", "斯嘉丽·约翰逊", "玛格特·罗比", "安雅·泰勒-乔伊", "娜塔莉·波特曼", "盖尔·加朵",
    "詹妮弗·劳伦斯", "安妮·海瑟薇", "查理兹·塞隆", "安吉丽娜·朱莉", "伊丽莎白·赫莉", "凯特·温丝莱特", "妮可·基德曼", "朱莉娅·罗伯茨", "卡梅隆·迪亚兹", "哈莉·贝瑞",
    "赛琳娜·戈麦斯", "泰勒·斯威夫特", "碧昂丝", "蕾哈娜", "艾薇儿·拉维尼", "詹妮弗·洛佩兹", "比莉·艾利什", "杜阿·利帕", "吉吉·哈迪德", "贝拉·哈迪德",
    "肯达尔·詹娜", "米兰达·可儿", "亚历山德拉·安布罗休", "阿德瑞娜·利玛", "坎蒂丝·斯瓦内普尔", "泰勒·希尔", "莉莉·奥尔德里奇", "芭芭拉·帕尔文", "莫妮卡·鲁伊兹", 
    "秀兰·邓波儿", "刘嘉玲", "费雯·丽"
]

TARGET_NAME = "王喆"

def type_text(placeholder, text, speed=0.2, css_class="question"):
    output = ""
    for char in text:
        output += char
        placeholder.markdown(f"<p class='{css_class}'>{output}</p>", unsafe_allow_html=True)
        time.sleep(speed)

def show_question():
    question_placeholder_1 = st.empty()
    question_placeholder_2 = st.empty()

    if "question_displayed" not in st.session_state:
        type_text(question_placeholder_1, "谁是这个世界上", 0.2, css_class="question")
        time.sleep(0.5)
        type_text(question_placeholder_2, "最聪明最美丽的女人？", 0.2, css_class="question")
        st.session_state["question_displayed"] = True
    else:
        question_placeholder_1.markdown("<p class='question'>谁是这个世界上</p>", unsafe_allow_html=True)
        question_placeholder_2.markdown("<p class='question'>最聪明最美丽的女人？</p>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    button_placeholder = st.empty()
    if button_placeholder.button("✨ 点击筛选 ✨", key="start_button"):
        button_placeholder.empty()
        show_thinking_process()

    st.markdown(f"<div class='version'>版本：v{VERSION}</div>", unsafe_allow_html=True)

def show_thinking_process():
    thinking_placeholder = st.empty()

    thinking_placeholder.markdown("""
    <div class="thinking-container">
        <p class="thinking">正在全球女性数据库中筛选…</p>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(1)

    current_number = 1
    max_number = 3_922_276_273
    for _ in range(10):
        increment = random.randint(max_number // 100, max_number // 10)
        current_number = min(current_number + increment, max_number)
        thinking_placeholder.markdown(f"""
        <div class="thinking-container">
            <p class="thinking">正在全球女性数据库中筛选…</p>
            <p class="thinking">已经分析了 {current_number:,} 个女人…</p>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1)

    thinking_placeholder.empty()
    show_final_message()

def show_final_message():
    final_message_placeholder = st.empty()
    final_message_placeholder.markdown("""
    <div class="final-message-container">
        <p class="final-message">✅ 系统筛选完成！</p>
        <p class="final-message">将从全球前100名中选出最终人选！</p>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(3)
    final_message_placeholder.empty()

    show_name_selection()

def show_name_selection():
    # 使用一个占位符确保所有内容在同一位置显示
    placeholder = st.empty()
    displayed_names = set()

    # 随机显示前90个名字
    for _ in range(90):
        random_name = random.choice([name for name in NAME_POOL if name not in displayed_names])
        displayed_names.add(random_name)
        placeholder.markdown(f"<p class='name-selection'>{random_name}</p>", unsafe_allow_html=True)
        time.sleep(0.10)

    # 随后逐渐放慢速度，最后10个名字
    delay = 0.1
    for _ in range(10):
        placeholder.markdown(f"<p class='name-selection'>{random.choice(NAME_POOL)}</p>", unsafe_allow_html=True)
        time.sleep(delay)
        delay += 0.02

    # 显示“即将揭晓...”文本
    placeholder.markdown("""
    <p class='name-selection' id="final-text">即将揭晓...</p>
    """, unsafe_allow_html=True)
    time.sleep(1.5)

    # 淡出“即将揭晓...”文本，确保它消失
    placeholder.markdown("""
    <p class='name-selection hide' id="final-text">即将揭晓...</p>
    """, unsafe_allow_html=True)
    time.sleep(0.5)

    show_countdown(placeholder)  # 传递占位符到倒计时

def show_countdown(placeholder):
    # 显示倒计时
    countdown_text = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]

    for text in countdown_text:
        placeholder.markdown(f"""
        <p class='answer-box countdown show' id="final-text">{text}</p>
        """, unsafe_allow_html=True)
        time.sleep(1)

        # 让文本框消失再显示
        placeholder.markdown(f"""
        <p class='answer-box countdown hide' id="final-text">{text}</p>
        """, unsafe_allow_html=True)
        time.sleep(0.5)

    show_final_answer(placeholder)

def show_final_answer(placeholder):
    # 显示最终答案“王喆 👑”
    placeholder.markdown("""
    <p class='answer-box final-answer' id="final-answer">
       👑 王喆 👑
    </p>
    """, unsafe_allow_html=True)
    time.sleep(3)

    # 显示“重新筛选”按钮
    st.markdown("<br><br>", unsafe_allow_html=True)
    reset_button_placeholder = st.empty()
    if reset_button_placeholder.button("🔄 重新筛选", key="reset_button"):
        st.session_state.clear()
        st.rerun()

if __name__ == "__main__":
    show_question()  # 启动页面内容