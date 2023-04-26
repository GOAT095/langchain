from langchain import OpenAI
from langchain.chains import ConversationChain

# initialization of the large language model in this case openai lm
llm = OpenAI(
	temperature=0,
	openai_api_key="###", #the open ai key
	model_name="text-davinci-003"
)
# initialization the conversation chain
conversation = ConversationChain(llm=llm)

#print of the conversation chain just to see it...
print(conversation.prompt.template)

