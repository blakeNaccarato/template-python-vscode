<!-- TODO: Convert to RST -->

# Extensions

The following is a list of useful VSCode Extensions. Click the header of each to see the extension in your browser. Click "Install" and allow Chrome to launch VSCode for each Extension that you want to install. In general, you can find out what an extension does by clicking the "Feature Contributions" tab near the top of the extension description while you're viewing it in VSCode. Below is a brief description of each extension.

Throughout this guide, you will see items `>Extension: Like this (Shortcut)` that can be executed in the VSCode command palette by pressing `Ctrl+Shift+P` and typing some of the letters/words in the command. VSCode uses fuzzy matching, so you don't need to type the command exactly. Just type enough to narrow it down. If the command is bound to a key by default (or in our shared keyboard settings), the shortcut is in parentheses.

## [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)

Highlights comments that are tagged with "\!", "TODO", "\*", "?", in red, orange, light-green, or blue, respectively. Distinguishes between comments instead of the usual dark green everywhere. More useful for annotating JSON settings files than for code.

## [Bookmarks](https://marketplace.visualstudio.com/items?itemName=alefragnani.Bookmarks)

Similar to setting a debug breakpoint, except it's just a soft link to a line in the code that you're going to frequently.

## [Bracket Pair Colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer)

Colors matching pairs of brackets.

## [Bracketeer](https://marketplace.visualstudio.com/items?itemName=pustelto.bracketeer)

Allows replacing matched pairs of brackets/quotes with other bracket types. Useful for switching out `list` types for `set` or `dict` types in Python while refactoring code. You can also swap/remove quotes. For example, say you want the following to be a `set`.

```python
my_collection = ["John", "Engineer", 2]
```

- Place cursor just inside brackets, run command `> Expand selection (Shift+Alt+RightArrow)` until everything inside the brackets is selected
- Remove brackets `> Bracketeer: Remove brackets (Ctrl+Shift+Alt+I)`
- Enter the curly brace `{` on your keyboard. The selection will now be wrapped with curly braces
- Now you have a `set`

```python
my_collection = {"John", "Engineer", 2}
```

- Type in dictionary keys for each item
- Now you have a `dict`

```python
my_collection = {name: "John", job: "Engineer", years: 2}
```

You can always change your keyboard shortcuts of the commands used above `[> Preferences: Open Keyboard Shortcuts (Ctrl+K Ctrl+S)]` to your liking.

## [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)

For docstrings and readme files. It'll throw false positives, but should help cut down on spelling errors.

## [Data Preview](https://marketplace.visualstudio.com/items?itemName=RandomFractalsInc.vscode-data-preview)

Allows you to see CSV files in table format right inside VSCode.

`> Data: Preview Data`  
`> Data: Preview Remote Data`  
`> Data: Preview Data on Side`

## [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)

Some projects use Docker containers to simplify the development workflow. A team can define a certain development environment in a Docker container, then others can develop in that environment. Also useful for deploying repeatable environments to others. You need to install the Docker client on Windows, and you may want to enable WSL2 to leverage the new backend for Docker. Don't worry about this extension if you're just getting started.

## [DotENV](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv)

Syntax highlighting and features for manipulating `.env` files and the like. Such files are used for setting directory paths that are specific to your computer. Environment files allow teams to avoid hard-coding file paths into code.

Let's say that Sally has cloned a GitHub project at `C:\Users\Sally\Desktop\shared_project`, and John has cloned it to `C:\Users\John\Documents\shared_project`. Neither John nor Sally should be entering their directory paths into Python code for the project, since the absolute path to the project may differ. Instead, Sally can set `IMPORTANT_PATH = C:\Users\Sally\Desktop\shared_project` in an `.env` file, and John can set his own path in his own `.env` file. Then the code in the shared project can point to the *environment variable* as follows:

```python
important_path = os.environ["IMPORTANT_PATH"]
```

As long as John and Sally keep their own `.env` files (and make sure not to upload them to the shared GitHub repo using `.gitignore`), now the code can be generic and yet it will work for both John and Sally.

## [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml)

Just syntax highlighting and linting for a certain type of configuration file.

## [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory)

Allows plotting a flowchart of the progress of branches, commits, and merges to a repo.

## [Git Project Manager](https://marketplace.visualstudio.com/items?itemName=felipecaputo.git-project-manager)

