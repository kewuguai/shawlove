import streamlit as st
import time
import random

VERSION = "1.2.0"  #调整手机页面显示

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
    
    .question-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    text-align: center;
    min-width: 350px; /* ✅ 让文本不会因屏幕过窄而换行 */
}

       .question {
    font-family: 'ZCOOL XiaoWei', serif;
    font-size: 40px;  /* 🔥 字号调整小一点 */
    text-align: center;
    color: red;
    white-space: nowrap; /* 🔥 强制单行显示 */
    }

    /* 🔥 新增：适配手机端字体大小 */
    @media (max-width: 768px) {
        .question { font-size: 40px !important; }
        .answer-box { width: 90% !important; font-size: 40px !important; }
        .final-answer { font-size: 70px !important; }
    }

     /* 🔥 新增：适配手机端答案框居中 */
    @media (max-width: 768px) {
    .answer-box { 
        width: 95% !important; 
        font-size: 40px !important;
        min-height: 150px !important; /* ✅ 确保高度固定，防止位移 */
        display: flex; 
        align-items: center; 
        justify-content: center;
        margin: 0 auto !important; /* ✅ 确保手机端完全居中 */
    }
    .final-answer {
    font-size: 100px;
    color: gold;
    font-weight: bold;
    text-shadow: 0px 0px 20px rgba(255, 215, 0, 0.8);
    min-height: 150px; /* 🔥 ✅ 确保文本框高度固定，防止位移 */
    display: flex;
    align-items: center;
    justify-content: center;
    transition: opacity 0.5s ease-in-out; /* ✅ 让“即将揭晓”过渡消失，不闪烁 */
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
        background-color: white;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
        font-family: 'FangSong', serif;
    }

    .random-name {
        color: #FF6F61;
    }

    .final-answer {
        font-size: 100px;
        color: gold;
        font-weight: bold;
        text-shadow: 0px 0px 20px rgba(255, 215, 0, 0.8);
        animation: glowEffect 1.5s ease-in-out infinite alternate;
    }

    @keyframes glowEffect {
        from { text-shadow: 0px 0px 10px rgba(255, 215, 0, 0.6); }
        to { text-shadow: 0px 0px 30px rgba(255, 0, 0, 1); }
    }

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
    word-wrap: break-word; /* ✅ 确保超长数字在手机端换行 */
    overflow-wrap: break-word; /* ✅ 确保内容不会超出屏幕 */
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

def show_intro():
    question_placeholder_1 = st.empty()
    question_placeholder_2 = st.empty()

    if "question_displayed" not in st.session_state:
        # **✅ 先显示第一行**
        type_text(question_placeholder_1, "谁是这个世界上", 0.2, css_class="question")

        # **✅ 确保第一行静止不动**
        time.sleep(0.5)

        # **✅ 第二行执行动画**
        type_text(question_placeholder_2, "最聪明最美丽的女人？", 0.2, css_class="question")

        st.session_state["question_displayed"] = True
    else:
        # **✅ 直接显示完整问题**
        question_placeholder_1.markdown("<p class='question'>谁是这个世界上</p>", unsafe_allow_html=True)
        question_placeholder_2.markdown("<p class='question'>最聪明最美丽的女人？</p>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    button_placeholder = st.empty()
    if button_placeholder.button("✨ 点我筛选 ✨", key="start_button"):
        button_placeholder.empty()
        show_thinking_process()

    # **✅ 版本号**
    st.markdown(f"<div class='version'>版本：v{VERSION}</div>", unsafe_allow_html=True)  

def show_thinking_process():
    thinking_placeholder = st.empty()
    
    # **✅ 先显示第一行**
    thinking_placeholder.markdown("""
    <div class="thinking-container">
        <p class="thinking">系统正在筛选…</p>
    </div>
    """, unsafe_allow_html=True)
    
    time.sleep(1)
    
    # **✅ 再显示第二行**
    current_number = 1
    max_number = 3_922_276_273
    for _ in range(10):
        increment = random.randint(max_number // 100, max_number // 10)
        current_number = min(current_number + increment, max_number)
        thinking_placeholder.markdown(f"""
        <div class="thinking-container">
            <p class="thinking">系统正在筛选…</p>
            <p class="thinking">已经分析了 {current_number:,} 个女人…</p>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1)
    
    # **✅ 执行完成后清除**
    thinking_placeholder.empty()
    
    # **✅ 显示最终筛选完成提示**
    final_message_placeholder = st.empty()
    final_message_placeholder.markdown("""
    <div class="thinking-container">
        <p class="thinking">✅ 筛选完成！</p>
        <p class="thinking">将从全球前100名中选出最终胜者！</p>
    </div>
    """, unsafe_allow_html=True)
    
    time.sleep(2)  # **🔥 短暂显示后消失**
    
    # **✅ 清除文本**
    final_message_placeholder.empty()

    # **✅ 进入人名筛选**
    show_name_selection()

def show_name_selection():
    name_placeholder = st.empty()
    displayed_names = set()

    # **✅ 先随机显示前 90 个名字**
    for _ in range(90):
        random_name = random.choice([name for name in NAME_POOL if name not in displayed_names])
        displayed_names.add(random_name)
        name_placeholder.markdown(f"<p class='answer-box random-name'>{random_name}</p>", unsafe_allow_html=True)
        time.sleep(0.08)

    # **✅ 逐渐放慢速度，最后 10 个名字**
    delay = 0.1
    for _ in range(10):
        name_placeholder.markdown(f"<p class='answer-box random-name'>{random.choice(NAME_POOL)}</p>", unsafe_allow_html=True)
        time.sleep(delay)
        delay += 0.02  # 逐渐增加延迟，营造悬念

    # **✅ 先显示“即将揭晓...”**
    name_placeholder.markdown("""
<p class='answer-box final-answer' id="final-text">即将揭晓...</p>
""", unsafe_allow_html=True)
    time.sleep(1.5)  # ✅ 修正缩进，确保与上一行对齐

    # **✅ 调用最终答案**
    show_final_result(name_placeholder)  # ✅ 确保所有动画在同一个对话框里

def show_final_result(placeholder):
    # **✅ 先让 “即将揭晓...” 渐隐，防止跳动**
    placeholder.markdown("""
    <p class='answer-box final-answer' id="final-text" style="opacity:1;">即将揭晓...</p>
    """, unsafe_allow_html=True)
    time.sleep(1.5)

    # **✅ 让即将揭晓淡出，而不是直接消失，避免跳动**
    placeholder.markdown("""
    <p class='answer-box final-answer' id="final-text" style="opacity:0;">即将揭晓...</p>
    """, unsafe_allow_html=True)
    time.sleep(0.5)  # ✅ 让透明过渡生效，防止直接替换跳动

    # **✅ 倒计时**
    countdown_text = ["9...", "8...", "7...", "6...", "5...", "4...", "3...", "2...", "1..."]
    for text in countdown_text:
        placeholder.markdown(f"""
        <p class='answer-box final-answer' id="final-text" style="opacity:1;">{text}</p>
        """, unsafe_allow_html=True)
        time.sleep(1)

    # **✅ 让 `王喆 👑` 100% 居中，防止位移**
    placeholder.markdown("""
    <p class='answer-box final-answer' 
       style="background: transparent; opacity: 1; color: gold; font-size: 100px; font-weight: bold; 
              text-shadow: 0px 0px 20px rgba(255, 215, 0, 0.8); min-height: 150px; display: flex; 
              align-items: center; justify-content: center;">
       👑 王喆 👑
    </p>
    """, unsafe_allow_html=True)

    time.sleep(3)  # ✅ 让答案停留 3 秒后再显示按钮

    # ✅ 让按钮始终位于页面底部
    st.markdown("<br><br>", unsafe_allow_html=True)  # 🔥 增加空行，让按钮下移
    reset_button_placeholder = st.empty()

    if reset_button_placeholder.button("🔄 重新筛选", key="reset_button"):
        st.session_state.clear()
        st.rerun()

if __name__ == "__main__":
    show_intro()