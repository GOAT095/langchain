from datasets import load_dataset
import pod_gpt
from tqdm.auto import tqdm
import os
from dotenv import load_dotenv
load_dotenv()


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_ENV = 'us' #server
#load dataset
data = load_dataset('source',
    split='train')
data

#Initialize the indexer object.

indexer = pod_gpt.Indexer(
    openai_api_key=OPENAI_API_KEY,
    pinecone_api_key=PINECONE_API_KEY,
    pinecone_environment=PINECONE_ENV,
    index_name="pod-gpt"
)
