import streamlit as st

# ── page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="JanSetu — Bridging Citizens to Development",
    page_icon="🌉",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── language data ─────────────────────────────────────────────
LANGUAGES = {
    "English": {
        "nav_home": "Home", "nav_about": "About", "nav_services": "Services",
        "hero_tag": "Digital Public Infrastructure · BRICS Initiative",
        "hero_title": "Your Voice Builds the Nation",
        "hero_sub": "JanSetu bridges citizen development requests directly to national policymakers — in your language, from your district.",
        "cta_issue": "📍 Share a Local Issue",
        "cta_dashboard": "View Dashboard",
        "stat1_val": "28+", "stat1_label": "Languages Supported",
        "stat2_val": "BRICS", "stat2_label": "Nations Connected",
        "stat3_val": "AI", "stat3_label": "Powered Analysis",
        "stat4_val": "Real", "stat4_label": "Time Insights",
        "how_title": "How JanSetu Works",
        "s1_title": "Submit Your Issue", "s1_desc": "Voice or text, in any of 28+ languages. No forms. No offices.",
        "s2_title": "AI Understands", "s2_desc": "Gemini translates, classifies sector, urgency and location automatically.",
        "s3_title": "Clusters Form", "s3_desc": "Similar issues from your district group together — amplifying your voice.",
        "s4_title": "Policy Action", "s4_desc": "Policymakers see ranked priority maps and take targeted action.",
        "sectors_title": "Issues We Cover",
        "footer_tag": "A Digital Public Good · Built for BRICS Nations",
        "modal_title": "Share a Local Issue",
        "modal_name": "Your Name (optional)",
        "modal_district": "Your District",
        "modal_sector": "Issue Category",
        "modal_desc": "Describe your issue",
        "modal_urgency": "Urgency",
        "modal_submit": "Submit Issue",
        "modal_success": "✅ Your issue has been submitted. Thank you for your voice.",
    },
    "हिन्दी": {
        "nav_home": "होम", "nav_about": "हमारे बारे में", "nav_services": "सेवाएं",
        "hero_tag": "डिजिटल सार्वजनिक अवसंरचना · BRICS पहल",
        "hero_title": "आपकी आवाज़ राष्ट्र बनाती है",
        "hero_sub": "जनसेतु नागरिकों की विकास मांगों को सीधे नीति-निर्माताओं तक पहुंचाता है।",
        "cta_issue": "📍 स्थानीय समस्या साझा करें",
        "cta_dashboard": "डैशबोर्ड देखें",
        "stat1_val": "28+", "stat1_label": "भाषाएं",
        "stat2_val": "BRICS", "stat2_label": "देश जुड़े",
        "stat3_val": "AI", "stat3_label": "संचालित",
        "stat4_val": "रियल", "stat4_label": "टाइम डेटा",
        "how_title": "जनसेतु कैसे काम करता है",
        "s1_title": "समस्या बताएं", "s1_desc": "आवाज़ या टेक्स्ट में, किसी भी भाषा में।",
        "s2_title": "AI समझता है", "s2_desc": "Gemini अनुवाद करता है और श्रेणी तय करता है।",
        "s3_title": "समूह बनते हैं", "s3_desc": "समान समस्याएं एकत्रित होती हैं।",
        "s4_title": "नीति कार्रवाई", "s4_desc": "नीति-निर्माता प्राथमिकता देखते हैं।",
        "sectors_title": "हम किन समस्याओं को कवर करते हैं",
        "footer_tag": "एक डिजिटल सार्वजनिक वस्तु · BRICS देशों के लिए",
        "modal_title": "स्थानीय समस्या साझा करें",
        "modal_name": "आपका नाम (वैकल्पिक)",
        "modal_district": "आपका जिला",
        "modal_sector": "समस्या श्रेणी",
        "modal_desc": "अपनी समस्या बताएं",
        "modal_urgency": "गंभीरता",
        "modal_submit": "समस्या जमा करें",
        "modal_success": "✅ आपकी समस्या जमा हो गई। धन्यवाद।",
    },
    "ଓଡ଼ିଆ": {
        "nav_home": "ହୋମ", "nav_about": "ଆମ ବିଷୟରେ", "nav_services": "ସେବା",
        "hero_tag": "ଡିଜିଟାଲ ସାର୍ବଜନୀନ ଭିତ୍ତିଭୂମି · BRICS ଉଦ୍ୟୋଗ",
        "hero_title": "ଆପଣଙ୍କ ସ୍ୱର ଜାତି ଗଢ଼େ",
        "hero_sub": "ଜନସେତୁ ନାଗରିକଙ୍କ ବିକାଶ ଦାବିକୁ ସିଧା ନୀତି ନିର୍ମାତାଙ୍କ ନିକଟ ପହଞ୍ଚାଏ।",
        "cta_issue": "📍 ସ୍ଥାନୀୟ ସମସ୍ୟା ଜଣାନ୍ତୁ",
        "cta_dashboard": "ଡ୍ୟାଶବୋର୍ଡ ଦେଖନ୍ତୁ",
        "stat1_val": "28+", "stat1_label": "ଭାଷା",
        "stat2_val": "BRICS", "stat2_label": "ଦେଶ",
        "stat3_val": "AI", "stat3_label": "ଚାଳିତ",
        "stat4_val": "ରିଅଲ", "stat4_label": "ଟାଇମ",
        "how_title": "ଜନସେତୁ କିପରି କାମ କରେ",
        "s1_title": "ସମସ୍ୟା ଜଣାନ୍ତୁ", "s1_desc": "ଯେକୌଣସି ଭାଷାରେ ଆବେଦନ କରନ୍ତୁ।",
        "s2_title": "AI ବୁଝେ", "s2_desc": "Gemini ଅନୁବାଦ ଓ ବର୍ଗୀକରଣ କରେ।",
        "s3_title": "ଗୋଷ୍ଠୀ ଗଠନ", "s3_desc": "ସମାନ ସମସ୍ୟା ଏକାଠି ହୁଏ।",
        "s4_title": "ନୀତି କାର୍ଯ୍ୟ", "s4_desc": "ନୀତି ନିର୍ମାତା ଅଗ୍ରାଧିକାର ଦେଖନ୍ତି।",
        "sectors_title": "ଆମେ ଯେଉଁ ସମସ୍ୟା ଆଚ୍ଛାଦନ କରୁ",
        "footer_tag": "ଏକ ଡିଜିଟାଲ ସାର୍ବଜନୀନ ସୁବିଧା · BRICS ଦେଶ ପାଇଁ",
        "modal_title": "ସ୍ଥାନୀୟ ସମସ୍ୟା ଜଣାନ୍ତୁ",
        "modal_name": "ଆପଣଙ୍କ ନାମ (ଐଚ୍ଛିକ)",
        "modal_district": "ଆପଣଙ୍କ ଜିଲ୍ଲା",
        "modal_sector": "ସମସ୍ୟା ଶ୍ରେଣୀ",
        "modal_desc": "ଆପଣଙ୍କ ସମସ୍ୟା ବର୍ଣ୍ଣନା କରନ୍ତୁ",
        "modal_urgency": "ଜରୁରୀ ସ୍ତର",
        "modal_submit": "ଦାଖଲ କରନ୍ତୁ",
        "modal_success": "✅ ଆପଣଙ୍କ ସମସ୍ୟା ଦାଖଲ ହୋଇଛି। ଧନ୍ୟବାଦ।",
    },
    "বাংলা": {
        "nav_home": "হোম", "nav_about": "আমাদের সম্পর্কে", "nav_services": "পরিষেবা",
        "hero_tag": "ডিজিটাল পাবলিক ইনফ্রাস্ট্রাকচার · BRICS উদ্যোগ",
        "hero_title": "আপনার কণ্ঠ জাতি গড়ে",
        "hero_sub": "জনসেতু নাগরিকদের উন্নয়নের দাবি সরাসরি নীতিনির্ধারকদের কাছে পৌঁছে দেয়।",
        "cta_issue": "📍 স্থানীয় সমস্যা জানান",
        "cta_dashboard": "ড্যাশবোর্ড দেখুন",
        "stat1_val": "28+", "stat1_label": "ভাষা",
        "stat2_val": "BRICS", "stat2_label": "দেশ",
        "stat3_val": "AI", "stat3_label": "চালিত",
        "stat4_val": "রিয়েল", "stat4_label": "টাইম",
        "how_title": "জনসেতু কীভাবে কাজ করে",
        "s1_title": "সমস্যা জানান", "s1_desc": "যেকোনো ভাষায় আবেদন করুন।",
        "s2_title": "AI বোঝে", "s2_desc": "Gemini অনুবাদ ও শ্রেণীবিভাগ করে।",
        "s3_title": "গ্রুপ তৈরি", "s3_desc": "একই সমস্যা একসাথে আসে।",
        "s4_title": "নীতি পদক্ষেপ", "s4_desc": "নীতিনির্ধারকরা অগ্রাধিকার দেখেন।",
        "sectors_title": "আমরা যে সমস্যাগুলি কভার করি",
        "footer_tag": "একটি ডিজিটাল পাবলিক গুড · BRICS দেশগুলির জন্য",
        "modal_title": "স্থানীয় সমস্যা জানান",
        "modal_name": "আপনার নাম (ঐচ্ছিক)",
        "modal_district": "আপনার জেলা",
        "modal_sector": "সমস্যার বিভাগ",
        "modal_desc": "আপনার সমস্যা বর্ণনা করুন",
        "modal_urgency": "জরুরি মাত্রা",
        "modal_submit": "সমস্যা জমা দিন",
        "modal_success": "✅ আপনার সমস্যা জমা হয়েছে। ধন্যবাদ।",
    },
    "தமிழ்": {
        "nav_home": "முகப்பு", "nav_about": "எங்களை பற்றி", "nav_services": "சேவைகள்",
        "hero_tag": "டிஜிட்டல் பொது உள்கட்டமைப்பு · BRICS முயற்சி",
        "hero_title": "உங்கள் குரல் தேசத்தை கட்டுகிறது",
        "hero_sub": "ஜன்சேது குடிமக்களின் வளர்ச்சி கோரிக்கைகளை நேரடியாக கொள்கை வகுப்பாளர்களிடம் சேர்க்கிறது.",
        "cta_issue": "📍 உள்ளூர் சிக்கலை பகிரவும்",
        "cta_dashboard": "டாஷ்போர்டு காண்க",
        "stat1_val": "28+", "stat1_label": "மொழிகள்",
        "stat2_val": "BRICS", "stat2_label": "நாடுகள்",
        "stat3_val": "AI", "stat3_label": "இயங்கு",
        "stat4_val": "நேரடி", "stat4_label": "தகவல்",
        "how_title": "ஜன்சேது எவ்வாறு செயல்படுகிறது",
        "s1_title": "சிக்கலை தெரிவிக்கவும்", "s1_desc": "எந்த மொழியிலும் தெரிவிக்கலாம்.",
        "s2_title": "AI புரிந்துகொள்கிறது", "s2_desc": "Gemini மொழிபெயர்த்து வகைப்படுத்துகிறது.",
        "s3_title": "குழுக்கள் உருவாகின்றன", "s3_desc": "ஒத்த சிக்கல்கள் ஒன்றிணைகின்றன.",
        "s4_title": "கொள்கை நடவடிக்கை", "s4_desc": "கொள்கை வகுப்பாளர்கள் முன்னுரிமை காண்கிறார்கள்.",
        "sectors_title": "நாங்கள் உள்ளடக்கும் சிக்கல்கள்",
        "footer_tag": "ஒரு டிஜிட்டல் பொது நலன் · BRICS நாடுகளுக்காக",
        "modal_title": "உள்ளூர் சிக்கலை பகிரவும்",
        "modal_name": "உங்கள் பெயர் (விருப்பமானது)",
        "modal_district": "உங்கள் மாவட்டம்",
        "modal_sector": "சிக்கல் வகை",
        "modal_desc": "உங்கள் சிக்கலை விவரிக்கவும்",
        "modal_urgency": "அவசரநிலை",
        "modal_submit": "சிக்கலை சமர்ப்பிக்கவும்",
        "modal_success": "✅ உங்கள் சிக்கல் சமர்ப்பிக்கப்பட்டது. நன்றி.",
    },
    "తెలుగు": {
        "nav_home": "హోమ్", "nav_about": "మా గురించి", "nav_services": "సేవలు",
        "hero_tag": "డిజిటల్ పబ్లిక్ ఇన్‌ఫ్రాస్ట్రక్చర్ · BRICS చొరవ",
        "hero_title": "మీ స్వరం దేశాన్ని నిర్మిస్తుంది",
        "hero_sub": "జన్‌సేతు పౌరుల అభివృద్ధి అభ్యర్థనలను నేరుగా విధాన నిర్ణేతలకు చేరుస్తుంది.",
        "cta_issue": "📍 స్థానిక సమస్యను పంచుకోండి",
        "cta_dashboard": "డాష్‌బోర్డ్ చూడండి",
        "stat1_val": "28+", "stat1_label": "భాషలు",
        "stat2_val": "BRICS", "stat2_label": "దేశాలు",
        "stat3_val": "AI", "stat3_label": "ఆధారిత",
        "stat4_val": "రియల్", "stat4_label": "టైమ్",
        "how_title": "జన్‌సేతు ఎలా పని చేస్తుంది",
        "s1_title": "సమస్య నివేదించండి", "s1_desc": "ఏ భాషలోనైనా దరఖాస్తు చేయండి.",
        "s2_title": "AI అర్థం చేసుకుంటుంది", "s2_desc": "Gemini అనువదించి వర్గీకరిస్తుంది.",
        "s3_title": "సమూహాలు ఏర్పడతాయి", "s3_desc": "ఒకే రకమైన సమస్యలు కలిసివస్తాయి.",
        "s4_title": "విధాన చర్య", "s4_desc": "విధాన నిర్ణేతలు ప్రాధాన్యతలు చూస్తారు.",
        "sectors_title": "మేము కవర్ చేసే సమస్యలు",
        "footer_tag": "ఒక డిజిటల్ పబ్లిక్ గుడ్ · BRICS దేశాల కోసం",
        "modal_title": "స్థానిక సమస్యను పంచుకోండి",
        "modal_name": "మీ పేరు (ఐచ్ఛికం)",
        "modal_district": "మీ జిల్లా",
        "modal_sector": "సమస్య వర్గం",
        "modal_desc": "మీ సమస్యను వివరించండి",
        "modal_urgency": "అత్యవసరత",
        "modal_submit": "సమస్య సమర్పించండి",
        "modal_success": "✅ మీ సమస్య సమర్పించబడింది. ధన్యవాదాలు.",
    },
    "मराठी": {
        "nav_home": "मुख्यपृष्ठ", "nav_about": "आमच्याबद्दल", "nav_services": "सेवा",
        "hero_tag": "डिजिटल सार्वजनिक पायाभूत सुविधा · BRICS उपक्रम",
        "hero_title": "तुमचा आवाज राष्ट्र घडवतो",
        "hero_sub": "जनसेतू नागरिकांच्या विकास मागण्या थेट धोरण निर्मात्यांपर्यंत पोहोचवतो.",
        "cta_issue": "📍 स्थानिक समस्या सांगा",
        "cta_dashboard": "डॅशबोर्ड पाहा",
        "stat1_val": "28+", "stat1_label": "भाषा",
        "stat2_val": "BRICS", "stat2_label": "राष्ट्रे",
        "stat3_val": "AI", "stat3_label": "चालित",
        "stat4_val": "रिअल", "stat4_label": "टाइम",
        "how_title": "जनसेतू कसे कार्य करते",
        "s1_title": "समस्या सांगा", "s1_desc": "कोणत्याही भाषेत अर्ज करा.",
        "s2_title": "AI समजते", "s2_desc": "Gemini भाषांतर आणि वर्गीकरण करते.",
        "s3_title": "गट तयार होतात", "s3_desc": "सारख्या समस्या एकत्र येतात.",
        "s4_title": "धोरण कृती", "s4_desc": "धोरण निर्माते प्राधान्य पाहतात.",
        "sectors_title": "आम्ही कोणत्या समस्या हाताळतो",
        "footer_tag": "एक डिजिटल सार्वजनिक वस्तू · BRICS राष्ट्रांसाठी",
        "modal_title": "स्थानिक समस्या सांगा",
        "modal_name": "तुमचे नाव (पर्यायी)",
        "modal_district": "तुमचा जिल्हा",
        "modal_sector": "समस्येची श्रेणी",
        "modal_desc": "तुमची समस्या सांगा",
        "modal_urgency": "तातडी",
        "modal_submit": "समस्या सादर करा",
        "modal_success": "✅ तुमची समस्या सादर झाली. धन्यवाद.",
    },
    "ਪੰਜਾਬੀ": {
        "nav_home": "ਹੋਮ", "nav_about": "ਸਾਡੇ ਬਾਰੇ", "nav_services": "ਸੇਵਾਵਾਂ",
        "hero_tag": "ਡਿਜੀਟਲ ਜਨਤਕ ਬੁਨਿਆਦੀ ਢਾਂਚਾ · BRICS ਪਹਿਲ",
        "hero_title": "ਤੁਹਾਡੀ ਆਵਾਜ਼ ਰਾਸ਼ਟਰ ਬਣਾਉਂਦੀ ਹੈ",
        "hero_sub": "ਜਨਸੇਤੂ ਨਾਗਰਿਕਾਂ ਦੀਆਂ ਮੰਗਾਂ ਨੂੰ ਸਿੱਧੇ ਨੀਤੀ ਨਿਰਮਾਤਾਵਾਂ ਤੱਕ ਪਹੁੰਚਾਉਂਦਾ ਹੈ।",
        "cta_issue": "📍 ਸਥਾਨਕ ਸਮੱਸਿਆ ਦੱਸੋ",
        "cta_dashboard": "ਡੈਸ਼ਬੋਰਡ ਦੇਖੋ",
        "stat1_val": "28+", "stat1_label": "ਭਾਸ਼ਾਵਾਂ",
        "stat2_val": "BRICS", "stat2_label": "ਦੇਸ਼",
        "stat3_val": "AI", "stat3_label": "ਚਾਲਿਤ",
        "stat4_val": "ਰੀਅਲ", "stat4_label": "ਟਾਈਮ",
        "how_title": "ਜਨਸੇਤੂ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ",
        "s1_title": "ਸਮੱਸਿਆ ਦੱਸੋ", "s1_desc": "ਕਿਸੇ ਵੀ ਭਾਸ਼ਾ ਵਿੱਚ ਅਰਜ਼ੀ ਦਿਓ।",
        "s2_title": "AI ਸਮਝਦਾ ਹੈ", "s2_desc": "Gemini ਅਨੁਵਾਦ ਅਤੇ ਵਰਗੀਕਰਨ ਕਰਦਾ ਹੈ।",
        "s3_title": "ਸਮੂਹ ਬਣਦੇ ਹਨ", "s3_desc": "ਸਮਾਨ ਸਮੱਸਿਆਵਾਂ ਇਕੱਠੀਆਂ ਹੁੰਦੀਆਂ ਹਨ।",
        "s4_title": "ਨੀਤੀ ਕਾਰਵਾਈ", "s4_desc": "ਨੀਤੀ ਨਿਰਮਾਤਾ ਤਰਜੀਹ ਦੇਖਦੇ ਹਨ।",
        "sectors_title": "ਅਸੀਂ ਕਿਹੜੀਆਂ ਸਮੱਸਿਆਵਾਂ ਕਵਰ ਕਰਦੇ ਹਾਂ",
        "footer_tag": "ਇੱਕ ਡਿਜੀਟਲ ਜਨਤਕ ਵਸਤੂ · BRICS ਦੇਸ਼ਾਂ ਲਈ",
        "modal_title": "ਸਥਾਨਕ ਸਮੱਸਿਆ ਦੱਸੋ",
        "modal_name": "ਤੁਹਾਡਾ ਨਾਮ (ਵਿਕਲਪਿਕ)",
        "modal_district": "ਤੁਹਾਡਾ ਜ਼ਿਲ੍ਹਾ",
        "modal_sector": "ਸਮੱਸਿਆ ਸ਼੍ਰੇਣੀ",
        "modal_desc": "ਆਪਣੀ ਸਮੱਸਿਆ ਦੱਸੋ",
        "modal_urgency": "ਫੌਰੀਅਤ",
        "modal_submit": "ਸਮੱਸਿਆ ਜਮ੍ਹਾਂ ਕਰੋ",
        "modal_success": "✅ ਤੁਹਾਡੀ ਸਮੱਸਿਆ ਜਮ੍ਹਾਂ ਹੋ ਗਈ। ਧੰਨਵਾਦ।",
    },
    "Português": {
        "nav_home": "Início", "nav_about": "Sobre", "nav_services": "Serviços",
        "hero_tag": "Infraestrutura Pública Digital · Iniciativa BRICS",
        "hero_title": "Sua Voz Constrói a Nação",
        "hero_sub": "JanSetu conecta pedidos de desenvolvimento dos cidadãos diretamente aos formuladores de políticas.",
        "cta_issue": "📍 Compartilhar um Problema Local",
        "cta_dashboard": "Ver Painel",
        "stat1_val": "28+", "stat1_label": "Idiomas",
        "stat2_val": "BRICS", "stat2_label": "Nações",
        "stat3_val": "IA", "stat3_label": "Alimentado",
        "stat4_val": "Tempo", "stat4_label": "Real",
        "how_title": "Como o JanSetu Funciona",
        "s1_title": "Envie seu Problema", "s1_desc": "Voz ou texto, em qualquer idioma.",
        "s2_title": "A IA Entende", "s2_desc": "Gemini traduz e classifica automaticamente.",
        "s3_title": "Clusters se Formam", "s3_desc": "Problemas semelhantes se agrupam.",
        "s4_title": "Ação Política", "s4_desc": "Formuladores veem prioridades mapeadas.",
        "sectors_title": "Problemas que Cobrimos",
        "footer_tag": "Um Bem Público Digital · Construído para as Nações BRICS",
        "modal_title": "Compartilhar um Problema Local",
        "modal_name": "Seu Nome (opcional)",
        "modal_district": "Seu Distrito",
        "modal_sector": "Categoria do Problema",
        "modal_desc": "Descreva seu problema",
        "modal_urgency": "Urgência",
        "modal_submit": "Enviar Problema",
        "modal_success": "✅ Seu problema foi enviado. Obrigado.",
    },
    "Русский": {
        "nav_home": "Главная", "nav_about": "О нас", "nav_services": "Услуги",
        "hero_tag": "Цифровая публичная инфраструктура · Инициатива БРИКС",
        "hero_title": "Ваш голос строит нацию",
        "hero_sub": "JanSetu передаёт запросы граждан на развитие непосредственно политикам.",
        "cta_issue": "📍 Сообщить о местной проблеме",
        "cta_dashboard": "Просмотр панели",
        "stat1_val": "28+", "stat1_label": "Языков",
        "stat2_val": "БРИКС", "stat2_label": "Нации",
        "stat3_val": "ИИ", "stat3_label": "Работает",
        "stat4_val": "Реал", "stat4_label": "Тайм",
        "how_title": "Как работает JanSetu",
        "s1_title": "Сообщите о проблеме", "s1_desc": "Голосом или текстом на любом языке.",
        "s2_title": "ИИ понимает", "s2_desc": "Gemini переводит и классифицирует.",
        "s3_title": "Кластеры формируются", "s3_desc": "Похожие проблемы объединяются.",
        "s4_title": "Политические действия", "s4_desc": "Политики видят приоритеты на карте.",
        "sectors_title": "Проблемы, которые мы охватываем",
        "footer_tag": "Цифровое общественное благо · Для наций БРИКС",
        "modal_title": "Сообщить о местной проблеме",
        "modal_name": "Ваше имя (необязательно)",
        "modal_district": "Ваш район",
        "modal_sector": "Категория проблемы",
        "modal_desc": "Опишите вашу проблему",
        "modal_urgency": "Срочность",
        "modal_submit": "Отправить проблему",
        "modal_success": "✅ Ваша проблема отправлена. Спасибо.",
    },
    "中文": {
        "nav_home": "首页", "nav_about": "关于我们", "nav_services": "服务",
        "hero_tag": "数字公共基础设施 · 金砖国家倡议",
        "hero_title": "您的声音建设国家",
        "hero_sub": "JanSetu将公民的发展诉求直接传达给政策制定者。",
        "cta_issue": "📍 分享本地问题",
        "cta_dashboard": "查看仪表板",
        "stat1_val": "28+", "stat1_label": "语言",
        "stat2_val": "金砖", "stat2_label": "国家",
        "stat3_val": "人工智能", "stat3_label": "驱动",
        "stat4_val": "实时", "stat4_label": "数据",
        "how_title": "JanSetu如何工作",
        "s1_title": "提交问题", "s1_desc": "用任何语言，语音或文字。",
        "s2_title": "AI理解", "s2_desc": "Gemini自动翻译和分类。",
        "s3_title": "集群形成", "s3_desc": "相似问题被归为一组。",
        "s4_title": "政策行动", "s4_desc": "政策制定者看到优先级地图。",
        "sectors_title": "我们涵盖的问题",
        "footer_tag": "数字公共产品 · 为金砖国家而建",
        "modal_title": "分享本地问题",
        "modal_name": "您的姓名（可选）",
        "modal_district": "您的地区",
        "modal_sector": "问题类别",
        "modal_desc": "描述您的问题",
        "modal_urgency": "紧急程度",
        "modal_submit": "提交问题",
        "modal_success": "✅ 您的问题已提交。谢谢。",
    },
    "اردو": {
        "nav_home": "ہوم", "nav_about": "ہمارے بارے میں", "nav_services": "خدمات",
        "hero_tag": "ڈیجیٹل عوامی بنیادی ڈھانچہ · BRICS اقدام",
        "hero_title": "آپ کی آواز قوم بناتی ہے",
        "hero_sub": "جن سیتو شہریوں کی ترقیاتی درخواستوں کو براہ راست پالیسی سازوں تک پہنچاتا ہے۔",
        "cta_issue": "📍 مقامی مسئلہ بتائیں",
        "cta_dashboard": "ڈیش بورڈ دیکھیں",
        "stat1_val": "28+", "stat1_label": "زبانیں",
        "stat2_val": "BRICS", "stat2_label": "ممالک",
        "stat3_val": "AI", "stat3_label": "چلتا",
        "stat4_val": "ریل", "stat4_label": "ٹائم",
        "how_title": "جن سیتو کیسے کام کرتا ہے",
        "s1_title": "مسئلہ بتائیں", "s1_desc": "کسی بھی زبان میں درخواست دیں۔",
        "s2_title": "AI سمجھتا ہے", "s2_desc": "Gemini ترجمہ اور درجہ بندی کرتا ہے۔",
        "s3_title": "گروپ بنتے ہیں", "s3_desc": "ایک جیسے مسائل اکٹھے ہوتے ہیں۔",
        "s4_title": "پالیسی کارروائی", "s4_desc": "پالیسی ساز ترجیحات دیکھتے ہیں۔",
        "sectors_title": "ہم کون سے مسائل کور کرتے ہیں",
        "footer_tag": "ایک ڈیجیٹل عوامی خیر · BRICS ممالک کے لیے",
        "modal_title": "مقامی مسئلہ بتائیں",
        "modal_name": "آپ کا نام (اختیاری)",
        "modal_district": "آپ کا ضلع",
        "modal_sector": "مسئلے کی قسم",
        "modal_desc": "اپنا مسئلہ بیان کریں",
        "modal_urgency": "فوریت",
        "modal_submit": "مسئلہ جمع کریں",
        "modal_success": "✅ آپ کا مسئلہ جمع ہو گیا۔ شکریہ۔",
    },
    "ગુજરાતી": {"nav_home": "હોમ", "nav_about": "અમારા વિશે", "nav_services": "સેવાઓ", "hero_tag": "ડિજિટલ જાહેર માળખું · BRICS પહેલ", "hero_title": "તમારો અવાજ રાષ્ટ્ર બનાવે છે", "hero_sub": "જનસેતુ નાગરિકોની વિકાસ માગણીઓ સીધી નીતિ ઘડનારાઓ સુધી પહોંચાડે છે.", "cta_issue": "📍 સ્થાનિક સમસ્યા જણાવો", "cta_dashboard": "ડૅશબોર્ડ જુઓ", "stat1_val": "28+", "stat1_label": "ભાષાઓ", "stat2_val": "BRICS", "stat2_label": "દેશો", "stat3_val": "AI", "stat3_label": "સંચાલિત", "stat4_val": "રિઅલ", "stat4_label": "ટાઇમ", "how_title": "જનસેતુ કેવી રીતે કામ કરે છે", "s1_title": "સમસ્યા જણાવો", "s1_desc": "કોઈ પણ ભાષામાં.", "s2_title": "AI સમજે છે", "s2_desc": "Gemini અનુવાદ કરે છે.", "s3_title": "જૂથ બને છે", "s3_desc": "સમાન સમસ્યાઓ ભેગી થાય છે.", "s4_title": "નીતિ કાર્ય", "s4_desc": "નીતિ ઘડનારાઓ અગ્રતા જુએ છે.", "sectors_title": "અમે કઈ સમસ્યાઓ આવરીએ છીએ", "footer_tag": "ડિજિટલ જાહેર ભલું · BRICS દેશો માટે", "modal_title": "સ્થાનિક સમસ્યા જણાવો", "modal_name": "તમારું નામ (વૈકલ્પિક)", "modal_district": "તમારો જિલ્લો", "modal_sector": "સમસ્યાની શ્રેણી", "modal_desc": "તમારી સમસ્યા વર્ણવો", "modal_urgency": "તાકીદ", "modal_submit": "સમસ્યા સબમિટ કરો", "modal_success": "✅ તમારી સમસ્યા સબમિટ થઈ. આભાર."},
    "ಕನ್ನಡ": {"nav_home": "ಮನೆ", "nav_about": "ನಮ್ಮ ಬಗ್ಗೆ", "nav_services": "ಸೇವೆಗಳು", "hero_tag": "ಡಿಜಿಟಲ್ ಸಾರ್ವಜನಿಕ ಮೂಲಸೌಕರ್ಯ · BRICS ಉಪಕ್ರಮ", "hero_title": "ನಿಮ್ಮ ಧ್ವನಿ ರಾಷ್ಟ್ರ ನಿರ್ಮಿಸುತ್ತದೆ", "hero_sub": "ಜನಸೇತು ನಾಗರಿಕರ ಅಭಿವೃದ್ಧಿ ಮನವಿಗಳನ್ನು ನೀತಿ ನಿರ್ಮಾತರಿಗೆ ನೇರವಾಗಿ ತಲುಪಿಸುತ್ತದೆ.", "cta_issue": "📍 ಸ್ಥಳೀಯ ಸಮಸ್ಯೆ ಹಂಚಿಕೊಳ್ಳಿ", "cta_dashboard": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್ ನೋಡಿ", "stat1_val": "28+", "stat1_label": "ಭಾಷೆಗಳು", "stat2_val": "BRICS", "stat2_label": "ರಾಷ್ಟ್ರಗಳು", "stat3_val": "AI", "stat3_label": "ಚಾಲಿತ", "stat4_val": "ರಿಯಲ್", "stat4_label": "ಟೈಮ್", "how_title": "ಜನಸೇತು ಹೇಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ", "s1_title": "ಸಮಸ್ಯೆ ವರದಿ ಮಾಡಿ", "s1_desc": "ಯಾವುದೇ ಭಾಷೆಯಲ್ಲಿ.", "s2_title": "AI ಅರ್ಥಮಾಡಿಕೊಳ್ಳುತ್ತದೆ", "s2_desc": "Gemini ಅನುವಾದ ಮಾಡುತ್ತದೆ.", "s3_title": "ಗುಂಪುಗಳು ರಚನೆಯಾಗುತ್ತವೆ", "s3_desc": "ಇದೇ ರೀತಿಯ ಸಮಸ್ಯೆಗಳು ಸೇರುತ್ತವೆ.", "s4_title": "ನೀತಿ ಕ್ರಮ", "s4_desc": "ನೀತಿ ನಿರ್ಮಾತರು ಆದ್ಯತೆ ನೋಡುತ್ತಾರೆ.", "sectors_title": "ನಾವು ಒಳಗೊಳ್ಳುವ ಸಮಸ್ಯೆಗಳು", "footer_tag": "ಡಿಜಿಟಲ್ ಸಾರ್ವಜನಿಕ ಒಳಿತು · BRICS ರಾಷ್ಟ್ರಗಳಿಗಾಗಿ", "modal_title": "ಸ್ಥಳೀಯ ಸಮಸ್ಯೆ ಹಂಚಿಕೊಳ್ಳಿ", "modal_name": "ನಿಮ್ಮ ಹೆಸರು (ಐಚ್ಛಿಕ)", "modal_district": "ನಿಮ್ಮ ಜಿಲ್ಲೆ", "modal_sector": "ಸಮಸ್ಯೆ ವರ್ಗ", "modal_desc": "ನಿಮ್ಮ ಸಮಸ್ಯೆ ವಿವರಿಸಿ", "modal_urgency": "ತುರ್ತು", "modal_submit": "ಸಮಸ್ಯೆ ಸಲ್ಲಿಸಿ", "modal_success": "✅ ನಿಮ್ಮ ಸಮಸ್ಯೆ ಸಲ್ಲಿಸಲಾಗಿದೆ. ಧನ್ಯವಾದ."},
    "മലയാളം": {"nav_home": "ഹോം", "nav_about": "ഞങ്ങളെക്കുറിച്ച്", "nav_services": "സേവനങ്ങൾ", "hero_tag": "ഡിജിറ്റൽ പൊതു അടിസ്ഥാന സൗകര്യം · BRICS സംരംഭം", "hero_title": "നിങ്ങളുടെ ശബ്ദം രാഷ്ട്രം നിർമ്മിക്കുന്നു", "hero_sub": "ജൻസേതു പൗരന്മാരുടെ വികസന അഭ്യർത്ഥനകൾ നേരിട്ട് നയരൂപകർത്താക്കൾക്ക് എത്തിക്കുന്നു.", "cta_issue": "📍 പ്രാദേശിക പ്രശ്നം പങ്കിടുക", "cta_dashboard": "ഡാഷ്ബോർഡ് കാണുക", "stat1_val": "28+", "stat1_label": "ഭാഷകൾ", "stat2_val": "BRICS", "stat2_label": "രാഷ്ട്രങ്ങൾ", "stat3_val": "AI", "stat3_label": "ഓടുന്നു", "stat4_val": "റിയൽ", "stat4_label": "ടൈം", "how_title": "ജൻസേതു എങ്ങനെ പ്രവർത്തിക്കുന്നു", "s1_title": "പ്രശ്നം റിപ്പോർട്ട് ചെയ്യുക", "s1_desc": "ഏത് ഭാഷയിലും.", "s2_title": "AI മനസ്സിലാക്കുന്നു", "s2_desc": "Gemini വിവർത്തനം ചെയ്യുന്നു.", "s3_title": "ക്ലസ്റ്ററുകൾ രൂപപ്പെടുന്നു", "s3_desc": "സമാന പ്രശ്നങ്ങൾ ഒന്നിക്കുന്നു.", "s4_title": "നയ നടപടി", "s4_desc": "നയരൂപകർത്താക്കൾ മുൻഗണനകൾ കാണുന്നു.", "sectors_title": "ഞങ്ങൾ ഉൾക്കൊള്ളുന്ന പ്രശ്നങ്ങൾ", "footer_tag": "ഒരു ഡിജിറ്റൽ പൊതു നന്മ · BRICS രാഷ്ട്രങ്ങൾക്ക് വേണ്ടി", "modal_title": "പ്രാദേശിക പ്രശ്നം പങ്കിടുക", "modal_name": "നിങ്ങളുടെ പേര് (ഐച്ഛികം)", "modal_district": "നിങ്ങളുടെ ജില്ല", "modal_sector": "പ്രശ്ന വിഭാഗം", "modal_desc": "നിങ്ങളുടെ പ്രശ്നം വിവരിക്കുക", "modal_urgency": "അടിയന്തിരത", "modal_submit": "പ്രശ്നം സമർപ്പിക്കുക", "modal_success": "✅ നിങ്ങളുടെ പ്രശ്നം സമർപ്പിച്ചു. നന്ദി."},
    "Français": {"nav_home": "Accueil", "nav_about": "À propos", "nav_services": "Services", "hero_tag": "Infrastructure Publique Numérique · Initiative BRICS", "hero_title": "Votre Voix Construit la Nation", "hero_sub": "JanSetu relie les demandes de développement des citoyens directement aux décideurs politiques.", "cta_issue": "📍 Signaler un Problème Local", "cta_dashboard": "Voir le Tableau de Bord", "stat1_val": "28+", "stat1_label": "Langues", "stat2_val": "BRICS", "stat2_label": "Nations", "stat3_val": "IA", "stat3_label": "Propulsé", "stat4_val": "Temps", "stat4_label": "Réel", "how_title": "Comment fonctionne JanSetu", "s1_title": "Soumettez votre problème", "s1_desc": "Voix ou texte, dans n'importe quelle langue.", "s2_title": "L'IA comprend", "s2_desc": "Gemini traduit et classe automatiquement.", "s3_title": "Des clusters se forment", "s3_desc": "Des problèmes similaires se regroupent.", "s4_title": "Action politique", "s4_desc": "Les décideurs voient les priorités cartographiées.", "sectors_title": "Problèmes que nous couvrons", "footer_tag": "Un Bien Public Numérique · Construit pour les Nations BRICS", "modal_title": "Signaler un Problème Local", "modal_name": "Votre nom (optionnel)", "modal_district": "Votre district", "modal_sector": "Catégorie du problème", "modal_desc": "Décrivez votre problème", "modal_urgency": "Urgence", "modal_submit": "Soumettre le problème", "modal_success": "✅ Votre problème a été soumis. Merci."},
    "Español": {"nav_home": "Inicio", "nav_about": "Acerca de", "nav_services": "Servicios", "hero_tag": "Infraestructura Pública Digital · Iniciativa BRICS", "hero_title": "Tu Voz Construye la Nación", "hero_sub": "JanSetu conecta las solicitudes de desarrollo de los ciudadanos directamente con los responsables de políticas.", "cta_issue": "📍 Compartir un Problema Local", "cta_dashboard": "Ver Panel", "stat1_val": "28+", "stat1_label": "Idiomas", "stat2_val": "BRICS", "stat2_label": "Naciones", "stat3_val": "IA", "stat3_label": "Impulsado", "stat4_val": "Tiempo", "stat4_label": "Real", "how_title": "Cómo funciona JanSetu", "s1_title": "Envíe su problema", "s1_desc": "Voz o texto, en cualquier idioma.", "s2_title": "La IA entiende", "s2_desc": "Gemini traduce y clasifica automáticamente.", "s3_title": "Se forman clústeres", "s3_desc": "Problemas similares se agrupan.", "s4_title": "Acción política", "s4_desc": "Los responsables ven prioridades mapeadas.", "sectors_title": "Problemas que cubrimos", "footer_tag": "Un Bien Público Digital · Construido para las Naciones BRICS", "modal_title": "Compartir un Problema Local", "modal_name": "Su nombre (opcional)", "modal_district": "Su distrito", "modal_sector": "Categoría del problema", "modal_desc": "Describa su problema", "modal_urgency": "Urgencia", "modal_submit": "Enviar problema", "modal_success": "✅ Su problema ha sido enviado. Gracias."},
    "Deutsch": {"nav_home": "Startseite", "nav_about": "Über uns", "nav_services": "Dienste", "hero_tag": "Digitale öffentliche Infrastruktur · BRICS-Initiative", "hero_title": "Ihre Stimme baut die Nation", "hero_sub": "JanSetu verbindet Entwicklungsanfragen der Bürger direkt mit politischen Entscheidungsträgern.", "cta_issue": "📍 Lokales Problem melden", "cta_dashboard": "Dashboard anzeigen", "stat1_val": "28+", "stat1_label": "Sprachen", "stat2_val": "BRICS", "stat2_label": "Nationen", "stat3_val": "KI", "stat3_label": "Betrieben", "stat4_val": "Echt", "stat4_label": "Zeit", "how_title": "Wie JanSetu funktioniert", "s1_title": "Problem melden", "s1_desc": "Sprache oder Text, in jeder Sprache.", "s2_title": "KI versteht", "s2_desc": "Gemini übersetzt und klassifiziert.", "s3_title": "Cluster bilden sich", "s3_desc": "Ähnliche Probleme gruppieren sich.", "s4_title": "Politische Maßnahmen", "s4_desc": "Entscheidungsträger sehen Prioritäten.", "sectors_title": "Probleme, die wir abdecken", "footer_tag": "Ein digitales öffentliches Gut · Für BRICS-Nationen gebaut", "modal_title": "Lokales Problem melden", "modal_name": "Ihr Name (optional)", "modal_district": "Ihr Bezirk", "modal_sector": "Problemkategorie", "modal_desc": "Beschreiben Sie Ihr Problem", "modal_urgency": "Dringlichkeit", "modal_submit": "Problem einreichen", "modal_success": "✅ Ihr Problem wurde eingereicht. Danke."},
    "日本語": {"nav_home": "ホーム", "nav_about": "私たちについて", "nav_services": "サービス", "hero_tag": "デジタル公共インフラ · BRICS イニシアティブ", "hero_title": "あなたの声が国を作る", "hero_sub": "JanSetuは市民の開発要求を政策立案者に直接届けます。", "cta_issue": "📍 地域の問題を共有", "cta_dashboard": "ダッシュボードを見る", "stat1_val": "28+", "stat1_label": "言語", "stat2_val": "BRICS", "stat2_label": "国家", "stat3_val": "AI", "stat3_label": "搭載", "stat4_val": "リアル", "stat4_label": "タイム", "how_title": "JanSetuの仕組み", "s1_title": "問題を報告", "s1_desc": "任意の言語で音声またはテキスト。", "s2_title": "AIが理解", "s2_desc": "Geminiが翻訳・分類します。", "s3_title": "クラスターが形成", "s3_desc": "類似の問題がグループ化されます。", "s4_title": "政策行動", "s4_desc": "政策立案者が優先事項を確認。", "sectors_title": "対応する問題", "footer_tag": "デジタル公共財 · BRICS諸国のために構築", "modal_title": "地域の問題を共有", "modal_name": "お名前（任意）", "modal_district": "あなたの地区", "modal_sector": "問題のカテゴリ", "modal_desc": "問題を説明してください", "modal_urgency": "緊急度", "modal_submit": "問題を送信", "modal_success": "✅ 問題が送信されました。ありがとうございます。"},
    "한국어": {"nav_home": "홈", "nav_about": "소개", "nav_services": "서비스", "hero_tag": "디지털 공공 인프라 · BRICS 이니셔티브", "hero_title": "당신의 목소리가 국가를 만든다", "hero_sub": "JanSetu는 시민의 개발 요청을 정책 입안자에게 직접 전달합니다.", "cta_issue": "📍 지역 문제 공유", "cta_dashboard": "대시보드 보기", "stat1_val": "28+", "stat1_label": "언어", "stat2_val": "BRICS", "stat2_label": "국가", "stat3_val": "AI", "stat3_label": "구동", "stat4_val": "실시간", "stat4_label": "데이터", "how_title": "JanSetu 작동 방식", "s1_title": "문제 보고", "s1_desc": "모든 언어로 음성 또는 텍스트.", "s2_title": "AI 이해", "s2_desc": "Gemini가 번역 및 분류합니다.", "s3_title": "클러스터 형성", "s3_desc": "유사한 문제가 그룹화됩니다.", "s4_title": "정책 조치", "s4_desc": "정책 입안자가 우선순위를 봅니다.", "sectors_title": "다루는 문제", "footer_tag": "디지털 공공재 · BRICS 국가를 위해 구축", "modal_title": "지역 문제 공유", "modal_name": "이름 (선택사항)", "modal_district": "지역구", "modal_sector": "문제 카테고리", "modal_desc": "문제를 설명하세요", "modal_urgency": "긴급도", "modal_submit": "문제 제출", "modal_success": "✅ 문제가 제출되었습니다. 감사합니다."},
    "Bahasa Indonesia": {"nav_home": "Beranda", "nav_about": "Tentang", "nav_services": "Layanan", "hero_tag": "Infrastruktur Publik Digital · Inisiatif BRICS", "hero_title": "Suara Anda Membangun Bangsa", "hero_sub": "JanSetu menghubungkan permintaan pembangunan warga langsung ke pembuat kebijakan.", "cta_issue": "📍 Laporkan Masalah Lokal", "cta_dashboard": "Lihat Dasbor", "stat1_val": "28+", "stat1_label": "Bahasa", "stat2_val": "BRICS", "stat2_label": "Negara", "stat3_val": "AI", "stat3_label": "Didukung", "stat4_val": "Real", "stat4_label": "Time", "how_title": "Cara Kerja JanSetu", "s1_title": "Laporkan Masalah", "s1_desc": "Suara atau teks, dalam bahasa apa pun.", "s2_title": "AI Memahami", "s2_desc": "Gemini menerjemahkan dan mengklasifikasikan.", "s3_title": "Cluster Terbentuk", "s3_desc": "Masalah serupa dikelompokkan.", "s4_title": "Tindakan Kebijakan", "s4_desc": "Pembuat kebijakan melihat prioritas.", "sectors_title": "Masalah yang Kami Tangani", "footer_tag": "Barang Publik Digital · Dibangun untuk Negara BRICS", "modal_title": "Laporkan Masalah Lokal", "modal_name": "Nama Anda (opsional)", "modal_district": "Distrik Anda", "modal_sector": "Kategori Masalah", "modal_desc": "Jelaskan masalah Anda", "modal_urgency": "Urgensi", "modal_submit": "Kirim Masalah", "modal_success": "✅ Masalah Anda telah dikirim. Terima kasih."},
    "Kiswahili": {"nav_home": "Nyumbani", "nav_about": "Kuhusu", "nav_services": "Huduma", "hero_tag": "Miundombinu ya Umma ya Dijitali · Mpango wa BRICS", "hero_title": "Sauti Yako Inajenga Taifa", "hero_sub": "JanSetu inaunganisha maombi ya maendeleo ya raia moja kwa moja kwa watunga sera.", "cta_issue": "📍 Shiriki Tatizo la Mtaa", "cta_dashboard": "Tazama Dashibodi", "stat1_val": "28+", "stat1_label": "Lugha", "stat2_val": "BRICS", "stat2_label": "Mataifa", "stat3_val": "AI", "stat3_label": "Inayoendeshwa", "stat4_val": "Wakati", "stat4_label": "Halisi", "how_title": "Jinsi JanSetu Inavyofanya Kazi", "s1_title": "Wasilisha Tatizo", "s1_desc": "Sauti au maandishi, kwa lugha yoyote.", "s2_title": "AI Inaelewa", "s2_desc": "Gemini inatafsiri na kuainisha.", "s3_title": "Makundi Yanaunda", "s3_desc": "Matatizo yanayofanana yanakusanyika.", "s4_title": "Hatua ya Sera", "s4_desc": "Watunga sera wanaona vipaumbele.", "sectors_title": "Matatizo Tunayoshughulikia", "footer_tag": "Bidhaa ya Umma ya Dijitali · Imejengwa kwa Mataifa ya BRICS", "modal_title": "Shiriki Tatizo la Mtaa", "modal_name": "Jina lako (hiari)", "modal_district": "Wilaya yako", "modal_sector": "Aina ya Tatizo", "modal_desc": "Elezea tatizo lako", "modal_urgency": "Uharaka", "modal_submit": "Wasilisha Tatizo", "modal_success": "✅ Tatizo lako limewasilishwa. Asante."},
    "Türkçe": {"nav_home": "Ana Sayfa", "nav_about": "Hakkımızda", "nav_services": "Hizmetler", "hero_tag": "Dijital Kamu Altyapısı · BRICS Girişimi", "hero_title": "Sesiniz Milleti İnşa Eder", "hero_sub": "JanSetu, vatandaşların kalkınma taleplerini doğrudan politika yapıcılara iletir.", "cta_issue": "📍 Yerel Sorunu Paylaş", "cta_dashboard": "Paneli Görüntüle", "stat1_val": "28+", "stat1_label": "Dil", "stat2_val": "BRICS", "stat2_label": "Ülke", "stat3_val": "AI", "stat3_label": "Destekli", "stat4_val": "Gerçek", "stat4_label": "Zaman", "how_title": "JanSetu Nasıl Çalışır", "s1_title": "Sorunu Bildirin", "s1_desc": "Herhangi bir dilde ses veya metin.", "s2_title": "AI Anlar", "s2_desc": "Gemini çevirir ve sınıflandırır.", "s3_title": "Kümeler Oluşur", "s3_desc": "Benzer sorunlar gruplandırılır.", "s4_title": "Politika Eylemi", "s4_desc": "Politika yapıcılar öncelikleri görür.", "sectors_title": "Kapsadığımız Sorunlar", "footer_tag": "Dijital Kamu Malı · BRICS Ulusları İçin İnşa Edildi", "modal_title": "Yerel Sorunu Paylaş", "modal_name": "Adınız (isteğe bağlı)", "modal_district": "İlçeniz", "modal_sector": "Sorun Kategorisi", "modal_desc": "Sorununuzu açıklayın", "modal_urgency": "Aciliyet", "modal_submit": "Sorunu Gönder", "modal_success": "✅ Sorununuz gönderildi. Teşekkürler."},
    "العربية": {"nav_home": "الرئيسية", "nav_about": "عنّا", "nav_services": "الخدمات", "hero_tag": "البنية التحتية الرقمية العامة · مبادرة BRICS", "hero_title": "صوتك يبني الأمة", "hero_sub": "جانسيتو يربط طلبات التنمية من المواطنين مباشرةً بصانعي السياسات.", "cta_issue": "📍 شارك مشكلة محلية", "cta_dashboard": "عرض لوحة التحكم", "stat1_val": "+28", "stat1_label": "لغة", "stat2_val": "BRICS", "stat2_label": "أمم", "stat3_val": "ذكاء اصطناعي", "stat3_label": "مدعوم", "stat4_val": "وقت", "stat4_label": "فعلي", "how_title": "كيف يعمل جانسيتو", "s1_title": "أرسل مشكلتك", "s1_desc": "صوت أو نص بأي لغة.", "s2_title": "الذكاء الاصطناعي يفهم", "s2_desc": "Gemini يترجم ويصنف تلقائياً.", "s3_title": "تتشكل المجموعات", "s3_desc": "تتجمع المشكلات المتشابهة.", "s4_title": "إجراء السياسات", "s4_desc": "يرى صانعو السياسات الأولويات.", "sectors_title": "المشكلات التي نغطيها", "footer_tag": "خير عام رقمي · مبني لأمم BRICS", "modal_title": "شارك مشكلة محلية", "modal_name": "اسمك (اختياري)", "modal_district": "منطقتك", "modal_sector": "فئة المشكلة", "modal_desc": "صف مشكلتك", "modal_urgency": "الإلحاح", "modal_submit": "إرسال المشكلة", "modal_success": "✅ تم إرسال مشكلتك. شكراً."},
    "Italiano": {"nav_home": "Home", "nav_about": "Chi siamo", "nav_services": "Servizi", "hero_tag": "Infrastruttura Pubblica Digitale · Iniziativa BRICS", "hero_title": "La Tua Voce Costruisce la Nazione", "hero_sub": "JanSetu collega le richieste di sviluppo dei cittadini direttamente ai responsabili delle politiche.", "cta_issue": "📍 Segnala un Problema Locale", "cta_dashboard": "Visualizza Dashboard", "stat1_val": "28+", "stat1_label": "Lingue", "stat2_val": "BRICS", "stat2_label": "Nazioni", "stat3_val": "IA", "stat3_label": "Alimentato", "stat4_val": "Tempo", "stat4_label": "Reale", "how_title": "Come funziona JanSetu", "s1_title": "Invia il tuo problema", "s1_desc": "Voce o testo, in qualsiasi lingua.", "s2_title": "L'IA capisce", "s2_desc": "Gemini traduce e classifica automaticamente.", "s3_title": "Si formano cluster", "s3_desc": "Problemi simili si raggruppano.", "s4_title": "Azione politica", "s4_desc": "I responsabili vedono le priorità mappate.", "sectors_title": "Problemi che copriamo", "footer_tag": "Un Bene Pubblico Digitale · Costruito per le Nazioni BRICS", "modal_title": "Segnala un Problema Locale", "modal_name": "Il tuo nome (opzionale)", "modal_district": "Il tuo distretto", "modal_sector": "Categoria del problema", "modal_desc": "Descrivi il tuo problema", "modal_urgency": "Urgenza", "modal_submit": "Invia problema", "modal_success": "✅ Il tuo problema è stato inviato. Grazie."},
    "Polski": {"nav_home": "Strona główna", "nav_about": "O nas", "nav_services": "Usługi", "hero_tag": "Cyfrowa Infrastruktura Publiczna · Inicjatywa BRICS", "hero_title": "Twój Głos Buduje Naród", "hero_sub": "JanSetu łączy prośby obywateli o rozwój bezpośrednio z decydentami.", "cta_issue": "📍 Zgłoś Lokalny Problem", "cta_dashboard": "Zobacz Panel", "stat1_val": "28+", "stat1_label": "Języki", "stat2_val": "BRICS", "stat2_label": "Narody", "stat3_val": "AI", "stat3_label": "Zasilany", "stat4_val": "Czas", "stat4_label": "Rzeczywisty", "how_title": "Jak działa JanSetu", "s1_title": "Zgłoś problem", "s1_desc": "Głos lub tekst w dowolnym języku.", "s2_title": "AI rozumie", "s2_desc": "Gemini tłumaczy i klasyfikuje.", "s3_title": "Tworzą się klastry", "s3_desc": "Podobne problemy grupują się.", "s4_title": "Działanie polityczne", "s4_desc": "Decydenci widzą priorytety.", "sectors_title": "Problemy, które obejmujemy", "footer_tag": "Cyfrowe Dobro Publiczne · Zbudowane dla Narodów BRICS", "modal_title": "Zgłoś Lokalny Problem", "modal_name": "Twoje imię (opcjonalne)", "modal_district": "Twój okręg", "modal_sector": "Kategoria problemu", "modal_desc": "Opisz swój problem", "modal_urgency": "Pilność", "modal_submit": "Wyślij problem", "modal_success": "✅ Twój problem został wysłany. Dziękujemy."},
}

SECTORS = [
    "Roads & Transport", "Air Quality / Dust", "Water Supply",
    "Electricity", "Sanitation", "Health", "Education",
    "Industrial Pollution", "Housing", "Agriculture", "Digital Connectivity"
]

URGENCY_LEVELS = ["Low", "Medium", "High", "Critical"]

# ── session state init ────────────────────────────────────────
if "lang" not in st.session_state:
    st.session_state.lang = "English"
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "show_modal" not in st.session_state:
    st.session_state.show_modal = False
if "submitted" not in st.session_state:
    st.session_state.submitted = False

L = LANGUAGES[st.session_state.lang]
rtl_langs = {"اردو", "العربية"}
is_rtl = st.session_state.lang in rtl_langs

# ── CSS ───────────────────────────────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans:wght@400;600;700&display=swap');

/* ── reset & base ── */
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

.stApp {{ background: #F5F6FA; }}

/* hide streamlit chrome */
#MainMenu, footer, header {{ visibility: hidden; }}
.stDeployButton {{ display: none; }}
[data-testid="stSidebar"] {{ display: none; }}
.block-container {{ padding: 0 !important; max-width: 100% !important; }}
div[data-testid="stVerticalBlock"] > div {{ padding: 0; }}

/* ── typography ── */
:root {{
  --navy:   #0A1628;
  --indigo: #1B3A6B;
  --blue:   #1E56A0;
  --sky:    #3B82F6;
  --saffron:#F97316;
  --gold:   #FBBF24;
  --white:  #FFFFFF;
  --slate:  #64748B;
  --light:  #F5F6FA;
  --card:   #FFFFFF;
  --border: #E2E8F0;
  --green:  #16A34A;
}}

body, .stApp {{ font-family: 'Inter', 'Noto Sans', sans-serif; }}

/* ── NAV ── */
.js-nav {{
  background: var(--navy);
  padding: 0 5vw;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 16px rgba(0,0,0,0.18);
  direction: {'rtl' if is_rtl else 'ltr'};
}}
.js-logo {{
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--white);
  letter-spacing: -0.5px;
  display: flex;
  align-items: center;
  gap: 8px;
}}
.js-logo span {{ color: var(--saffron); }}
.js-nav-links {{
  display: flex;
  gap: 8px;
  align-items: center;
}}
.js-nav-btn {{
  background: none;
  border: none;
  color: rgba(255,255,255,0.75);
  font-size: 0.92rem;
  font-weight: 500;
  padding: 8px 18px;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
  font-family: 'Inter', sans-serif;
}}
.js-nav-btn:hover {{ color: #fff; background: rgba(255,255,255,0.08); }}
.js-nav-btn.active {{ color: #fff; background: var(--blue); }}

/* ── HERO ── */
.js-hero {{
  background: linear-gradient(135deg, var(--navy) 0%, var(--indigo) 55%, #163561 100%);
  min-height: 92vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 80px 5vw 100px;
  position: relative;
  overflow: hidden;
  direction: {'rtl' if is_rtl else 'ltr'};
}}
.js-hero::before {{
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 70% 40%, rgba(59,130,246,0.18) 0%, transparent 60%),
              radial-gradient(ellipse at 20% 80%, rgba(249,115,22,0.10) 0%, transparent 50%);
  pointer-events: none;
}}
.js-ashoka-wheel {{
  position: absolute;
  right: -60px;
  top: 50%;
  transform: translateY(-50%);
  width: 420px;
  height: 420px;
  opacity: 0.04;
  font-size: 420px;
  line-height: 1;
  pointer-events: none;
  user-select: none;
}}
.js-hero-tag {{
  display: inline-block;
  background: rgba(59,130,246,0.18);
  border: 1px solid rgba(59,130,246,0.35);
  color: #93C5FD;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  padding: 6px 18px;
  border-radius: 100px;
  margin-bottom: 28px;
}}
.js-hero h1 {{
  font-size: clamp(2.2rem, 5vw, 3.8rem);
  font-weight: 800;
  color: var(--white);
  line-height: 1.12;
  margin-bottom: 20px;
  letter-spacing: -1px;
}}
.js-hero h1 span {{ color: var(--saffron); }}
.js-hero p {{
  font-size: clamp(1rem, 2vw, 1.18rem);
  color: rgba(255,255,255,0.72);
  max-width: 640px;
  margin: 0 auto 40px;
  line-height: 1.7;
}}
.js-hero-btns {{
  display: flex;
  gap: 16px;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 64px;
}}
.js-btn-primary {{
  background: var(--saffron);
  color: var(--navy);
  border: none;
  padding: 14px 32px;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
  font-family: 'Inter', sans-serif;
  box-shadow: 0 4px 20px rgba(249,115,22,0.35);
}}
.js-btn-primary:hover {{ background: #EA6C00; transform: translateY(-2px); box-shadow: 0 8px 28px rgba(249,115,22,0.45); }}
.js-btn-secondary {{
  background: rgba(255,255,255,0.08);
  color: var(--white);
  border: 1.5px solid rgba(255,255,255,0.25);
  padding: 14px 32px;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  font-family: 'Inter', sans-serif;
}}
.js-btn-secondary:hover {{ background: rgba(255,255,255,0.15); border-color: rgba(255,255,255,0.5); }}

/* ── STATS BAR ── */
.js-stats {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1px;
  background: rgba(255,255,255,0.08);
  border-top: 1px solid rgba(255,255,255,0.10);
  width: 100%;
  max-width: 860px;
  margin: 0 auto;
  border-radius: 12px;
  overflow: hidden;
}}
.js-stat {{
  padding: 24px 16px;
  text-align: center;
  background: rgba(255,255,255,0.05);
}}
.js-stat-val {{
  font-size: 2rem;
  font-weight: 800;
  color: var(--saffron);
  display: block;
  line-height: 1;
  margin-bottom: 6px;
}}
.js-stat-label {{
  font-size: 0.78rem;
  color: rgba(255,255,255,0.55);
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 500;
}}

/* ── FLOATING CTA ── */
.js-floating {{
  position: fixed;
  bottom: 32px;
  right: 32px;
  z-index: 999;
  background: var(--saffron);
  color: var(--navy);
  border: none;
  padding: 16px 28px;
  border-radius: 100px;
  font-size: 0.95rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 8px 32px rgba(249,115,22,0.5);
  transition: all 0.25s;
  font-family: 'Inter', sans-serif;
  display: flex;
  align-items: center;
  gap: 8px;
  animation: pulse-ring 2.5s ease infinite;
}}
.js-floating:hover {{
  transform: translateY(-3px) scale(1.04);
  box-shadow: 0 14px 40px rgba(249,115,22,0.6);
  background: #EA6C00;
}}
@keyframes pulse-ring {{
  0%, 100% {{ box-shadow: 0 8px 32px rgba(249,115,22,0.5); }}
  50% {{ box-shadow: 0 8px 48px rgba(249,115,22,0.8), 0 0 0 10px rgba(249,115,22,0.08); }}
}}

/* ── SECTION ── */
.js-section {{
  padding: 80px 5vw;
  direction: {'rtl' if is_rtl else 'ltr'};
}}
.js-section-title {{
  font-size: clamp(1.6rem, 3vw, 2.2rem);
  font-weight: 800;
  color: var(--navy);
  text-align: center;
  margin-bottom: 12px;
  letter-spacing: -0.5px;
}}
.js-section-sub {{
  text-align: center;
  color: var(--slate);
  font-size: 1.05rem;
  margin-bottom: 56px;
  max-width: 560px;
  margin-left: auto;
  margin-right: auto;
}}

/* ── HOW IT WORKS ── */
.js-steps {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 24px;
  max-width: 1000px;
  margin: 0 auto;
}}
.js-step {{
  background: var(--card);
  border: 1.5px solid var(--border);
  border-radius: 16px;
  padding: 32px 24px;
  position: relative;
  transition: all 0.25s;
}}
.js-step:hover {{
  border-color: var(--sky);
  box-shadow: 0 8px 32px rgba(30,86,160,0.10);
  transform: translateY(-4px);
}}
.js-step-num {{
  width: 42px;
  height: 42px;
  background: var(--blue);
  color: white;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 1.1rem;
  margin-bottom: 20px;
}}
.js-step h3 {{
  font-size: 1rem;
  font-weight: 700;
  color: var(--navy);
  margin-bottom: 10px;
}}
.js-step p {{
  font-size: 0.88rem;
  color: var(--slate);
  line-height: 1.6;
}}

/* ── SECTORS ── */
.js-sectors-grid {{
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  justify-content: center;
  max-width: 860px;
  margin: 0 auto;
}}
.js-sector-pill {{
  background: var(--card);
  border: 1.5px solid var(--border);
  border-radius: 100px;
  padding: 10px 22px;
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--indigo);
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.2s;
}}
.js-sector-pill:hover {{
  background: var(--blue);
  color: white;
  border-color: var(--blue);
  transform: translateY(-2px);
}}

/* ── ABOUT PAGE ── */
.js-about-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  max-width: 1000px;
  margin: 0 auto;
  align-items: start;
}}
.js-about-text h2 {{
  font-size: 2rem;
  font-weight: 800;
  color: var(--navy);
  margin-bottom: 20px;
  letter-spacing: -0.5px;
}}
.js-about-text p {{
  color: var(--slate);
  line-height: 1.8;
  margin-bottom: 16px;
  font-size: 0.98rem;
}}
.js-badge {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #EFF6FF;
  color: var(--blue);
  border: 1px solid #BFDBFE;
  padding: 6px 16px;
  border-radius: 100px;
  font-size: 0.82rem;
  font-weight: 600;
  margin: 4px;
}}
.js-about-cards {{
  display: flex;
  flex-direction: column;
  gap: 16px;
}}
.js-about-card {{
  background: var(--card);
  border: 1.5px solid var(--border);
  border-radius: 14px;
  padding: 24px;
  border-left: 4px solid var(--saffron);
}}
.js-about-card h4 {{
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--navy);
  margin-bottom: 8px;
}}
.js-about-card p {{
  font-size: 0.85rem;
  color: var(--slate);
  line-height: 1.6;
}}

/* ── SERVICES PAGE ── */
.js-services-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  max-width: 1100px;
  margin: 0 auto;
}}
.js-service-card {{
  background: var(--card);
  border: 1.5px solid var(--border);
  border-radius: 18px;
  padding: 36px 28px;
  transition: all 0.25s;
  position: relative;
  overflow: hidden;
}}
.js-service-card::before {{
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--blue), var(--saffron));
}}
.js-service-card:hover {{
  box-shadow: 0 12px 40px rgba(30,86,160,0.12);
  transform: translateY(-5px);
}}
.js-service-icon {{
  font-size: 2.4rem;
  margin-bottom: 20px;
  display: block;
}}
.js-service-card h3 {{
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--navy);
  margin-bottom: 12px;
}}
.js-service-card p {{
  font-size: 0.88rem;
  color: var(--slate);
  line-height: 1.7;
}}

