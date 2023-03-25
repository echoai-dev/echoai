#!/usr/bin/env python

import argparse
import logging
import openai
import os
import re
from pygments import highlight
from pygments.lexers import PythonLexer, MarkdownLexer, BashLexer
from pygments.formatters import TerminalFormatter

def get_completion(prompt, engine='davinci-instruct-beta'):
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
        engine=engine,
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

def get_chat_completion(prompt, engine='gpt-3.5-turbo-0301'):
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
            engine=engine,
            messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": prompt},
            ]
        )
    else:
        response = openai.ChatCompletion.create(
            model=engine,
            messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": prompt},
            ]
        )

    logging.debug("Received response from OpenAI API: %s", response)

    # Extract the text from the OpenAI chat engine response
    text = response.choices[0]['message']['content']
    return text

def format_text(text):
    """
    Formats text with syntax highlighting and colors using the Markdown syntax and Pygments library.

    :param text: The text to format
    :return: The formatted text
    """

    # Format the text with syntax highlighting and colors
    formatted_text = highlight(text, MarkdownLexer(), TerminalFormatter())
    return formatted_text

def print_output(output):
    """
    Prints output to the console.

    :param output: The output to print
    """

    # Print output to the console
    logging.debug("Printing output:\n%s", output)
    print(output)

def main():
    """
    The main function that processes command line arguments, initializes the OpenAI API key,
    sends the prompt to either OpenAI's Codex engine or the GPT-3.5 turbo chat model (depending on the argument),
    formats the response with syntax highlighting and colors,
    and prints the output to the console.
    """

    # Set up logging
    log_level = os.getenv("LOG_LEVEL", "INFO")
    logging.basicConfig(level=log_level)

    # Define command line arguments
    parser = argparse.ArgumentParser(description="Generate code completions using OpenAI Codex.")
    parser.add_argument("prompt", help="The prompt for code completion.")
    parser.add_argument("--nochat", help="DO NOT Use the GPT-3.5 turbo chat model instead of the Codex model.", action="store_true")

    # Parse command line arguments
    args = parser.parse_args()

    # Initialize OpenAI API key
    openai.api_key = os.getenv('OPENAI_API_KEY')
    openai_engine = os.getenv('OPENAI_API_ENGINE','gpt-3.5-turbo-0301')
    openai.api_version = os.getenv('OPENAI_API_VERSION')

    # Get response from OpenAI
    if not args.nochat:
        logging.debug("Getting chat response from OpenAI for prompt: %s", args.prompt)
        response = get_chat_completion(args.prompt, openai_engine)
    else:
        logging.debug("Getting completion from OpenAI Codex for prompt: %s", args.prompt)
        response = get_completion(args.prompt, openai_engine)

    # Format response with syntax highlighting and colors
    logging.debug("Formatting response")
    formatted_response = format_text(response)

    # Print the output in a pretty format
    print_output(formatted_response)

if __name__ == "__main__":
    main()
