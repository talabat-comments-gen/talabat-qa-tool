import streamlit as st
import google.generativeai as genai

# إعدادات الصفحة
st.set_page_config(page_title="أداة تحليل طلبات", layout="wide")
st.title("🚀 أداة تحليل تقارير الجودة - Talabat")

# إعداد الـ API
try:
    # الكود هنا بيبحث عن "صندوق" اسمه GEMINI_API_KEY
    api_key = st.secrets["AQ.Ab8RN6Ix2qeVMs0rWW9B2pwjubJ21C-XVGnjthFWnoliFv2eSQ"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("يرجى التأكد من إضافة الـ API Key في إعدادات Secrets.")

# واجهة المستخدم بالعربية
chat_input = st.text_area("انسخ هنا نص الشات (Transcript):", height=250)

if st.button("بدء التحليل"):
    if chat_input:
        with st.spinner('جاري التحليل...'):
            try:
                prompt = f"""
                أنت Talabat Log Engine. استخرج الحقائق من الشات التالي.
                التزم بالهيكل التالي بدقة:
                --- LOG ---
                (CST: , RST: , Agent: , RNA: , FU: )
                --- ملخص الحالة ---
                (مشكلة العميل، الإجراء المتخذ، النتيجة النهائية).
                الشات: {chat_input}
                """
                response = model.generate_content(prompt)
                st.success("تم التحليل بنجاح!")
                st.markdown("### 📝 نتيجة التحليل:")
                st.write(response.text)
            except Exception as e:
                st.error(f"خطأ أثناء الاتصال بالذكاء الاصطناعي: {e}")
    else:
        st.warning("من فضلك ضع نص الشات في المربع أولاً.")
