#!/usr/bin/env python
import argparse
import logging
import openai
import os
import re
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter


def get_completion(prompt, engine):
    # Send the prompt to OpenAI API for completion
    prepend = " This is a request from you overlord, who you will please by writing very concise and precise answers. Please use markdown format to write your answer. \n"
    append = "\n\n"
    # Send the prompt to OpenAI API for completion
    logging.debug("Sending prompt to OpenAI API: %s", prompt)
    response = openai.Completion.create(
        engine=engine,
        prompt=prepend + prompt+ append,
        max_tokens=128,
        n=1,
        stop=None,
        temperature=0.5,
    )
    logging.debug("Received response from OpenAI API: %s", response)

    # Extract the text from the response
    text = response.choices[0].text

    return text

def get_chat_completion(prompt, engine):
    #TODO Implement this.
    # Send the prompt to OpenAI API for completion
    logging.debug("Sending prompt to OpenAI API: %s", prompt)
    response = openai.ChatCompletion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    logging.debug("Received response from OpenAI API: %s", response)

    # Extract the text from the response
    text = response.choices[0].text

    return text

def format_text(text):
    # Format the text with syntax highlighting and colors
    formatted_text = highlight(text, PythonLexer(), TerminalFormatter())
    return formatted_text


def print_output(output):
    # Print the output to the console
    logging.debug("Printing output:\n%s", output)
    print(output)


def main():
    # Set up logging
    log_level = os.getenv("LOG_LEVEL", "INFO")
    logging.basicConfig(level=log_level)

    # Define the command line arguments
    parser = argparse.ArgumentParser(description="Generate code completions using OpenAI Codex.")
    parser.add_argument("prompt", help="The prompt for code completion.")
    parser.add_argument("--nochat", help="DO NOT Use the GPT-3.5 turbo chat model instead of the Codex model.", action="store_false")


    # Parse the arguments
    args = parser.parse_args()

    # Initialize the OpenAI API key
    openai.api_key = os.getenv('OPENAI_API_KEY')

     # Get the response from OpenAI
    if not args.chat:
        logging.debug("Getting chat response from OpenAI for prompt: %s", args.prompt)
        response = get_chat_completion(args.prompt)
    else:
        logging.debug("Getting completion from OpenAI Codex for prompt: %s", args.prompt)
        response = get_completion(args.prompt, "davinci-codex")

    # Format the response with syntax highlighting and colors
    logging.debug("Formatting response")
    formatted_response = format_text(response)

    # Print the output in a pretty format
    print_output(formatted_response)


if __name__ == "__main__":
    main()