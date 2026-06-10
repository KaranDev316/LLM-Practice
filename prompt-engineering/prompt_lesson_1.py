from data_lesson_1 import text
def build_prompt(user_input):
    return f"""
    You must answer using ONLY the information \
    inside the triple backticks. \
    
    If the answer cannot be found in the context, \
    say "I don't have enough information." \
    
    Perform the following actions : \
    1. summarize the following text in delimited.\
    2. translate the summary into french. \
    
    
    
    user message:
    {user_input}
    
    
    ```{text}```
    
    Do not say "Based on the information provided". \
    
    Return a concise answer. \
    
    """