import os
import shutil
import re
from pathlib import Path

os.chdir(Path(__file__).parent.parent)
if os.path.exists('wiki'):
    shutil.rmtree('wiki')

os.mkdir('wiki')

link_re = re.compile(r'([^!]|^)\[(.+?)\]\((.+?)\.md\)')

def replace_link(text):
    def _on_link(res):
        prefix = res.group(1)
        title = res.group(2)
        href = res.group(3).replace("/", "-")
        print(title, href)
        return f"{prefix}[{title}]({href})"
    return link_re.sub(_on_link, text)

for root, dirs, files in os.walk('src'):
    for fn in files:
        text = open(f'{root}/{fn}').read()
        text = replace_link(text)
        if fn == 'SUMMARY.md':
            text = replace_link(text)
            open('wiki/Home.md', 'w').write(text)
        else:
            parnet = root[4:]
            fp = parnet + ("/" if parnet else "") + fn
            fp2 = fp.replace('/', '-')
            open(f'wiki/{fp2}', 'w').write(text)
