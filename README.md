# EchoAI DEV: The command line tool to interface with Generative AI

## Install

```bash
pip install echoai-dev
```

## Usage

You can use this cli with either openai GPT or Anthropic Claude (through AWS Bedrock). To use GPT models, configure your OpenAI API token. 

```bash
export OPENAI_API_KEY='sk-...'
```
For Anthropic Claude models, use the aws cli to configure your environement by running the command: `aws config`

Use the environment variable `ECHOAI_BACKEND` to define which backend model to use. This variable can take two values `bedrock` or `openai`. If the variable is not define, the default behavior is `openai`.

Once that's done, you can use the `echoai` command-line tool to interface with Generative AI. Here is an example of how you can use it:

```bash
echoai "Why does the Python live on land?"
```

This will generate a response from the Generative AI that hopefully answers the question. Of course, the quality of the response will depend on the specific model and prompt used.

> Disclaimer: AI jokes may not be funny to human beings. Use at your own risk.

### Azure OpenAI environment variables. 

The `echoai` cli works with the environment variables set for OpenAI. If you use Azure endpoints, you can set your `OPENAI_API_TYPE`, `_VERSION`, `_ENGINE` and `_BASE` according to your Azure project.

## New features

- [x] Support for AWS Bedrock (Claude models)
- [ ] Read files from mentioned paths
- [ ] Print code blocks to file
