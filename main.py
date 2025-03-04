import streamlit as st
from openai import OpenAI

# Configure the Streamlit page
st.set_page_config(
    page_title="Gemini AI Chat Sample",
    layout="centered",
    page_icon="🤖"
)

# Set up the page title and sidebar content
st.title("Gemini AI Chat Sample")
with st.sidebar:
    st.image("logo-white.png", width=180)
    st.write("A sample Streamlit app to test Gemini AI.")
    # Sidebar: Enter your Gemini API Key
    api_key = st.text_input("Gemini API Key", type="password")

# Inject custom CSS to adjust sidebar width and image sizing
st.markdown(
    """
    <style>
        h1 { font-size: 1.75em !important; }
        section[data-testid="stSidebar"] {
            width: 200px !important; /* Set the width to your desired value */
        }
        section[data-testid="stSidebar"] img {
            max-width: 180px !important;
            height: auto;
            width: 100% !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main area: Text area for entering the prompt
prompt = st.text_area("Enter the prompt to instruct the AI:", value="")

# Main area: Dropdown for selecting the AI model
model_options = {
    "Gemini 2.0 Flash": "gemini-2.0-flash",
    "Gemini 2.0 Flash-Lite": "gemini-2.0-flash-lite",
    "Gemini 1.5 Flash": "gemini-1.5-flash",
    "Gemini 1.5 Flash-8B": "gemini-1.5-flash-8b",
    "Gemini 1.5 Pro": "gemini-1.5-pro"
}
selected_model_label = st.selectbox("Select model:", list(model_options.keys()))
selected_model = model_options[selected_model_label]

# Button to trigger the API call with improved error handling and spinner
if st.button("Run", type="primary", use_container_width=True):
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar.")
    elif not prompt.strip():
        st.error("Please enter a prompt to instruct the AI.")
    else:
        # Create the OpenAI client with the provided API key and Gemini base URL
        client = OpenAI(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )

        # Define conversation messages: system prompt and user instruction
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]

        # Use a spinner to indicate that the response is being generated
        with st.spinner("Waiting for AI response..."):
            try:
                response = client.chat.completions.create(
                    model=selected_model,
                    n=1,
                    messages=messages
                )
                # Display the AI response with a horizontal rule separator
                st.write("---")
                st.markdown("#### Response")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"An error occurred: {e}")
