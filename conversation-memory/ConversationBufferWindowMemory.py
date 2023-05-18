from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.callbacks import get_openai_callback
from langchain.chains.conversation.memory import ConversationBufferWindowMemory

import os
from dotenv import load_dotenv
load_dotenv()

#initialization of the large language model in this case openai lm
llm = OpenAI(
	temperature=0,
	openai_api_key= os.getenv('OPENAI_API_KEY'), #the open ai key
	model_name="text-davinci-003"
)


#the raw input of the past conversation between the human and AI is passed
conversation_bufw = ConversationChain(
    llm=llm,
    memory=ConversationBufferWindowMemory(k=1) #buffer to keep in memory (last prompt)
)

# #to see that the summarization is powered by an LLM
# print(conversation_sum.memory.prompt.template)
#token counter (result is what matters counter is just for exprimenting)
def count_tokens(chain, query):
    with get_openai_callback() as cb:
        result = chain.run(query)
        print(f'Spent {cb.total_tokens} tokens')

    return result


count_tokens(
    conversation_bufw, 
    "My interest here is to explore the potential of integrating AI to a company"
)

count_tokens(
    conversation_bufw, 
    "I just want to analyze the different possibilities. What can you think of?"
)

count_tokens(
    conversation_bufw, 
    "can you explain further please"
)

count_tokens(
    conversation_bufw, 
    "What is my aim again?"
)
#prints the last interaction only !
print(bufw_history = conversation_bufw.memory.load_memory_variables(
    inputs=[]
)['history'])

#pros:
#-Summarizer means we can remember distant interactions
#-Buffer prevents us from missing information from the most recent interactions

#cons:
#-Storing the raw interactions — even if just the most recent interactions — increases token count
#-cant remember old interactions (depending on how much K is set to)