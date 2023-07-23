[![blog-link](https://img.shields.io/badge/ecrivai-blog-blue)](https://ruankie.github.io/ecrivai-blog-hugo/)
[![auto-publish](https://github.com/ruankie/ecrivai-blog-hugo/actions/workflows/sheduled-publish.yml/badge.svg)](https://github.com/ruankie/ecrivai-blog-hugo/actions/workflows/sheduled-publish.yml)
[![GitHub stars](https://img.shields.io/github/stars/ruankie/ecrivai)](https://github.com/ruankie/ecrivai/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ruankie/ecrivai)](https://github.com/ruankie/ecrivai/network)
[![GitHub contributors](https://img.shields.io/github/contributors/ruankie/ecrivai)](https://github.com/ruankie/ecrivai/graphs/contributors)
[![GitHub last commit](https://img.shields.io/github/last-commit/ruankie/ecrivai)](https://github.com/ruankie/ecrivai/commits/main)


# 🦜🔗✏️EcrivAI
EcrivAI is an automated blog writer that uses LangChain and GPT type LLMs for topic selection and content generation. The content is published to [this blog](https://ruankie.github.io/ecrivai-blog-hugo/)

## Usage
### Prerequisites
1. 🐍 You will need a working install of [`conda`](https://www.anaconda.com/download#downloads).
2. 🔑 You will need an API key from OpenAI. You can create one for free [here](https://platform.openai.com/account/api-keys).

### Dev Environment Setup
1. Set up your API keys in a file called `.env` (see `.env.example` for an example)
2. Set up and activate conda environment
    ```bash
    conda env create -f conda.yml
    conda activate ecrivai
    ```

> If you are having trouble setting your environment variables with the `.env` file or you want to manually add them instead of using a `.env` file, you can set your environment variable in your `ecrivai` conda environment like this:
>```shell
> # set api key env var
> conda env config vars set OPENAI_API_KEY="your-api-key-here"
> # re-activate env
> conda activate base
> conda activate ecrivai
>```

### CLI

> Note: Remember to activate your `ecrivai` conda environment before doing this (see above)

You can quickly generate a new original blog by running:

```
python ecrivai/add_blog.py
```

This will add a blog to a Markdown file in a directory called `content/`. You can also specify your own output directory by running this instead:
```
python ecrivai/add_blog.py --out-dir path/to/dir
```
