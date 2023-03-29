import unittest
import argparse
import logging
from unittest import mock
from pygments.formatters import TerminalFormatter
from pygments.lexers import MarkdownLexer
from pygments import highlight
from echoai.clients.openai_client import OpenAIClient
from echoai.main import print_output, main, format_text


class TestOpenAI(unittest.TestCase):
    def test_format_text(self):
        text = "This is some text with code."
        expected_output = "\x1b[38;5;28mThis is some text with \x1b[38;5;166mcode\x1b[38;5;28m.\n\x1b[0m"
        self.assertEqual(format_text(text), expected_output)

    def test_print_output(self):
        with mock.patch('builtins.print') as mocked_print:
            output = "This is some output."
            print_output(output)
            mocked_print.assert_called_once_with(output)

    def test_main(self):
        with mock.patch('builtins.print') as mocked_print:
            with mock.patch.object(OpenAIClient, 'get_chat_completion', return_value="This is a chat response.") as mock_chat_response:
                # Test with --nochat flag
                with mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(prompt="test prompt", nochat=True)):
                    main()
                    mock_chat_response.assert_not_called()
                    mocked_print.assert_called_once_with("\x1b[38;5;28mThis is a chat response.\n\x1b[0m")

                # Test without --nochat flag
                with mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(prompt="test prompt", nochat=False)):
                    with mock.patch.object(OpenAIClient, 'get_completion', return_value="This is a completion."):
                        main()
                        mock_chat_response.assert_not_called()
                        mocked_print.assert_called_once_with("\x1b[38;5;28mThis is a completion.\n\x1b[0m")
                    mock_chat_response.assert_not_called()
