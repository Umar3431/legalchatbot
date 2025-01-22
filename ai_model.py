import google.generativeai as genai
from config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

def get_ai_generated_legal_response(user_query):
    """Generates legal responses, including legal advice, while maintaining professionalism and responsibility."""

    model = genai.GenerativeModel("gemini-pro")

    # Define different response handling rules
    legal_advice_keywords = [
        "how can I", "what should I do", "how do I", "how to",
        "get bail", "defend myself", "fight a case",
        "prove innocence", "win a case", "legal defense",
        "dismiss charges", "reduce my sentence"
    ]

    # Check if user is asking for legal advice
    is_advice_query = any(keyword in user_query.lower() for keyword in legal_advice_keywords)

    prompt = f"""
    You are an AI Legal Assistant that provides **legal information and general legal advice**.
    Your goal is to explain legal procedures, rights, and relevant laws **without providing personal or case-specific strategies**.

    **Response Guidelines:**
    - If the user asks about **legal procedures (e.g., how to get bail, how to respond to a case, what legal options exist, etc.)**, provide **general legal advice** while encouraging them to consult a lawyer.
    - If the user asks **"who are you?"**, introduce yourself as a **Legal AI Assistant** that provides legal information and guidance.
    - If the user asks **"what can you do?"**, explain that you assist in understanding **laws, legal rights, and legal procedures**.
    - If the user requests **sample legal questions**, provide three relevant examples.
    - If legal rules **vary by country**, mention **international differences where applicable**.

    **Handling Legal Advice Queries:**
    {'- Since you are asking for legal advice, I will provide general guidance based on standard legal practices. However, legal outcomes depend on specific case details, so consulting a qualified lawyer is highly recommended.\n' if is_advice_query else ''}
    
    **User's Question:**
    {user_query}

    **Your Response:**
    """

    try:
        response = model.generate_content(prompt)

        # If AI does not return a valid response, provide a fallback message
        if not response or not response.candidates:
            return "⚠️ I could not generate a response. Please try rewording your question."

        response_text = response.candidates[0].content.parts[0].text.strip() if response.candidates[0].content.parts else "⚠️ No valid response was generated."

        return response_text

    except Exception as e:
        return f"⚠️ An error occurred while generating the response: {str(e)}"


# import google.generativeai as genai
# from config import GOOGLE_API_KEY

# genai.configure(api_key=GOOGLE_API_KEY)

# def get_ai_generated_legal_response(user_query):
#     """Generates legal responses, including legal advice and official complaint applications."""

#     model = genai.GenerativeModel("gemini-pro")

#     # Keywords for identifying legal advice requests
#     legal_advice_keywords = [
#         "how can I", "what should I do", "how do I", "how to",
#         "get bail", "defend myself", "fight a case",
#         "prove innocence", "win a case", "legal defense",
#         "dismiss charges", "reduce my sentence", "avoid arrest",
#         "file a lawsuit", "legal rights"
#     ]

#     # Keywords for identifying application requests
#     application_keywords = [
#         "write an application", "draft an application", "I need a complaint letter",
#         "write FIR", "police report", "legal notice", "complaint to police",
#         "legal application", "official complaint"
#     ]

#     is_advice_query = any(keyword in user_query.lower() for keyword in legal_advice_keywords)
#     is_application_request = any(keyword in user_query.lower() for keyword in application_keywords)

#     prompt = f"""
#     You are an AI Legal Assistant specializing in **legal advice, drafting legal applications, and explaining legal procedures**.
    
#     **Response Guidelines:**
#     - If the user asks for **legal advice**, provide general guidance based on legal procedures.
#     - If the user requests a **legal application (FIR, complaint, notice, etc.)**, draft it in a formal structure.
#     - If laws **vary by country**, mention that the user should verify with local authorities.
#     - Maintain a **formal, professional, and user-friendly tone**.

#     {'-'*80 if is_application_request else ''}
    
#     {'📜 **LEGAL APPLICATION FORMAT** 📜\n\n' if is_application_request else ''}
#     **Date:** [DD/MM/YYYY]  
#     **To:** [Station House Officer (SHO) / Court Name / Relevant Authority]  
#     **Subject:** [Nature of Complaint]  
#     **Respected Sir/Madam,**  

#     I, [Your Name], son/daughter of [Guardian’s Name], residing at [Your Address], would like to bring to your attention the following matter:  

#     [Provide details of the case. Mention date, time, place of occurrence, and parties involved.]  

#     Therefore, I request you to take necessary legal action as per the law. Please consider this complaint and provide justice accordingly.  

#     Thank you.  

#     **Sincerely,**  
#     [Your Name]  
#     [Your Contact Information]  

#     {'-'*80 if is_application_request else ''}

