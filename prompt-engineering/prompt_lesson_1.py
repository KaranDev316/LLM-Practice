from data_lesson_1 import text

def build_prompt(user_input):
    return f"""
    You must answer using ONLY the information \
    inside the triple backticks. \
    
    Identify a list of emotions that the writer of the,\
    Return only the list no other explanation \
    Identify the number of people who are saying positive or negative,\
 
    user message:
    {user_input}
   
    
    review :```{text}```
    Check if the user's input is related to the review .\
    If the answer cannot be found in the review, \
    say "I don't have enough information." \
    
    example 1:
    user message: who is ronaldo?
    say "I don't have enough information."
    
    example 2:
    user message: who wrote negative review?
    say the name only no explanation \
    
    example 3:
    user message: identify the number of people who are saying positive/negative \
    say only the number like 1 or 2 no further explanation \
    
    """