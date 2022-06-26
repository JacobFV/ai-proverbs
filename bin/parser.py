import re
import yaml

# input
file_name = "./what-ai-thinks-about-family.md"
_posts_dir = "./ai-proverbs/_posts/"

# post frontmatter
author = "Jacob"
categories = ["family"]
tags = []

for post in open(file_name).read().split('##'):
    post = post.strip()
    if post == "":
        continue
    title = post.split('\n')[0]
    # remove markdown formatting on title
    title = re.sub(r'\*\*|\*|_|__', '', title)

    # replaces underscores, spaces, etc with hyphens
    post_file_name = re.sub(r'[^\w-]', '-', title).lower()
    post_file_name = _posts_dir + post_file_name + ".md"
    with open(post_file_name, 'w') as f:
        f.writelines([
            f"---\n",
            f"layout: post\n",
            f"title:  {title}\n",
            f"author: {author}\n",
            f"categories: {categories}\n",
            f"tags: {tags}\n",
            f"image: assets/images/\n",
            f"description: \n",
            f"featured: false\n",
            f"hidden: false\n",
            f"rating: \n",
            f"---\n\n",
            f"{post}\n",
        ])
    print("Wrote " + post_file_name)
