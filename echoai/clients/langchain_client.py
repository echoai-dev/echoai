import logging
from langchain.llms import OpenAI
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import openai
import os

from echoai.utils.callback_handler import FormattedStreamingStdOutCallbackHandler

class LangChainClient:
    def __init__(self, cfg: dict = {}) -> None:
        pass
    def get_completion(self, prompt):
        logging.debug("Using LangChain to query OpenAI with prompt: %s", prompt)
        return self._call_llm(prompt)

    def _call_llm(self, prompt):
        raise NotImplementedError("The '_call_llm' method should be overwritten by a subclass")

    def get_chat_completion(self, prompt):
        raise NotImplementedError("Chat with LangChain Clients has not been implemented yet.")

class OpenAILangChain(LangChainClient):
    def __init__(self, cfg: dict = {}, ) -> None:
        super().__init__(cfg=cfg,)
        # Set self.llm to the OpenAI LLMS function
        self.llm = OpenAI(streaming=True,callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),verbose=True).__call__

    def _call_llm(self, prompt):
        return self.llm(prompt)
