import os
import re
import datetime
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def to_markdown(blog_text: str, out_dir: str = "content/") -> str:
    """
    Given the blog text, write it to a markdown file in the
    output dir. The output file will have the date and time
    as a name.

    Args:
        blog_text (str): The body of the blog.
        out_dir (str): The output directory where the blog will be saved as a Markdown file.

    Returns:
        str: Output file name
    """
    now = datetime.datetime.now()
    now_str = now.strftime("%Y%m%d%H%M")

    out_file_name = f"{now_str}.md"
    out_file_path = os.path.join(out_dir, out_file_name)

    if not os.path.exists(out_dir):
        logging.info(f"Creating output dir: {out_dir}")
        os.makedirs(out_dir)

    logging.info("Writing blog text to Markdown file")
    with open(out_file_path, "w") as f:
        f.write(blog_text.strip())

    return out_file_name

def md2hugo(md_file_path: str, out_file_path: str) -> None:
    """
    Opens a Markown file and reformats the title so
    that Hugo can interpret it as a new blog post.

    Args:
        md_file_path (str): The path to the input Markdown file.
        out_file_path (str): The output path to save the formatted Markdown file.

    Returns:
        None
    """
    logging.info("Extracting title form blog")

    # get original blog content
    with open(md_file_path, "r") as f:
        blog_text = f.read()

    # extract title (look for 1st level heading then 2nd level heading)
    match = re.search(r"^# (.*)$", blog_text, flags=re.MULTILINE)
    if match:
        blog_title = match.group(1)
        logging.info(f"Found blog title (1st level): {blog_title}")
    else:
        match = re.search(r"^## (.*)$", blog_text, flags=re.MULTILINE)
        if match:
            blog_title = match.group(1)
            logging.info(f"Found blog title (2nd level): {blog_title}")
        else:
            logging.warning("No blog title found in 1st or 2nd level headings")
            blog_title = "Blog Title"

    now = datetime.datetime.now(datetime.timezone.utc)
    now_str = now.isoformat(timespec="seconds")

    # new header
    header = f"""
---
title: "{blog_title.replace('"', "'")}"
date: {now_str}
draft: false
---

"""

    logging.info("Replacing file header")
    text_without_title = blog_text.split("\n")[1:]
    text_without_title = "\n".join(text_without_title).strip()
    new_blog_text = header + text_without_title
    with open(out_file_path, "w") as f:
        f.write(new_blog_text)