/* ── MODAL ── */
.js-modal-overlay {{
  position: fixed;
  inset: 0;
  background: rgba(10,22,40,0.75);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  backdrop-filter: blur(4px);
}}
.js-modal {{
  background: var(--white);
  border-radius: 20px;
  padding: 40px;
  width: 100%;
  max-width: 520px;
  box-shadow: 0 24px 80px rgba(0,0,0,0.25);
  direction: {'rtl' if is_rtl else 'ltr'};
}}
.js-modal h2 {{
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--navy);
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  gap: 10px;
}}
.js-success {{
  background: #F0FDF4;
  border: 1.5px solid #86EFAC;
  border-radius: 12px;
  padding: 20px;
  color: var(--green);
  font-weight: 600;
  font-size: 1rem;
  text-align: center;
}}

/* ── BRICS STRIP ── */
.js-brics {{
  background: var(--navy);
  padding: 40px 5vw;
  text-align: center;
}}
.js-brics-title {{
  color: rgba(255,255,255,0.5);
  font-size: 0.75rem;
  letter-spacing: 2px;
  text-transform: uppercase;
  margin-bottom: 20px;
  font-weight: 600;
}}
.js-brics-flags {{
  display: flex;
  gap: 24px;
  justify-content: center;
  flex-wrap: wrap;
  align-items: center;
}}
.js-brics-item {{
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  opacity: 0.7;
  transition: opacity 0.2s;
}}
.js-brics-item:hover {{ opacity: 1; }}
.js-brics-flag {{ font-size: 2.2rem; }}
.js-brics-name {{
  font-size: 0.72rem;
  color: rgba(255,255,255,0.6);
  font-weight: 500;
  letter-spacing: 0.5px;
}}

