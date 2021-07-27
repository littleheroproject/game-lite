import os
import shutil
import re
from pathlib import Path

os.chdir(Path(__file__).parent.parent)
if os.path.exists('src'):
    shutil.rmtree('src')

os.mkdir('src')

link_re = re.compile(r'([^!]|^)\[(.+?)\]\((.+?)(#.+?)?\)')
def replace_link(text):
    return link_re.sub("\g<1>[\g<2>](\g<3>.md\g<4>)", text)

for fn in os.listdir('wiki'):
    if os.path.isdir(fn):
        continue
    text = open(f'wiki/{fn}').read()
    text = replace_link(text)
    if fn == 'Home.md':
        target = 'SUMMARY.md'
    else:
        target = fn
    open(f'src/{target}', 'w').write(text)
