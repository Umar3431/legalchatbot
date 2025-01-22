from legal_scraper import scrape_legal_information
from ai_model import get_ai_generated_legal_response

def process_legal_query(user_query):
    """Processes the legal query by searching the web or using AI"""
    
    # Step 1: Scrape legal information from the internet
    legal_info = scrape_legal_information(user_query)

    if legal_info:
        return f"📜 **Relevant Law Found:** {legal_info}"
    
    # Step 2: If no exact match, use AI for legal insights
    return get_ai_generated_legal_response(user_query)
