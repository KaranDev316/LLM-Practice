from data_lesson_1 import text

def build_prompt(user_input):
    return f"""
    You must answer using ONLY the information \
    inside the triple backticks. \
    
    If the answer cannot be found in the context, \
    say "I don't have enough information." \
    
    Your task is to generate a short summary of a product \
    review from an ecommerce site.
    Summarize the review below, delimited by triple
    backticks, in at most 30 words.
    
    
    user message:
    {user_input}
    
    
    review :```{text}```
    
    
    """