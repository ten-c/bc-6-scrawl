# **Scrawl**
A python based note-taking console app

> **"Scrawl"** - *write (something) in a hurried, careless way.*

## **1. Installation**
### Prerequisites:

 1. Python
    - supports both 2 and 3
 2. Python pip module

### Recommended / Optional:
 - virtualenv to isolate the project
    - [Virtualenv (unix based systems)](https://github.com/pypa/virtualenv)
    - [Virtualenv (for windows)](https://github.com/davidmarble/virtualenvwrapper-win)

### Steps to get scrawling:

1. [optional] create a virtualenv and activate it
2. On the console :
        - `pip install scrawl`

#### ***That's it !!***

----------

## **2.Usage:**
-----
Once installed, scrawl exposes two interfaces to be used in issuing commands:

    1. $ scrawl
    2. $ scrawl2
**1. scrwal:**
<table><thead><tr><th>Command</th><th>Use</th><th>Arguments</th><th>Options</th></tr></thead><tbody><tr><td>createnote</td><td>Command to create a note</td><td>content</td><td></td></tr><tr><td>viewnote</td><td>view a specific note</td><td>note id</td><td></td></tr><tr><td>listnotes</td><td>view/display notes</td><td></td><td>--limit
 display notes in sets of --limit</td></tr><tr><td>searchnotes</td><td>search notes</td><td></td><td>--limit
 display search result in sets of --limit</td></tr><tr><td>export</td><td>export notes</td><td>[filename]
</td><td>[--csv]</td></tr><tr><td>importnotes</td><td>import notes</td><td>[path]</td><td></td></tr><tr><td>sync</td><td>sync notes with firebase</td><td></td><td></td></tr></tbody></table>


> *all commands provide help on how there are be used.
> Just issue scrawl {command} --help*

**2. scrawl2 :**
>  **why scrawl2 ?**
>  *scrwal2 delivers same functionality as scrawl above but with:*
>  - better UI
>      + Command results, prompts and notifications are displayed in colorful manner as opposed to monochrome
>  - addedd functionality tabulated below:

<table><thead><tr><th>Command</th><th>New Arguments
 & why</th><th>New Options
 & why</th></tr></thead><tbody><tr><td>createnote</td><td>-</td><td>
            [--title] : a note should be titled.

            [--noeditor : ability to use editor or not. default = editor]
            </td></tr><tr><td>viewnote</td><td></td><td></td></tr><tr><td>listnotes</td><td></td><td></td></tr><tr><td>searchnotes</td><td></td><td>
                [--field] - to specify field to query - title or content
                <br>
                highlights the queried string
            </td></tr><tr><td>export</td><td>[filename]
</td><td>[--csv]</td></tr><tr><td>importnotes</td><td>[path]</td><td></td></tr><tr><td>sync</td><td></td><td>Progress bars</td></tr></tbody></table>

# App-related links
- [Firebase link ](https://bc-6-scrawl.firebaseio.com/)
- [Package on pypi](https://pypi.python.org/pypi/scrawl)
- [Sample json data](https://drive.google.com/file/d/0B8bTejAhLbuFQTdoSGpDalJsT3c/view?usp=sharing)