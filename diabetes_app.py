# diabetes_management_app.py
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Page configuration - MUST BE FIRST
st.set_page_config(
    page_title="Diabetes Management Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
if 'user_info' not in st.session_state:
    st.session_state.user_info = {}

def main():
    # Sidebar for user information
    with st.sidebar:
        st.header("👤 User Profile")
        st.session_state.user_info['type'] = st.selectbox(
            "I am a:",
            ["Patient", "Healthcare Professional", "Caregiver", "Student"]
        )
        st.session_state.user_info['experience'] = st.selectbox(
            "Diabetes Experience:",
            ["Newly Diagnosed", "1-5 Years", "5+ Years", "Professional"]
        )
        
        st.markdown("---")
        st.header("📋 Navigation")
        # Simple navigation using markdown
        st.markdown("""
        **Main Sections:**
        - 🏠 Dashboard
        - 📊 Health Overview  
        - 💬 Clinical Q&A
        - 📚 Resources
        """)
        
        st.markdown("---")
        st.header("🆘 Emergency Info")
        st.error("""
        **Low Blood Sugar Emergency:**
        - Symptoms: Shaking, sweating, confusion
        - Action: 15g fast carbs + recheck in 15min
        
        **Call your doctor or 911 for emergencies**
        """)

    # Main content
    st.title("🩺 Diabetes Management Assistant")
    st.markdown("### *Evidence-Based Clinical Decision Support System*")
    
    # Create tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🏠 Dashboard", "📊 Health Overview", "💬 Clinical Q&A", "📚 Resources"])
    
    with tab1:
        show_dashboard()
    
    with tab2:
        show_health_overview()
    
    with tab3:
        show_qa_system()
    
    with tab4:
        show_resources()

def show_dashboard():
    """Show main dashboard with overview"""
    st.header("🏠 Diabetes Management Dashboard")
    
    # Key metrics row
    st.subheader("🎯 Key Clinical Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("HbA1c Target", "<7.0%", "ADA Guideline")
    with col2:
        st.metric("Fasting Glucose", "80-130 mg/dL", "Optimal Range")
    with col3:
        st.metric("Post-Meal", "<180 mg/dL", "2 hours after")
    with col4:
        st.metric("Blood Pressure", "<140/90 mmHg", "Target")
    
    # Management pillars
    st.subheader("🎯 Management Pillars")
    pillars = st.columns(5)
    
    pillar_data = [
        ("💊", "Medication", "Take as prescribed"),
        ("🥗", "Nutrition", "Balanced diet"),
        ("🏃", "Exercise", "150 mins/week"),
        ("📊", "Monitoring", "Regular checks"),
        ("🎓", "Education", "Continuous learning")
    ]
    
    for i, (icon, title, desc) in enumerate(pillar_data):
        with pillars[i]:
            st.markdown(f"""
            <div style='text-align: center; padding: 15px; background: #e8f4f8; border-radius: 10px; margin: 5px;'>
                <h2>{icon}</h2>
                <strong>{title}</strong><br>
                <small>{desc}</small>
            </div>
            """, unsafe_allow_html=True)
    
    # Quick actions
    st.subheader("🚀 Quick Actions")
    action_cols = st.columns(4)
    
    actions = [
        ("📝", "Log Blood Sugar", "Record glucose reading"),
        ("💊", "Medication Info", "Learn about treatments"),
        ("🥗", "Meal Planning", "Diet recommendations"),
        ("📈", "View Trends", "See progress over time")
    ]
    
    for i, (icon, title, desc) in enumerate(actions):
        with action_cols[i]:
            if st.button(f"{icon} {title}", use_container_width=True, help=desc):
                st.info(f"**{title}** feature would open here. This is a demonstration.")
    
    # Recent activity
    st.subheader("📋 Today's Summary")
    summary_cols = st.columns(3)
    
    with summary_cols[0]:
        st.markdown("**Glucose Checks**")
        st.write("✅ 2 completed today")
        st.write("🕒 Last: 120 mg/dL")
    
    with summary_cols[1]:
        st.markdown("**Medications**")
        st.write("✅ All taken today")
        st.write("💊 Metformin 500mg")
    
    with summary_cols[2]:
        st.markdown("**Activity**")
        st.write("🏃 30 mins walking")
        st.write("🥗 Meals logged: 2")

def show_health_overview():
    """Show health metrics and diagrams"""
    st.header("📊 Diabetes Health Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🩸 Blood Glucose Ranges")
        
        # Glucose range visualization
        glucose_ranges = pd.DataFrame({
            'Range': ['Normal', 'Prediabetes', 'Diabetes', 'Critical'],
            'Min': [70, 100, 126, 200],
            'Max': [99, 125, 199, 400]
        })
        
        # Display as a table with color coding
        st.dataframe(glucose_ranges, use_container_width=True)
        
        st.subheader("📈 Sample Glucose Monitoring")
        # Sample glucose data throughout day
        time_data = pd.DataFrame({
            'Time': ['6 AM', '9 AM', '12 PM', '3 PM', '6 PM', '9 PM', '12 AM'],
            'Glucose': [95, 150, 140, 130, 120, 110, 100]
        })
        st.line_chart(time_data.set_index('Time'))
    
    with col2:
        st.subheader("🔬 Diabetes Statistics")
        
        # Diabetes statistics
        diabetes_stats = pd.DataFrame({
            'Type': ['Type 2', 'Type 1', 'Prediabetes', 'Gestational'],
            'Percentage': [90, 5, 38, 2],
            'Description': ['Most common', 'Autoimmune', 'At risk', 'Pregnancy']
        })
        st.dataframe(diabetes_stats, use_container_width=True)
        
        st.subheader("🎯 HbA1c Targets by Group")
        hba1c_data = pd.DataFrame({
            'Group': ['Most Adults', 'Elderly', 'Children', 'Pregnant'],
            'Target HbA1c': [6.5, 7.5, 7.0, 6.1],
            'Range': ['<7.0%', '<8.0%', '<7.5%', '<6.5%']
        })
        st.dataframe(hba1c_data, use_container_width=True)
        
        # Visual indicators
        st.subheader("📊 Risk Indicators")
        risk_cols = st.columns(3)
        with risk_cols[0]:
            st.metric("Heart Disease Risk", "2.5x", "Higher with diabetes")
        with risk_cols[1]:
            st.metric("Kidney Disease", "40%", "Of diabetics affected")
        with risk_cols[2]:
            st.metric("Annual Eye Exams", "Recommended", "For all patients")

def show_qa_system():
    """Show the question-answering system"""
    st.header("💬 Clinical Question & Answer System")
    st.markdown("### *Get evidence-based answers to your diabetes questions*")
    
    # User context
    user_type = st.session_state.user_info.get('type', 'Patient')
    experience = st.session_state.user_info.get('experience', 'Newly Diagnosed')
    
    st.info(f"👤 **Session for**: {user_type} | **Experience**: {experience}")
    
    # Quick question buttons
    st.subheader("🚀 Common Questions")
    
    col1, col2 = st.columns(2)
    
    common_questions = {
        "Blood Sugar": "What are the target blood sugar ranges for diabetes?",
        "Medication": "What is the first-line medication for type 2 diabetes?",
        "Diet": "What foods should I eat with diabetes?",
        "Exercise": "How much exercise is recommended for diabetes management?",
        "Symptoms": "What are the common symptoms of diabetes?",
        "Monitoring": "How often should I check my blood sugar?"
    }
    
    with col1:
        for i, (title, question) in enumerate(list(common_questions.items())[:3]):
            if st.button(f"🎯 {title}", key=f"quick_{i}", use_container_width=True):
                process_question(question, user_type)
    
    with col2:
        for i, (title, question) in enumerate(list(common_questions.items())[3:]):
            if st.button(f"🎯 {title}", key=f"quick_{i+3}", use_container_width=True):
                process_question(question, user_type)
    
    # Custom question input
    st.subheader("💭 Ask Your Own Question")
    custom_question = st.text_area(
        "Type your diabetes-related question:",
        placeholder="Examples:\n• What are the symptoms of low blood sugar?\n• How can I prevent diabetes complications?\n• What's the difference between type 1 and type 2?",
        height=100
    )
    
    if st.button("🎯 Get Clinical Answer", type="primary", use_container_width=True):
        if custom_question.strip():
            process_question(custom_question, user_type)
        else:
            st.warning("Please enter a question first.")
    
    # Conversation history
    if st.session_state.conversation_history:
        st.subheader("📖 Conversation History")
        
        for i, conversation in enumerate(reversed(st.session_state.conversation_history[-5:])):
            with st.expander(f"💬 {conversation['question'][:50]}..."):
                st.markdown(f"**🗣️ Question:** {conversation['question']}")
                st.markdown(f"**🤖 Answer:** {conversation['answer']}")
                st.markdown(f"*📅 Asked on: {conversation['timestamp'].strftime('%Y-%m-%d %H:%M')}*")
                
                if conversation.get('sources'):
                    with st.expander("📚 Clinical Sources"):
                        for source in conversation['sources']:
                            st.write(f"• {source}")

def process_question(question, user_type):
    """Process and answer diabetes questions"""
    # Comprehensive knowledge base
    knowledge_base = {
        'blood sugar': {
            'answer': """
**🩸 Blood Glucose Management - Clinical Guidelines**

**Target Ranges (ADA Standards 2023):**
- **Fasting/Pre-meal**: 80-130 mg/dL (4.4-7.2 mmol/L)
- **Postprandial (1-2hr after meal)**: <180 mg/dL (<10.0 mmol/L)
- **HbA1c (3-month average)**: <7.0% for most adults
- **Bedtime/Overnight**: 90-150 mg/dL (5.0-8.3 mmol/L)

**Individualized Targets:**
- **Young/Healthy**: HbA1c <6.5%
- **Elderly/Comorbidities**: HbA1c <8.0%
- **Pregnancy**: HbA1c <6.0-6.5%

**Monitoring Frequency:**
- **Type 1**: 4-10 times daily
- **Type 2 on insulin**: 2-4 times daily
- **Type 2 non-insulin**: As directed by provider
""",
            'sources': ["ADA Standards of Care 2023", "Clinical Diabetes 2022", "Diabetes Care Journal"]
        },
        'medication': {
            'answer': """
**💊 Diabetes Pharmacotherapy - Evidence-Based Approach**

**First-Line Therapy (Type 2 Diabetes):**
- **Metformin**: Initial choice, improves insulin sensitivity
- **Dosing**: 500-1000mg twice daily, with meals
- **Benefits**: Weight neutral, cardiovascular safety

**Second-Line Options (Individualized):**
- **SGLT2 Inhibitors** (Empagliflozin, Dapagliflozin):
  - Cardio-renal protection, weight loss
  - Monitor for UTI, dehydration

- **GLP-1 Receptor Agonists** (Semaglutide, Liraglutide):
  - Significant weight loss, cardiovascular benefits
  - GI side effects common initially

- **DPP-4 Inhibitors** (Sitagliptin, Linagliptin):
  - Weight neutral, well-tolerated
  - Neutral cardiovascular profile

**Insulin Therapy:**
- **Basal Insulin**: Start 10 units or 0.1-0.2 units/kg
- **Bolus Insulin**: For meal coverage as needed
""",
            'sources': ["ADA Pharmacotherapy Guidelines", "NEJM Diabetes Review", "Lancet Endocrinology"]
        },
        'diet': {
            'answer': """
**🥗 Medical Nutrition Therapy - Evidence-Based Approach**

**Plate Method (Visual Guide):**
- **½ Plate**: Non-starchy vegetables (broccoli, spinach, peppers)
- **¼ Plate**: Lean protein (chicken, fish, tofu, legumes)
- **¼ Plate**: Quality carbohydrates (whole grains, fruits)

**Carbohydrate Management:**
- **Counting**: 45-60g per meal for most adults
- **Quality**: Emphasize low glycemic index foods
- **Timing**: Consistent carbohydrate intake

**Specific Recommendations:**
- **Fiber**: 25-30g daily from whole foods
- **Sodium**: <2300mg daily, <1500mg if hypertension
- **Fats**: Emphasize unsaturated fats, limit saturated <7%

**Food Choices:**
- **Recommended**: Vegetables, whole grains, lean proteins, healthy fats
- **Limit**: Sugary beverages, processed foods, refined grains
""",
            'sources': ["ADA Nutrition Guidelines", "Clinical Nutrition", "Diabetes Care"]
        },
        'exercise': {
            'answer': """
**🏃 Physical Activity - Clinical Recommendations**

**Aerobic Exercise:**
- **Frequency**: 3-7 days per week
- **Duration**: 150 minutes moderate or 75 minutes vigorous
- **Examples**: Brisk walking, cycling, swimming

**Resistance Training:**
- **Frequency**: 2-3 non-consecutive days weekly
- **Types**: Weight machines, free weights, resistance bands
- **Benefits**: Improves insulin sensitivity, preserves muscle

**Flexibility & Balance:**
- **Yoga/Tai Chi**: 2-3 times weekly for flexibility
- **Balance exercises**: Important for elderly patients

**Safety Considerations:**
- **Pre-exercise glucose**: 100-250 mg/dL ideal range
- **Hypoglycemia risk**: Carry fast-acting carbohydrates
- **Foot care**: Inspect feet daily, proper footwear
""",
            'sources': ["ADA Exercise Guidelines", "Sports Medicine", "Clinical Exercise Physiology"]
        },
        'symptom': {
            'answer': """
**🩺 Diabetes Symptoms & Recognition**

**Hyperglycemia (High Blood Sugar):**
- **Classic Symptoms**: Polyuria, polydipsia, polyphagia
- **Other Signs**: Fatigue, blurred vision, slow healing
- **Severe**: Nausea/vomiting, abdominal pain, confusion

**Hypoglycemia (Low Blood Sugar):**
- **Autonomic**: Shakiness, sweating, palpitations, anxiety
- **Neuroglycopenic**: Confusion, drowsiness, speech difficulty
- **Severe**: Seizures, unconsciousness, coma

**Long-term Complications:**
- **Microvascular**: Retinopathy, nephropathy, neuropathy
- **Macrovascular**: Cardiovascular disease, stroke, PAD

**Screening Recommendations:**
- **High Risk**: Screen starting at age 35, or earlier if risk factors
- **Prediabetes**: Annual monitoring recommended
""",
            'sources': ["Clinical Medicine Journal", "Diabetes Symptoms Review", "Preventive Medicine"]
        }
    }
    
    # Find best matching answer
    question_lower = question.lower()
    answer_data = None
    
    for key in knowledge_base:
        if key in question_lower:
            answer_data = knowledge_base[key]
            break
    
    if not answer_data:
        # General answer for unmatched questions
        answer_data = {
            'answer': f"""
**💡 Diabetes Management Guidance**

Based on your question about *"{question}"*, here are key principles:

**General Diabetes Management:**
- **Individualized Care**: Treatment plans should be personalized
- **Regular Monitoring**: Track blood glucose, blood pressure, weight
- **Lifestyle Foundation**: Nutrition and exercise are cornerstone therapies
- **Medication Adherence**: Take prescribed medications consistently
- **Preventive Care**: Regular eye, foot, dental exams

**Next Steps:**
- Discuss specific concerns with your healthcare provider
- Consider diabetes education programs
- Join support groups for shared experiences

*For more specific information, try asking about: blood sugar targets, medications, diet, exercise, or symptoms.*
""",
            'sources': ["General Diabetes Education", "Clinical Practice Guidelines"]
        }
    
    # Customize answer based on user type
    if user_type == "Healthcare Professional":
        answer_data['answer'] = f"**Clinical Perspective - {user_type}**\n\n{answer_data['answer']}"
    elif user_type == "Patient":
        answer_data['answer'] = f"**Patient Education - Simplified Explanation**\n\n{answer_data['answer']}"
    
    # Store in conversation history
    st.session_state.conversation_history.append({
        'question': question,
        'answer': answer_data['answer'],
        'sources': answer_data['sources'],
        'timestamp': datetime.now(),
        'user_type': user_type
    })
    
    # Display the answer
    st.success("✅ **Clinical Answer Generated**")
    st.markdown(answer_data['answer'])
    
    # Show sources in expander
    with st.expander("📚 **Evidence Sources & References**"):
        st.write("**Clinical Guidelines & Research:**")
        for source in answer_data['sources']:
            st.write(f"• {source}")
        st.markdown("*Based on current evidence-based medicine principles*")

def show_resources():
    """Show educational resources"""
    st.header("📚 Diabetes Educational Resources")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏥 Clinical Guidelines")
        st.markdown("""
        **American Diabetes Association (ADA):**
        - Standards of Medical Care in Diabetes
        - Nutrition Therapy Recommendations
        - Technology Standards
        
        **International Guidelines:**
        - WHO Diabetes Guidelines
        - NICE Guidelines (UK)
        - IDF Global Diabetes Plan
        
        **Specialty Organizations:**
        - AACE Comprehensive Guidelines
        - Endocrine Society Guidelines
        - ADA/EASD Consensus Reports
        """)
        
        st.subheader("🔬 Research Databases")
        st.markdown("""
        **Medical Literature:**
        - PubMed/MEDLINE
        - Cochrane Library
        - ClinicalTrials.gov
        
        **Professional Journals:**
        - Diabetes Care
        - The Lancet Diabetes & Endocrinology
        - Diabetologia
        - JAMA Diabetes Specialties
        """)
    
    with col2:
        st.subheader("📱 Patient Tools & Apps")
        st.markdown("""
        **Monitoring Tools:**
        - Blood Glucose Logs
        - Carbohydrate Counting Guides
        - Meal Planning Templates
        - Exercise Trackers
        
        **Mobile Applications:**
        - Glucose Monitoring Apps
        - Medication Reminders
        - Nutrition Databases
        - Physical Activity Guides
        
        **Educational Platforms:**
        - Diabetes Self-Management Education
        - Online Support Communities
        - Video Learning Libraries
        """)
        
        st.subheader("🎓 Professional Development")
        st.markdown("""
        **Continuing Education:**
        - ADA Professional Membership
        - Clinical Conference Updates
        - Certification Programs
        - Research Opportunities
        
        **Teaching Resources:**
        - Patient Education Materials
        - Clinical Decision Tools
        - Guideline Implementation
        - Quality Improvement
        """)
    
    # Emergency section
    st.markdown("---")
    st.error("""
    🚨 **MEDICAL EMERGENCY PROTOCOL**
    
    **For Hypoglycemia (Low Blood Sugar) Emergency:**
    1. Check blood glucose if possible
    2. If <70 mg/dL with symptoms: Give 15g fast-acting carbohydrate
    3. Recheck in 15 minutes, repeat if still low
    4. If unconscious or unable to swallow: CALL 911 IMMEDIATELY
    5. Administer glucagon if prescribed
    
    **For Hyperglycemia (High Blood Sugar) Emergency:**
    1. Check blood glucose and ketones if possible
    2. If glucose >240 mg/dL with symptoms: Contact healthcare provider
    3. If symptoms severe (vomiting, confusion): SEEK EMERGENCY CARE
    4. Follow sick day management protocol
    
    **ALWAYS SEEK PROFESSIONAL MEDICAL HELP FOR EMERGENCIES**
    """)

# Run the application
if __name__ == "__main__":
    main()
