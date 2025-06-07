import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Угаалгын бизнес танилцуулга",
    page_icon="🌀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    
    .slide-container {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .highlight-box {
        background: linear-gradient(135deg, #f093fb, #f5576c);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        text-align: center;
    }
    
    .feature-card {
        background: linear-gradient(135deg, #84fab0, #8fd3f4);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .special-card {
        background: linear-gradient(135deg, #ff9a9e, #fecfef);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .stat-card {
        background: linear-gradient(135deg, #a8edea, #fed6e3);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
    }
    
    .phase-card {
        background: linear-gradient(135deg, #ffecd2, #fcb69f);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
    }
    
    .call-to-action {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
    }
    
    .image-placeholder {
        background: linear-gradient(135deg, #a8edea, #fed6e3);
        padding: 3rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        font-size: 1.5rem;
        font-weight: bold;
        color: #667eea;
    }
    
    h1, h2, h3 {
        color: #667eea;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("🌀 Навигаци")
slide_options = [
    "🏠 Нүүр хуудас",
    "🎯 Бидний зорилго", 
    "👥 Хамтрагч гэр бүлүүд",
    "💡 Бизнесийн боломж",
    "💰 Санхүүгийн төлөвлөгөө",
    "🚀 Хөгжлийн алсын хараа",
    "🔥 Яагаад одоо?",
    "🤝 Эрмүүн гэрбүлд урилга"
]

selected_slide = st.sidebar.selectbox("Слайд сонгох:", slide_options)

# Slide 1: Title Page
if selected_slide == "🏠 Нүүр хуудас":
    st.markdown("""
    <div class="main-header">
        <h1>🌀 УГААЛГЫН БИЗНЕС</h1>
        <h3>Найз гэр бүлүүдийн хамтарсан бизнес төсөл</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="image-placeholder">
        🌀 WASHING MACHINES
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; font-size: 1.5rem; margin-top: 2rem;">
        <strong>Тэмүүжин • Амраа • Ганбаяр • Эрмүүн</strong>
    </div>
    """, unsafe_allow_html=True)

# Slide 2: Goal
elif selected_slide == "🎯 Бидний зорилго":
    st.markdown("# 🎯 БИДНИЙ ЗОРИЛГО")
    
    st.markdown("""
    <div class="highlight-box">
        <h2>🏙️ Улаанбаатар хотын 21-р хорооноос эхлэн орон даяар угаалгын үйлчилгээний сүлжээ байгуулах</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="image-placeholder">
        🏢 BUSINESS SPACE
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 3rem;">🏢</div>
            <h3>Анхны салбар</h3>
            <p>21-р хороонд эхний угаалгын газар</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 3rem;">🌟</div>
            <h3>Чанартай үйлчилгээ</h3>
            <p>Орчин үеийн тоног төхөөрөмж</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 3rem;">🚀</div>
            <h3>Өргөжүүлэх</h3>
            <p>21 аймагт салбар нээх</p>
        </div>
        """, unsafe_allow_html=True)

# Slide 3: Team
elif selected_slide == "👥 Хамтрагч гэр бүлүүд":
    st.markdown("# 👥 ХАМТРАГЧ ГЭР БҮЛҮҮД")
    
    st.markdown("""
    <div class="image-placeholder">
        🤝 TEAM COLLABORATION
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 3rem;">👨‍👩‍👧‍👦</div>
            <h3>Тэмүүжин гэр бүл</h3>
            <p>Туршлагатай ах дүүгийн мэдлэг</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 3rem;">🔨</div>
            <h3>Ганбаяр гэр бүл</h3>
            <p>Дотоод засал чиглэлээр туслах боломжтой</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 3rem;">🌀</div>
            <h3>Амраа гэр бүл</h3>
            <p>40м² байршил</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="special-card">
            <div style="font-size: 3rem;">⭐</div>
            <h3>Эрмүүн гэр бүл</h3>
            <p><strong>Урилга хүлээж байна!</strong></p>
        </div>
        """, unsafe_allow_html=True)

# Slide 4: Business Opportunity
elif selected_slide == "💡 Бизнесийн боломж":
    st.markdown("# 💡 БИЗНЕСИЙН БОЛОМЖ")
    
    st.markdown("""
    <div class="image-placeholder">
        🌀 PROFESSIONAL LAUNDROMAT
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stat-card">
            <div style="font-size: 2.5rem; font-weight: bold; color: #667eea;">40м²</div>
            <div>Байршилын талбай</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <div style="font-size: 2.5rem; font-weight: bold; color: #667eea;">700K-1M₮</div>
            <div>Өдрийн орлого</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <div style="font-size: 2.5rem; font-weight: bold; color: #667eea;">21</div>
            <div>Дүүрэг/Аймаг</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
        <h3>✅ Бидэнд байгаа давуу тал:</h3>
        <ul style="list-style: none; text-align: left;">
            <li>📍 <strong>Байршил:</strong> Амраагийн эцэг эх 40м² нэмэлт талбайтай</li>
            <li>🎓 <strong>Туршлага:</strong> Тэмүүжингийн ах угаалгын бизнес эхлүүлсэн</li>
            <li>💰 <strong>Орлого:</strong> Өдөрт 700,000-1,000,000₮</li>
            <li>🏆 <strong>Түлхүүр:</strong> Байршил маш чухал!</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Slide 5: Financial Plan
elif selected_slide == "💰 Санхүүгийн төлөвлөгөө":
    st.markdown("# 💰 САНХҮҮГИЙН ТӨЛӨВЛӨГӨӨ")
    
    st.markdown("""
    <div class="highlight-box">
        <h3>6 сарын хуримтлалын төлөвлөгөө</h3>
        <p style="font-size: 1.2rem;">Гэр бүл тус бүр долоо хоногт $1,000</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="image-placeholder">
        💰 INVESTMENT PLAN
    </div>
    """, unsafe_allow_html=True)
    
    # Financial table
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("**Гэр бүл**")
        st.write("Тэмүүжин")
        st.write("Амраа")
        st.write("Ганбаяр")
        st.write("Эрмүүн")
        st.write("**НИЙТ**")
    
    with col2:
        st.markdown("**Долоо хоногт**")
        st.write("$1,000")
        st.write("$1,000")
        st.write("$1,000")
        st.write("$1,000")
        st.write("**$4,000**")
    
    with col3:
        st.markdown("**Сард**")
        st.write("$4,000")
        st.write("$4,000")
        st.write("$4,000")
        st.write("$4,000")
        st.write("**$16,000**")
    
    with col4:
        st.markdown("**6 сард**")
        st.write("$24,000")
        st.write("$24,000")
        st.write("$24,000")
        st.write("$24,000")
        st.write("**$96,000**")
    
    st.markdown("""
    <div style="text-align: center; font-size: 1.5rem; color: #667eea; font-weight: bold; margin-top: 2rem;">
        ≈ 240,000,000₮ нийт хөрөнгө оруулалт
    </div>
    """, unsafe_allow_html=True)

# Slide 6: Development Vision
elif selected_slide == "🚀 Хөгжлийн алсын хараа":
    st.markdown("# 🚀 ХӨГЖЛИЙН АЛСЫН ХАРАА")
    
    st.markdown("""
    <div class="image-placeholder">
        🚀 BUSINESS GROWTH
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="phase-card">
            <div style="background: #667eea; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px; font-size: 1.2rem; font-weight: bold;">1</div>
            <h3>Улаанбаатар 21-р хороо</h3>
            <ul style="list-style: none; padding: 0;">
                <li>✓ Анхны угаалгын газар нээх</li>
                <li>✓ Зах зээлийн хэрэгцээ судлах</li>
                <li>✓ Процесс тогтоох</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="phase-card">
            <div style="background: #667eea; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px; font-size: 1.2rem; font-weight: bold;">2</div>
            <h3>Нийслэлд өргөжүүлэх</h3>
            <ul style="list-style: none; padding: 0;">
                <li>✓ Амжилттай дүүргүүдэд салбар</li>
                <li>✓ Брэнд танигдах болгох</li>
                <li>✓ Үйлчилгээний чанар</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="phase-card">
            <div style="background: #667eea; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px; font-size: 1.2rem; font-weight: bold;">3</div>
            <h3>Орон даяар өргөжүүлэх</h3>
            <ul style="list-style: none; padding: 0;">
                <li>✓ 21 аймагт салбар</li>
                <li>✓ Төрөл бүрийн үйлчилгээ</li>
                <li>✓ Ажлын байр бий болгох</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Slide 7: Why Now
elif selected_slide == "🔥 Яагаад одоо?":
    st.markdown("# 🔥 ЯАГААД ОДОО?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 3rem;">⚡</div>
            <h3>Боломж</h3>
            <p>Угаалгын үйлчилгээний хэрэгцээ өсөн нэмэгдэж байна</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 3rem;">📈</div>
            <h3>Зах зээл</h3>
            <p>Хотын хүн ам өсөж, амьдралын түвшин дээшилж байна</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 3rem;">⏰</div>
            <h3>Хэрэгцээ</h3>
            <p>Цагийн хомсдол улмаас үйлчилгээ илүүтэй ашиглах болсон</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
        <h3>💪 Бидний давуу тал:</h3>
        <p>🎓 Туршлагатай ах дүүгийн зөвлөгөө</p>
        <p>📍 Тохиромжтой байршил</p>
        <p>🤝 Найрсаг хамтрагч нар</p>
        <p>💰 Хангалттай хөрөнгө босгох боломж</p>
    </div>
    """, unsafe_allow_html=True)

# Slide 8: Call to Action
elif selected_slide == "🤝 Эрмүүн гэрбүлд урилга":
    st.markdown("# 🤝 ЭРМҮҮН ГЭРБҮЛД УРИЛГА")
    
    st.markdown("""
    <div class="call-to-action">
        <h3>🎊 Эрмүүн гэр бүл, та нар бидэнтэй нэгдэх үү?</h3>
        <p style="font-size: 1.2rem;">Энэ бол зөвхөн бизнес биш, бидний гэр бүлүүдийн ирээдүйн баталгаа!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="image-placeholder">
        🎉 SUCCESS PARTNERSHIP
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 3rem;">💫</div>
            <h3>Та нарын оролцоо чухал</h3>
            <p>Найрсаг хамтын ажиллагаа, тэгш эрх ба үр дүн</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 3rem;">📝</div>
            <h3>Хэрэв орилцохоор шийдвэл</h3>
            <p>Өнөөдрөөс хуримтлал эхлүүлэх</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
        <h3>Дараагийн алхамууд:</h3>
        <p>1️⃣ Өнөөдрөөс хуримтлал эхлүүлэх</p>
        <p>2️⃣ Долоо хоног бүр $1,000</p>
        <p>3️⃣ 6 сарын дараа бизнес эхлүүлэх</p>
        <p>4️⃣ Хамтдаа амжилтанд хүрэх</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-top: 2rem; font-style: italic; font-size: 1.2rem;">
        📞 Холбоо барих: Тэмүүжин, Амраа, Ганбаяр
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("**Угаалгын бизнес танилцуулга** | Найз гэр бүлүүдийн хамтарсан төсөл")