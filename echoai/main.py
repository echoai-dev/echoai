#!/usr/bin/env python
import argparse
import logging
import os
from pygments import highlight
from pygments.lexers import PythonLexer, MarkdownLexer, BashLexer, guess_lexer
from pygments.formatters.terminal256 import Terminal256Formatter
from echoai.clients.openai_client import OpenAIClient
from echoai.clients.langchain_client import OpenAILangChain

def format_text(text):
    """
    Formats text with syntax highlighting and colors using the Markdown syntax and Pygments library.

    :param text: The text to format
    :return: The formatted text
    """

    # Format the text with syntax highlighting and colors
    # guess = guess_lexer(text)
    formatted_text = highlight(text, MarkdownLexer(), Terminal256Formatter())
    # formatted_text = highlight(text, guess, Terminal256Formatter())
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
    parser.add_argument("--chat", help="Use chat interface", action="store_true")
    parser.add_argument("--format", help="Use Pygments to format the terminal output", action="store_true")

    # Parse command line arguments
    args = parser.parse_args()

    client = OpenAILangChain(is_chat=args.chat)
    
    # Get response from OpenAI
    if args.chat:
        
        logging.debug("Getting chat response from OpenAI for prompt: %s", args.prompt)
        response = client.get_chat_completion(args.prompt)
    else:
        logging.debug("Getting completion from OpenAI Codex for prompt: %s", args.prompt)
        response = client.get_completion(args.prompt)

    logging.debug(f"\nGot response: {response}")
    if args.format:
        # Format response with syntax highlighting and colors
        logging.debug("Formatting response")
        formatted_response = format_text(response)

        # Print the output in a pretty format
        print_output(formatted_response)

if __name__ == "__main__":
    main()
