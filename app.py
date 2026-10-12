import random
from datetime import date
import streamlit as st

st.set_page_config(
    page_title="دستیار تولید محتوای اینستاگرام",
    page_icon="🎨",
    layout="centered",
)

st.title("🎨 دستیار تولید محتوای اینستاگرام")
st.caption("نسخهٔ آزمایشی رایگان برای ایده‌پردازی، کپشن، هشتگ و تحلیل آمار")

with st.sidebar:
    st.header("دربارهٔ ابزار")
    st.write("این نسخه از الگوهای آماده استفاده می‌کند و هنوز به مدل هوش مصنوعی یا حساب اینستاگرام وصل نیست.")
    st.write("برای تحلیل، آمار را خودت وارد کن.")

tab_content, tab_analytics = st.tabs(["✍️ تولید محتوا", "📊 تحلیل آمار"])

with tab_content:
    st.subheader("برای چه محتوایی ایده می‌خواهی؟")
    product = st.selectbox(
        "نوع محصول یا پیج",
        ["تابلو کالیگرافی", "توت‌بگ دست‌ساز", "محصول هنری دیگر", "پیج آموزشی", "کسب‌وکار دیگر"],
    )
    goal = st.selectbox(
        "هدف انتشار",
        ["فروش محصول", "افزایش تعامل", "معرفی محصول", "آموزش", "افزایش بازدید"],
    )
    format_type = st.selectbox("نوع محتوا", ["ریلز", "پست", "استوری", "هرکدام مناسب‌تر است"])
    tone = st.selectbox("لحن متن", ["صمیمی و گرم", "هنری و لطیف", "حرفه‌ای", "کوتاه و پرانرژی"])
    details = st.text_input("جزئیات محصول (اختیاری)", placeholder="مثلاً طرح گل، رنگ آبی، کار دست")

    if st.button("✨ تولید پیشنهاد محتوا", type="primary", use_container_width=True):
        product_names = {
            "تابلو کالیگرافی": "تابلوی کالیگرافی",
            "توت‌بگ دست‌ساز": "توت‌بگ دست‌ساز",
            "محصول هنری دیگر": "محصول هنری",
            "پیج آموزشی": "محتوای آموزشی",
            "کسب‌وکار دیگر": "محصول یا خدمات شما",
        }
        item = product_names[product]
        detail_text = f" با ویژگی «{details.strip()}»" if details.strip() else ""
        if goal == "فروش محصول":
            caption = f"دنبال یک انتخاب خاص و متفاوتی؟ ✨\n{item}{detail_text} با عشق و دقت آماده شده تا به روزت رنگ و حس تازه‌ای بدهد.\nبرای اطلاع از قیمت و سفارش، پیام بده 💌"
            hook = f"۳ دلیل که این {item} می‌تونه انتخاب خاصی باشه"
            cta = "برای قیمت و سفارش، دایرکت بده."
        elif goal == "افزایش تعامل":
            caption = f"یک سؤال برای دوست‌داران هنر 🎨\nاگر قرار باشه یک اثر هنری{detail_text} انتخاب کنی، چه رنگ یا طرحی رو ترجیح می‌دی؟ نظرت رو برام بنویس 💬"
            hook = f"تو کدوم طرح {item} رو انتخاب می‌کنی؟"
            cta = "در کامنت‌ها نظرت رو بنویس."
        elif goal == "معرفی محصول":
            caption = f"معرفی یک کار دوست‌داشتنی از دنیای هنر ✨\nاین {item}{detail_text} با توجه به جزئیات و حس‌وحال طرح آماده شده.\nاگر دوست داری بیشتر ببینی، همراه من باش."
            hook = f"از ایده تا آماده‌شدن این {item}"
            cta = "برای دیدن جزئیات بیشتر پیام بده."
        elif goal == "آموزش":
            caption = f"یک نکتهٔ کوچک برای دوست‌داران هنر 🎨\nامروز دربارهٔ {item}{detail_text} یک نکتهٔ کاربردی یاد می‌گیریم. این پست رو ذخیره کن تا بعداً دوباره بهش سر بزنی."
            hook = f"یک نکتهٔ ساده دربارهٔ {item} که به کارت میاد"
            cta = "برای نکته‌های بعدی ذخیره کن و دنبال کن."
        else:
            caption = f"بیا این جزئیات رو از نزدیک ببینیم! 👀✨\n{item}{detail_text}؛ یک ایدهٔ تازه برای کسانی که هنر و خلاقیت رو دوست دارن."
            hook = f"این جزئیات رو از دست نده!"
            cta = "تا آخر ببین و نظرت رو بگو."

        if tone == "هنری و لطیف":
            caption = caption.replace("✨", "🌿").replace("💌", "🤍")
        elif tone == "حرفه‌ای":
            caption = caption.replace("با عشق و دقت", "با توجه به جزئیات").replace("بیا ", " ")
        elif tone == "کوتاه و پرانرژی":
            caption = f"{item}{detail_text} ✨\nخاص، هنری و متفاوت!\n{cta}"

        tags_by_product = {
            "تابلو کالیگرافی": "#کالیگرافی #تابلو_هنری #هنر_ایرانی #دکوراسیون #هنر_دست",
            "توت‌بگ دست‌ساز": "#توت_بگ #توتبگ_دستساز #نقاشی_روی_پارچه #هنر_دست #استایل",
            "محصول هنری دیگر": "#هنر #محصول_هنری #هنر_دست #طراحی #خلاقیت",
            "پیج آموزشی": "#آموزش #یادگیری #نکته_آموزشی #مهارت #آموزش_آنلاین",
            "کسب‌وکار دیگر": "#کسب_و_کار #معرفی_محصول #خدمات #خلاقیت #ایده",
        }
        story_ideas = [
            f"استوری نظرسنجی: کدام طرح از {item} رو بیشتر دوست داری؟",
            f"نمای نزدیک از جزئیات {item} و پرسیدن نظر مخاطب",
            f"پشت‌صحنهٔ آماده‌سازی {item} در چند کلیپ کوتاه",
            f"پرسش و پاسخ دربارهٔ سفارش یا ویژگی‌های {item}",
            f"دعوت به دیدن پست جدید دربارهٔ {item}",
        ]

        st.success("پیشنهاد محتوا آماده شد. قبل از انتشار، متن را با جزئیات واقعی محصولت هماهنگ کن.")
        st.markdown("### 🎬 ایده یا شروع محتوا")
        st.write(hook)
        st.markdown("### 📝 کپشن پیشنهادی")
        st.text_area("کپشن", value=caption, height=150, key="generated_caption")
        st.markdown("### #️⃣ هشتگ‌ها")
        st.code(tags_by_product[product], language=None)
        st.markdown("### 📱 ایده‌های استوری")
        for idea in random.sample(story_ideas, k=len(story_ideas)):
            st.write("• " + idea)
        st.markdown("### 👉 دعوت به اقدام")
        st.write(cta)
        st.caption("این خروجی‌ها الگومحور هستند؛ بازده واقعی به محتوا، مخاطب و زمان انتشار بستگی دارد.")

