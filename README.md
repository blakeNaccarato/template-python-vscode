# template_python_vscode

Template repo for Python projects in VSCode.

## Tree

The files that are intended to be duplicated to each project.

```Text
template_python_vscode
├── .github
│   └── workflows
│       └── close.yml
├── .vscode
│   ├── launch.json
│   └── settings.json
├── .env
├── .flake8
├── .gitignore
└── .pylintrc
```

## Environment File (`.env`)

General environment file. While developing, sometimes you need to set paths and special variables that are specific to your machine. For example, OpenCV expects to see the environment variables `OPENCV_DIR`, `OPENCV_SAMPLES_DATA_PATH`, and `PYTHONPATH` set appropriately. The way that you set these variables will vary by platform.

### PowerShell and Set-PSEnv in Windows

You can install `Set-PSEnv` with `Install-Module -Name Set-PsEnv.` This module supports setting variables as well as prefixing with `:=` and appending with `=:`. An example follows.

#### `.env`

```env
OPENCV_DIR = C:\opencv\4.4.0
OPENCV_SAMPLES_DATA_PATH = C:\opencv\4.4.0\samples
PYTHONPATH = C:\opencv\4.4.0\python
PATH := C:\opencv\4.4.0\x64\vc15\bin
```

#### Sources

<https://www.powershellgallery.com/packages/Set-PsEnv/>  
<https://github.com/rajivharris/Set-PsEnv/blob/master/README.md>

### python-dotenv in Python

You can install `python-dotenv` with `pip install python-dotenv`. You can then load
your environment directly in Python code. However, you should avoid hardcoding
environment loading like this, as end-user code is run in the end-user's environment.
You can invoke `dotenv` in a developer context, as a pre-launch task or something of
the sort. Note that you cannot prefix/append to existing environment variables with
this format.  

#### `.env`

```env
OPENCV_DIR = C:\opencv\4.4.0
OPENCV_SAMPLES_DATA_PATH = C:\opencv\4.4.0\samples
PYTHONPATH = C:\opencv\4.4.0\python
```

<https://pypi.org/project/python-dotenv/>

### Sourcing an .env file in `~/.bashrc`

If you are working in Ubuntu or another UNIX-like system, you can put the following
into your `~/.bashrc` to source environment variables. You can prefix/append with a
different syntax

#### `~/.bashrc`

```bash
#? Import dotenv aka .env environment variables if it is found
if [ -f ./.env ] ; then
    set -o allexport # enable shell option to export all created variables
    source ./.env # now this will export all vars instead of just one
    set +o allexport # disable shell option to export all created variables
fi
```

#### `.env`

```env
OPENCV_DIR=~/opencv/4.4.0
OPENCV_SAMPLES_DATA_PATH=~/opencv/4.4.0/samples
PYTHONPATH=~/opencv/4.4.0/python
PATH=~/opencv/4.4.0/x64/vc15/bin:$PATH
```

### Environment handling in VSCode

Aside from the approaches just discussed, VSCode configurations can also handle environment setup. From experience up to August 2020, the following approaches approaches don't always work the same for every system. So for now, it is preferable to use one of the above approaches for environment handling. There are `"terminal.integrated.env.windows"` and `"python.envFile"` keys in `settings.json`. There are `"env"` and `"envFile"` keys in `launch.json`.