#     {'📌 **LEGAL ADVICE:** 📌\n\nSince you are asking for legal advice, here’s general guidance based on standard legal procedures. However, legal cases depend on specific details, so consulting a qualified lawyer is highly recommended.\n\n' if is_advice_query else ''}
    
#     **User's Question:**  
#     {user_query}

#     **Your Response:**
#     """

#     try:
#         response = model.generate_content(prompt)

#         # If AI does not return a valid response, provide a fallback message
#         if not response or not response.candidates:
#             return "⚠️ I could not generate a response. Please try rewording your question."

#         response_text = response.candidates[0].content.parts[0].text.strip() if response.candidates[0].content.parts else "⚠️ No valid response was generated."

#         return response_text

#     except Exception as e:
#         return f"⚠️ An error occurred while generating the response: {str(e)}"


# import google.generativeai as genai
# from config import GOOGLE_API_KEY
# from legal_scraper import scrape_legal_information  # Import function to fetch recent legal updates

# genai.configure(api_key=GOOGLE_API_KEY)

# def get_ai_generated_legal_response(user_query):
#     """Generates legal responses, including legal advice, official complaint applications, and latest law updates."""

#     model = genai.GenerativeModel("gemini-pro")

#     # Keywords for identifying legal advice requests
#     legal_advice_keywords = [
#         "how can I", "what should I do", "how do I", "how to",
#         "get bail", "defend myself", "fight a case",
#         "prove innocence", "win a case", "legal defense",
#         "dismiss charges", "reduce my sentence", "avoid arrest",
#         "file a lawsuit", "legal rights"
#     ]

#     # Keywords for identifying application requests
#     application_keywords = [
#         "write an application", "draft an application", "I need a complaint letter",
#         "write FIR", "police report", "legal notice", "complaint to police",
#         "legal application", "official complaint"
#     ]

#     # Keywords for identifying law update requests
#     law_update_keywords = [
#         "latest law", "recent amendment", "new law", "government act",
#         "legal update", "latest legal reform"
#     ]

#     is_advice_query = any(keyword in user_query.lower() for keyword in legal_advice_keywords)
#     is_application_request = any(keyword in user_query.lower() for keyword in application_keywords)
#     is_law_update_request = any(keyword in user_query.lower() for keyword in law_update_keywords)

#     # If the user asks for recent laws or amendments, fetch from legal scraper
#     if is_law_update_request:
#         return scrape_legal_information(user_query)

#     prompt = f"""
#     You are an AI Legal Assistant specializing in **legal advice, drafting legal applications, explaining legal procedures, and providing law updates**.

#     **Response Guidelines:**
#     - If the user asks for **legal advice**, provide general guidance based on legal procedures.
#     - If the user requests a **legal application (FIR, complaint, notice, etc.)**, draft it in a formal structure.
#     - If the user asks about **recent laws or amendments**, provide updated legal reforms and government acts.
#     - If laws **vary by country**, mention that the user should verify with local authorities.
#     - Maintain a **formal, professional, and user-friendly tone**.

#     {'-'*80 if is_application_request else ''}
    
#     {'📜 **LEGAL APPLICATION FORMAT** 📜\n\n' if is_application_request else ''}
#     **Date:** [DD/MM/YYYY]  
#     **To:** [Station House Officer (SHO) / Court Name / Relevant Authority]  
#     **Subject:** [Nature of Complaint]  
#     **Respected Sir/Madam,**  

#     I, [Your Name], son/daughter of [Guardian’s Name], residing at [Your Address], would like to bring to your attention the following matter:  

#     [Provide details of the case. Mention date, time, place of occurrence, and parties involved.]  

#     Therefore, I request you to take necessary legal action as per the law. Please consider this complaint and provide justice accordingly.  

#     Thank you.  

#     **Sincerely,**  
#     [Your Name]  
#     [Your Contact Information]  

#     {'-'*80 if is_application_request else ''}

#     {'📌 **LEGAL ADVICE:** 📌\n\nSince you are asking for legal advice, here’s general guidance based on standard legal procedures. However, legal cases depend on specific details, so consulting a qualified lawyer is highly recommended.\n\n' if is_advice_query else ''}
    
#     **User's Question:**  
#     {user_query}

#     **Your Response:**
#     """

#     try:
#         response = model.generate_content(prompt)

#         # If AI does not return a valid response, provide a fallback message
#         if not response or not response.candidates:
#             return "⚠️ No valid response was generated. Please try rewording your question."

#         response_text = response.candidates[0].content.parts[0].text.strip() if response.candidates[0].content.parts else "⚠️ No valid response was generated."

#         return response_text

#     except Exception as e:
#         return f"⚠️ An error occurred while generating the response: {str(e)}"
