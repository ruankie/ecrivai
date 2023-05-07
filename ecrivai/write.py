import os
import datetime

def to_markdown(blog_text: str, out_dir: str = "content/") -> None:
    """
    Given the blog text, write it to a markdown file in the
    output dir. The output file will have the date and time
    as a name.
    """
    now = datetime.datetime.now()
    now_str = now.strftime("%Y%m%d%H%M")

    out_file_name = f"{now_str}.md"
    out_file_path = os.path.join(out_dir, out_file_name)

    with open(out_file_path, "w") as f:
        f.write(blog_text.strip())