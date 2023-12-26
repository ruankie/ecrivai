import os
import argparse
import logging
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import LLMChain, SimpleSequentialChain
from prompt_templates import content_prompt, topic_prompt
from write import to_markdown, md2hugo


load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def get_blog_chain():
    logging.info("Loading LLM config")
    # set up some parameters of the LLM
    content_llm_kwargs = {
        "temperature": 0.7,
        "model": "gemini-pro",
        "max_output_tokens": 1500 # ~ 1125 words
    }

    topic_llm_kwargs = {
        "temperature": 0.7,
        "model": "gemini-pro",
        "max_output_tokens": 50 # ~ 38words
    }

    # create LLMs with kwargs specified above
    content_llm = GoogleGenerativeAI(**content_llm_kwargs)
    topic_llm = GoogleGenerativeAI(**topic_llm_kwargs)

    # chain it all together
    topic_chain = LLMChain(llm=topic_llm, prompt=topic_prompt)
    content_chain = LLMChain(llm=content_llm, prompt=content_prompt)

    chain = SimpleSequentialChain(
        chains=[
            topic_chain,
            content_chain
        ],
        verbose=True
    )

    return chain

if __name__ == "__main__":
    logging.info("Parsing CLI args")
    parser = argparse.ArgumentParser(description="A create a blog post as a Markdown file with ecrivai")
    parser.add_argument("--out-dir", type=str, default="./content", help="The path to the output directory")
    args = parser.parse_args()
    
    chain = get_blog_chain()
    logging.info("Generating topic and blog (can take some time)...")
    blog_text = chain.run("")
    logging.info("Blog content finished")

    out_dir = args.out_dir
    logging.info(f"Writing blog to Markdown file at: {out_dir}")
    md_file_name = to_markdown(blog_text, out_dir=out_dir)
    logging.info(f"Formatting file header for Hugo")
    blof_file_path = os.path.join(out_dir, md_file_name)
    md2hugo(blof_file_path, blof_file_path)
    logging.info(f"Done")

