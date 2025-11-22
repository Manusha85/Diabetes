# diabetes_app_fixed.py - GUARANTEED WORKING VERSION
import streamlit as st
import pandas as pd

# MUST be the very first Streamlit command
st.set_page_config(
    page_title="Diabetes Management Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state at the top level
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

def main():
    st.title("🩺 Diabetes Management Assistant")
    st.markdown("### Evidence-Based Q&A System using Clinical Guidelines")
    
    # Display diabetes information immediately
    show_diabetes_overview()
    
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["📊 Diabetes Overview", "💬 Ask Questions", "📚 Clinical Resources"])
    
    with tab1:
        show_diabetes_diagrams()
    
    with tab2:
        show_qa_section()
    
    with tab3:
        show_resources_section()

def show_diabetes_overview():
    """Show diabetes overview information"""
    st.header("📊 Diabetes Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔬 What is Diabetes?")
        st.markdown("""
        Diabetes is a chronic condition that affects how your body processes blood sugar (glucose).
        
        **Main Types:**
        - **Type 1 Diabetes**: Autoimmune condition, usually diagnosed in children/young adults
        - **Type 2 Diabetes**: Insulin resistance, most common type
        - **Prediabetes**: Elevated blood sugar, high risk for developing Type 2
        - **Gestational Diabetes**: Occurs during pregnancy
        
        **Key Metrics to Monitor:**
        - **HbA1c**: 3-month average blood sugar
        - **Fasting Glucose**: Morning blood sugar before eating
        - **Postprandial**: Blood sugar after meals
        """)
    
    with col2:
        st.subheader("🎯 Treatment Goals")
        st.markdown("""
        **Blood Glucose Targets:**
        - **Fasting**: 80-130 mg/dL
        - **After meals**: <180 mg/dL
        - **HbA1c**: <7% for most adults
        
        **Management Pillars:**
        1. 🥗 **Nutrition**: Balanced diet, carbohydrate counting
        2. 🏃 **Exercise**: 150 mins/week moderate activity
        3. 💊 **Medication**: As prescribed by your doctor
        4. 📊 **Monitoring**: Regular blood sugar checks
        5. 🎓 **Education**: Understanding your condition
        """)

def show_diabetes_diagrams():
    """Show diabetes charts and diagrams"""
    st.header("📈 Diabetes Management Diagrams")
    
    # Simple charts using Streamlit's native charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Blood Glucose Monitoring")
        # Create sample glucose data
        glucose_data = pd.DataFrame({
            'Time': ['6 AM', '9 AM', '12 PM', '3 PM', '6 PM', '9 PM'],
            'Glucose': [95, 150, 140, 130, 120, 110]
        })
        st.line_chart(glucose_data.set_index('Time'))
        
        st.subheader("HbA1c Targets")
        hba1c_data = pd.DataFrame({
            'Patient Group': ['Most Adults', 'Elderly', 'Children', 'Pregnant'],
            'Target': [6.5, 7.5, 7.0, 6.1]
        })
        st.bar_chart(hba1c_data.set_index('Patient Group'))
    
    with col2:
        st.subheader("Diabetes Statistics")
        stats_data = pd.DataFrame({
            'Type': ['Type 2', 'Type 1', 'Prediabetes'],
            'Percentage': [90, 5, 5]
        })
        st.bar_chart(stats_data.set_index('Type'))
        
        st.subheader("Key Metrics Display")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Fasting Glucose", "80-130", "mg/dL")
        with col_b:
            st.metric("After Meals", "<180", "mg/dL")
        with col_c:
            st.metric("HbA1c Target", "<7.0", "%")

def show_qa_section():
    """Show question and answer section"""
    st.header("💬 Ask Diabetes Questions")
    
    # User type selection
    user_type = st.radio(
        "I am a:",
        ["Patient", "Healthcare Professional"],
        horizontal=True,
        key="user_type"
    )
    
    # Pre-defined quick questions
    st.subheader("🚀 Quick Questions")
    quick_questions = [
        "What is the target HbA1c for diabetes?",
        "Which medication is first-line for type 2 diabetes?",
        "How can diet help manage blood glucose?",
        "What are normal blood sugar levels?",
        "When should I check my blood sugar?",
        "What are symptoms of diabetes?"
    ]
    
    # Create buttons for quick questions
    cols = st.columns(2)
    for i, question in enumerate(quick_questions):
        col = cols[i % 2]
        with col:
            if st.button(f"❓ {question}", key=f"quick_{i}", use_container_width=True):
                handle_question(question, user_type)
    
    # Custom question input
    st.subheader("💭 Your Question")
    user_question = st.text_area(
        "Type your diabetes question here:",
        placeholder="e.g., What foods should I eat with diabetes? How often should I check my blood sugar?",
        height=100,
        key="custom_question"
    )
    
    if st.button("🎯 Get Answer", type="primary", key="get_answer"):
        if user_question.strip():
            handle_question(user_question, user_type)
        else:
            st.warning("Please enter a question first.")
    
    # Show conversation history
    if st.session_state.conversation_history:
        st.subheader("📖 Conversation History")
        for i, conversation in enumerate(reversed(st.session_state.conversation_history[-5:])):
            with st.expander(f"Q: {conversation['question']}"):
                st.markdown(f"**A:** {conversation['answer']}")
                if conversation.get('sources'):
                    st.markdown("**Sources:**")
                    for source in conversation['sources']:
                        st.markdown(f"- {source}")