with tab_analytics:
    st.subheader("تحلیل سادهٔ آمار محتوا")
    st.write("وارد کردن آمار اختیاری است. اعداد را از Insights اینستاگرام خودت وارد کن.")
    col1, col2 = st.columns(2)
    with col1:
        views = st.number_input("بازدید / پخش", min_value=0, step=1, value=0)
        likes = st.number_input("پسندها", min_value=0, step=1, value=0)
        comments = st.number_input("کامنت‌ها", min_value=0, step=1, value=0)
    with col2:
        saves = st.number_input("ذخیره‌ها", min_value=0, step=1, value=0)
        shares = st.number_input("اشتراک‌گذاری‌ها", min_value=0, step=1, value=0)
        followers_gained = st.number_input("فالوورهای جذب‌شده", min_value=0, step=1, value=0)

    if st.button("📈 تحلیل آمار", use_container_width=True):
        interactions = likes + comments + saves + shares
        if views == 0:
            st.warning("برای محاسبهٔ نرخ تعامل، تعداد بازدید را بیشتر از صفر وارد کن.")
        else:
            engagement = interactions / views * 100
            st.metric("تعامل‌های ثبت‌شده", interactions)
            st.metric("نرخ تعامل نسبت به بازدید", f"{engagement:.2f}%")
            st.metric("فالوورهای جذب‌شده", followers_gained)
            st.markdown("### پیشنهادهای اولیه")
            if saves > likes:
                st.write("• ذخیره‌ها نسبت به پسندها بیشترند؛ محتوای کاربردی یا قابل رجوع را بررسی کن.")
            if shares > 0:
                st.write("• محتوا اشتراک‌گذاری شده؛ موضوع و قالبش را یادداشت کن و نمونه‌های مشابه را آزمایش کن.")
            if comments == 0:
                st.write("• برای تشویق گفت‌وگو، یک سؤال مشخص و ساده در کپشن یا استوری بپرس.")
            if engagement < 2:
                st.write("• یک شروع جذاب‌تر، موضوع روشن‌تر و دعوت به اقدام مشخص را آزمایش کن. این عدد به‌تنهایی معیار قطعی نیست.")
            else:
                st.write("• این محتوا را با پست‌های قبلی خودت مقایسه کن و ببین کدام موضوع یا قالب بهتر عمل کرده.")
            st.caption("این تحلیل ساده و راهنمای آزمایش است، نه ارزیابی قطعی عملکرد پیج.")

st.divider()
st.caption(f"نسخهٔ آزمایشی • {date.today().year} • ساخته‌شده برای تمرین و بازخورد")
