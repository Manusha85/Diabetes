# diabetes_app.py - COMPATIBLE WITH MODERN PYTHON VERSIONS
import streamlit as st
import pandas as pd
try:
    import plotly.graph_objects as go
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False
    st.warning("Plotly not available - using basic charts")

# Set page configuration
st.set_page_config(
    page_title="Diabetes Management Assistant",
    page_icon="🩺",
    layout="wide"
)

def create_simple_charts():
    """Create charts that work without Plotly if needed"""
    if PLOTLY_AVAILABLE:
        # Blood Sugar Chart
        fig = go.Figure()
        hours = list(range(24))
        glucose = [95, 92, 88, 85, 90, 110, 150, 165, 155, 140, 130, 125,
                  115, 105, 100, 95, 100, 120, 135, 125, 115, 105, 98, 95]
        
        fig.add_trace(go.Scatter(x=hours, y=glucose, mode='lines', name='Blood Glucose'))
        fig.update_layout(title='Blood Glucose Monitoring', height=300)
        return fig
    else:
        # Fallback to Streamlit native charts
        data = pd.DataFrame({
            'Time': list(range(24)),
            'Glucose': [95, 92, 88, 85, 90, 110, 150, 165, 155, 140, 130, 125,
                       115, 105, 100, 95, 100, 120, 135, 125, 115, 105, 98, 95]
        })
        return data

def main():
    st.title("🩺 Diabetes Management Assistant")
    st.markdown("### Evidence-Based Q&A System")
    
    # Initialize session state
    if 'history' not in st.session_state:
        st.session_state.history = []
    
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["📊 Diabetes Overview", "💬 Ask Questions", "📚 Resources"])
    
    with tab1:
        st.header("Understanding Diabetes")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🔬 What is Diabetes?")
            st.markdown("""
            Diabetes is a chronic condition that affects how your body processes blood sugar (glucose).
            
            **Main Types:**
            - **Type 1**: Autoimmune, usually young onset
            - **Type 2**: Insulin resistance, most common
            - **Prediabetes**: High risk state
            - **Gestational**: During pregnancy
            """)
            
            st.subheader("🎯 Blood Sugar Targets")
            st.markdown("""
            - **Fasting**: 80-130 mg/dL
            - **After meals**: <180 mg/dL  
            - **HbA1c**: <7% for most adults
            - **Bedtime**: 90-150 mg/dL
            """)
        
        with col2:
            st.subheader("💊 Management Plan")
            st.markdown("""
            **Key Components:**
            1. **Medication**: As prescribed
            2. **Nutrition**: Balanced diet
            3. **Exercise**: 150 mins/week
            4. **Monitoring**: Regular checks
            5. **Education**: Continuous learning
            """)
            
            st.subheader("🚨 Emergency Signs")
            st.markdown("""
            **Low Blood Sugar:**
            - Shaking, sweating, dizziness
            - **Action**: 15g fast carbs
            
            **High Blood Sugar:**
            - Extreme thirst, frequent urination
            - **Action**: Contact doctor
            """)
        
        # Display charts
        st.subheader("📈 Diabetes Monitoring")
        chart_data = create_simple_charts()
        
        if PLOTLY_AVAILABLE:
            st.plotly_chart(chart_data, use_container_width=True)
        else:
            st.line_chart(chart_data.set_index('Time'))
        
        # Diabetes statistics
        st.subheader("📊 Diabetes Statistics")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Type 2 Diabetes", "90%", "Most common")
        with col2:
            st.metric("Adults Affected", "1 in 10", "Global estimate")
        with col3:
            st.metric("Prediabetes", "38% US Adults", "At risk")
    
    with tab2:
        st.header("💬 Ask Diabetes Questions")
        
        # User type selection
        user_type = st.radio("I am a:", ["Patient", "Healthcare Professional"], horizontal=True)
        
        # Quick questions
        st.subheader("🚀 Quick Questions")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🎯 Blood Sugar Targets", use_container_width=True):
                show_answer("What are normal blood sugar levels?", user_type)
            if st.button("💊 First Medication", use_container_width=True):
                show_answer("What is first-line medication for type 2 diabetes?", user_type)
            if st.button("🥗 Diet Advice", use_container_width=True):
                show_answer("What should I eat with diabetes?", user_type)
        
        with col2:
            if st.button("🏃 Exercise Guidelines", use_container_width=True):
                show_answer("How much exercise for diabetes?", user_type)
            if st.button("📊 HbA1c Meaning", use_container_width=True):
                show_answer("What is HbA1c?", user_type)
            if st.button("🩺 Symptoms", use_container_width=True):
                show_answer("What are diabetes symptoms?", user_type)
        
        # Custom question
        st.subheader("💭 Your Question")
        question = st.text_input("Type your diabetes question:", placeholder="e.g., How often check blood sugar?")
        
        if st.button("🎯 Get Answer", type="primary") and question:
            show_answer(question, user_type)
        
        # Conversation history
        if st.session_state.history:
            st.subheader("📖 Recent Questions")
            for i, (q, a) in enumerate(reversed(st.session_state.history[-5:])):
                with st.expander(f"Q: {q}"):
                    st.markdown(f"**A:** {a}")
    
    with tab3:
        st.header("📚 Clinical Resources")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🏥 Guidelines")
            st.markdown("""
            - **American Diabetes Association (ADA)**
            - **World Health Organization (WHO)**
            - **National Institute of Health (NIH)**
            - **Clinical Practice Guidelines**
            """)
            
            st.subheader("🔬 Monitoring Tools")
            st.markdown("""
            - Blood Glucose Logs
            - Meal Planning Templates
            - Exercise Trackers
            - Medication Schedules
            """)
        
        with col2:
            st.subheader("📱 Patient Resources")
            st.markdown("""
            - Diabetes Education Programs
            - Support Groups
            - Mobile Apps
            - Online Communities
            """)
            
            st.subheader("🎓 Learning Materials")
            st.markdown("""
            - Nutrition Guides
            - Exercise Videos
            - Medication Information
            - Complication Prevention
            """)
        
        # Emergency information
        st.error("""
        🚨 **Medical Emergency Notice** 
        This application provides educational information only. 
        For medical emergencies, contact your healthcare provider or call emergency services immediately.
        """)

def show_answer(question, user_type):
    """Provide answers based on question content"""
    question_lower = question.lower()
    
    # Knowledge base
    answers = {
        'blood sugar': """
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
        'medication': """
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
        'diet': """
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
        'exercise': """
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
        'hba1c': """
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
        'symptom': """
**🩺 Common Diabetes Symptoms:**

**High Blood Sugar:**
- Increased thirst and urination
- Blurred vision
- Fatigue and weakness
- Slow-healing cuts

**Low Blood Sugar:**
- Shakiness or nervousness
- Sweating and chills
- Dizziness and confusion
- Hunger and nausea
"""
    }
    
    # Find matching answer
    answer = """
**💡 General Diabetes Management Tips:**

- **Monitor regularly**: Check blood sugar as advised
- **Healthy eating**: Follow balanced meal plan  
- **Stay active**: Get regular physical activity
- **Take medications**: As prescribed by doctor
- **Regular check-ups**: See healthcare team regularly

For specific questions, try asking about blood sugar, diet, exercise, medications, or symptoms.
"""
    
    for key in answers:
        if key in question_lower:
            answer = answers[key]
            break
    
    # Store in history
    st.session_state.history.append((question, answer))
    
    # Display answer
    st.success("✅ Answer Generated")
    st.markdown(answer)

if __name__ == "__main__":
    main()