/* ── FOOTER ── */
.js-footer {{
  background: #060E1C;
  padding: 32px 5vw;
  text-align: center;
  direction: {'rtl' if is_rtl else 'ltr'};
}}
.js-footer-brand {{
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--white);
  margin-bottom: 8px;
}}
.js-footer-brand span {{ color: var(--saffron); }}
.js-footer-sub {{
  font-size: 0.82rem;
  color: rgba(255,255,255,0.35);
  margin-bottom: 16px;
}}
.js-footer-links {{
  display: flex;
  gap: 20px;
  justify-content: center;
  margin-bottom: 20px;
}}
.js-footer-link {{
  font-size: 0.82rem;
  color: rgba(255,255,255,0.45);
  text-decoration: none;
  transition: color 0.2s;
}}
.js-footer-link:hover {{ color: rgba(255,255,255,0.8); }}
.js-copy {{
  font-size: 0.75rem;
  color: rgba(255,255,255,0.2);
}}

/* ── RESPONSIVE ── */
@media (max-width: 768px) {{
  .js-stats {{ grid-template-columns: repeat(2, 1fr); }}
  .js-hero {{ min-height: 85vh; padding: 60px 5vw 80px; }}
  .js-about-grid {{ grid-template-columns: 1fr; gap: 32px; }}
  .js-nav-links {{ gap: 0; }}
  .js-nav-btn {{ padding: 8px 10px; font-size: 0.82rem; }}
  .js-floating {{ bottom: 20px; right: 20px; padding: 13px 20px; font-size: 0.88rem; }}
  .js-modal {{ padding: 28px 20px; }}
  .js-section {{ padding: 56px 4vw; }}
}}
@media (max-width: 480px) {{
  .js-stats {{ grid-template-columns: repeat(2, 1fr); }}
  .js-hero h1 {{ font-size: 1.9rem; }}
  .js-hero-btns {{ flex-direction: column; align-items: center; }}
  .js-btn-primary, .js-btn-secondary {{ width: 100%; max-width: 300px; }}
}}
</style>
""", unsafe_allow_html=True)

# ── LANGUAGE PICKER ──────────────────────────────────────────
with st.container():
    lang_col, _ = st.columns([2, 8])
    with lang_col:
        chosen = st.selectbox(
            "🌐",
            list(LANGUAGES.keys()),
            index=list(LANGUAGES.keys()).index(st.session_state.lang),
            label_visibility="collapsed",
            key="lang_picker"
        )
        if chosen != st.session_state.lang:
            st.session_state.lang = chosen
            st.rerun()

L = LANGUAGES[st.session_state.lang]

# ── NAV ──────────────────────────────────────────────────────
st.markdown(f"""
<div class="js-nav">
  <div class="js-logo">🌉 Jan<span>Setu</span></div>
  <div class="js-nav-links" id="nav-links"></div>
