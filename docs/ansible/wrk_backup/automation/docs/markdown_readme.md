# Markdown Cheatsheet / Examples
## Introduction
Markdown is a text-to-HTML conversion 
tool for web writers. 
Quick reference and showcase to write Markdown page.
For moew details pl. visit,

Ref. Link -
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links

    ```
    "Github" 
     - https://daringfireball.net/projects/markdown/
    "Basic writing and formatting syntax."
     - https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax
    "Other Markdown tools:"
     - https://github.com/adam-p/markdown-here/wiki/Other-Markdown-Tools
    
    ``` 
 
## Table of contents
1. [Headers](#Headers)
2. [Emphasis](#Emphasis)
    1. [Ordered list](#Ordered list)
    2. [Unordered list](#Unordered list)
3. [Lists](#Lists)
4. [Links](#Links)
5. [Images](#Images)
6. [Code and Syntax Highlighting](#Code and Syntax Highlighting)
7. [Tables](#Tables)
8. [Blockquotes](#Blockquotes)
9. [Inline HTML](#Inline HTML)
10. [Horizontal Rule](#Horizontal Rule)
11. [Line Breaks](#Line Breaks)
12. [YouTube Videos](#YouTube Videos)
13. [Some more Examples](#Some more Examples)

## Headers<a name="Headers"></a>
This is test of H1.
# H1
## H2
### H3
#### H4
##### H5
###### H6

Alternatively, for H1 and H2, an underline-ish style:
E.g.
H1 using ==
========
and H2 using using ---
------
Use === for H1 and use --- for H2.

## Emphasis <a name="Emphasis"></a>
italics -  with *asterisks* or _underscores_.

bold -  with **asterisks** or __underscores__.

Combined - emphasis with **asterisks and _underscores_**.

Strikethrough - uses two tildes ~~Scratch this~~

## Lists <a name="Lists"></a>
(In this example, leading and trailing spaces are shown with with dots: ⋅)
#
###### Ordered list <a name="Ordered list"></a>
1. First ordered list item
2. Another item 
#
###### Unordered list <a name="Unordered list"></a>
- Unordered sub-list.
#
   1. Actual numbers don't matter, just that it's a number.
   2. Ordered sub-list.
   3. And another item.

    You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).
    To have a line break without a paragraph, you will need to use two trailing spaces.
    Note that this line is separate, but within the same paragraph.
    (This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)
#
* Unordered list can use asterisks
- Or minuses
+ Or pluses
#

## Links <a name="Links"></a>
There are two ways to create links.

[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../blob/master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links. 
http://www.example.com or <http://www.example.com> and sometimes 
example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

[arbitrary case-insensitive reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com

## Images <a name="Images"></a>
Here's our logo (hover to see the title text):

Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

Reference-style: 
![alt text][logo]

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"

## Code and Syntax Highlighting <a name="Code and Syntax Highlighting"></a>
Code blocks are part of the Markdown spec, but syntax highlighting 
isn't. However, many renderers -- like Github's and Markdown 
Here -- support syntax highlighting. Which languages are supported 
and how those language names should be written will vary from renderer 
to renderer. Markdown Here supports highlighting for dozens of 
languages (and not-really-languages, like diffs and HTTP headers); 
to see the complete list, and how to write the language names, see the 
highlight.js demo page.

    Inline `code` has `back-ticks around` it.

Blocks of code are either fenced by lines with three back-ticks ```, 
or are indented with four spaces. I recommend only using the fenced 
code blocks -- they're easier and only they support syntax 
highlighting.

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
 
```python
s = "Python syntax highlighting"
print s
```
 
```
    No language indicated, so no syntax highlighting. 
    But let's throw in a <b>tag</b>.


var s = "JavaScript syntax highlighting";
alert(s);

s = "Python syntax highlighting"
print s

No language indicated, so no syntax highlighting in Markdown Here (varies on Github). 
But let's throw in a <b>tag</b>.
```

## Tables <a name="Tables"></a>
Tables aren't part of the core Markdown spec, but they are part of GFM and Markdown 
Here supports them. They are an easy way of adding tables to your email -- a 
task that would otherwise require copy-pasting from another application.

Colons can be used to align columns.

| Tables        | Are         | Cool  
| ----------- |:-------------:| ---   :|
| Col 3 is the example of table in markdown.     | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

## Blockquotes <a name="Blockquotes"></a>
> Blockquotes are very handy in email to emulate reply text. 
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when 
it wraps. Oh boy let's keep writing to make sure this is long 
enough to actually wrap for everyone. Oh, you can *put* **Markdown** 
into a blockquote. 

## Inline HTML <a name="Inline HTML"></a>
You can also use raw HTML in your Markdown, and it'll mostly 
work pretty well.
<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
</dl>

## Horizontal Rule <a name="Horizontal Rule"></a>

**Three or more Hypenes, Asterisks or Underscores. E.g.**

----
Hyphens

***
Asterisks
___
______
Underscores

## Line Breaks <a name="Line Breaks"></a>
My basic recommendation for learning how line breaks work is to 
experiment and discover -- hit <Enter> once (i.e., insert one 
newline), then hit it twice (i.e., insert two newlines), see 
what happens. You'll soon learn to get what you want. 
"Markdown Toggle" is your friend.

Here are some things to try out:

Here's a line for us to start with.


This line is separated from the one above by two newlines, so it 
will be a *separate paragraph*.

This line is also a separate paragraph, but...
This line is only separated by a single newline, so it's a 
separate line in the *same paragraph*.

## YouTube Videos <a name="YouTube Videos"></a>
They can't be added directly but you can add an image with a 
link to the video like this:

<a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VIDEO_ID_HERE
"target="_blank"> <img src="http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="140" height="80" border="10" /></a>

Or, in pure Markdown, but losing the image sizing and border:
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)


Referencing a bug by #bugID in your git commit links it to the slip. For example #1.

## Some more Examples <a name="Some more Examples"></a>

### Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs help` - Print this help message.

### Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

### Test page
    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

### Mark text (Yellow Backgroud to highlight text)
<mark> yellow background </mark>
