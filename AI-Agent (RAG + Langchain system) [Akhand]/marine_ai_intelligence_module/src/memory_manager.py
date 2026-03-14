conversation_memory=[]

def save_message(question,response):

    conversation_memory.append({

    "question":question,

    "response":response

    })


def get_history():

    return conversation_memory