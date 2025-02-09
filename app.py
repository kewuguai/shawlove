import streamlit as st
import time
import random

VERSION = "2.1.41"

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

# **🔥 全球前100位最美丽女性名单**
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
    "肯达尔·詹娜", "米兰达·可儿", "亚历山德拉·安布罗休", "阿德瑞娜·利玛", "坎蒂丝·斯瓦内普尔", "泰勒·希尔", "莉莉·奥尔德里奇", "芭芭拉·帕尔文", "莫妮卡·鲁伊兹", "王喆"
]
TARGET_NAME = "王喆"

# **🔥 逐字动画**
def type_text(placeholder, text, speed=0.3, css_class="question"):
    output = ""
    for char in text:
        output += char
        placeholder.markdown(f"<p class='{css_class}'>{output}</p>", unsafe_allow_html=True)
        time.sleep(speed)

def show_intro():
    st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)

    question_placeholder = st.empty()
    type_text(question_placeholder, "谁是世界上最美的女人？", 0.5, css_class="question")

    st.markdown("<br><br>", unsafe_allow_html=True)

    if st.button("✨ 点我筛选 ✨"):
        show_thinking_process()

    st.markdown(f"<div class='version'>版本：v{VERSION}</div>", unsafe_allow_html=True)

def show_thinking_process():
    placeholder = st.empty()
    placeholder.markdown("<p class='thinking'>🔍 系统正在筛选...</p>", unsafe_allow_html=True)
    time.sleep(0.5)

    for i in range(10):
        num = random.randint(100000000, 4000000000)
        placeholder.markdown(f"<p class='thinking'>🔍 系统正在筛选，已经分析了 {num:,} 个女人...</p>", unsafe_allow_html=True)
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

    if st.button("🔄 重新筛选"):
        st.experimental_rerun()

# **🔥 运行程序**
if __name__ == "__main__":
    show_intro()