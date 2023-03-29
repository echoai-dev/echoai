#!/usr/bin/env python
import argparse
import logging
import os
from pygments import highlight
from pygments.lexers import PythonLexer, MarkdownLexer, BashLexer
from pygments.formatters import TerminalFormatter
from echoai.clients.openai_client import OpenAIClient

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

    client = OpenAIClient(
        key = os.getenv('OPENAI_API_KEY'),
        engine = os.getenv('OPENAI_API_ENGINE','gpt-3.5-turbo-0301'),
        version = os.getenv('OPENAI_API_VERSION')

    )
    
    # Get response from OpenAI
    if not args.nochat:
        logging.debug("Getting chat response from OpenAI for prompt: %s", args.prompt)
        response = client.get_chat_completion(args.prompt)
    else:
        logging.debug("Getting completion from OpenAI Codex for prompt: %s", args.prompt)
        response = client.get_completion(args.prompt)

    # Format response with syntax highlighting and colors
    logging.debug("Formatting response")
    formatted_response = format_text(response)

    # Print the output in a pretty format
    print_output(formatted_response)

if __name__ == "__main__":
    main()