def handle_question(question, user_type):
    """Handle question answering"""
    # Simple knowledge base - no external dependencies
    knowledge_base = {
        'blood sugar': {
            'answer': """
**🩸 Blood Sugar Management:**

**Target Ranges:**
- **Fasting** (before meals): 80-130 mg/dL
- **After meals** (1-2 hours): <180 mg/dL  
- **HbA1c** (3-month average): <7%
- **Bedtime**: 90-150 mg/dL

**Monitoring Tips:**
- Check as advised by your doctor
- Keep a log of readings
- Note patterns with food/exercise
""",
            'sources': ["ADA Standards of Care 2023", "Clinical Practice Guidelines"]
        },
        'hba1c': {
            'answer': """
**📊 Understanding HbA1c:**

**What is HbA1c?**
- Average blood sugar over 2-3 months
- Measured as a percentage

**Target Ranges:**
- **Normal**: Below 5.7%
- **Prediabetes**: 5.7% to 6.4%
- **Diabetes**: 6.5% or higher
- **Goal for most**: Below 7.0%
""",
            'sources': ["American Diabetes Association", "WHO Guidelines"]
        },
        'medication': {
            'answer': """
**💊 Common Diabetes Medications:**

**Type 2 Diabetes:**
- **Metformin**: Usually first treatment
- **SGLT2 inhibitors**: Heart/kidney protection
- **GLP-1 receptor agonists**: Weight loss benefits
- **Insulin**: When other medications aren't enough

**Type 1 Diabetes:**
- **Insulin** required (multiple types)

**Always take medications as prescribed by your doctor.**
""",
            'sources': ["ADA Pharmacotherapy Guidelines", "Clinical Trials"]
        },
        'diet': {
            'answer': """
**🥗 Diabetes Nutrition Guide:**

**Recommended Foods:**
- Non-starchy vegetables (broccoli, spinach)
- Whole grains (oats, brown rice)
- Lean proteins (chicken, fish, tofu)
- Healthy fats (avocado, nuts)

**Foods to Limit:**
- Sugary drinks and sweets
- White bread and pasta
- Fried and processed foods

**Plate Method:**
- ½ plate non-starchy vegetables
- ¼ plate lean protein
- ¼ plate whole grains
""",
            'sources': ["ADA Nutrition Guidelines", "Dietary Recommendations"]
        },
        'exercise': {
            'answer': """
**🏃 Physical Activity Guidelines:**

**Recommendations:**
- **150 minutes** per week moderate activity
- Spread over at least 3 days
- Strength training 2-3 times per week

**Safety Tips:**
- Check blood sugar before/after exercise
- Carry fast-acting carbs for lows
- Stay hydrated
""",
            'sources': ["Exercise Physiology Guidelines", "ADA Recommendations"]
        }
    }
    
    # Find the best matching answer
    question_lower = question.lower()
    answer_data = None
    
    for key in knowledge_base:
        if key in question_lower:
            answer_data = knowledge_base[key]
            break
    
    if not answer_data:
        # Default answer if no specific match
        answer_data = {
            'answer': """
**💡 General Diabetes Management Tips:**

- **Monitor regularly**: Check blood sugar as advised
- **Healthy eating**: Follow balanced meal plan  
- **Stay active**: Get regular physical activity
- **Take medications**: As prescribed by doctor
- **Regular check-ups**: See healthcare team regularly

For specific questions, try asking about blood sugar targets, diet recommendations, exercise guidelines, or medication information.
""",
            'sources': ["General Diabetes Education Materials"]
        }
    
    # Adjust answer based on user type
    final_answer = answer_data['answer']
    if user_type == "Healthcare Professional":
        final_answer = f"**Clinical Perspective:**\n{final_answer}"
    
    # Store in conversation history
    st.session_state.conversation_history.append({
        'question': question,
        'answer': final_answer,
        'sources': answer_data['sources'],
        'timestamp': pd.Timestamp.now()
    })
    
    # Display the answer
    st.success("✅ Answer Generated")
    st.markdown(final_answer)
    
    # Show sources
    with st.expander("📚 Clinical Sources"):
        for source in answer_data['sources']:
            st.write(f"• {source}")

def show_resources_section():
    """Show resources and references"""
    st.header("📚 Clinical Resources & References")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏥 Clinical Guidelines")
        st.markdown("""
        - **American Diabetes Association (ADA) Standards of Care**
        - **World Health Organization (WHO) Diabetes Guidelines** 
        - **National Institute for Health and Care Excellence (NICE)**
        - **International Diabetes Federation (IDF) Standards**
        """)
        
        st.subheader("🔬 Research & Evidence")
        st.markdown("""
        - **PubMed Clinical Trials Database**
        - **Cochrane Diabetes Systematic Reviews**
        - **ClinicalKey Medical Database**
        - **UpToDate Clinical Decision Support**
        """)
    
    with col2:
        st.subheader("📱 Patient Resources")
        st.markdown("""
        - **Diabetes Self-Management Education Programs**
        - **Nutritional Planning and Meal Prep Tools**
        - **Blood Glucose Monitoring Logs**
        - **Medication Adherence Trackers**
        - **Physical Activity Planning Guides**
        """)
        
        st.subheader("🆘 Emergency Information")
        st.markdown("""
        **Hypoglycemia (Low Blood Sugar):**
        - Symptoms: Shakiness, dizziness, sweating, confusion
        - Treatment: 15g fast-acting carbs + recheck in 15 minutes
        
        **Hyperglycemia (High Blood Sugar):**
        - Symptoms: Frequent urination, increased thirst, fatigue
        - Action: Contact healthcare provider immediately
        """)
    
    # Medical disclaimer
    st.markdown("---")
    st.error("""
    🚨 **Medical Emergency Notice**: 
    This system provides educational information only. For medical emergencies, 
    immediately contact your healthcare provider or call emergency services.
    Do not delay seeking medical advice based on information from this system.
    """)

# This ensures the app runs
if __name__ == "__main__":
    main()
