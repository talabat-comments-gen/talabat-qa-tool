import streamlit as st
import google.generativeai as genai

# إعدادات الصفحة بالعربي
st.set_page_config(page_title="أداة تحليل طلبات", layout="centered") # خليناها centered عشان العرض يقل
st.title("🚀 أداة تحليل تقارير الجودة - Talabat")

# محاولة سحب المفتاح
try:
    api_key = st.secrets["AQ.Ab8RN6Ix2qeVMs0rWW9B2pwjubJ21C-XVGnjthFWnoliFv2eSQ"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # واجهة المستخدم (بالعربي)
    chat_input = st.text_area("انسخ هنا نص الشات (Transcript):", height=400) # زودنا الطول لـ 400

    if st.button("بدء التحليل"):
        if chat_input:
            with st.spinner('جاري التحليل...'):
                prompt = f"""
                أنت Talabat Log Engine. استخرج الحقائق من الشات التالي باللغة العربية.
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
        else:
            st.warning("من فضلك ضع نص الشات في المربع.")

except Exception as e:
    st.error("⚠️ خطأ: تأكد من إضافة الـ API Key في إعدادات Secrets في Streamlit.")
