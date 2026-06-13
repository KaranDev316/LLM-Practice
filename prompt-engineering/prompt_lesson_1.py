from data_lesson_1 import text

def build_prompt(user_input):
    return f"""
    You must answer using ONLY the information \
    inside the triple backticks. \
    
    If the answer cannot be found in the context, \
    say "I don't have enough information." \
    Give your answer as a single word, either "positive" \
    or "negative".
    
    user message:
    {user_input}
    
    
    review :```{text}```
    
    
    """