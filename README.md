# langchain
langchain research


``` diff
# Conversational Memory for LLMs with Langchain

```
Conversational memory is how a chatbot can respond to multiple queries in a chat-like manner. It enables a coherent conversation, and without it, every query would be treated as an entirely independent input without considering past interactions.



ConversationChain
We can start by initializing the ConversationChain. We will use OpenAI’s text-davinci-003 as the LLM, but other models like gpt-3.5-turbo can be used.

``` python
from langchain import OpenAI
from langchain.chains import ConversationChain

# first initialize the large language model
llm = OpenAI(
	temperature=0,
	openai_api_key="OPENAI_API_KEY",
	model_name="text-davinci-003"
)

# now initialize the conversation chain
conversation = ConversationChain(llm=llm)

```



https://www.geeksforgeeks.org/how-to-use-chatgpt-api-in-python/
https://docs.langchain.com/docs/
https://docs.langchain.com/docs/category/components
https://docs.langchain.com/docs/use-cases/chatbots
https://docs.langchain.com/docs/use-cases/qa-docs
https://python.langchain.com/en/latest/modules/memory/examples/adding_memory.html
https://python.langchain.com/en/latest/modules/models/chat/getting_started.html
https://python.langchain.com/en/latest/modules/memory/getting_started.html
https://python.langchain.com/en/latest/modules/memory/types/buffer.html
https://python.langchain.com/en/latest/modules/memory/types/buffer_window.html
https://python.langchain.com/en/latest/modules/memory/types/entity_summary_memory.html
https://python.langchain.com/en/latest/modules/memory/types/summary.html
https://python.langchain.com/en/latest/modules/memory/types/summary_buffer.html

https://github.com/hwchase17/langchain
