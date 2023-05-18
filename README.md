# langchain
langchain research


# <strong>Conversational Memory for LLMs with Langchain </strong>

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
These two parameters — {history} and {input} — are passed to the LLM within the prompt template, and the output that we (hopefully) return is simply the predicted continuation of the conversation.

  <h1 >Forms of Conversational Memory</h1>
  <h2 > ConversationBufferMemory : </h2>
The ConversationBufferMemory is the most straightforward conversational memory in LangChain. As we described above, the raw input of the past conversation between the human and AI is passed — in its raw form — to the {history} parameter.

``` python
from langchain.chains.conversation.memory import ConversationBufferMemory

conversation_buf = ConversationChain(
    llm=llm,
    memory=ConversationBufferMemory()
)
conversation_buf("Good morning AI!")
```
{'input': 'Good morning AI!',
 'history': '',
 'response': " Good morning! It's a beautiful day today, isn't it? How can I help you?"}


<h4> Pros </h4>
<ul>
<li>
	Storing everything gives the LLM the maximum amount of information
</li>
	<li>
		Storing everything is simple and intuitive
	</li>
</ul>
<h4> cons </h4>
<ul>
	<li>
		More tokens mean slowing response times and higher costs
	</li>
	<li>
		Long conversations cannot be remembered as we hit the LLM token limit (4096 tokens for text-davinci-003 and gpt-3.5-turbo)</li>

</ul>
<h2 > ConversationBufferMemory : </h2>
o avoid excessive token usage, we can use ConversationSummaryMemory. As the name would suggest, this form of memory summarizes the conversation history before it is passed to the {history} parameter.













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
