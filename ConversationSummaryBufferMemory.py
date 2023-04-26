from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.callbacks import get_openai_callback
from langchain.chains.conversation.memory import ConversationSummaryBufferMemory
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
conversation_sum_bufw = ConversationChain(
    llm=llm,
    memory=ConversationSummaryBufferMemory(
        llm=llm,
        max_token_limit=650)
)

# #to see that the summarization is powered by an LLM
# print(conversation_sum.memory.prompt.template)

def count_tokens(chain, query):
    with get_openai_callback() as cb:
        result = chain.run(query)
        print(f'Spent a total of {cb.total_tokens} tokens')

    return result


count_tokens(
    conversation_sum_bufw, 
    "My interest here is to explore the potential of integrating AI to a company"
)

count_tokens(
    conversation_sum_bufw, 
    "I just want to analyze the different possibilities. What can you think of?"
)

count_tokens(
    conversation_sum_bufw, 
    "can you explain further please"
)

count_tokens(
    conversation_sum_bufw, 
    "What is my aim again?"
)
#print the summarized convo 
print(conversation_sum_bufw.memory.buffer)

#pros:
#-Enables much longer conversations
#-shortens the number of tokens used

#cons:
#-must have a very good LLM to get the best results
#-requires token usage for the summarization LLM; this increases costs (but does not limit conversation length)