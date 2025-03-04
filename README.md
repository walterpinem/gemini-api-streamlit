# A Simple Python Streamlit App for Testing Gemini AI Models
Testing Gemini AI Models using Streamlit with a simple interface.

![A Simple Python Streamlit App for Testing Gemini AI Models](https://walterpinem.com/wp-content/uploads/2025/03/Gemini-AI-Streamlit-App.png)

#### Simple usage:

`streamlit run main.py`

---
Here’s how you can get things rolling:

#### **1\. Create a Python Virtual Environment**

Open your terminal (or Command Prompt on Windows) and navigate to your project directory. Then run:

##### Windows & Mac

    python -m venv gemini_env
    

Activate it by running: 

**On Windows:**

    gemini_env\Scripts\activate
    

**On macOS/Linux:**

    source gemini_env/bin/activate
    

For more detailed cover up, learn my post about [**Python virtual environment**](https://walterpinem.com/python-virtual-environment/).

#### **2\. Install Required Packages**

With your virtual environment activated, install Streamlit and [**OpenAI Python SDK**](https://github.com/openai/openai-python) as Gemini AI API is compatible with OpenAI (as well as any other dependencies you need) using `pip`:

    pip install streamlit openai
    

This will install the Streamlit framework, which we use to build our interactive web app, and the OpenAI package, which is required to interact with the Gemini AI API.

#### **3\. Prepare the Project Structure**

Organize your project directory so that you have all the necessary files in place:

    gemini-ai-chat-app/
    ├── main.py
    └── logo-white.png
    
You can change the logo name or even remove it.
