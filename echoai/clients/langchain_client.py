import logging
from langchain.llms import OpenAI
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import openai

class LangChainOpenAIClient():
    def __init__(self,
                 cfg: dict = {},
                 key = None,
                 engine = 'gpt-3.5-turbo',
                 version = None) -> None:
        
        
        # Initialize OpenAI API key
        openai.api_key = key
        self.engine = engine
        openai.api_version = version

        ## Initialize OpenAI through Langchain
        self.llm = OpenAI(**cfg)

    def  get_completion(self, prompt):
        logging.debug("Using LangChain to query OpenAI with prompt: %s", prompt)
        text = self.llm(prompt)
        return text
    
    def get_chat_completion(self, prompt):
        raise NotImplementedError("Chat with LangChain Clients has not been implemented yet.")


