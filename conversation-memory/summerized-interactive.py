from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationSummaryMemory
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
conversation_sum = ConversationChain(
    llm=llm,
    memory=ConversationSummaryMemory(llm=llm)
)

# #to see that the summarization is powered by an LLM
# print(conversation_sum.memory.prompt.template)

def count_tokens(chain, query):
    with get_openai_callback() as cb:
        result = chain.run(query)
        print(f'Spent {cb.total_tokens} tokens')

    return result

def qNa():
    while True:
        query = input('Please ask your question here: ')
        print(count_tokens(conversation_buf, query))


def main():
    qNa()
    
if __name__ == "__main__":
    main()