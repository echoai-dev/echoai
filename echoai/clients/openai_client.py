import logging
import openai


class OpenAIClient():
    def __init__(self,
                 key = None,
                 engine = 'gpt-3.5-turbo',
                 version = None) -> None:
        
        # Initialize OpenAI API key
        openai.api_key = key
        self.engine = engine
        openai.api_version = version


    def get_completion(self, prompt):
        """
        Sends a prompt to OpenAI's API for completion and returns the extracted text.

        :param prompt: The prompt for code completion
        :param engine: The engine to use (e.g. "davinci-codex" or "davinci") 
        :return: The extracted text from the OpenAI completion response
        """

        # Prepend and append text to the prompt
        prepend = "This is a request from you overlord, who you will please by writing very concise and precise answers. Please use markdown format to write your answer. \n"
        append = "\n\n"
        
        # Send the prompt to the OpenAI API for completion
        logging.debug("Sending prompt to OpenAI API: %s", prompt)
        response = openai.Completion.create(
            engine=self.engine,
            prompt=prepend + prompt + append,
            max_tokens=128,
            n=1,
            stop=None,
            temperature=0.5,
        )
        logging.debug("Received response from OpenAI API: %s", response)

        # Extract the text from the OpenAI completion response
        text = response.choices[0].text
        return text

    def get_chat_completion(self, prompt):
        """
        Sends a prompt to the GPT-3.5 turbo chat engine and returns the extracted text.

        :param prompt: The prompt for the chat engine
        :param engine: The chat engine to use (default is 'gpt-3.5-turbo')
        :return: The extracted text from the OpenAI chat engine response
        """
        # Send the prompt to the OpenAI chat engine for completion
        logging.debug("Sending prompt to OpenAI API: %s", prompt)
        if "azure" in openai.api_type:
            response = openai.ChatCompletion.create(
                engine=self.engine,
                messages=[
                {"role": "system", "content": "You are a helpful coding assistant."},
                {"role": "user", "content": prompt},
                ]
            )
        else:
            response = openai.ChatCompletion.create(
                model=self.engine,
                messages=[
                {"role": "system", "content": "You are a helpful coding assistant."},
                {"role": "user", "content": prompt},
                ]
            )

        logging.debug("Received response from OpenAI API: %s", response)

        # Extract the text from the OpenAI chat engine response
        text = response.choices[0]['message']['content']
        return text