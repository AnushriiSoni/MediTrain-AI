import streamlit as st
import requests

# Define the API URL for chatbot response
API_URL_CHAT = "http://localhost:5000/response"  

# Set up the Streamlit page configuration
st.set_page_config(
    page_title="MediTrain AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


    # Add custom CSS styles for the entire app
st.markdown(
    """
    <style>
    /* General Page Styles */
    .css-1v3fvcr {
        text-align: center;
        font-size: 40px;
        color: #008000; /* Green */
    }

    /* Input Fields */
    .stTextInput>div>input,
    .stTextArea>div>textarea {
        background-color: #f0f8ff; /* Light Blue */
        border: 2px solid #ff69b4; /* Dark Pink */
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
        color: #333;
    }

    /* Buttons */
   /* Buttons for Dashboard */
.stButton>button {
    background-color: #d6eaf8; /* Light Blue Faded */
    color: #333;
    border-radius: 12px;
    padding: 12px 24px;
    font-size: 16px;
    border: none;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
}

.stButton>button:hover {
    background-color: #aed6f1; /* Slightly More Intense Light Blue */
    box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
}


    /* Chat Container */
    .chat-container {
        font-family: 'Arial', sans-serif;
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f0f8ff; /* Light Blue */
        border: 2px solid #ff69b4; /* Dark Pink */
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
    }

    /* Chat Header */
    .chat-header {
        font-size: 28px;
        font-weight: bold;
        color: #008000; /* Green */
        text-align: center;
        margin-bottom: 20px;
    }

    /* Response Boxes */
    .response-box {
        background-color: #e6f7ff; /* Very Light Blue */
        border-left: 5px solid #ff69b4; /* Dark Pink */
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        font-size: 16px;
        color: #333;
    }

    /* Labels */
    label {
        font-size: 18px;
        color: #008000; /* Green */
        font-weight: bold;
    }

    /* Sidebar */
    .css-1d391kg {
        background-color: #f0f8ff; /* Light Blue */
        color: #008000; /* Green */
        border: none;
        border-radius: 10px;
        padding: 20px;
    }

    /* Footer Links */
    a {
        color: #ff69b4; /* Dark Pink */
        text-decoration: none;
        font-weight: bold;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True
)


def home():
    st.title("Welcome to Meditrain AI")
    st.markdown("### **Your Partner in Mastering Medical Knowledge and Patient Care** 🤖💡")
    
    st.markdown("""
    **Meditrain AI** is a state-of-the-art platform designed to assist healthcare professionals, medical students, and patients. 
    By leveraging advanced artificial intelligence, we provide insights, enhance learning, and support healthcare decision-making.

    #### Key Features:
    - **Interactive Simulations**: Practice diagnosing and managing medical cases.
    - **Personalized Insights**: Get tailored recommendations to improve your medical knowledge.
    - **Health Education**: Learn actionable health tips and promote better patient care.
    
    Join us in redefining healthcare education and communication. Start your journey with Meditrain AI and explore the future of healthcare learning today!
    """)

    st.markdown("""
    ### Ready to get started?
     Head over to the **Chat** page to begin practicing your diagnostic skills.
    """)

    
# Chat Page
def chat():
    # Initialize the conversation history
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Define the API URL for chatbot response
    API_URL_CHAT = "http://localhost:5000/response"  

    # Chat header
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.markdown('<div class="chat-header"> MediTrain AI</div>', unsafe_allow_html=True)

    # Display the conversation history
    for message in st.session_state.history:
        st.markdown(f"<div class='response-box'><strong>{message['sender']}:</strong> {message['text']}</div>", unsafe_allow_html=True)

    # Input field for user query
    st.markdown('<label for="chat_input" style="font-size: 20px;">Ask MediTrain something:</label>', unsafe_allow_html=True)
    user_query = st.text_input("", key="chat_input", label_visibility="collapsed", placeholder="Type your message here")

    # Button for sending the message
    if st.button("Send", help="Click to get response"):
        if user_query.strip():
            # Save the user's message in history
            st.session_state.history.append({"sender": "You", "text": user_query})

            with st.spinner("Thinking... 🤔"):
                try:
                    # Make a POST request to the chatbot API
                    response = requests.post(API_URL_CHAT, json={"query": user_query})
                    if response.status_code == 200:
                        # Get the chatbot's response from the API
                        chatbot_response = response.json().get("response", "No response.")
                        # Save the chatbot's response in history
                        st.session_state.history.append({"sender": "MediTrain", "text": chatbot_response})

                        # Display the chatbot response in the styled response box
                        st.markdown("<div class='response-box'>", unsafe_allow_html=True)
                        st.markdown(f"<strong>MediTrain : </strong> {chatbot_response}", unsafe_allow_html=True)
                        st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.error(f"Error: {response.status_code} - {response.text}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please type something to ask MediTrain!")

    # Close the chat container
    st.markdown('</div>', unsafe_allow_html=True)


# About Page
def about():
    st.title("About Meditrain AI")
    st.markdown("""
    MediTrain AI is an advanced conversational assistant redefining how healthcare education and communication are experienced. Built to empower medical students, professionals, and health-conscious individuals, MediTrain bridges the gap between knowledge and practice through interactive simulations and insightful guidance.

    ## Our Vision:
    We aim to make healthcare education accessible, engaging, and impactful. By offering a platform where users can learn, practice, and grow, MediTrain AI fosters a deeper understanding of healthcare concepts and promotes informed decision-making.

    ## Key Features:

    ##### 1. Patient Interaction Simulations:
    Engage in realistic scenarios to enhance diagnostic skills and patient communication. MediTrain’s diverse simulations help users tackle complex cases with confidence.

    ##### 2. Medical Education and Insights:
    Receive concise and clear explanations of medical concepts tailored to your knowledge level. Whether you're a student or a seasoned professional, MediTrain ensures learning remains relevant and straightforward.

    ##### 3. Health Awareness and Preventive Care:
    Explore actionable wellness advice and health tips designed to promote healthy habits. While we avoid personalized medical recommendations, MediTrain AI encourages users to consult qualified professionals for specific concerns.

    ## How We Engage:
    MediTrain AI combines knowledge with empathy, ensuring a supportive and dynamic user experience.

    - **Empathy and Encouragement:** Our assistant communicates with warmth and positivity, making users feel valued.
    - **Simplified Communication:** Avoiding unnecessary jargon, MediTrain explains terms and concepts in a user-friendly manner.
    - **Proactive Assistance:** Whether clarifying concepts or expanding on queries, MediTrain provides thoughtful and helpful guidance.

    ## Why Choose MediTrain AI?

    - **Realistic Learning:** Practice medical scenarios that mimic real-world challenges.
    - **Customized Experience:** Tailored interactions adapt to your expertise, making learning more effective.
    - **Health Literacy Promotion:** Empowering users with accurate, understandable, and actionable information to make informed health decisions.

    MediTrain AI is more than just a tool; it’s your partner in mastering healthcare concepts, improving patient interactions, and fostering a proactive approach to health and wellness. Together, we can build a healthier, more informed world.
    """)


# How to Use Page
def how_to_use():
    st.title("How to Use Meditrain AI")
    st.markdown("""
    MediTrain AI helps you practice diagnosing medical conditions and learn about healthcare concepts through interactive simulations. Follow the steps below to get started:

    ## Steps to Use:
    1. **Go to the Chat page.**
    2. **Ask questions or describe your symptoms.**
    3. **Meditrain AI will provide recommendations based on your inputs.**
    4. **Use the feedback button to provide us with suggestions or ask for further assistance.**

    ## Tips:
    - **Be as specific as possible with your queries.**
    - **Meditrain AI continuously learns and improves, so your feedback helps us serve you better.**

    ## Use Case Scenario

    **Scenario: Medical Student Diagnosing a Patient’s Condition**

    1. **User Opens Chat:**  
    Alex opens the Meditrain AI app and navigates to the Chat page to start a patient diagnosis simulation.

    2. **Initiating the Chat:**  
    MediTrain AI: *“Hello, Alex! I’m here to help you practice diagnosing medical cases. Are you ready for a simulation?”*  
    Alex: *“Yes, let’s start.”*

    3. **Presenting a Case:**  
    MediTrain AI: *“A 45-year-old male presents with fever, sore throat, body aches, and a persistent cough. What condition do you suspect?”*  
    Alex: *“It sounds like the flu.”*

    4. **Asking Probing Questions:**  
    MediTrain AI: *“Does the patient have any difficulty breathing or chest pain?”*  
    Alex: *“No, there’s no chest pain or shortness of breath.”*

    5. **Confirming Diagnosis:**  
    MediTrain AI: *“The flu seems likely, but always watch for complications. Would you like to explore more about flu management?”*  
    Alex: *“Yes.”*

    6. **Educational Insights:**  
    MediTrain AI: *“Flu is caused by influenza viruses and resolves in 1-2 weeks. Rest, fluids, and over-the-counter medications are key.”*  
    Alex: *“Thanks for the details!”*
    """)



# Feedback Page
import streamlit as st

def feedback():
    st.title("Feedback for Meditrain AI")
    st.markdown("""
    We value your feedback! Please share your thoughts and suggestions with us. Your feedback helps us improve and provide a better experience for all users.
    """)
    
    # Feedback Form
    st.subheader("Rate Your Experience")
    rating = st.slider("How would you rate your experience with Meditrain AI?", 1, 5)
    
    # User Comments
    st.subheader("Your Feedback")
    user_feedback = st.text_area("Please share any comments, suggestions, or issues you encountered:")

    # Optional Contact Information
    st.subheader("Contact Information (Optional)")
    user_email = st.text_input("Email (optional)")

    # Submit Feedback Button
    if st.button("Submit Feedback"):
        if user_feedback:
            st.success("Thank you for your feedback!")
            # Store the feedback in a file or database (optional)
            # For example, saving to a text file:
            with open("feedback.txt", "a") as file:
                file.write(f"Rating: {rating}\nFeedback: {user_feedback}\nEmail: {user_email if user_email else 'N/A'}\n\n")
        else:
            st.warning("Please provide feedback before submitting.")

    # Additional Resources
    st.markdown("""
    - [LinkedIn](https://www.linkedin.com/in/anushri-soni)  
    - [Gmail](mailto:your-email@gmail.com)  
    """)



# Main function to navigate between pages
def main():
    if 'page' not in st.session_state:
        st.session_state.page = "home"

    # Sidebar with navigation buttons
    st.sidebar.title("Dashboard")
    if st.sidebar.button("Home"):
        st.session_state.page = "home"
    if st.sidebar.button("About"):
        st.session_state.page = "about"
    if st.sidebar.button("How to Use"):
        st.session_state.page = "how_to_use"
    if st.sidebar.button("Chat"):
        st.session_state.page = "chat"
    if st.sidebar.button("Feedback"):
        st.session_state.page = "feedback"

    # Display the selected page
    if st.session_state.page == "home":
        home()
    elif st.session_state.page == "about":
        about()
    elif st.session_state.page == "how_to_use":
        how_to_use()
    elif st.session_state.page == "chat":
        chat()
    elif st.session_state.page == "feedback":
        feedback()

if __name__ == "__main__":
    main()
