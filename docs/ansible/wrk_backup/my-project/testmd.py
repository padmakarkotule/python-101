from markdown import Markdown
from mdx_gfm import GithubFlavoredMarkdownExtension

# extensions is a list, even if it's just one
md = Markdown(extensions=[GithubFlavoredMarkdownExtension()])

source = '''```python
print('Hello World')
```'''

html = md.convert(source)