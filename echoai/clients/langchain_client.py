import logging
from langchain.llms import OpenAI
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import openai
import os

from langchain.prompts import (
    ChatPromptTemplate, 
    MessagesPlaceholder, 
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
)
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

class LangChainClient:
    def __init__(self, cfg: dict = {}) -> None:
        pass
    def get_completion(self, prompt):
        logging.debug("Using LangChain to query OpenAI with prompt: %s", prompt)
        return self._call_llm(prompt)

    def _call_llm(self, prompt):
        raise NotImplementedError("The '_call_llm' method should be overwritten by a subclass")
    
    def _call_chat(self, prompt):
        raise NotImplementedError("The '_call_chat' method should be overwritten by a subclass")

    def get_chat_completion(self, prompt):
        try:
            if prompt:
                    print("\nechoai>>")
                    self._call_chat(prompt)
                    print("\n")
            while True:
                user_input = input(">>")
                if user_input.lower() == "quit":
                    break
                self._call_chat(user_input)
                print("\n")

        except KeyboardInterrupt:
            print("\nChat interrupted by user... \nGoodbye.")

class OpenAILangChain(LangChainClient):
    def __init__(self, cfg: dict = {}, is_chat: bool=False) -> None:
        super().__init__(cfg=cfg,)
        # Set self.llm to the OpenAI LLMS function
        self.llm = OpenAI(streaming=True,callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),verbose=True).__call__
        if is_chat:
            self.chat = ChatOpenAI(streaming=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), verbose=True)

            self.prompt_template = ChatPromptTemplate.from_messages([
                SystemMessagePromptTemplate.from_template("The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know."),
                MessagesPlaceholder(variable_name="history"),
                HumanMessagePromptTemplate.from_template("{input}")
            ])

            self.memory = ConversationBufferMemory(return_messages=True)

            self.conversation = ConversationChain(memory=self.memory, prompt=self.prompt_template, llm=self.chat)


    def _call_llm(self, prompt):
        return self.llm(prompt)
    
    def _call_chat(self, prompt):
        return self.conversation.predict(input=prompt)
