# EchoAI DEV: The command line tool to interface with Generative AI

## Install

```bash
pip install openai-dev
```

## Usage

This cli depends on `openai` and it needs to be configured with your OpenAI API token. 

```bash
export OPENAI_API_KEY='sk-...'
```

Once that's done, you can use the `echoai` command-line tool to interface with Generative AI. Here is an example of how you can use it:

```bash
echoai "Why does the Python live on land?"
```

This will generate a response from the Generative AI that hopefully answers the question. Of course, the quality of the response will depend on the specific model and prompt used.

>Disclaimer: AI jokes may not be funny to human beings. Use at your own risk.