Facilitates switching between git project folders from the command palette.

## [gitflow](https://marketplace.visualstudio.com/items?itemName=vector-of-bool.gitflow)

Helps with adherence to [git-flow](https://nvie.com/posts/a-successful-git-branching-model/), a tried-and-true branching model. Basically, you do most of your work on the `develop` branch, and the feature/issue branches that merge into it, either through conventional merging or pull requests. Only stable releases and hotfixes get merged to master/main. I mainly use this to automate releases, but it's not entirely necessary.

## [Git Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)

This allows you to browse Issues and Pull Requests for a GitHub repo, entirely within VSCode. Great for collaboration, as you can perform code review in the environment you're used to, rather than the web interface.

## [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

A great visualization of the active project. Shows branches, file history, facilitates comparison of all kinds. A must have.

## [HTTP/s and relative link checker](https://marketplace.visualstudio.com/items?itemName=blackmist.LinkCheckMD)

Ensure links are working in documentation.

## [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare)

The main extension for a shared remote workspace.

## [Live Share Audio](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare-audio)

Allows voice calls through VSCode. A bit buggy.

## [Live Share Whiteboard](https://marketplace.visualstudio.com/items?itemName=lostintangent.vsls-whiteboard)

A collaborative, live whiteboard in the Live Share session.

## [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)

Core markdown features. Allows refactoring of lists, headings, etc. in Markdown. This very guide is written in Markdown. It's a simple language with symbols that represent headers, lists, links  etc. Essentially surfaces the most important bits of HTML without requiring you to use a bunch of ugly tags.

## [Markdown+Math](https://marketplace.visualstudio.com/items?itemName=goessner.mdmath)

For entering equations into Markdown. Haven't tried this one out yet.

## [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)

Linting for Markdown. Enforces consistency in documentation, but is sometimes a bit aggressive if your use-case deviates too far from Markdown's original intent, for easy layout and hierarchy of sections of text. Complains if you use repeat headings, for example. You will learn when to conform to its recommendations, and when to occasionally suppress its warnings.

## [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

Enables virtually all the Python functionality of VSCode. Integrates functionality of language servers, linting, helper extensions, and more. You will come to learn which features are coming from where as you learn more, but for now just install this and configure it the way I describe.

## [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)

A shortcut to insert Numpy-style docstrings as you write code. Ultimately unnecessary, but useful at first while you're still learning docstring conventions.

## [Python Test Explorer for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter)

Haven't gotten into this yet, but I think it'll serve as a better test runner than the built-in functionality. It seems like it will be to code testing as GitLens is to git.

## [Test Explorer Status Bar](https://marketplace.visualstudio.com/items?itemName=connorshea.vscode-test-explorer-status-bar)

Puts test info in the bottom status bar of VSCode.

## [Test Explorer UI](https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer)

Part of the Test Explorer suite.

## [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)

Quick-and-dirty highlighting of CSV by coloring columns in-place. Use Data Preview for a more sophisticated view of data.

## [reStructuredText](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext)

Allows previewing documentation without having to explicitly rebuild it constantly. Good for interactive building of documentation.

## [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

For remoting into Docker containers and others.

## [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)

For SSH into servers and the like.

## [Remote - SSH: Editing Configuration Files](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh-edit)

Helper extension to Remote - SSH.

## [Remote - WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)

A must-have if you're working in WSL. You will eventually come across software that only works on Unix-like systems, and WSL will help you bridge that gap.

## [Rewrap](https://marketplace.visualstudio.com/items?itemName=stkb.rewrap)

For automatically wrapping text as you write. Performs hard-wrapping, useful in code comments and docstrings. Currently, I only soft-wrap documentation and Markdown, though that may change in the future.

## [Shell Launcher](https://marketplace.visualstudio.com/items?itemName=Tyriar.shell-launcher)

A way to launch multiple shells (PowerShell, Bash, IPython, etc.) besides the default one.

## [Test Explorer Live Share](https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer-liveshare)

For using the extended Test Explorer UI in a Live Share session.

## [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)

Another configuration file format helper extension. YAML is pretty common in Python libraries, so this is helpful.

## [vscode-icons](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons)

Adds icons to files/folders in the Explorer sidebar. Makes things a bit more visually distinct than the minimalist folding arrows of the default icon set.
