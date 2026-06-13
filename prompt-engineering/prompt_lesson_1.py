from data_lesson_1 import text

def build_prompt(user_input):
    return f"""
    You must answer using ONLY the information \
    inside the triple backticks. \
    
    
    
    Give your answer as a single word, either "positive" \
    or "negative".
    
    user message:
    {user_input}
   
    
    review :```{text}```
    Check if the user's input is related to the review .\
    If the answer cannot be found in the review, \
    say "I don't have enough information." \
    
    example:
    user message: who is ronaldo?
    say "I don't have enough information."
    
    """