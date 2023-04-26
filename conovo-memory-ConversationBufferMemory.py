from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.callbacks import get_openai_callback
import os
from dotenv import load_dotenv
load_dotenv()

# initialization of the large language model in this case openai lm
llm = OpenAI(
	temperature=0,
	openai_api_key= os.getenv('OPENAI_API_KEY'), #the open ai key
	model_name="text-davinci-003"
)
# initialization the conversation chain
conversation = ConversationChain(llm=llm)

#print of the conversation chain just to see it...
print(conversation.prompt.template)

#the raw input of the past conversation between the human and AI is passed
conversation_buf = ConversationChain(
    llm=llm,
    memory=ConversationBufferMemory()
)

# #buffer fed to the history
# conversation_buf("Good morning AI!") #can change this this with input later


#token counter 

def count_tokens(chain, query):
    with get_openai_callback() as cb:
        result = chain.run(query)
        print(f'Spent a total of {cb.total_tokens} tokens')

    return result

count_tokens(
    conversation_buf, 
    "My interest here is to explore the potential of integrating AI to a companie"
)

count_tokens(
    conversation_buf, 
    "I just want to analyze the different possibilities. What can you think of?"
)

count_tokens(
    conversation_buf, 
    "can you explain further please"
)

count_tokens(
    conversation_buf, 
    "What is my aim again?"
)

#print of the whole history buffer stored
print(conversation_buf.memory.buffer)