</div>
""", unsafe_allow_html=True)

nav_c1, nav_c2, nav_c3 = st.columns([1, 1, 1])
with nav_c1:
    if st.button(L["nav_home"], key="nav_home",
                 type="primary" if st.session_state.page == "Home" else "secondary",
                 use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()
with nav_c2:
    if st.button(L["nav_about"], key="nav_about",
                 type="primary" if st.session_state.page == "About" else "secondary",
                 use_container_width=True):
        st.session_state.page = "About"
        st.rerun()
with nav_c3:
    if st.button(L["nav_services"], key="nav_services",
                 type="primary" if st.session_state.page == "Services" else "secondary",
                 use_container_width=True):
        st.session_state.page = "Services"
        st.rerun()

# ══════════════════════════════════════════════════════════════
# PAGE: HOME
# ══════════════════════════════════════════════════════════════
if st.session_state.page == "Home":

    # ── HERO
    st.markdown(f"""
    <div class="js-hero">
      <div class="js-ashoka-wheel">☸</div>
      <div class="js-hero-tag">{L["hero_tag"]}</div>
      <h1>Your Voice <span>Builds</span> the Nation</h1>
      <p>{L["hero_sub"]}</p>
      <div class="js-stats">
        <div class="js-stat"><span class="js-stat-val">{L["stat1_val"]}</span><span class="js-stat-label">{L["stat1_label"]}</span></div>
        <div class="js-stat"><span class="js-stat-val">{L["stat2_val"]}</span><span class="js-stat-label">{L["stat2_label"]}</span></div>
        <div class="js-stat"><span class="js-stat-val">{L["stat3_val"]}</span><span class="js-stat-label">{L["stat3_label"]}</span></div>
        <div class="js-stat"><span class="js-stat-val">{L["stat4_val"]}</span><span class="js-stat-label">{L["stat4_label"]}</span></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── HOW IT WORKS
    st.markdown(f"""
    <div class="js-section" style="background:#fff;">
      <div class="js-section-title">{L["how_title"]}</div>
      <div class="js-steps">
        <div class="js-step"><div class="js-step-num">1</div><h3>{L["s1_title"]}</h3><p>{L["s1_desc"]}</p></div>
        <div class="js-step"><div class="js-step-num">2</div><h3>{L["s2_title"]}</h3><p>{L["s2_desc"]}</p></div>
        <div class="js-step"><div class="js-step-num">3</div><h3>{L["s3_title"]}</h3><p>{L["s3_desc"]}</p></div>
        <div class="js-step"><div class="js-step-num">4</div><h3>{L["s4_title"]}</h3><p>{L["s4_desc"]}</p></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── SECTORS
    sector_icons = ["🛣️","💨","💧","⚡","🚽","🏥","🎓","🏭","🏠","🌾","📡"]
    pills = "".join([
        f'<div class="js-sector-pill">{icon} {s}</div>'
        for icon, s in zip(sector_icons, SECTORS)
    ])
    st.markdown(f"""
    <div class="js-section">
      <div class="js-section-title">{L["sectors_title"]}</div>
      <div class="js-sectors-grid">{pills}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── BRICS NATIONS STRIP
    brics_nations = [
        ("🇧🇷","Brazil"), ("🇷🇺","Russia"), ("🇮🇳","India"),
        ("🇨🇳","China"), ("🇿🇦","S. Africa"), ("🇪🇬","Egypt"),
        ("🇪🇹","Ethiopia"), ("🇮🇷","Iran"), ("🇦🇪","UAE"),
    ]
    flags_html = "".join([
        f'<div class="js-brics-item"><span class="js-brics-flag">{f}</span><span class="js-brics-name">{n}</span></div>'
        for f, n in brics_nations
    ])
    st.markdown(f"""
    <div class="js-brics">
      <div class="js-brics-title">BRICS Nations Connected</div>
      <div class="js-brics-flags">{flags_html}</div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# PAGE: ABOUT
# ══════════════════════════════════════════════════════════════
elif st.session_state.page == "About":
    st.markdown("""
    <div class="js-section" style="background:#fff; min-height:90vh;">
      <div class="js-about-grid">
        <div class="js-about-text">
          <h2>Bridging Citizens<br>to Development</h2>
          <p>JanSetu is a Digital Public Good designed to solve one of governance's oldest problems — the gap between what citizens need and what governments fund.</p>
          <p>Development requests today live in WhatsApp groups, paper forms, and verbal complaints that never reach the right desk. JanSetu changes that — aggregating every voice, in every language, into actionable intelligence for policymakers.</p>
          <p>Built as part of the BRICS Innovation track, JanSetu is designed to be interoperable across nations — the same platform that works in Paradeep, Odisha can work in a township in South Africa or a favela in Brazil.</p>
          <div style="margin-top:24px; display:flex; flex-wrap:wrap; gap:8px;">
            <span class="js-badge">🏛️ Digital Public Good</span>
            <span class="js-badge">🌐 BRICS Initiative</span>
            <span class="js-badge">🤖 Gemini AI</span>
            <span class="js-badge">🔓 Open API</span>
            <span class="js-badge">🗣️ 28+ Languages</span>
          </div>
        </div>
        <div class="js-about-cards">
          <div class="js-about-card">
            <h4>🎯 Mission</h4>
            <p>Make every citizen's development request visible, understood, and actionable — regardless of language, literacy, or location.</p>
          </div>
          <div class="js-about-card">
            <h4>🏗️ Built With</h4>
            <p>Python, Streamlit, Google Gemini 1.5 Flash, sentence-transformers, HDBSCAN, Folium, and ReportLab — fully open source.</p>
          </div>
          <div class="js-about-card">
            <h4>🌍 BRICS Interoperability</h4>
            <p>Federated architecture — each nation runs its own JanSetu node, shares anonymized cluster models across borders.</p>
          </div>
          <div class="js-about-card">
            <h4>👥 Team</h4>
            <p>Built by student developers from Paradeep, Odisha — where dust, traffic and infrastructure gaps are daily lived realities.</p>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# PAGE: SERVICES
# ══════════════════════════════════════════════════════════════
elif st.session_state.page == "Services":
    services = [
        ("🎙️", "Multilingual Voice Input", "Submit issues in your native language by voice. JanSetu transcribes and understands 28+ languages — no typing, no forms, no barriers."),
        ("🧠", "AI-Powered Classification", "Google Gemini automatically translates, extracts the sector, urgency level, and location from every submission — zero manual tagging."),
        ("🔗", "Smart Clustering", "Sentence-transformer embeddings group similar issues from your district together, amplifying the signal from thousands of voices into one clear demand."),
        ("📊", "Need Score Engine", "A composite scoring model fuses citizen demand volume with infrastructure deficit indices and demographic data to rank districts by genuine need — not just noise."),
        ("🗺️", "Hotspot Mapping", "Interactive choropleth maps reveal where development pressure is highest — at district, state, and BRICS-nation level — giving policymakers spatial clarity."),
        ("📄", "Policy Brief Generation", "One-click AI-generated policy briefs summarise the top priority, evidence base, and recommended action — ready for a ministry meeting or a parliamentary brief."),
    ]
    cards = "".join([
        f'<div class="js-service-card"><span class="js-service-icon">{icon}</span><h3>{title}</h3><p>{desc}</p></div>'
        for icon, title, desc in services
    ])
    st.markdown(f"""
    <div class="js-section" style="min-height:90vh;">
      <div class="js-section-title">{L["nav_services"]}</div>
      <div class="js-section-sub">Everything JanSetu does — and why it matters for governance at scale.</div>
      <div class="js-services-grid">{cards}</div>
    </div>
    """, unsafe_allow_html=True)

# ── FOOTER (all pages)
st.markdown(f"""
<div class="js-footer">
  <div class="js-footer-brand">🌉 Jan<span>Setu</span></div>
  <div class="js-footer-sub">{L["footer_tag"]}</div>
  <div class="js-copy">© 2026 JanSetu · Code for Communities 2 · Hack2skill × GDG</div>
</div>
""", unsafe_allow_html=True)

# ── FLOATING BUTTON ──────────────────────────────────────────
st.markdown(f"""
<style>
.js-float-wrap {{
  position: fixed; bottom: 32px; right: 32px; z-index: 999;
}}
</style>
""", unsafe_allow_html=True)

if st.button(f"📍 {L['cta_issue']}", key="floating_cta",
             help="Report a local issue",
             type="primary"):
    st.session_state.show_modal = True
    st.rerun()

# ── MODAL ────────────────────────────────────────────────────
if st.session_state.show_modal:
    st.markdown("""<div class="js-modal-overlay">""", unsafe_allow_html=True)

    with st.container():
        st.markdown(f"""<div class="js-modal">""", unsafe_allow_html=True)

        st.subheader(f"📍 {L['modal_title']}")

        if st.session_state.submitted:
            st.markdown(f"""<div class="js-success">{L["modal_success"]}</div>""", unsafe_allow_html=True)
            if st.button("✕ Close", key="close_success"):
                st.session_state.show_modal = False
                st.session_state.submitted = False
                st.rerun()
        else:
            name = st.text_input(L["modal_name"], placeholder="e.g. Ramesh Kumar", key="m_name")
            district = st.text_input(L["modal_district"], placeholder="e.g. Jagatsinghpur", key="m_district")
            sector = st.selectbox(L["modal_sector"], SECTORS, key="m_sector")
            urgency = st.selectbox(L["modal_urgency"], URGENCY_LEVELS, key="m_urgency")
            desc = st.text_area(L["modal_desc"], height=120,
                                placeholder="Describe the issue in any language...", key="m_desc")

            col_submit, col_cancel = st.columns(2)
            with col_submit:
                if st.button(L["modal_submit"], type="primary",
                             use_container_width=True, key="submit_issue"):
                    if desc.strip():
                        st.session_state.submitted = True
                        st.rerun()
                    else:
                        st.error("Please describe your issue.")
            with col_cancel:
                if st.button("✕ Cancel", use_container_width=True, key="cancel_modal"):
                    st.session_state.show_modal = False
                    st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
