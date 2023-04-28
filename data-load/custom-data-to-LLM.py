import openai
from gpt_index import PromptHelper, SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, ServiceContext

from langchain import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

    # def createVectorIndex(path): 
def createVectoreIndexx(path):
    max_input = 4096
    tokens = 256
    chunk_size = 600
    max_chunk_overlap = 20
    prompt_Helper = PromptHelper(max_input, tokens, max_chunk_overlap, chunk_size_limit=chunk_size)

    #define the LLM (language module openai for exemple)
    llmPredictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003", max_tokens=tokens))    #define parameters
    #load data to path
    docs = SimpleDirectoryReader(path).load_data()

    #create vector index
    serviceContext = ServiceContext.from_defaults(llm_predictor=llmPredictor, prompt_helper=prompt_Helper)
    vectorIndex = GPTSimpleVectorIndex.from_documents(documents=docs,service_context=serviceContext)
    vectorIndex.save_to_disk('vectorIndex.json')
    return vectorIndex
def qNa(vectorIndex):
    vIndex = GPTSimpleVectorIndex.load_from_disk(vectorIndex)
    while True:
        prompt = input('Please ask your question here: ')
        response = vIndex.query(prompt, response_mode="compact")
        print(f"Response: {response} \n")

vectorIndex = createVectoreIndexx('../source')
qNa('vectorIndex.json')