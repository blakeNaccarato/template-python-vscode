# Extensions

The following is a list of useful VSCode Extensions. Click the header of each to see the extension in your browser. Click "Install" and allow Chrome to launch VSCode for each Extension that you want to install. In general, you can find out what an extension does by clicking the "Feature Contributions" tab near the top of the extension description while you're viewing it in VSCode. Below is a brief description of each extension.

Throughout this guide, you will see items `>Extension: Like this (Shortcut)` that can be executed in the VSCode command palette by pressing `Ctrl+Shift+P` and typing some of the letters/words in the command. VSCode uses fuzzy matching, so you don't need to type the command exactly. Just type enough to narrow it down. If the command is bound to a key by default (or in our shared keyboard settings), the shortcut is in parentheses.

## [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)

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

## [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory)

## [Git Project Manager](https://marketplace.visualstudio.com/items?itemName=felipecaputo.git-project-manager)

## [gitflow](https://marketplace.visualstudio.com/items?itemName=vector-of-bool.gitflow)

## [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)

## [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

## [HTTP/s and relative link checker](https://marketplace.visualstudio.com/items?itemName=blackmist.LinkCheckMD)

## [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare)

## [Live Share Audio](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare-audio)

## [Live Share Whiteboard](https://marketplace.visualstudio.com/items?itemName=lostintangent.vsls-whiteboard)

## [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)

## [Markdown+Math](https://marketplace.visualstudio.com/items?itemName=goessner.mdmath)

## [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)

## [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)

## [Python Test Explorer for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter)

## [Test Explorer Status Bar](https://marketplace.visualstudio.com/items?itemName=connorshea.vscode-test-explorer-status-bar)

## [Test Explorer UI](https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer)

## [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)

## [reStructuredText](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext)

## [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)

## [Remote - SSH: Editing Configuration Files](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh-edit)

## [Remote - WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)

## [Rewrap](https://marketplace.visualstudio.com/items?itemName=stkb.rewrap)

## [Shell Launcher](https://marketplace.visualstudio.com/items?itemName=Tyriar.shell-launcher)

## [Test Explorer Live Share](https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer-liveshare)

## [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)

## [vscode-icons](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons)
