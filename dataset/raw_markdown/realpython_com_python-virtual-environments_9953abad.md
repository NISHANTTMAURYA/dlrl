[ ![Real Python](/static/real-python-logo.893c30edea53.svg) ](/)

  * [Start Here](/start-here/)
  * [ Learn Python ](#)

[Python Tutorials →  
In-depth articles and video courses](/search?kind=article&kind=course&order=newest) [Learning Paths →  
Guided study plans for accelerated learning](/learning-paths/) [Quizzes & Exercises →  
Check your learning progress](/quizzes/) [Browse Topics →  
Focus on a specific area or skill level](/tutorials/all/) [Community Chat →  
Learn with other Pythonistas](/community/) [Office Hours →  
Live Q&A; calls with Python experts](/office-hours/) [Podcast →  
Hear what’s new in the world of Python](/podcasts/rpp/) [Books →  
Round out your knowledge and learn offline](/products/books/) [Reference →  
Concise definitions for common Python terms](/ref/) [Code Mentor →Beta  
Personalized code assistance & learning tools](/mentor/) [Unlock All Content →](/account/join/)

  * [ More ](#)

[Learner Stories](/learner-stories/) [Python Newsletter](/newsletter/) [Python Job Board](https://www.pythonjobshq.com) [Meet the Team](/team/) [Become a Tutorial Writer](/write-for-us/) [Become a Video Instructor](/become-an-instructor/)




  * [ Search](/search "Search")



[](/search "Search") /

  * [Join](/account/join/)
  * [Sign‑In](/account/login/?next=%2Fpython-virtual-environments-a-primer%2F)



— FREE Email Series —

🐍 Python Tricks 💌

![Python Tricks Dictionary Merge](/static/pytrick-dict-merge.4201a0125a5e.png)

Get Python Tricks »

🔒 No spam. Unsubscribe any time.

[Browse Topics](/tutorials/all/) [Guided Learning Paths](/learning-paths/)   
[ Basics](/search?level=basics) [ Intermediate](/search?level=intermediate) [ Advanced](/search?level=advanced)

* * *

[ai](/tutorials/ai/) [api](/tutorials/api/) [best-practices](/tutorials/best-practices/) [career](/tutorials/career/) [community](/tutorials/community/) [databases](/tutorials/databases/) [data-science](/tutorials/data-science/) [data-structures](/tutorials/data-structures/) [data-viz](/tutorials/data-viz/) [devops](/tutorials/devops/) [django](/tutorials/django/) [docker](/tutorials/docker/) [editors](/tutorials/editors/) [flask](/tutorials/flask/) [front-end](/tutorials/front-end/) [gamedev](/tutorials/gamedev/) [gui](/tutorials/gui/) [machine-learning](/tutorials/machine-learning/) [news](/tutorials/news/) [numpy](/tutorials/numpy/) [projects](/tutorials/projects/) [python](/tutorials/python/) [testing](/tutorials/testing/) [tools](/tutorials/tools/) [web-dev](/tutorials/web-dev/) [web-scraping](/tutorials/web-scraping/)

[Table of Contents](#toc)

  * [How Can You Work With a Python Virtual Environment?](#how-can-you-work-with-a-python-virtual-environment)
    * [Create It](#create-it)
    * [Activate It](#activate-it)
    * [Install Packages Into It](#install-packages-into-it)
    * [Deactivate It](#deactivate-it)
  * [How Do You Enable a Venv in Your IDE?](#how-do-you-enable-a-venv-in-your-ide)
    * [Create and Activate a Virtual Environment in VS Code](#create-and-activate-a-virtual-environment-in-vs-code)
    * [Create and Activate a Virtual Environment in PyCharm](#create-and-activate-a-virtual-environment-in-pycharm)
  * [Why Do You Need Virtual Environments?](#why-do-you-need-virtual-environments)
    * [Avoid System Pollution](#avoid-system-pollution)
    * [Sidestep Dependency Conflicts](#sidestep-dependency-conflicts)
    * [Minimize Reproducibility Issues](#minimize-reproducibility-issues)
    * [Dodge Installation Privilege Lockouts](#dodge-installation-privilege-lockouts)
  * [What Is a Python Virtual Environment?](#what-is-a-python-virtual-environment)
    * [A Folder Structure](#a-folder-structure)
    * [An Isolated Python Installation](#an-isolated-python-installation)
  * [How Does a Virtual Environment Work?](#how-does-a-virtual-environment-work)
    * [It Copies Structure and Files](#it-copies-structure-and-files)
    * [It Adapts the Prefix-Finding Process](#it-adapts-the-prefix-finding-process)
    * [It Links Back to Your Standard Library](#it-links-back-to-your-standard-library)
    * [It Modifies Your PYTHONPATH](#it-modifies-your-pythonpath)
    * [It Changes Your Shell PATH Variable on Activation](#it-changes-your-shell-path-variable-on-activation)
    * [It Runs From Anywhere With Absolute Paths](#it-runs-from-anywhere-with-absolute-paths)
  * [How Can You Customize a Virtual Environment?](#how-can-you-customize-a-virtual-environment)
    * [Change the Command Prompt](#change-the-command-prompt)
    * [Overwrite Existing Environments](#overwrite-existing-environments)
    * [Create Multiple Virtual Environments at Once](#create-multiple-virtual-environments-at-once)
    * [Update the Core Dependencies](#update-the-core-dependencies)
    * [Avoid Installing pip](#avoid-installing-pip)
    * [Include the System Site-Packages](#include-the-system-site-packages)
    * [Copy or Link Your Executables](#copy-or-link-your-executables)
    * [Upgrade Your Python to Match the System Python](#upgrade-your-python-to-match-the-system-python)
  * [What Other Popular Options Exist, Aside From venv?](#what-other-popular-options-exist-aside-from-venv)
    * [The Virtualenv Project](#the-virtualenv-project)
    * [The Conda Package and Environment Manager](#the-conda-package-and-environment-manager)
  * [How Can You Manage Your Virtual Environments?](#how-can-you-manage-your-virtual-environments)
    * [Decide Where to Create Your Environment Folders](#decide-where-to-create-your-environment-folders)
    * [Treat Them as Disposables](#treat-them-as-disposables)
    * [Pin Your Dependencies](#pin-your-dependencies)
    * [Avoid Virtual Environments in Production](#avoid-virtual-environments-in-production)
    * [Use Third-Party Tools](#use-third-party-tools)
  * [Conclusion](#conclusion)
  * [Frequently Asked Questions](#frequently-asked-questions)



Mark as Completed

[](/feedback/survey/article/python-virtual-environments-a-primer/liked/?from=article-sidebar "Liked it") [](/feedback/survey/article/python-virtual-environments-a-primer/disliked/?from=article-sidebar "Disliked it")

Share

Recommended Video Course  
[Working With Python Virtual Environments](/courses/working-python-virtual-environments/)

![Python Virtual Environments \(venv\)](https://files.realpython.com/media/Python-Virtual-Environments_Watermarked.4c787192d42f.jpg)

# Python Virtual Environments: A Primer

by [Martin Breuss](#author) Publication date Nov 30, 2024 Reading time estimate 1h 37m [](#reader-comments) [intermediate](/tutorials/intermediate/) [devops](/tutorials/devops/) [tools](/tutorials/tools/)

Mark as Completed Share

Table of Contents

  * [How Can You Work With a Python Virtual Environment?](#how-can-you-work-with-a-python-virtual-environment)
    * [Create It](#create-it)
    * [Activate It](#activate-it)
    * [Install Packages Into It](#install-packages-into-it)
    * [Deactivate It](#deactivate-it)
  * [How Do You Enable a Venv in Your IDE?](#how-do-you-enable-a-venv-in-your-ide)
    * [Create and Activate a Virtual Environment in VS Code](#create-and-activate-a-virtual-environment-in-vs-code)
    * [Create and Activate a Virtual Environment in PyCharm](#create-and-activate-a-virtual-environment-in-pycharm)
  * [Why Do You Need Virtual Environments?](#why-do-you-need-virtual-environments)
    * [Avoid System Pollution](#avoid-system-pollution)
    * [Sidestep Dependency Conflicts](#sidestep-dependency-conflicts)
    * [Minimize Reproducibility Issues](#minimize-reproducibility-issues)
    * [Dodge Installation Privilege Lockouts](#dodge-installation-privilege-lockouts)
  * [What Is a Python Virtual Environment?](#what-is-a-python-virtual-environment)
    * [A Folder Structure](#a-folder-structure)
    * [An Isolated Python Installation](#an-isolated-python-installation)
  * [How Does a Virtual Environment Work?](#how-does-a-virtual-environment-work)
    * [It Copies Structure and Files](#it-copies-structure-and-files)
    * [It Adapts the Prefix-Finding Process](#it-adapts-the-prefix-finding-process)
    * [It Links Back to Your Standard Library](#it-links-back-to-your-standard-library)
    * [It Modifies Your PYTHONPATH](#it-modifies-your-pythonpath)
    * [It Changes Your Shell PATH Variable on Activation](#it-changes-your-shell-path-variable-on-activation)
    * [It Runs From Anywhere With Absolute Paths](#it-runs-from-anywhere-with-absolute-paths)
  * [How Can You Customize a Virtual Environment?](#how-can-you-customize-a-virtual-environment)
    * [Change the Command Prompt](#change-the-command-prompt)
    * [Overwrite Existing Environments](#overwrite-existing-environments)
    * [Create Multiple Virtual Environments at Once](#create-multiple-virtual-environments-at-once)
    * [Update the Core Dependencies](#update-the-core-dependencies)
    * [Avoid Installing pip](#avoid-installing-pip)
    * [Include the System Site-Packages](#include-the-system-site-packages)
    * [Copy or Link Your Executables](#copy-or-link-your-executables)
    * [Upgrade Your Python to Match the System Python](#upgrade-your-python-to-match-the-system-python)
  * [What Other Popular Options Exist, Aside From venv?](#what-other-popular-options-exist-aside-from-venv)
    * [The Virtualenv Project](#the-virtualenv-project)
    * [The Conda Package and Environment Manager](#the-conda-package-and-environment-manager)
  * [How Can You Manage Your Virtual Environments?](#how-can-you-manage-your-virtual-environments)
    * [Decide Where to Create Your Environment Folders](#decide-where-to-create-your-environment-folders)
    * [Treat Them as Disposables](#treat-them-as-disposables)
    * [Pin Your Dependencies](#pin-your-dependencies)
    * [Avoid Virtual Environments in Production](#avoid-virtual-environments-in-production)
    * [Use Third-Party Tools](#use-third-party-tools)
  * [Conclusion](#conclusion)
  * [Frequently Asked Questions](#frequently-asked-questions)



[Remove ads](/account/join/)

Watch Now This tutorial has a related video course created by the Real Python team. Watch it together with the written tutorial to deepen your understanding: [**Working With Python Virtual Environments**](/courses/working-python-virtual-environments/)

Creating a Python virtual environment allows you to manage dependencies separately for different projects, preventing conflicts and maintaining cleaner setups. With Python’s `venv` module, you can create isolated environments that use different versions of libraries or Python itself. This tutorial guides you through creating, activating, and managing these environments efficiently.

**By the end of this tutorial, you ’ll understand that:**

  * Python virtual environments provide **lightweight and isolated** Python development environments.
  * You can use Python’s **`venv` module** to manage dependencies **independently for each project**.
  * You create and **set up a venv in Python** using the command `python -m venv path/to/venv/`.
  * You **refer** to a virtual environment by the **folder name** that you used when creating the venv.
  * You **activate a venv on Windows** with `venv\Scripts\activate`, and **on macOS and Linux** with `source venv/bin/activate`.
  * You can **enable a venv in VS Code** by opening the Command Palette and choosing _Python: Select Interpreter_.



Working with virtual environments is a common and effective practice in Python development. Gaining a better understanding of how they work, why you need them, and what you can do with them will help you master your Python programming workflow.

Throughout the tutorial, you can select code examples for either Windows, Linux, or macOS. Pick your platform at the top right of the relevant code blocks to get the commands that you need, and feel free to switch between them if you want to learn how to work with virtual environments on other operating systems.

**Get Your Cheat Sheet:** [Click here to download a free cheat sheet](https://realpython.com/bonus/python-virtual-environments-a-primer-pdf/) that summarizes the main venv commands you’ll learn about in this tutorial.

**Take the Quiz:** Test your knowledge with our interactive “Python Virtual Environments: A Primer” quiz. You’ll receive a score upon completion to help you track your learning progress:

* * *

[ ![Python Virtual Environments \(venv\)](https://files.realpython.com/media/Python-Virtual-Environments_Watermarked.4c787192d42f.jpg) ](/quizzes/python-virtual-environments-a-primer/)

**Interactive Quiz**

[Python Virtual Environments: A Primer](/quizzes/python-virtual-environments-a-primer/)

In this quiz, you'll test your understanding of Python virtual environments. With this knowledge, you'll be able to avoid dependency conflicts and help other developers reproduce your development environment.

## How Can You Work With a Python Virtual Environment?[](#how-can-you-work-with-a-python-virtual-environment "Permanent link")

If you just need to get a virtual environment up and running to continue working on your favorite project, then this section is for you.

This tutorial uses [Python’s `venv` module](https://docs.python.org/3/library/venv.html) to create virtual environments. This module is part of Python’s standard library, and it’s been the [officially recommended](https://docs.python.org/3/library/venv.html#creating-virtual-environments) way to create virtual environments since Python 3.5.

**Note:** There are other great third-party tools for creating virtual environments, such as [conda](#the-conda-package-and-environment-manager) and [virtualenv](#the-virtualenv-project), that you’ll learn more about later in this tutorial. Either of these tools can help you set up a virtual environment and also go beyond just that.

For basic usage, `venv` is an excellent choice because it already comes packaged with your Python installation. With that in mind, you’re ready to create your first virtual environment.

[ Remove ads](/account/join/)

### Create It[](#create-it "Permanent link")

Any time you’re working on a Python project that uses external dependencies you’re [installing with `pip`](https://realpython.com/what-is-pip/), it’s best to first create a virtual environment:

  * [Windows](#windows-1)
  * [Linux](#linux-1)
  * [macOS](#macos-1)



Windows PowerShell
    
    
    PS> py -m venv venv\
    

This command allows the [Python launcher for Windows](https://docs.python.org/3/using/windows.html#launcher) to select an appropriate version of Python to execute. It comes bundled with the official installation and is the most convenient way to execute [Python on Windows](https://realpython.com/python-coding-setup-windows/).

You can bypass the launcher and run the Python executable directly using the `python` command, but if you haven’t configured the `PATH` and `PATHEXT` variables, then you might need to provide the full path:

Windows PowerShell
    
    
    PS> C:\Users\Name\AppData\Local\Programs\Python\Python312\python -m venv venv\
    

The system path shown above assumes that you installed Python 3.12 using the Windows installer provided by the [Python downloads page](https://www.python.org/downloads/). The path to the Python executable on your system might be different. Working with PowerShell, you can find the path using the `where.exe python` command.

**Note:** You don’t need to include the backslash (`\`) at the end of the name of your virtual environment, but it’s a helpful reminder that you’re creating a folder.

Shell
    
    
    $ python3 -m venv venv/
    

Many Linux operating systems ship with a version of Python 3. If `python3` doesn’t work, then you’ll have to first [install Python](https://realpython.com/installing-python/) and you may need to use the specific name of the executable version that you installed, for example, `python3.12` for Python 3.12.x. If that’s the case for you, remember to replace mentions of `python3` in the code blocks with your specific version number.

**Note:** You don’t need to include the slash (`/`) at the end of the name of your virtual environment, but it’s a helpful reminder that you’re creating a folder.

Shell
    
    
    $ python3 -m venv venv/
    

Older versions of macOS come with a system installation of Python 2.7.x that you should _never_ use to run your scripts. If you’re working on macOS < 12.3 and invoke the Python interpreter with `python` instead of `python3`, then you might accidentally start up the outdated system Python interpreter.

If running `python3` doesn’t work, then you’ll have to first [install a modern version of Python](https://realpython.com/installing-python/).

**Note:** You don’t need to include the slash (`/`) at the end of the name of your virtual environment, but it’s a helpful reminder that you’re creating a folder.

This command creates a new virtual environment named _venv_ using Python’s built-in `venv` module. The first `venv` that you use in the command specifies the module, and the second `venv/` sets the name for your virtual environment. You could name it differently, but calling it _venv_ is a good practice for consistency.

### Activate It[](#activate-it "Permanent link")

Great! Your project now has its own virtual environment. Generally, before you start to use it, you’ll **activate** the environment by executing a script that comes with the installation:

  * [Windows](#windows-2)
  * [Linux + macOS](#linux-macos-2)



Windows PowerShell
    
    
    PS> venv\Scripts\activate
    (venv) PS>
    

If your attempt to run this command produces an error, then you’ll first have to [loosen the execution policy](https://realpython.com/python-coding-setup-windows/#loosening-your-execution-policy).

Shell
    
    
    $ source venv/bin/activate
    (venv) $
    

Before you run this command, make sure that you’re in the folder containing the virtual environment you just created. If you’ve named your virtual environment something other than _venv_ , then you’ll have to use that name in the path instead of _venv_ when you source the activation script.

**Note:** You can also work with your virtual environment without activating it. To do this, you [provide the full path](#it-runs-from-anywhere-with-absolute-paths) to its Python interpreter when executing a command. However, you’ll likely want to activate the virtual environment after you create it to save yourself the effort of having to repeatedly type long pathnames.

Once you can see the name of your virtual environment in your command prompt—in this case `(venv)`—then you’ll know that your virtual environment is active. Now you’re all set and ready to install your external packages!

### Install Packages Into It[](#install-packages-into-it "Permanent link")

After you’ve created and activated your virtual environment, you can install any external dependencies that you need for your project:

  * [Windows](#windows-3)
  * [Linux + macOS](#linux-macos-3)



Windows PowerShell
    
    
    (venv) PS> python -m pip install <package-name>
    

Shell
    
    
    (venv) $ python -m pip install <package-name>
    

This command is the default command that you should use to install external Python packages with `pip`. Because you first created and activated the virtual environment, `pip` will install the packages in an isolated location.

**Note:** Since you created your virtual environment using a version of Python 3, you don’t need to call `python3` or `pip3` explicitly. As long as your virtual environment is active, `python` and `pip` link to the same executable files that `python3` and `pip3` do.

You can now install your packages to your virtual environment. To get to this point, you created a virtual environment named `venv` and then activated it in your current shell session.

As long as you don’t close your terminal, every [Python package](https://realpython.com/python-modules-packages/) that you install will end up in this isolated environment instead of your global Python site-packages. This means that you can now work on your Python project without worrying about dependency conflicts.

[ Remove ads](/account/join/)

### Deactivate It[](#deactivate-it "Permanent link")

Once you’re done working with this virtual environment, you can deactivate it:

  * [Windows](#windows-4)
  * [Linux + macOS](#linux-macos-4)



Windows PowerShell
    
    
    (venv) PS> deactivate
    PS>
    

Shell
    
    
    (venv) $ deactivate
    $
    

After executing the `deactivate` command, your command prompt returns to normal. This change means that you’ve exited your virtual environment. If you interact with Python or `pip` now, you’ll interact with your globally configured Python environment.

If you want to go back into a virtual environment that you’ve created before, then you’ll need to [run the activate script](#activate-it) for that virtual environment once again.

Before you install a package, look for the name of your virtual environment within parentheses just before your command prompt. In the example above, the name of the environment is `venv`.

If the name appears, then you know that your virtual environment is active and you can install your external dependencies. If you don’t see the name in your command prompt, remember to activate your Python virtual environment before installing any packages.

At this point, you’ve covered the essentials of working with Python virtual environments using the `venv` module.

## How Do You Enable a Venv in Your IDE?[](#how-do-you-enable-a-venv-in-your-ide "Permanent link")

Working with virtual environments directly from your [Integrated Development Environment (IDE)](https://realpython.com/python-ides-code-editors-guide/) can streamline your development process. Popular IDEs like [Visual Studio Code (VS Code)](https://realpython.com/python-development-visual-studio-code/) and [PyCharm](https://realpython.com/pycharm-guide/) provide built-in support for managing Python virtual environments, allowing you to create, activate, and manage them without leaving the editor.

### Create and Activate a Virtual Environment in VS Code[](#create-and-activate-a-virtual-environment-in-vs-code "Permanent link")

Visual Studio Code is a lightweight but powerful code editor that supports Python development. To create and activate a [Python environment in VS Code](https://code.visualstudio.com/docs/python/environments), follow these steps:

  1. **Open Your Workspace** : Launch VS Code and open the folder that contains your Python project.

  2. **Open the Integrated Terminal** : Navigate to _View → Terminal_ in the menu to launch the integrated terminal.

  3. **Create a Virtual Environment** : In the terminal, create a new virtual environment with the `venv` module using the commands that you saw [earlier](#create-it).

  4. **Activate the Virtual Environment** : Still using the integrated terminal, use your platform-specific command to [activate the virtual environment](#activate-it).




VS Code may automatically detect the active virtual environment. To ensure that you’re using it for all project files, open the Command Palette by pressing `Ctrl`+`Shift`+`P` on Windows and Linux, or `Cmd`+`Shift`+`P` on macOS, and start typing _Python: Select Interpreter_ until it shows up as an option:

[![A view of the VS Code editor with an open command prompt showing the option to select the Python interpreter is highlighted](https://files.realpython.com/media/venv-vscode-command-prompt-select-interpreter.e163a162f62c.png)](https://files.realpython.com/media/venv-vscode-command-prompt-select-interpreter.e163a162f62c.png)

After you press `Enter` to select that command option, VS Code will display a drop-down of available Python interpreters. This list may be shorter or longer for you, depending on how many virtual environments VS Code discovers on your system. Use the arrow keys to find the virtual environment you just created:

[![A view on the VS Code command palette displaying a drop down to select a Python interpreter from multiple options](https://files.realpython.com/media/venv-vscode-select-interpreter.4c89e6ce8f05.png)](https://files.realpython.com/media/venv-vscode-select-interpreter.4c89e6ce8f05.png)

You’ll know that it’s the right one if the path to the interpreter displays as `.\venv\Scripts\python` on Windows or `./venv/bin/python` on macOS and Linux. Press `Enter` to select that interpreter within your newly created virtual environment.

With these steps, you’ve successfully set up and activated a virtual environment in VS Code. You’ll also see the changes reflected in the VS Code status bar, which shows the name of the active interpreter.

[ Remove ads](/account/join/)

### Create and Activate a Virtual Environment in PyCharm[](#create-and-activate-a-virtual-environment-in-pycharm "Permanent link")

PyCharm, another leading Python IDE, offers robust support for managing virtual environments within your Python projects. In a couple of scenarios, PyCharm handles the virtual environment creation and activation for you.

If you open an existing PyCharm project that already has a virtual environment in the project folder, then PyCharm will automatically recognize and activate it for you:

[![PyCharm interface showing an activated virtual environment after opening a project that already has a virtual environment](https://files.realpython.com/media/venv-pycharm-open-project-with-existing-venv.f36ef52efdd3.png)](https://files.realpython.com/media/venv-pycharm-open-project-with-existing-venv.f36ef52efdd3.png)

If you create a new PyCharm project, then it’ll prompt you to create a virtual environment by selecting a tooling option and a base Python interpreter:

[![PyCharm window prompting you to create a new virtual environment for a new project](https://files.realpython.com/media/venv-pycharm-new-project.0593b22ce307.png)](https://files.realpython.com/media/venv-pycharm-new-project.0593b22ce307.png)

After you click _Create_ , PyCharm sets up the virtual environment with the default name `.venv` and activates it for you:

[![PyCharm project windows showing a new and activated virtual environment path](https://files.realpython.com/media/venv-pycharm-new-project-created.abb76ef641dc.png)](https://files.realpython.com/media/venv-pycharm-new-project-created.abb76ef641dc.png)

Both of these options are straightforward and you won’t have to do a lot for PyCharm to present you with a working virtual environment.

Finally, if you open up an existing project that doesn’t yet have a virtual environment folder, then you can still [configure the Python interpreter in PyCharm](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html).

To start, open your project in PyCharm using _File → Open …_ and select your existing project folder.

Next, open your project settings by navigating to _File → Settings_ on Windows—or _PyCharm → Settings_ on macOS—and from the left sidebar, select _Project: Your Project Name → Python Interpreter_ :

[![Project settings of a PyCharm project with the Python Interpreter setting selected in the side bar](https://files.realpython.com/media/venv-pycharm-project-settings.07093605d0f2.png)](https://files.realpython.com/media/venv-pycharm-project-settings.07093605d0f2.png)

Click on _Add Interpreter → Add Local Interpreter_ to open a pop-up window that allows you to create a new virtual environment. You can customize what tool and Python base interpreter you want to use, but in most cases, you can just leave the default settings and click _OK_ :

[![Pop up window in PyCharm giving you the option to create a new Python interpreter](https://files.realpython.com/media/venv-pycharm-add-interpreter.75c29e71f4b7.png)](https://files.realpython.com/media/venv-pycharm-add-interpreter.75c29e71f4b7.png)

PyCharm creates and activates a new virtual environment in your project folder that it calls `.venv` by default. Click _OK_ again to exit your project settings. You can confirm that your project is set up to use your new virtual environment called `.venv` by hovering over the name of the Python interpreter in the bottom right corner:

[![PyCharm main project window showing an activated virtual environment path when hovering over the Python interpreter name in the bottom right corner](https://files.realpython.com/media/venv-pycharm-hover-environment-path.7ac7d94474f4.png)](https://files.realpython.com/media/venv-pycharm-hover-environment-path.7ac7d94474f4.png)

It’ll show the path to your Python interpreter that’s nested within the virtual environment folder. Any scripts that you run through PyCharm will use the configured virtual environment without you needing to manually activate it.

Now you know how to create and activate virtual environments manually, and how to set them up in two popular Python IDEs. If that’s all you need, then happy trails as you continue creating!

However, if you want to learn the nuts and bolts of what exactly happens when you create a virtual environment using `venv`, why so many tutorials ask you to make one in the first place, and what a virtual environment really _is_ , then keep on reading! You’re about to go deep!

[ Remove ads](/account/join/)

## Why Do You Need Virtual Environments?[](#why-do-you-need-virtual-environments "Permanent link")

Nearly everyone in the Python community suggests that you use virtual environments for all your projects. But why? If you want to find out why you need to set up a virtual environment in the first place, then this is the right section for you.

The short answer is that Python isn’t great at dependency management. If you’re not specific, then `pip` will place all the external packages that you install in a folder called `site-packages/` in your base Python installation.

Deep Dive: site-packagesShow/Hide

Technically, Python comes with _two_ site-packages folders:

  1. **`purelib/`** should contain only modules written in pure Python code.
  2. **`platlib/`** should contain binaries that aren’t written in pure Python, for example `.dll`, `.so`, or `.pydist` files.



You can find these folders in different locations if you’re working on Fedora or RedHat Linux distributions.

However, most operating systems implement Python’s site-packages setting so that both locations point to the same path, effectively creating a single site-packages folder. You can check the paths using `sysconfig`:

  * [Windows](#windows-5)
  * [Linux](#linux-5)
  * [macOS](#macos-5)



Python
    
    
    >>> import sysconfig
    >>> sysconfig.get_path("purelib")
    'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages'
    >>> sysconfig.get_path("platlib")
    'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages'
    

Python
    
    
    >>> import sysconfig
    >>> sysconfig.get_path("purelib")
    '/usr/local/lib/python3.12/site-packages'
    >>> sysconfig.get_path("platlib")
    '/usr/local/lib/python3.12/site-packages'
    

Python
    
    
    >>> import sysconfig
    >>> sysconfig.get_path("purelib")
    '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages'
    >>> sysconfig.get_path("platlib")
    '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages'
    

Most likely, both outputs will show you the same path. If both outputs are the same, then your operating system doesn’t put `purelib` modules into a different folder than `platlib` modules. If two different paths show up, then your operating system makes this distinction.

Even if your operating system distinguishes between the two, dependency conflicts will still arise because all `purelib` modules will go into a single location for `purelib` modules, and the same will happen with the `platlib` modules.

To work with virtual environments, you don’t need to worry about the implementation details of a single site-packages folder or two separate ones. In fact, you probably won’t ever need to think about it again. You can, however, keep in mind that when someone mentions Python’s site-packages directory, they _could_ be talking about two different directories.

Several issues can come up if all of your external packages land in the same folder. Next up, you’ll learn more about these issues and other problems that virtual environments mitigate.

### Avoid System Pollution[](#avoid-system-pollution "Permanent link")

Linux and macOS come preinstalled with a version of Python that the operating system uses for internal tasks.

If you install packages to your operating system’s global Python, these packages will mix with the system-relevant packages. This mix-up could have unexpected side effects on tasks crucial to your operating system’s normal behavior.

Additionally, if you update your operating system, then the packages you installed might get overwritten and lost, and you don’t want either of those headaches to happen!

### Sidestep Dependency Conflicts[](#sidestep-dependency-conflicts "Permanent link")

One of your projects might require a different version of an external library compared to another project. If you only have one place to install packages, then you won’t be able to work with two different versions of the same library. This is a common reason why it’s recommended to use a Python virtual environment.

To better understand why this is so important, imagine you’re building [Django websites](https://realpython.com/get-started-with-django-1/) for two different clients:

  * One client is comfortable with their existing web app, which you initially built using [Django 2.2.26](https://pypi.org/project/Django/2.2.26/), and this client refuses to update their project to a modern Django version.
  * Another client wants you to include async functionality in their website, which is only available [starting with Django 3.1](https://docs.djangoproject.com/en/5.1/releases/3.1/#what-s-new-in-django-3-1). You’ll want to use a modern Django version for this client!



If you install Django globally, you can only have one version installed:

  * [Windows](#windows-6)
  * [Linux + macOS](#linux-macos-6)



Windows PowerShell
    
    
    PS> py -m pip install django==2.2.26
    PS> py -m pip list
    Package  Version
    -------- -------
    Django   2.2.26
    pip      24.2
    pytz     2024.1
    sqlparse 0.5.1
    
    PS> py -m pip install django==5.1
    PS> py -m pip list
    Package  Version
    -------- -------
    asgiref  3.8.1
    Django   5.1
    pip      24.2
    pytz     2024.1
    sqlparse 0.5.1
    tzdata   2024.1
    

Shell
    
    
    $ python3 -m pip install django==2.2.26
    $ python3 -m pip list
    Package  Version
    -------- -------
    Django   2.2.26
    pip      24.2
    pytz     2024.1
    sqlparse 0.5.1
    
    $ python3 -m pip install django==5.1
    $ python3 -m pip list
    Package  Version
    -------- -------
    asgiref  3.8.1
    Django   5.1
    pip      24.2
    pytz     2024.1
    sqlparse 0.5.1
    

If you install two different versions of the same package into your global Python environment, the second installation overwrites the first one. For the same reason, having a single virtual environment for both clients won’t work either. You can’t have two different versions of the same package in a single Python environment.

Looks like you won’t be able to work on one of the two projects with this setup! However, if you create a virtual environment for each of your clients’ projects, then you can install a different version of Django into each of them:

  * [Windows](#windows-7)
  * [Linux + macOS](#linux-macos-7)



Windows PowerShell
    
    
    PS> py -m venv client-old\
    PS> client-old\Scripts\activate
    (client-old) PS> python -m pip install django==2.2.26
    (client-old) PS> python -m pip list
    Package  Version
    -------- -------
    Django   2.2.26
    pip      24.2
    pytz     2024.1
    sqlparse 0.5.1
    (client-old) PS> deactivate
    
    PS> py -m venv client-new\
    PS> client-new\Scripts\activate
    (client-new) PS> python -m pip install django==5.1
    (client-new) PS> python -m pip list
    Package  Version
    -------- -------
    asgiref  3.8.1
    Django   5.1
    pip      24.2
    sqlparse 0.5.1
    tzdata   2024.1
    (client-new) PS> deactivate
    

Shell
    
    
    $ python3 -m venv client-old/
    $ source client-old/bin/activate
    (client-old) $ python -m pip install django==2.2.26
    (client-old) $ python -m pip list
    Package  Version
    -------- -------
    Django   2.2.26
    pip      24.2
    pytz     2024.1
    sqlparse 0.5.1
    (client-old) $ deactivate
    
    $ python3 -m venv client-new/
    $ source client-new/bin/activate
    (client-new) $ python -m pip install django==5.1
    (client-new) $ python -m pip list
    Package  Version
    -------- -------
    asgiref  3.8.1
    Django   5.1
    pip      24.2
    sqlparse 0.5.1
    (client-new) $ deactivate
    

If you now activate either of the two virtual environments, then you’ll notice that it still holds its own specific version of Django. The two environments also have different dependencies, and each only contains the dependencies necessary for that version of Django.

With this setup, you can activate one environment when you work on one project and another when you work the other project. Now you can keep any number of clients happy at the same time!

[ Remove ads](/account/join/)

### Minimize Reproducibility Issues[](#minimize-reproducibility-issues "Permanent link")

If all your packages live in one location, then it’ll be difficult to only [pin dependencies](#pin-your-dependencies) that are relevant for a single project.

If you’ve worked with Python for a while, then your global Python environment might already include all sorts of third-party packages. If that’s not the case, then pat yourself on the back! You’ve probably installed a new version of Python recently, or you already know how to handle virtual environments to [avoid system pollution](#avoid-system-pollution).

To clarify what reproducibility issues you can encounter when sharing a Python environment across multiple projects, you’ll look at an example next. Imagine you’ve worked on two independent projects over the past month:

  1. [A web scraping project with Beautiful Soup](https://realpython.com/beautiful-soup-web-scraper-python/)
  2. [A Flask application](https://realpython.com/python-web-applications-with-flask-part-i/)



Unaware of virtual environments, you installed all necessary packages into your global Python environment:

  * [Windows](#windows-8)
  * [Linux + macOS](#linux-macos-8)



Windows PowerShell
    
    
    PS> py -m pip install beautifulsoup4 requests
    PS> py -m pip install flask
    

Shell
    
    
    $ python3 -m pip install beautifulsoup4 requests
    $ python3 -m pip install flask
    

Your Flask app has turned out to be quite helpful, so other developers want to work on it as well. They need to reproduce the environment that you used for working on it. You want to go ahead and [pin your dependencies](#pin-your-dependencies) so that you can share your project online:

  * [Windows](#windows-9)
  * [Linux + macOS](#linux-macos-9)



Windows PowerShell
    
    
    PS> py -m pip freeze
    beautifulsoup4==4.12.3
    blinker==1.8.2
    certifi==2024.8.30
    charset-normalizer==3.3.2
    click==8.1.7
    colorama==0.4.6
    Flask==3.0.3
    idna==3.8
    itsdangerous==2.2.0
    Jinja2==3.1.4
    MarkupSafe==2.1.5
    requests==2.32.3
    soupsieve==2.6
    urllib3==2.2.2
    Werkzeug==3.0.4
    

Shell
    
    
    $ python3 -m pip freeze
    beautifulsoup4==4.12.3
    blinker==1.8.2
    certifi==2024.8.30
    charset-normalizer==3.3.2
    click==8.1.7
    Flask==3.0.3
    idna==3.8
    itsdangerous==2.2.0
    Jinja2==3.1.4
    MarkupSafe==2.1.5
    requests==2.32.3
    soupsieve==2.6
    urllib3==2.2.2
    Werkzeug==3.0.4
    

Which of these packages are relevant to your Flask app, and which ones are here because of your web scraping project? It’s hard to tell when all external dependencies are in a single bucket.

With a single environment like this, you’d have to manually go through the dependencies and know which are necessary for your project and which aren’t. At best, this approach is tedious, but even more so, it’s error-prone.

If you use a separate virtual environment for each of your projects, then it’ll be more straightforward to read the project requirements from your pinned dependencies. That means you can more easily share your success when you develop a great app, making it possible for others to collaborate with you!

### Dodge Installation Privilege Lockouts[](#dodge-installation-privilege-lockouts "Permanent link")

Finally, you may need administrator privileges on a computer to install packages into the host Python’s site-packages directory. In a corporate work environment, you most likely won’t have that level of access to the machine that you’re working on.

If you use virtual environments, then you create a new installation location within the scope of your user privileges, which allows you to install and work with external packages.

Whether you’re coding as a hobby on your own machine, developing websites for clients, or working in a corporate environment, using a virtual environment will save you lots of grief in the long run.

## What Is a Python Virtual Environment?[](#what-is-a-python-virtual-environment "Permanent link")

At this point, you’re convinced that you want to work with virtual environments. Great, but _what_ are you working with when you use a virtual environment? If you want to understand what virtual environments are, then this is the right section for you.

The short answer is that a Python virtual environment is a folder structure that gives you everything you need to run a lightweight yet isolated Python environment.

[ Remove ads](/account/join/)

### A Folder Structure[](#a-folder-structure "Permanent link")

When you create a new virtual environment using the `venv` module, Python creates a self-contained folder structure and copies or [symlinks](https://en.wikipedia.org/wiki/Symbolic_link) the Python [executable files](https://en.wikipedia.org/wiki/Executable) into that folder structure.

You don’t need to dig deeply into this folder structure to learn more about what virtual environments are made of. In just a bit, you’ll carefully scrape off the topsoil and investigate the high-level structures that you uncover.

However, if you already have your shovel ready and you’re itching to dig, then open the collapsible section below:

Virtual environment folder structureShow/Hide

Welcome, brave one. You’ve accepted the challenge to venture deeper into your virtual environment’s folder structure! In this collapsible section, you’ll find instructions on how to take a look into that dark abyss.

On your command line, navigate to the folder that contains your virtual environment. Take a deep breath and brace yourself, then execute the `tree` command to display the contents of the directory:

  * [Windows](#windows-10)
  * [Linux](#linux-10)
  * [macOS](#macos-10)



Windows PowerShell
    
    
    PS> tree venv\ /F
    

Shell
    
    
    $  tree venv/
    

You may need to first [install `tree`](https://gitlab.com/OldManProgrammer/unix-tree), for example with `sudo apt install tree`.

Shell
    
    
    $ tree venv/
    

You may need to first [install `tree`](https://gitlab.com/OldManProgrammer/unix-tree), for example by [using HomeBrew](https://formulae.brew.sh/formula/tree#default).

The `tree` command displays the content of your `venv` directory in a _very_ long tree structure.

**Note:** Alternatively, you could hone your skills by creating a new virtual environment, install the [`rptree` package](https://github.com/realpython/rptree) into it, and use that to display the folder’s tree structure. You could even take a bigger detour and [build that directory tree generator](https://realpython.com/directory-tree-generator-python/) yourself!

However you end up displaying the contents of the `venv/` folder, you might be surprised by what you find. Many developers experience a slight shock when they first take a peek. There are _a lot_ of files in there!

If this was your first time and you felt that way, then welcome to the group of people who have taken a look and been a bit overwhelmed !

A virtual environment folder contains a lot of files and folders, but you might notice that most of what makes this tree structure so long rests inside the `site-packages/` folder. If you trim down the subfolders and files in there, you end up with a tree structure that isn’t too overwhelming:

  * [Windows](#windows-11)
  * [Linux](#linux-11)
  * [macOS](#macos-11)


    
    
    venv\
    │
    ├── Include\
    │
    ├── Lib\
    │   │
    │   └── site-packages\
    │       │
    │       ├── pip\
    │       │
    │       └── pip-24.2.dist-info\
    │
    │
    ├── Scripts\
    │   ├── Activate.ps1
    │   ├── activate
    │   ├── activate.bat
    │   ├── deactivate.bat
    │   ├── pip.exe
    │   ├── pip3.12.exe
    │   ├── pip3.exe
    │   ├── python.exe
    │   └── pythonw.exe
    │
    └── pyvenv.cfg
    
    
    
    venv/
    │
    ├── bin/
    │   ├── Activate.ps1
    │   ├── activate
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── pip
    │   ├── pip3
    │   ├── pip3.12
    │   ├── python
    │   ├── python3
    │   └── python3.12
    │
    ├── include/
    │   │
    │   └── python3.12/
    │
    ├── lib/
    │   │
    │   └── python3.12/
    │       │
    │       └── site-packages/
    │           │
    │           ├── pip/
    │           │
    │           └── pip-24.2.dist-info/
    │
    ├── lib64/
    │   │
    │   └── python3.12/
    │       │
    │       └── site-packages/
    │           │
    │           ├── pip/
    │           │
    │           └── pip-24.2.dist-info/
    │
    └── pyvenv.cfg
    
    
    
    venv/
    │
    ├── bin/
    │   ├── Activate.ps1
    │   ├── activate
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── pip
    │   ├── pip3
    │   ├── pip3.12
    │   ├── python
    │   ├── python3
    │   └── python3.12
    │
    ├── include/
    │
    ├── lib/
    │   │
    │   └── python3.12/
    │       │
    │       └── site-packages/
    │           │
    │           ├── pip/
    │           │
    │           └── pip-24.2.dist-info/
    │
    └── pyvenv.cfg
    

This reduced tree structure gives you a better overview of what’s going on in your virtual environment folder:

  * [Windows](#windows-12)
  * [Linux](#linux-12)
  * [macOS](#macos-12)



  * **`Include\`** is an initially empty folder that Python uses to [include C header files](https://docs.python.org/3/c-api/intro.html#include-files) for packages you might install that depend on C extensions.

  * **`Lib\`** contains the `site-packages\` folder, which is one of the main reasons for creating your virtual environment. This folder is where you’ll install external packages that you want to use within your virtual environment. [Starting with Python 3.12](https://github.com/python/cpython/issues/95299), your virtual environment comes preinstalled with only one dependency, `pip`. You’ll learn more about this in a bit.

  * **`Scripts\`** contains the executable files of your virtual environment. Most notable are the Python interpreter (`python.exe`), the `pip` executable (`pip.exe`), and the activation script for your virtual environment, which comes in a couple of different flavors to allow you to work with different shells. In this tutorial, you’ve used `activate`, which handles the activation of your virtual environment for Windows across most shells.




  * **`bin/`** contains the executable files of your virtual environment. Most notable are the Python interpreter (`python`) and the `pip` executable (`pip`), as well as their respective symlinks (`python3`, `python3.12`, `pip3`, `pip3.12`). The folder also contains activation scripts for your virtual environment. Your specific activation script depends on what shell you use. For example, in this tutorial, you ran `activate`, which works for the Bash and Zsh shells.

  * **`include/`** is an initially empty folder that Python uses to [include C header files](https://docs.python.org/3/c-api/intro.html#include-files) for packages you might install that depend on C extensions.

  * **`lib/`** contains the `site-packages/` directory nested in a folder that designates the Python version (`python3.12/`). `site-packages/` is one of the main reasons for creating your virtual environment. This folder is where you’ll install the external packages that you want to use within your virtual environment. [Starting with Python 3.12](https://github.com/python/cpython/issues/95299), your virtual environment comes preinstalled with only one dependency, `pip`. You’ll learn more about it in a bit.

  * **`lib64/`** in many Linux systems comes as a symlink to `lib/` [for compatibility reasons](https://stackoverflow.com/a/11370995/5717580). Some Linux systems may use the distinction between `lib/` and `lib64/` to install different versions of libraries depending on their architecture.




  * **`bin/`** contains the executable files of your virtual environment. Most notable are the Python interpreter (`python`) and the `pip` executable (`pip`), as well as their respective symlinks (`python3`, `python3.12`, `pip3`, `pip3.12`). The folder also contains activation scripts for your virtual environment. Your specific activation script depends on what shell you use. For example, in this tutorial, you ran `activate`, which works for the Bash and Zsh shells.

  * **`include/`** is an initially empty folder that Python uses to [include C header files](https://docs.python.org/3/c-api/intro.html#include-files) for packages you might install that depend on C extensions.

  * **`lib/`** contains the `site-packages/` directory nested in a folder that designates the Python version (`python3.12/`). `site-packages/` is one of the main reasons for creating your virtual environment. This folder is where you’ll install external packages that you want to use within your virtual environment. [Starting with Python 3.12](https://github.com/python/cpython/issues/95299), your virtual environment comes preinstalled with only one dependency, `pip`. You’ll learn more about it in a bit.




  * **A`{name}-{version}.dist-info/` directory**, which you get by default for `pip`, contains [package distribution](https://realpython.com/pypi-publish-python-package/) information that exists to [record information about installed packages](https://packaging.python.org/en/latest/specifications/recording-installed-packages/#the-dist-info-directory).

  * **`pyvenv.cfg`** is a crucial file for your virtual environment. It contains only a couple of key-value pairs that Python uses to set variables in the `sys` module that determine which Python interpreter and site-packages directory the current Python session will use. You’ll learn more about the settings in this file when you read about how a virtual environment works.




From this bird’s-eye view of the contents of your virtual environment folder, you can zoom out even further to discover that there are three essential parts to a virtual environment:

  1. A copy or a symlink of the **Python binary**
  2. A **`pyvenv.cfg` file**
  3. A **site-packages directory**



The installed package inside `site-packages/` is optional but comes as a reasonable default. However, your virtual environment would still be a valid virtual environment if this directory were empty, and there are ways to create it [without installing any dependencies](#avoid-installing-pip).

With the default settings, `venv` will install only `pip`, which is the recommended tool to install packages in Python. Because installing other packages is the most common use case for virtual environments, you’ll want to have access to `pip`.

You can double-check that Python installed `pip` into your virtual environment by using `pip list`:

  * [Windows](#windows-13)
  * [Linux + macOS](#linux-macos-13)



Windows PowerShell
    
    
    (venv) PS> python -m pip list
    Package    Version
    ---------- -------
    pip        24.2
    

Shell
    
    
    (venv) $ python -m pip list
    Package    Version
    ---------- -------
    pip        24.2
    

Your version numbers may differ, but this output confirms that Python installed `pip` when you created the virtual environment with its default settings.

**Note:** Below that output, `pip` might also display a warning that you’re not using the latest version of the module. Don’t worry about this yet. Later, you’ll learn more about why this happens and how to [automatically update `pip`](#update-the-core-dependencies) when you create your virtual environment.

The files that make up `pip` constitute most of the content of your new virtual environment. If you avoid looking at the package contents, then the structure is already a lot less daunting.

If you’re working with a Python version that’s older than 3.12, then you’ll noticed that there are a couple of additional folders in the `site-packages/` directory. Expand the collapsible section below to learn more about them:

Packages installed by default before Python 3.12Show/Hide

  * **The`setuptools` module** has been a fundamental tool in the Python packaging ecosystem for many years. `setuptools` extended the `distutils` module with features like package discovery and distribution, and dependency management. Including `setuptools` by default ensured that users had immediate access to these features without having to install additional tools. Before the adoption of [PEP 517](https://peps.python.org/pep-0517/) and [PEP 518](https://peps.python.org/pep-0518/), many packages relied on `setuptools` for installation.

  * **The`_distutils_hack/` module**, [in a manner true to its name](https://github.com/pypa/setuptools/blob/main/_distutils_hack/), ensures that when performing package installations, Python picks the local `._distutils` submodule of `setuptools` over the standard library’s `distutils` module.

  * **The`pkg_resources/` module** helps applications discover plugins automatically and allows Python packages to access their resource files. It’s [distributed together with `setuptools`](https://setuptools.pypa.io/en/latest/pkg_resources.html).




Finally, there’s also a file named **`distutils-precedence.pth`**. This file helps set the path precedence for `distutils` imports and works together with `_distutils_hack` to ensure that Python prefers the version of `distutils` that comes bundled with `setuptools` over the built-in one.

You’re learning about these additional files and folders for the sake of completeness. If you’re on Python 3.12 or later, then they won’t come preinstalled in your virtual environment. Even if you’re working with an older version of Python, you won’t need to remember them to effectively work with your virtual environments.

It’s enough to keep in mind that any preinstalled packages in your `site-packages/` directory are standard tools that make installing _other_ packages more user-friendly.

At this point, you’ve seen all the files and folders that make up a virtual environment if you’ve installed it using the built-in `venv` module.

Remember that your virtual environment is just a folder structure, which means that you can delete and re-create it anytime you want. But why _this specific_ folder structure, and what does this structure make possible?

[ Remove ads](/account/join/)

### An Isolated Python Installation[](#an-isolated-python-installation "Permanent link")

Python virtual environments aim to provide a lightweight, isolated Python environment that you can quickly create and then discard when you don’t need it anymore. The folder structure that you just explored makes that possible by providing three key pieces:

  1. A copy or a symlink of the **Python binary**
  2. A **`pyvenv.cfg` file**
  3. A **site-packages directory**



You want to achieve an isolated environment so that any external packages you install won’t conflict with global site-packages. To make this possible, `venv` reproduces the folder structure that a standard Python installation creates.

This structure accounts for the location of the copy or symlink of the Python binary and the site-packages directory, where Python installs external packages.

**Note:** Whether or not the Python executable in your virtual environment is a copy or a symlink of the Python executable that you’ve based the environment on depends primarily on your operating system.

Windows and Linux may create symlinks instead of copies, while macOS always creates a copy. You can try to [influence the default behavior](#copy-or-link-your-executables) with optional arguments when you create the virtual environment. However, this is something you won’t have to worry about in most cases.

In addition to the Python binary and site-packages directory, you also get the `pyvenv.cfg` file. It’s a small file that contains only a couple of key-value pairs. However, these settings are crucial for making your virtual environment work:

  * [Windows](#windows-14)
  * [Linux](#linux-14)
  * [macOS](#macos-14)



Configuration File `pyvenv.cfg`
    
    
    home = C:\Users\Name\AppData\Local\Programs\Python\Python312
    include-system-site-packages = false
    version = 3.12.5
    executable = C:\Users\Name\AppData\Local\Programs\Python\Python312\python312.exe
    command = C:\Users\Name\AppData\Local\Programs\Python\Python312\python312.exe -m venv C:\Users\Name\path\to\project\venv
    

Configuration File `pyvenv.cfg`
    
    
    home = /usr/local/bin
    include-system-site-packages = false
    version = 3.12.5
    executable = /usr/local/bin/python3.12
    command = /usr/local/bin/python3.12 -m venv /home/name/path/to/project/venv
    

Configuration File `pyvenv.cfg`
    
    
    home = /Library/Frameworks/Python.framework/Versions/3.12/bin
    include-system-site-packages = false
    version = 3.12.5
    executable = /Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12
    command = /Library/Frameworks/Python.framework/Versions/3.12/bin/python -m venv /Users/name/path/to/project/venv
    

You’ll learn more about this file later when reading about [how a virtual environment works](#how-does-a-virtual-environment-work).

Suppose you closely inspect your newly minted virtual environment’s [folder structure](#a-folder-structure). You might notice that this lightweight installation doesn’t contain any of the trusted [standard library](https://docs.python.org/3/library/) modules. Some might say that Python without its standard library is like a toy car without batteries!

However, if you start the Python interpreter from within your virtual environment, then you can still access all the goodies from the standard library:

Python
    
    
    >>> import urllib
    >>> from pprint import pp
    >>> pp(dir(urllib))
    ['__builtins__',
     '__cached__',
     '__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__path__',
     '__spec__']
    

In this example code snippet, you’ve successfully [imported](https://realpython.com/python-import/) both the [`urllib` module](https://realpython.com/urllib-request/) and the `pp()` shortcut from the [pretty print module](https://realpython.com/python-pretty-print/). Then you used `dir()` to inspect the `urllib` module.

Both modules are part of the standard library, so how come you have access to them even though they’re not in the folder structure of your Python virtual environment?

You can access Python’s standard-library modules because your virtual environment reuses Python’s built-ins and standard-library modules from the Python installation you used to create your virtual environment. In a later section, you’ll learn _how_ the virtual environment achieves [linking to your base Python’s standard library](#it-links-back-to-your-standard-library).

**Note:** Because you always need an existing Python installation to create your virtual environment, `venv` opts to reuse the existing standard-library modules to avoid the overhead of copying them into your new virtual environment. This intentional behavior speeds up the creation of virtual environments and makes them more lightweight, as described in the [motivation for PEP 405](https://www.python.org/dev/peps/pep-0405/#motivation).

In addition to the standard-library modules, you can optionally [give your virtual environment access to the base installation’s site-packages](#include-the-system-site-packages) through an argument when you create the environment:

  * [Windows](#windows-15)
  * [Linux + macOS](#linux-macos-15)



Windows PowerShell
    
    
    PS> py -m venv venv\ --system-site-packages
    

Shell
    
    
    $ python3 -m venv venv/ --system-site-packages
    

If you add `--system-site-packages` when you call `venv`, Python will set the value to `include-system-site-packages` in `pyvenv.cfg` to `true`. This setting means that you can use any external packages that you installed to your base Python as if you’d installed them into your virtual environment.

This connection works in only one direction. Even if you give your virtual environment access to the source Python’s site-packages folder, any new packages you install into your virtual environment won’t mingle with the packages there. Python will respect the isolated nature of installations to your virtual environment and place them into the separate site-packages directory within the virtual environment.

You now understand that a virtual environment is basically a folder structure with a settings file. It may or may not come with `pip` preinstalled, and it has access to the source Python’s standard-library modules while remaining isolated. However, you might still be wondering how all of this works, and you’ll delve into that next.

[ Remove ads](/account/join/)

## How Does a Virtual Environment Work?[](#how-does-a-virtual-environment-work "Permanent link")

If you know what a virtual environment is but wonder how it manages to create the lightweight isolation that it provides, then you’re in the right section. Here you’ll [peek under the hood](https://realpython.com/podcasts/rpp/156/) and learn how the folder structure and the settings in your `pyvenv.cfg` file interact with Python to provide a reproducible and isolated space for installing external dependencies.

If you like the [Real Python Podcast](https://realpython.com/real-python-podcast-launch/), then you can listen to the episodes [Launching Python, Virtual Environments, and Locking Dependencies](https://realpython.com/podcasts/rpp/93/) and [Virtual Environment Structure & Surveying the Packaging Ecosystem](https://realpython.com/podcasts/rpp/156/), both with Brett Cannon, for an audio-guided tour on [how virtual environments work](https://snarky.ca/how-virtual-environments-work/).

### It Copies Structure and Files[](#it-copies-structure-and-files "Permanent link")

When you create a virtual environment using `venv`, the module re-creates the file and [folder structure](#a-folder-structure) of a standard Python installation on your operating system. Python also copies or symlinks into that folder structure the Python executable with which you’ve called `venv`:

  * [Windows](#windows-16)
  * [Linux](#linux-16)
  * [macOS](#macos-16)


    
    
    venv\
    │
    ├── Include\
    │
    ├── Lib\
    │   │
    │   └── site-packages\
    │
    ├── Scripts\
    │   ├── Activate.ps1
    │   ├── activate
    │   ├── activate.bat
    │   ├── deactivate.bat
    │   ├── pip.exe
    │   ├── pip3.12.exe
    │   ├── pip3.exe
    │   ├── python.exe
    │   └── pythonw.exe
    │
    └── pyvenv.cfg
    
    
    
    venv/
    │
    ├── bin/
    │   ├── Activate.ps1
    │   ├── activate
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── pip
    │   ├── pip3
    │   ├── pip3.12
    │   ├── python
    │   ├── python3
    │   └── python3.12
    │
    ├── include/
    │
    ├── lib/
    │   │
    │   └── python3.12/
    │       │
    │       └── site-packages/
    │
    ├── lib64/
    │   │
    │   └── python3.12/
    │       │
    │       └── site-packages/
    │
    └── pyvenv.cfg
    
    
    
    venv/
    │
    ├── bin/
    │   ├── Activate.ps1
    │   ├── activate
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── pip
    │   ├── pip3
    │   ├── pip3.12
    │   ├── python
    │   ├── python3
    │   └── python3.12
    │
    ├── include/
    │
    ├── lib/
    │   │
    │   └── python3.12/
    │       │
    │       └── site-packages/
    │
    └── pyvenv.cfg
    

If you locate your system-wide Python installation on your operating system and inspect the folder structure there, then you’ll see that your virtual environment resembles that structure.

You can find the base Python installation that your virtual environment is based on by navigating to the path you can find under the `home` key in `pyvenv.cfg`.

**Note:** On Windows, you may notice that `python.exe` in your base Python installation isn’t in `Scripts\` but is one folder level up. In your virtual environment, the executable is intentionally located in the `Scripts\` folder.

This small change to the folder structure means that you only need to add a single directory to your shell [`PATH`](https://realpython.com/add-python-to-path/) variable to activate the virtual environment.

While you might find some additional files and folders in your base Python installation, you’ll notice that the standard folder structure is the same as in your virtual environment. `venv` creates this folder structure to ensure that Python will work as expected in isolation, without needing to apply additional changes.

### It Adapts the Prefix-Finding Process[](#it-adapts-the-prefix-finding-process "Permanent link")

With the standard folder structure in place, the Python interpreter in your virtual environment can understand where all relevant files are located. It does this with only minor adaptations to its prefix-finding process according to the [`venv` specification](https://www.python.org/dev/peps/pep-0405/#specification).

Instead of looking for the `os` module to determine the location of the standard library, the Python interpreter first looks for a `pyvenv.cfg` file. If the interpreter finds this file and it contains a `home` key, then the interpreter will use that key to set the value for two variables:

  1. [`sys.base_prefix`](https://docs.python.org/3/library/sys.html#sys.base_prefix) will hold the path to the Python executable used to create this virtual environment, which you can find at the path defined under the `home` key in `pyvenv.cfg`.
  2. [`sys.prefix`](https://docs.python.org/3/library/sys.html#sys.prefix) will point to the directory containing `pyvenv.cfg`.



If the interpreter doesn’t find a `pyvenv.cfg` file, then it determines that it’s not running within a virtual environment, and both `sys.base_prefix` and `sys.prefix` will then point to the same path.

Exercise: Explore Prefix PathsShow/Hide

You can confirm that this works as described. Spin up a Python interpreter within an active virtual environment and inspect both variables:

  * [Windows](#windows-17)
  * [Linux](#linux-17)
  * [macOS](#macos-17)



Python
    
    
    >>> import sys
    >>> sys.base_prefix
    'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312'
    >>> sys.prefix
    'C:\\Users\\Name\\path\\to\\venv'
    

Python
    
    
    >>> import sys
    >>> sys.base_prefix
    '/usr/local'
    >>> sys.prefix
    '/home/name/path/to/venv'
    

Python
    
    
    >>> import sys
    >>> sys.base_prefix
    '/Library/Frameworks/Python.framework/Versions/3.12'
    >>> sys.prefix
    '/Users/name/path/to/venv'
    

You can see that the variables point to different locations on your system.

Now go ahead and deactivate the virtual environment, enter a new interpreter session, and rerun the same code:

  * [Windows](#windows-18)
  * [Linux](#linux-18)
  * [macOS](#macos-18)



Python
    
    
    >>> import sys
    >>> sys.base_prefix
    'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312'
    >>> sys.prefix
    'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312'
    

Python
    
    
    >>> import sys
    >>> sys.base_prefix
    '/usr/local'
    >>> sys.prefix
    '/usr/local'
    

Python
    
    
    >>> import sys
    >>> sys.base_prefix
    '/Library/Frameworks/Python.framework/Versions/3.12'
    >>> sys.prefix
    '/Library/Frameworks/Python.framework/Versions/3.12'
    

You should see that both `sys.base_prefix` and `sys.prefix` now point to the same path.

If these two variables have different values, then Python adapts where it’ll look for modules:

> The `site` and `sysconfig` standard-library modules are modified such that the standard library and header files are found relative to `sys.base_prefix` […], while site-package directories […] are still found relative to `sys.prefix` […]. ([Source](https://www.python.org/dev/peps/pep-0405/#specification))

This change effectively allows the Python interpreter in your virtual environment to use the standard-library modules from your base Python installation while pointing to its internal site-packages directory to install and access external packages.

[ Remove ads](/account/join/)

### It Links Back to Your Standard Library[](#it-links-back-to-your-standard-library "Permanent link")

Python virtual environments aim to be a lightweight way to provide you with an isolated Python environment that you can quickly create and then delete when you don’t need it anymore. To make this possible, `venv` copies only the minimally necessary files:

> [A] Python virtual environment in its simplest form would consist of nothing more than a copy or symlink of the Python binary accompanied by a `pyvenv.cfg` file and a site-packages directory. ([Source](https://www.python.org/dev/peps/pep-0405/#specification))

The Python executable in your virtual environment has access to the standard-library modules of the Python installation on which you based the environment. Python makes this possible by pointing to the file path of the base Python executable in the `home` setting in `pyvenv.cfg`:

  * [Windows](#windows-19)
  * [Linux](#linux-19)
  * [macOS](#macos-19)



Configuration File `pyvenv.cfg`
    
    
    home = C:\Users\Name\AppData\Local\Programs\Python\Python312
    include-system-site-packages = false
    ...
    

Configuration File `pyvenv.cfg`
    
    
    home = /usr/local/bin
    include-system-site-packages = false
    ...
    

Configuration File `pyvenv.cfg`
    
    
    home = /Library/Frameworks/Python.framework/Versions/3.12/bin
    include-system-site-packages = false
    ...
    

If you navigate to the path value of the highlighted line in `pyvenv.cfg` and list the contents of the folder, then you’ll find the base Python executable that you used to create your virtual environment. From there, you can navigate to find the folder that contains your standard-library modules:

  * [Windows](#windows-20)
  * [Linux](#linux-20)
  * [macOS](#macos-20)



Windows PowerShell
    
    
    PS> ls C:\Users\Name\AppData\Local\Programs\Python\Python312
    
     Directory: C:\Users\Name\AppData\Local\Programs\Python\Python312
    
    Mode              LastWriteTime      Length Name
    ----              -------------      ------ ----
    d-----     09/01/2024   5:09 PM             DLLs
    d-----     09/01/2024   5:09 PM             Doc
    d-----     09/01/2024   5:09 PM             include
    d-----     09/01/2024   5:09 PM             Lib
    d-----     09/01/2024   5:09 PM             libs
    d-----     09/01/2024   2:04 PM             Scripts
    d-----     09/01/2024   5:09 PM             tcl
    -a----     09/01/2024   4:28 AM       32762 LICENSE.txt
    -a----     09/01/2024   4:29 AM     1225432 NEWS.txt
    -a----     09/01/2024   4:28 AM       98544 python.exe
    -a----     09/01/2024   4:28 AM       61680 python3.dll
    -a----     09/01/2024   4:28 AM     4471024 python312.dll
    -a----     09/01/2024   4:28 AM       97008 pythonw.exe
    -a----     09/01/2024   4:29 AM       97168 vcruntime140.dll
    -a----     09/01/2024   4:29 AM       37240 vcruntime140_1.dll
    
    PS> ls C:\Users\Name\AppData\Local\Programs\Python\Python312\Lib
    
     Directory: C:\Users\Name\AppData\Local\Programs\Python\Python312\Lib
    
    Mode              LastWriteTime      Length Name
    ----              -------------      ------ ----
    d-----     09/01/2024   5:09 PM             asyncio
    d-----     09/01/2024   5:09 PM             collections
    
    ...
    
    -a----     09/01/2024   4:27 AM        5302 __future__.py
    -a----     09/01/2024   4:27 AM          65 __hello__.py
    

Shell
    
    
    $ ls /usr/local/bin
    
    2to3-3.12         pip3.12           python3.12
    idle3.12          pydoc3.12         python3.12-config
    
    $ ls /usr/local/lib/python3.12
    
    LICENSE.txt        fractions.py       runpy.py
    __future__.py      ftplib.py          sched.py
    __hello__.py       functools.py       secrets.py
    
    ...
    
    enum.py            random.py          zipimport.py
    filecmp.py         re                 zoneinfo
    fileinput.py       reprlib.py
    fnmatch.py         rlcompleter.py
    

Shell
    
    
    $ ls /Library/Frameworks/Python.framework/Versions/3.12/bin
    
    2to3               pip3.12            python3-intel64
    2to3-3.12          pydoc3             python3.12
    idle3              pydoc3.12          python3.12-config
    idle3.12           python3            python3.12-intel64
    pip3               python3-config
    
    $ ls /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12
    
    LICENSE.txt        fractions.py       runpy.py
    __future__.py      ftplib.py          sched.py
    __hello__.py       functools.py       secrets.py
    
    ...
    
    enum.py            random.py          zipimport.py
    filecmp.py         re                 zoneinfo
    fileinput.py       reprlib.py
    fnmatch.py         rlcompleter.py
    

Python is set up to find these modules by adding the relevant path to `sys.path`. During initialization, Python automatically imports [the `site` module](https://docs.python.org/3.12/library/site.html), which sets the defaults for this argument.

The paths that your Python session has access to in `sys.path` determine which locations Python can import modules from.

If you activate your virtual environment and enter a Python interpreter, then you can confirm that the path to the standard library folder of your base Python installation is available:

  * [Windows](#windows-21)
  * [Linux](#linux-21)
  * [macOS](#macos-21)



Python
    
    
    >>> import sys
    >>> sys.path
    ['',
     'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312\\python312.zip',
     'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312\\DLLs',
     'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312\\lib',
     'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312',
     'C:\\Users\\Name\\path\\to\\venv',
     'C:\\Users\\Name\\path\\to\\venv\\lib\\site-packages']
    

Python
    
    
    >>> import sys
    >>> sys.path
    ['',
     '/usr/local/lib/python312.zip',
     '/usr/local/lib/python3.12',
     '/usr/local/lib/python3.12/lib-dynload',
     '/home/name/path/to/venv/lib/python3.12/site-packages']
    

Python
    
    
    >>> import sys
    >>> sys.path
    ['',
     '/Library/Frameworks/Python.framework/Versions/3.12/lib/python312.zip',
     '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12',
     '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/lib-dynload',
     '/Users/name/path/to/venv/lib/python3.12/site-packages']
    

Because the path to the directory containing your standard-library modules is available in `sys.path`, you’ll be able to import any of them when you work with Python from within your virtual environment.

### It Modifies Your `PYTHONPATH`[](#it-modifies-your-pythonpath "Permanent link")

To ensure that the scripts you want to run use the Python interpreter within your virtual environment, `venv` modifies the [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH) environment variable that you can access using [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path).

If you inspect that variable _without_ an active virtual environment, you’ll see the default path locations for your default Python installation:

  * [Windows](#windows-22)
  * [Linux](#linux-22)
  * [macOS](#macos-22)



Python
    
    
    >>> import sys
    >>> sys.path
    ['',
     'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312\\python312.zip',
     'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312\\DLLs',
     'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312\\lib',
     'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312',
     'C:\\Users\\Name\\AppData\\Roaming\\Python\\Python312\\site-packages',
     'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312\\lib\\site-packages']
    

Python
    
    
    >>> import sys
    >>> sys.path
    ['',
     '/usr/local/lib/python312.zip',
     '/usr/local/lib/python3.12',
     '/usr/local/lib/python3.12/lib-dynload',
     '/usr/local/lib/python3.12/site-packages']
    

Python
    
    
    >>> import sys
    >>> sys.path
    ['',
     '/Library/Frameworks/Python.framework/Versions/3.12/lib/python312.zip',
     '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12',
     '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/lib-dynload',
     '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages']
    

Note the highlighted line, which represents the path to the site-packages directory. This folder contains external modules that you’d install, for example, using `pip`. Without an activated virtual environment, this directory is nested within the same folder structure as the Python executable.

**Note:** The `Roaming` folder on Windows contains an additional site-packages directory relevant for installations that use the `--user` flag with `pip`. This folder provides a small degree of virtualization, but it still collects all `--user` installed packages in one spot.

However, if you activate your virtual environment before starting another interpreter session and rerun the same commands, then you’ll get different output:

  * [Windows](#windows-23)
  * [Linux](#linux-23)
  * [macOS](#macos-23)



Python
    
    
    >>> import sys
    >>> sys.path
    ['',
     'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312\\python312.zip',
     'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312\\DLLs',
     'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312\\lib',
     'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312',
     'C:\\Users\\Name\\path\\to\\venv',
     'C:\\Users\\Name\\path\\to\\venv\\lib\\site-packages']
    

Python
    
    
    >>> import sys
    >>> sys.path
    ['',
     '/usr/local/lib/python312.zip',
     '/usr/local/lib/python3.12',
     '/usr/local/lib/python3.12/lib-dynload',
     '/home/name/path/to/venv/lib/python3.12/site-packages']
    

Python
    
    
    >>> import sys
    >>> sys.path
    ['',
     '/Library/Frameworks/Python.framework/Versions/3.12/lib/python312.zip',
     '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12',
     '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/lib-dynload',
     '/Users/name/path/to/venv/lib/python3.12/site-packages']
    

Python replaced the default site-packages directory path with the one that lives inside your virtual environment. This change means that Python will load any external packages installed in your virtual environment. Conversely, because the path to your base Python’s site-packages directory isn’t in this list anymore, Python won’t load modules from there.

**Note:** On Windows systems, Python additionally adds the root folder path of your virtual environment to `sys.path`.

This change in Python’s path settings effectively creates the isolation of external packages in your virtual environment.

Optionally, you can get read-only [access to the system site-packages](#include-the-system-site-packages) directory of your base Python installation by passing an argument when creating the virtual environment.

[ Remove ads](/account/join/)

### It Changes Your Shell `PATH` Variable on Activation[](#it-changes-your-shell-path-variable-on-activation "Permanent link")

Even though you don’t have to, you’ll usually activate your virtual environment before working in it for convenience sake.

To activate your virtual environment, you need to execute an activation script:

  * [Windows](#windows-24)
  * [Linux + macOS](#linux-macos-24)



Windows PowerShell
    
    
    PS> venv\Scripts\activate
    (venv) PS>
    

Shell
    
    
    $ source venv/bin/activate
    (venv) $
    

Which activation script you’ll run depends on your operating system and the shell that you’re using.

If you dig into your virtual environment’s folder structure, then you’ll find a few different activation scripts that it ships with:

  * [Windows](#windows-25)
  * [Linux](#linux-25)
  * [macOS](#macos-25)


    
    
    venv\
    │
    ├── Include\
    │
    ├── Lib\
    │
    ├── Scripts\
    │   ├── Activate.ps1
    │   ├── activate
    │   ├── activate.bat
    │   ├── deactivate.bat
    │   ├── pip.exe
    │   ├── pip3.12.exe
    │   ├── pip3.exe
    │   ├── python.exe
    │   └── pythonw.exe
    │
    └── pyvenv.cfg
    
    
    
    venv/
    │
    ├── bin/
    │   ├── Activate.ps1
    │   ├── activate
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── pip
    │   ├── pip3
    │   ├── pip3.12
    │   ├── python
    │   ├── python3
    │   └── python3.12
    │
    ├── include/
    │
    ├── lib/
    │
    ├── lib64/
    │
    └── pyvenv.cfg
    
    
    
    venv/
    │
    ├── bin/
    │   ├── Activate.ps1
    │   ├── activate
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── pip
    │   ├── pip3
    │   ├── pip3.12
    │   ├── python
    │   ├── python3
    │   └── python3.12
    │
    ├── include/
    │
    ├── lib/
    │
    └── pyvenv.cfg
    

These activation scripts all have the same purpose. However, they need to provide different ways of achieving it to accomodate the various operating systems and shells that users work with.

**Note:** You can open any of the highlighted files in [your favorite code editor](https://realpython.com/python-ides-code-editors-guide/) to inspect the content of a virtual environment activation script. Feel free to dig into that file to get a deeper understanding of what it does, or keep reading to quickly get the gist of it.

Two critical actions happen in the activation script:

  1. **Path:** Sets the `VIRTUAL_ENV` variable to the root folder path of your virtual environment and prepends the relative location of its Python executable to your `PATH`.
  2. **Command prompt:** Changes the command prompt to the name that you passed when you created the virtual environment. It takes that name and puts it into parentheses—for example, `(venv)`.



These two changes put the convenience of virtual environments into effect within your shell:

  1. **Path:** Because the path to all the executables in your virtual environment now lives at the front of your `PATH`, your shell will invoke the internal versions of `pip` or Python when you type `pip` or `python`.
  2. **Command prompt:** Because the script changed your command prompt, you’ll quickly know whether or not your virtual environment is activated.



Both of these changes are minor adaptations that exist purely for your convenience. They aren’t strictly necessary, but they make working with virtual environments more enjoyable.

You can inspect your `PATH` variable before and after activation of your virtual environment. If you’ve activated your virtual environment, then you’ll see the path to the folder containing your internal executables at the beginning of `PATH`:

  * [Windows](#windows-26)
  * [Linux](#linux-26)
  * [macOS](#macos-26)



Windows PowerShell
    
    
    (venv) PS> $Env:Path
    C:\Users\Name\path\to\venv\Scripts;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Users\Name\AppData\Local\Programs\Python\Python312\Scripts\;C:\Users\Name\AppData\Local\Programs\Python\Python312\;c:\users\name\.local\bin;c:\users\name\appdata\roaming\python\python312\scripts
    

Shell
    
    
    (venv) $ echo $PATH
    /home/name/path/to/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/name/.local/bin
    

Shell
    
    
    (venv) $ echo $PATH
    /Users/name/path/to/venv/bin:/Library/Frameworks/Python.framework/Versions/3.12/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/name/.local/bin
    

Keep in mind that the output of printing your `PATH` variable will likely look quite different. The important point is that the activation script has added the path to your virtual environment at the beginning of the `PATH` variable.

When you deactivate your virtual environment using `deactivate`, your shell reverses these changes and returns `PATH` and your command prompt back to how they were before.

**Note:** On Windows, the `deactivate` command executes a separate file called `deactivate.bat`. On UNIX systems, the same script you use for activating a virtual environment also provides the code logic for deactivating the virtual environment.

Give it a try and inspect the changes. This small change to your `PATH` variable allows you to run executables in your virtual environment without needing to provide the full path.

### It Runs From Anywhere With Absolute Paths[](#it-runs-from-anywhere-with-absolute-paths "Permanent link")

As you’ve learned, you don’t _need_ to activate your virtual environment to use it. You can work with your virtual environment without activating it, even though activating it is often recommended.

If you only provide the name of an executable to your shell, it’ll look at the location recorded in `PATH` for an executable file sporting that name. It’ll then pick and run the first one that matches that criterion.

The activation script [changes your `PATH` variable](#it-changes-your-shell-path-variable-on-activation) so that the binaries folder of your virtual environment is the first place your shell looks for executables. This change allows you to type only `pip` or `python` to run the respective programs situated inside your virtual environment.

If you _don ’t_ activate your virtual environment, then you can instead pass the **absolute path** of the Python executable inside your virtual environment to run any script from within your virtual environment:

  * [Windows](#windows-27)
  * [Linux](#linux-27)
  * [macOS](#macos-27)



Windows PowerShell
    
    
    PS> C:\Users\Name\path\to\venv\Scripts\python.exe
    

Shell
    
    
    $ /home/name/path/to/venv/bin/python
    

Shell
    
    
    $ /Users/name/path/to/venv/bin/python
    

This command will start the Python interpreter within your virtual environment precisely the same way it would if you first activated the virtual environment and then called it with `python`.

Exercise: Comprehension CheckShow/Hide

How can you confirm that using the absolute path without activating the virtual environment starts the same interpreter as when you activate the virtual environment and run `python`?

Make some notes of possible ways to check, and then try out some of the solutions mentioned in the _Solution_ block below.

Solution: Comprehension CheckShow/Hide

As described in previous sections of this tutorial, you could:

  * [Print `sys.path`](#it-modifies-your-pythonpath) and confirm that the site-packages directory within your virtual environment is listed.
  * Confirm that [`sys.prefix` has changed](#it-adapts-the-prefix-finding-process) and now points to a folder in your virtual environment folder structure.
  * Activate the virtual environment, then inspect the [`PATH` shell variable](#it-changes-your-shell-path-variable-on-activation) to find the path to your virtual environment’s binary executables.



If you’re unsure why any of these approaches could confirm that this works as described, follow the links above to the relevant sections in this tutorial to refresh your memory.

Alternatively, you could confirm which Python executable you’re using by starting the interpreter and running `import sys; sys.executable`. These commands will return the absolute path to your current Python interpreter. Does the path lead into your virtual environment folder structure?

You’ll often activate your virtual environment before working with it and deactivate it after you’re done. However, there’s an everyday use case where using the absolute paths is a valuable approach.

**Note:** Absolute paths can be helpful for running a scheduled script on your remote server or [in a Docker container](https://pythonspeed.com/articles/activate-virtualenv-dockerfile/). Specifically, you’ll want to use absolute paths if the script requires external dependencies that you want to isolate from the rest of your server in a virtual environment.

Embedding the activation of your virtual environment in your script is a fussy exercise that goes wrong more often than it doesn’t. Instead, equipped with the knowledge that you’ve gained in this tutorial, you can use the absolute path to the Python interpreter in your virtual environment when running your script.

You could use this, for example, if you were setting up an [hourly CRON job](https://crontab.guru/#0_*_*_*_*) on your remote Linux server that checks for [site connectivity](https://realpython.com/site-connectivity-checker-python/) asynchronously using the external `aiohttp` package that you installed in a virtual environment:

Shell
    
    
    0 * * * *
        /home/name/Documents/connectivity-checker/venv/bin/python
        -m rpchecker
        -u google.com twitter.com
        -a
    

You don’t need to fiddle with activating your virtual environment to use the right Python interpreter that has access to the dependencies you’ve installed inside the virtual environment. Instead, you can just pass the absolute path to the binary of that interpreter. Python takes care of the rest for you during initialization.

As long as you provide the path to your Python executable, you don’t need to activate your virtual environment to enjoy the benefits of using one.

## How Can You Customize a Virtual Environment?[](#how-can-you-customize-a-virtual-environment "Permanent link")

If you’re confident about what a virtual environment is and you want to customize it for a specific use case, then you’re in the right place. In this section, you’ll learn about the optional arguments that you can pass when creating a virtual environment with `venv`, and how these customizations can help you get precisely the virtual environment you need.

### Change the Command Prompt[](#change-the-command-prompt "Permanent link")

When you create your virtual environment, you can change the folder name that contains it by passing a name other than _venv_. In fact, you’ll often see different names in different projects. Some of the names commonly used are:

  * `venv`
  * `env`
  * `.venv`



In practice, you could name the folder you create for your virtual environment anything you want. 

**Note:** Naming your virtual environment folder _venv_ is just a convention. Sticking to this convention can help you reliably exclude your virtual environment from version control using a [`.gitignore`](https://realpython.com/python-git-github-intro/#gitignore) file.

Whatever name you choose will show up in your command prompt after you activate the virtual environment:

  * [Windows](#windows-28)
  * [Linux + macOS](#linux-macos-28)



Windows PowerShell
    
    
    PS> py -m venv your-fancy-name\
    PS> your-fancy-name\Scripts\activate
    (your-fancy-name) PS>
    

Shell
    
    
    $ python3 -m venv your-fancy-name/
    $ source your-fancy-name/bin/activate
    (your-fancy-name) $
    

If you give your virtual environment folder an alternate name, you’ll need to include that name when you want to run your activation script, as shown in the code example above.

If you want the convenience of seeing a different command prompt, but want to keep the folder name descriptive so that you’ll know it contains a virtual environment, then you can pass your desired command prompt name to `--prompt`:

  * [Windows](#windows-29)
  * [Linux + macOS](#linux-macos-29)



Windows PowerShell
    
    
    PS> py -m venv venv\ --prompt dev-env
    PS> venv\Scripts\activate
    (dev-env) PS>
    

Shell
    
    
    $ python3 -m venv venv/ --prompt dev-env
    $ source venv/bin/activate
    (dev-env) $
    

With the optional `--prompt` argument, you can set the command prompt that’ll show up when your virtual environment is active to a descriptive string without changing the name of your virtual environment’s folder.

**Note:** There’s even a [special case](https://github.com/python/cpython/issues/83082) for when you want to use the name of your current working directory as the command prompt of your virtual environment:

  * [Windows](#windows-30)
  * [Linux + macOS](#linux-macos-30)



Windows PowerShell
    
    
    PS> py -m venv venv\ --prompt .
    PS> venv\Scripts\activate
    (<current-folder-name>) PS>
    

Shell
    
    
    $ python3 -m venv venv/ --prompt .
    $ source venv/bin/activate
    (<current-folder-name>) $
    

When you [specify a dot (`.`)](https://github.com/python/cpython/blob/ff3bc82f7c9882c27aad597aac79355da7257186/Lib/venv/__init__.py#L55-L56) as the value for `--prompt`, then Python will use the output of `os.path.basename(os.getcwd())` as the command prompt for your virtual environment.

In the code snippets above, you can see that you’re still calling the folder `venv`, which means that you’ll be able to access the activate script with the familiar path. At the same time, the command prompt that displays after activation will be whatever you passed to `--prompt`.

### Overwrite Existing Environments[](#overwrite-existing-environments "Permanent link")

At any given time, you might want to delete and re-create one of your virtual environments. If you do this often, then you might be glad to know that you can add the `--clear` argument to delete the contents of an existing environment before Python creates the new one.

Before you try this out, it’s helpful to see that running the command to create a new virtual environment _without_ this argument won’t overwrite an existing virtual environment with the same name:

  * [Windows](#windows-31)
  * [Linux + macOS](#linux-macos-31)



Windows PowerShell
    
    
    PS> py -m venv venv\
    PS> venv\Scripts\pip.exe install requests
    PS> venv\Scripts\pip.exe list
    Package            Version
    ------------------ ---------
    certifi            2024.8.30
    charset-normalizer 3.3.2
    idna               3.8
    pip                24.2
    requests           2.32.3
    urllib3            2.2.2
    
    PS> py -m venv venv\
    PS> venv\Scripts\pip.exe list
    Package            Version
    ------------------ ---------
    certifi            2024.8.30
    charset-normalizer 3.3.2
    idna               3.8
    pip                24.2
    requests           2.32.3
    urllib3            2.2.2
    

Shell
    
    
    $ python3 -m venv venv/
    $ venv/bin/pip install requests
    $ venv/bin/pip list
    Package            Version
    ------------------ ---------
    certifi            2024.8.30
    charset-normalizer 3.3.2
    idna               3.8
    pip                24.2
    requests           2.32.3
    urllib3            2.2.2
    
    $ python3 -m venv venv/
    $ venv/bin/pip list
    Package            Version
    ------------------ ---------
    certifi            2024.8.30
    charset-normalizer 3.3.2
    idna               3.8
    pip                24.2
    requests           2.32.3
    urllib3            2.2.2
    

In this code example, you first created a virtual environment called _venv_ , then used the environment-internal `pip` executable to install `requests` into the site-packages directory of your virtual environment. You then used `pip list` to confirm that it was installed, together with its dependencies.

**Note:** You ran these commands without activating the virtual environment. Instead, you [used the full path](#it-runs-from-anywhere-with-absolute-paths) to the internal `pip` executable to install into your virtual environment. Alternatively, you could’ve [activated the virtual environment](#activate-it).

In the highlighted line, you attempted to create _another_ virtual environment using the same name, _venv_.

You might expect `venv` to notify you that there’s an existing virtual environment on the same path, but it doesn’t. You might also expect `venv` to automatically delete the existing virtual environment with the same name and replace it with a new one, but it doesn’t do that either. Instead, when `venv` finds an existing virtual environment with the same name on the path you provided, it doesn’t do anything—and again, it doesn’t communicate this to you.

If you list the installed packages after running the virtual environment creation command a second time, then you’ll notice that `requests` and its dependencies still show up. This might not be what you want.

Rather than navigate to your virtual environment folder and delete it, you can explicitly _overwrite_ an existing virtual environment using `--clear`:

  * [Windows](#windows-32)
  * [Linux + macOS](#linux-macos-32)



Windows PowerShell
    
    
    PS> py -m venv venv\
    PS> venv\Scripts\pip.exe install requests
    PS> venv\Scripts\pip.exe list
    Package            Version
    ------------------ ---------
    certifi            2024.8.30
    charset-normalizer 3.3.2
    idna               3.8
    pip                24.2
    requests           2.32.3
    urllib3            2.2.2
    
    PS> py -m venv venv\ --clear
    PS> venv\Scripts\pip.exe list
    Package    Version
    ---------- -------
    pip        24.2
    

Shell
    
    
    $ python3 -m venv venv/
    $ venv/bin/pip install requests
    $ venv/bin/pip list
    Package            Version
    ------------------ ---------
    certifi            2024.8.30
    charset-normalizer 3.3.2
    idna               3.8
    pip                24.2
    requests           2.32.3
    urllib3            2.2.2
    
    $ python3 -m venv venv/ --clear
    $ venv/bin/pip list
    Package    Version
    ---------- -------
    pip        24.2
    

Using the same example as before, you added the optional `--clear` argument when you ran the creation command a second time.

You then confirmed that Python automatically discarded the existing virtual environment with the same name and created a new default virtual environment without the previously installed packages.

### Create Multiple Virtual Environments at Once[](#create-multiple-virtual-environments-at-once "Permanent link")

If one virtual environment isn’t enough, then you can create multiple separate virtual environments in one go by passing more than one path to the command:

  * [Windows](#windows-33)
  * [Linux](#linux-33)
  * [macOS](#macos-33)



Windows PowerShell
    
    
    PS> py -m venv venv\ C:\Users\Name\Documents\virtualenvs\venv-copy\
    

Shell
    
    
    $ python3 -m venv venv/ /home/name/virtualenvs/venv-copy/
    

Shell
    
    
    $ python3 -m venv venv/ /Users/name/virtualenvs/venv-copy/
    

When you run this command, you create two separate virtual environments in two different locations. These two folders are independent virtual environment folders. Passing more than one path, therefore, just saves you the effort of typing the creation command more than once. 

In the example shown above, you might notice that the first argument, `venv/`, represents a relative path. Conversely, the second argument uses an absolute path to point to a new folder location. Either option works when you create a virtual environment. You can even mix and match, as you did here.

**Note:** The most common command for creating a virtual environment, `python3 -m venv venv/`, uses a relative path from your current location in your shell and creates a new folder named _venv_ in that directory.

You don’t have to do this. Instead, you could provide an absolute path that points anywhere on your system. If any of your path directories don’t yet exist, `venv` will create them for you.

You’re not limited to creating two virtual environments at once. You can pass as many valid paths as you want, separated by a whitespace character. Python will diligently set up a virtual environment at each location, and even create any missing folders along the way.

### Update the Core Dependencies[](#update-the-core-dependencies "Permanent link")

When you create a virtual environment using `venv` with its default settings and then install an external package using `pip`, you may encounter a message telling you that your installation of `pip` is outdated:

  * [Windows](#windows-34)
  * [Linux + macOS](#linux-macos-34)



Program Output
    
    
    WARNING: You are using pip version 23.2.4; however, version 24.2 is available.
    You should consider upgrading via the
    'C:\Users\Name\path\to\venv\Scripts\python.exe -m pip install --upgrade pip' command.
    

Program Output
    
    
    WARNING: You are using pip version 23.2.4; however, version 24.2 is available.
    You should consider upgrading via the
    '/path/to/venv/python -m pip install --upgrade pip' command.
    

It [can be frustrating](https://bugs.python.org/issue34556) to create something new only to see that it’s already outdated! Why does this happen?

The installation of `pip` that you’ll receive when creating a virtual environment with the default configuration of `venv` may be outdated because `venv` uses [`ensurepip`](https://docs.python.org/3/library/ensurepip.html) to bootstrap `pip` into your virtual environment.

`ensurepip` intentionally [doesn’t connect to the Internet](https://www.python.org/dev/peps/pep-0453/#explicit-bootstrapping-mechanism), but instead uses a `pip` wheel that comes bundled with each new CPython release. Therefore, the bundled `pip` has a different update cycle than the independent `pip` project.

Once you install an external package using `pip`, the program connects to PyPI and also identifies if `pip` itself is outdated. If `pip` is outdated, then you’ll receive the warning shown above.

While using the bootstrapped version of `pip` can be helpful in some cases, you might want to have the latest `pip` to avoid potential security issues or bugs that might still be around in an older version. For an existing virtual environment, you can follow the instructions that `pip` prints to your terminal and use `pip` to upgrade itself.

If you want to save the effort of doing this manually, you can specify that you want `pip` to contact PyPI and update itself right after installation by passing the `--upgrade-deps` argument:

  * [Windows](#windows-35)
  * [Linux + macOS](#linux-macos-35)



Windows PowerShell
    
    
    PS> py -m venv venv\ --upgrade-deps
    PS> venv\Scripts\activate
    (venv) PS> python -m pip install --upgrade pip
    Requirement already satisfied: pip in c:\users\name\path\to\venv\lib\site-packages (24.2)
    

Shell
    
    
    $ python3 -m venv venv/ --upgrade-deps
    $ source venv/bin/activate
    (venv) $ python -m pip install --upgrade pip
    Requirement already satisfied: pip in ./venv/lib/python3.12/site-packages (24.2)
    

Suppose you use the optional `--upgrade-deps` argument when creating your virtual environment. In that case, it’ll automatically poll PyPI for the newest version of `pip` and install it if the local wheel isn’t up-to-date.

Gone is that pesky warning message, and you can rest assured that you’re using the most recent version of `pip`.

### Avoid Installing `pip`[](#avoid-installing-pip "Permanent link")

You might wonder why it takes a while to set up a Python virtual environment when all it does is create a folder structure. The reason for the time delay is mainly the installation of `pip`. `pip` itself is quite large and blows up the size of your virtual environment from a few kilobytes to many megabytes!

In most use cases, you’ll want to have `pip` installed in your virtual environment because you’ll probably use it to install external packages from PyPI. However, if you don’t need `pip` for whatever reason, then you can use `--without-pip` to create a virtual environment without it:

  * [Windows](#windows-36)
  * [Linux](#linux-36)
  * [macOS](#macos-36)



Windows PowerShell
    
    
    PS> py -m venv venv\ --without-pip
    PS> (Get-ChildItem -Recurse .\venv\ | Measure-Object Length -Sum).Sum / 1MB
    0.533046722412109
    

Shell
    
    
    $ python3 -m venv venv/ --without-pip
    $ du -hs venv/
    56K venv
    

Shell
    
    
    $ python3 -m venv venv/ --without-pip
    $ du -hs venv/
    28K venv
    

Your virtual environment still does everything that qualifies it as a virtual environment by providing lightweight isolation with a separate Python executable.

**Note:** Even though you didn’t install `pip`, running `pip install <package-name>` might still _seem_ to work. Don’t do this, though, because running the command won’t give you what you’re looking for. You’d be using a `pip` executable from somewhere else on your system, and your package will land in the site-packages folder of whichever Python installation is associated with that `pip` executable.

To work with a virtual environment that doesn’t have `pip` installed, you can manually install packages into your site-packages directory or place your ZIP files there and then import them using [Python ZIP imports](https://realpython.com/python-zip-import/).

### Include the System Site-Packages[](#include-the-system-site-packages "Permanent link")

In some situations, you might want to keep access to your base Python’s site-packages directory instead of severing that tie. For example, you might have already set up your favorite deep learning framework, such as [PyTorch or TensorFlow](https://realpython.com/pytorch-vs-tensorflow/), including [CUDA](https://en.wikipedia.org/wiki/CUDA) support, in your global Python environment.

Both frameworks are large and can be tricky to set up correctly. You still want to keep your projects in separate environments, but installing these libraries into every environment can take a couple of minutes each. For quick iteration, you want to have access to the existing installation without needing to redo it for every virtual environment that you create.

You can access _all_ modules that you’ve installed into your base Python’s site-packages directory by adding the `--system-site-packages` flag when creating your virtual environment.

**Note:** If you install any additional external packages, then Python will put them into the site-packages directory of your virtual environment. Keep in mind that you only get read access to the system site-packages directory.

Create a new virtual environment while passing this argument. You’ll see that in addition to your local site-packages directory, the path to your base Python’s site-packages directory will stick around in `sys.path`.

To test this, you can create and activate a new virtual environment using the `--system-site-packages` argument:

  * [Windows](#windows-37)
  * [Linux + macOS](#linux-macos-37)



Windows PowerShell
    
    
    PS> py -m venv venv\ --system-site-packages
    PS> venv\Scripts\activate
    (venv) PS>
    

Shell
    
    
    $ python3 -m venv venv/ --system-site-packages
    $ source venv/bin/activate
    (venv) $
    

Once again, you’ve created a new virtual environment named `venv`, but this time you passed the `--system-site-packages` argument. Adding this optional argument resulted in a different setting in your `pyvenv.cfg` file:

  * [Windows](#windows-38)
  * [Linux](#linux-38)
  * [macOS](#macos-38)



Configuration File `pyvenv.cfg`
    
    
    home = C:\Users\Name\AppData\Local\Programs\Python\Python312
    include-system-site-packages = true
    ...
    

Configuration File `pyvenv.cfg`
    
    
    home = /usr/local/bin
    include-system-site-packages = true
    ...
    

Configuration File `pyvenv.cfg`
    
    
    home = /Library/Frameworks/Python.framework/Versions/3.12/bin
    include-system-site-packages = true
    ...
    

Instead of displaying the default value of `false`, the `include-system-site-packages` configuration is now set to `true`.

This change means that you’ll see an additional entry to `sys.path`, which allows the Python interpreter in your virtual environment to also access the system site-packages directory. Make sure your virtual environment is active, then start the Python interpreter to check the path variables:

  * [Windows](#windows-39)
  * [Linux](#linux-39)
  * [macOS](#macos-39)



Python
    
    
    >>> import sys
    >>> sys.path
    ['',
     'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312\\python312.zip',
     'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312\\DLLs',
     'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312\\lib',
     'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312',
     'C:\\Users\\Name\\path\\to\\venv',
     'C:\\Users\\Name\\path\\to\\venv\\lib\\site-packages',
     'C:\\Users\\Name\\AppData\\Roaming\\Python\\Python312\\site-packages',
     'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python312\\lib\\site-packages']
    

Python
    
    
    >>> import sys
    >>> sys.path
    ['',
     '/usr/local/lib/python312.zip',
     '/usr/local/lib/python3.12',
     '/usr/local/lib/python3.12/lib-dynload',
     '/home/name/path/to/venv/lib/python3.12/site-packages',
     '/home/name/.local/lib/python3.12/site-packages',
     '/usr/local/lib/python3.12/site-packages']
    

Python
    
    
    >>> import sys
    >>> sys.path
    ['',
     '/Library/Frameworks/Python.framework/Versions/3.12/lib/python312.zip',
     '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12',
     '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/lib-dynload',
     '/Users/name/path/to/venv/lib/python3.12/site-packages',
     '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages']
    

The highlighted lines show the additional paths present in a virtual environment when you create it using `--system-site-packages`. They point to the site-packages directories of your base Python installation and give the interpreter inside your virtual environment access to these packages.

### Copy or Link Your Executables[](#copy-or-link-your-executables "Permanent link")

Whether you receive a copy or a symlink of your Python binaries depends on the operating system that you’re working with:

  * **Windows** may create either a symlink or a copy, but some versions don’t support symlinks. Creating symlinks might require you to have administrator privileges.
  * **Linux** distributions may create either a symlink or a copy, but often opt for symlinks over copies.
  * **macOS** always creates a copy of the binaries.



PEP 405 mentions the advantages of creating symlinks:

> Symlinking is preferable where possible because, in the case of an upgrade to the underlying Python installation, a Python executable copied in a venv might become out-of-sync with the installed standard library and require manual upgrade. ([Source](https://www.python.org/dev/peps/pep-0405/#copies-versus-symlinks))

While it can be helpful to symlink the executables so that they automatically stay in sync even if you upgrade your base Python installation, the added flimsiness of this approach may outweigh its benefit. For example, when you double-click `python.exe` in Windows, the operating system will eagerly resolve the symlink and ignore your virtual environment.

Most likely, you won’t ever have to touch these arguments, but if you have a good reason for attempting to force either symlinks or copies over your operating system’s default, then you can do so:

  * **`--symlinks`** will attempt to create symlinks instead of copies. This option won’t have any effect on macOS builds.
  * **`--copies`** will attempt to create copies of your Python binaries instead of linking them to the base Python installation’s executables.



You can pass either one of these optional arguments when you create your virtual environment.

### Upgrade Your Python to Match the System Python[](#upgrade-your-python-to-match-the-system-python "Permanent link")

If you’ve built your virtual environment [using copies rather than symlinks](#copy-or-link-your-executables) and then later updated your base Python version on your operating system, you might run into a version mismatch with standard-library modules.

The `venv` module offers a solution to this. The optional `--upgrade` argument keeps your site-packages directory intact while updating the binary files to the new versions on your system:

  * [Windows](#windows-40)
  * [Linux + macOS](#linux-macos-40)



Windows PowerShell
    
    
    PS> py -m venv venv\ --upgrade
    

Shell
    
    
    $ python3 -m venv venv/ --upgrade
    

If you run this command and you’ve updated your Python version since you initially created the virtual environment, then you’ll keep your installed libraries, but `venv` will update the executables for `pip` and Python.

In this section, you’ve learned that you can apply a lot of customization to the virtual environments that you build with the `venv` module. These adaptations can be pure convenience updates, such as naming your command prompt differently from your environment folder, overwriting existing environments, or creating multiple environments with a single command.

Other customizations create different functionality in your virtual environments by, for example, skipping the installation of `pip` and its dependencies, or linking back to the base Python’s site-packages folder.

But what if you want to do even more than that? In the next section, you’ll explore alternatives to the built-in `venv` module.

## What Other Popular Options Exist, Aside From `venv`?[](#what-other-popular-options-exist-aside-from-venv "Permanent link")

The `venv` module is a great way to work with virtual environments. One of its main advantages is that `venv` comes preinstalled with Python starting from version 3.3. But it isn’t the only option you have. You can use other tools to create and handle virtual environments in Python.

The Python ecosystem sports a wide range of third-party tools for dependency management, packaging, and improving your workflows. Many of these tools allow you to create and manage virtual environments.

**Note:** If you’re interested in learning more about the available tools that can help you create and manage your virtual environments and more, then check out the section on using [third-party tools](#use-third-party-tools).

In this section, you’ll learn about two popular tools that people in the Python community frequently use with the primary intention of creating and handling isolated Python environments. These tools have very different scopes but are both commonly used for the same purpose as the `venv` module:

  1. **Virtualenv** is a superset of `venv` and provides the basis for its implementation. It’s a powerful, extendable tool for creating isolated Python environments.
  2. **Conda** offers package, dependency, and environment management for Python and other languages. What conda offers goes way beyond virtual environments, but it’s popular and intuitive enough that some people use it primarily for that.



These two projects have some advantages over `venv`, but they don’t come with your standard Python installation, so you’ll have to install them separately.

### The Virtualenv Project[](#the-virtualenv-project "Permanent link")

[Virtualenv](https://virtualenv.pypa.io/en/latest/) is a tool that was specifically made for creating isolated Python environments. It’s been a long-time favorite within the Python community and precedes the built-in `venv` module.

The package is a superset of `venv`, which allows you to do everything that you can do using `venv`, and more. Virtualenv allows you to:

  * Create virtual environments more quickly
  * [Discover](https://virtualenv.pypa.io/en/latest/user_guide.html#python-discovery) installed versions of Python without needing to provide the absolute path
  * Upgrade the tool using `pip`
  * Extend the functionality of the tool yourself



Any of these additional functionalities can come in handy when you’re working on your Python projects. You might even want to save a blueprint of your virtualenv in code together with your project to aid reproducibility. Virtualenv has a rich [programmatic API](https://virtualenv.pypa.io/en/latest/user_guide.html#programmatic-api) that allows you to describe virtual environments without creating them.

After [installing `virtualenv`](https://virtualenv.pypa.io/en/latest/installation.html) on your system, you can create and activate a new virtual environment similarly to how you do it using `venv`:

  * [Windows](#windows-41)
  * [Linux](#linux-41)
  * [macOS](#macos-41)



Windows PowerShell
    
    
    PS> virtualenv venv\
    created virtual environment CPython3.12.5.final.0-64 in 312ms
      creator CPython3Windows(dest=C:\Users\Name\path\to\venv, clear=False, no_vcs_ignore=False, global=False)
      seeder FromAppData(download=False, pip=bundle, via=copy, app_data_dir=C:\Users\Name\AppData\Local\pypa\virtualenv)
        added seed packages: pip==24.1
      activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
    PS> Set-ExecutionPolicy Unrestricted -Scope Process
    PS> venv\Scripts\activate
    (venv) PS>
    

To avoid running into issues with the execution policy when activating your virtual environment, you first changed the execution policy for the current PowerShell session using `Set-ExecutionPolicy Unrestricted -Scope Process`.

Shell
    
    
    $ virtualenv venv/
    created virtual environment CPython3.12.5.final.0-64 in 214ms
      creator CPython3Posix(dest=/home/name/path/to/venv, clear=False, no_vcs_ignore=False, global=False)
      seeder FromAppData(download=False, pip=bundle, via=copy, app_data_dir=/home/name/.local/share/virtualenv)
        added seed packages: pip==24.1
      activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
    $ source venv/bin/activate
    (venv) $
    

Shell
    
    
    $ virtualenv venv/
    created virtual environment CPython3.12.5.final.0-64 in 294ms
      creator CPython3Posix(dest=/Users/name/path/to/venv, clear=False, no_vcs_ignore=False, global=False)
      seeder FromAppData(download=False, pip=bundle, via=copy, app_data_dir=/Users/name/Library/Application Support/virtualenv)
        added seed packages: pip==24.1
      activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
    $ source venv/bin/activate
    (venv) $
    

Like with `venv`, you can pass a relative or an absolute path and name your virtual environment. Before working in your virtualenv, you’ll usually activate it using one of the provided scripts.

**Note:** You might notice that virtualenv creates the isolated environment [much more quickly](https://discuss.python.org/t/virtualenv-20-0-0-beta1-is-available/3077) than the built-in `venv` module, which is possible because the tool [caches platform-specific application data](https://virtualenv.pypa.io/en/latest/user_guide.html#seeders) which it can quickly read from.

There are two main user advantages with virtualenv over `venv`:

  1. **Speed:** Virtualenv creates environments much more quickly.
  2. **Updates:** Thanks to virtualenv’s [embedded wheels](https://virtualenv.pypa.io/en/latest/user_guide.html#wheels), you’ll receive up-to-date `pip` and `setuptools` without needing to connect to the Internet right when you first set up the virtual environment.



If you need to work with legacy versions of Python 2.x, then virtualenv can also be helpful for that. It supports building Python virtual environments using Python 2 executables, which isn’t possible using `venv`.

**Note:** If you want to try working with virtualenv but you don’t have the permissions to install it, you can use [Python’s `zipapp`](https://realpython.com/python-zipapp/) module to circumvent that. Follow the instructions in the docs on [installing virtualenv via zipapp](https://virtualenv.pypa.io/en/latest/installation.html#via-zipapp).

If you’re just getting started with virtual environments in Python, then you may want to stick with the built-in `venv` module. However, if you’ve used `venv` for a while and you’re bumping into the tool’s limitations, then it’s a great idea to [get started using virtualenv](https://virtualenv.pypa.io/en/latest/user_guide.html).

### The Conda Package and Environment Manager[](#the-conda-package-and-environment-manager "Permanent link")

[Conda](https://docs.conda.io/en/latest/) gives you an alternative package and environment management approach that can replace `pip` and `venv` in your workflow. While the tool is primarily associated with the data science community and the [Anaconda Python distribution](https://anaconda.org), its potential use cases include package, dependency, and environment management for any language.

While you can also use conda to set up an isolated environment to install Python packages, this is only _one_ feature of the tool:

> pip installs _python_ packages within _an_ environment; conda installs _any_ package within _conda_ environments. ([Source](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/#Myth-#3:-Conda-and-pip-are-direct-competitor))

As you may gather from this quote, conda accomplishes the isolation of Python and installed third-party packages differently than the `venv` module and virtualenv project.

**Note:** A complete discussion of the conda package and environment manager is outside the scope of this tutorial. You’ll gloss over the differences and look at conda specifically for creating and working with a virtual environment.

You can set up conda on your system using the [Miniconda installer](https://docs.conda.io/en/latest/miniconda.html), which brings along the minimal requirements for running `conda` on your system.

In its default configuration, conda get its packages from [repo.anaconda.com](https://repo.anaconda.com/) instead of the [Python Package Index (PyPI)](https://pypi.org/). This alternative package index is maintained by the Anaconda project and is similar to PyPI, but not identical.

Because conda isn’t limited to _Python_ packages, you’ll find other, often data-science-related packages on conda’s package index written in different languages. Conversely, there are Python packages available on PyPI that you can’t install using conda because they aren’t present in that package repository. If you need such a package in your conda environment, then you can instead install it there using `pip`.

If you’re working in the data science space and with Python alongside other data science projects, then conda is an excellent choice that works across platforms and languages.

After installing Anaconda or Miniconda, you can [create a conda environment](https://docs.conda.io/projects/conda/en/latest/commands/create.html):

  * [Windows](#windows-42)
  * [Linux](#linux-42)
  * [macOS](#macos-42)



Windows PowerShell
    
    
    PS> conda create -n <venv-name>
    Channels:
     - conda-forge
    Platform: win-64
    Collecting package metadata (repodata.json): done
    Solving environment: done
    
    ## Package Plan ##
    
      environment location: C:\Users\Name\miniconda3\envs\<venv-name>
    
    Proceed ([y]/n)? y
    
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    #
    # To activate this environment, use
    #
    #     $ conda activate <venv-name>
    #
    # To deactivate an active environment, use
    #
    #     $ conda deactivate
    

Suppose your standard PowerShell session doesn’t recognize the `conda` command after successfully installing Anaconda. In that case, you can look for the _Anaconda PowerShell Prompt_ in your programs and work with that one instead.

Shell
    
    
    $ conda create -n <venv-name>
    Channels:
     - conda-forge
    Platform: linux-64
    Collecting package metadata (repodata.json): done
    Solving environment: done
    
    ## Package Plan ##
    
      environment location: /home/name/miniconda3/envs/<venv-name>
    
    Proceed ([y]/n)? y
    
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    #
    # To activate this environment, use
    #
    #     $ conda activate <venv-name>
    #
    # To deactivate an active environment, use
    #
    #     $ conda deactivate
    

Shell
    
    
    $ conda create -n <venv-name>
    Channels:
     - conda-forge
    Platform: osx-arm64
    Collecting package metadata (repodata.json): done
    Solving environment: done
    
    ## Package Plan ##
    
      environment location: /Users/name/miniconda3/envs/<venv-name>
    
    Proceed ([y]/n)? y
    
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    #
    # To activate this environment, use
    #
    #     $ conda activate <venv-name>
    #
    # To deactivate an active environment, use
    #
    #     $ conda deactivate
    

This command creates a new conda environment in a central location on your computer.

**Note:** Because all conda environments live in the same location, all environment names need to be unique. Therefore, it’s best if you give them descriptive names instead of calling any conda environment `venv`.

To work within your new conda environment, you’ll need to activate it:

  * [Windows](#windows-43)
  * [Linux + macOS](#linux-macos-43)



Windows PowerShell
    
    
    PS> conda activate <venv-name>
    (<venv-name>) PS>
    

Shell
    
    
    $ conda activate <venv-name>
    (<venv-name>) $
    

After activating the environment, you can install packages from conda’s package repository into that environment:

  * [Windows](#windows-44)
  * [Linux + macOS](#linux-macos-44)



Windows PowerShell
    
    
    (<venv-name>) PS> conda install numpy
    

Shell
    
    
    (<venv-name>) $ conda install numpy
    

The `install` command installs a third-party package from conda’s package repository into your active conda environment.

When you’re done working in the environment, you’ll have to deactivate it:

  * [Windows](#windows-45)
  * [Linux + macOS](#linux-macos-45)



Windows PowerShell
    
    
    (<venv-name>) PS> conda deactivate
    PS>
    

Shell
    
    
    (<venv-name>) $ conda deactivate
    $
    

You might notice that the general idea is similar to working with virtual environments that you’ve created using `venv`. The commands differ slightly, but you’ll receive the same benefits of working within an isolated environment that you can delete and re-create when necessary.

If you primarily work on data science projects and already work with Anaconda, then you might never have to work with `venv`. In that case, you can read more about [conda environments](https://realpython.com/python-windows-machine-learning-setup/#understanding-conda-environments) and how to work with them effectively on your machine.

If you only have pure-Python dependencies and you haven’t worked with Anaconda before, then you’re better off using the more lightweight `venv` module directly, or giving [virtualenv](#the-virtualenv-project) a try.

## How Can You Manage Your Virtual Environments?[](#how-can-you-manage-your-virtual-environments "Permanent link")

If you’ve absorbed all the information from the previous sections, but you’re unsure how to handle the multitude of environment folders that have started agglomerating on your system, keep on reading.

In this section, you’ll learn how to extract the essential information of your virtual environment into a single file so that you can quickly delete and re-create your virtual environment folder at any time and on any computer.

You’ll also learn about two different ways to organize where to keep your virtual environment folders and explore some popular third-party tools that can help you manage your virtual environments.

### Decide Where to Create Your Environment Folders[](#decide-where-to-create-your-environment-folders "Permanent link")

Since a Python virtual environment is just a folder structure, you can place it anywhere on your system. However, a consistent structure can help, and there are two widely-held opinions about where to create your virtual environment folders:

  1. Inside each individual **project folder**
  2. In a **single location** , for example in a subfolder of your home directory



Both of these have merits and disadvantages, and your preference will ultimately depend on your workflow.

With the **project-folder approach** , you create a new virtual environment in the root folder of the project that’ll use this virtual environment:
    
    
    project_name/
    │
    ├── venv/
    │
    └── src/
    

The virtual environment folder then lives alongside any code that you write for that project.

The advantage of this structure is that you’ll know which virtual environment belongs to which project, and you can activate your virtual environment using a short relative path once you’ve navigated into the project folder.

With the **single-folder approach** , you keep _all_ of your virtual environments in a single folder, for example, in a subfolder of your home directory:

  * [Windows](#windows-46)
  * [Linux](#linux-46)
  * [macOS](#macos-46)


    
    
    C:\USERS\USERNAME\
    │
    ├── .local\
    │
    ├── Contacts\
    │
    ├── Desktop\
    │
    ├── Documents\
    │   │
    │   └── Projects\
    │       │
    │       ├── django-project\
    │       │
    │       ├── flask-project\
    │       │
    │       └── pandas-project\
    │
    ├── Downloads\
    │
    ├── Favorites\
    │
    ├── Links\
    │
    ├── Music\
    │
    ├── OneDrive\
    │
    ├── Pictures\
    │
    ├── Searches\
    │
    ├── venvs\
    │   │
    │   ├── django-venv\
    │   │
    │   ├── flask-venv\
    │   │
    │   └── pandas-venv\
    │
    └── Videos\
    
    
    
    name/
    │
    ├── Desktop/
    │
    ├── Documents/
    │   │
    │   └── projects/
    │       │
    │       ├── django-project/
    │       │
    │       ├── flask-project/
    │       │
    │       └── pandas-project/
    │
    ├── Downloads/
    │
    ├── Music/
    │
    ├── Pictures/
    │
    ├── Public/
    │
    ├── Templates/
    │
    ├── venvs
    │   │
    │   ├── django-venv/
    │   │
    │   ├── flask-venv/
    │   │
    │   └── pandas-venv/
    │
    └── Videos/
    
    
    
    name/
    │
    ├── Applications/
    │
    ├── Desktop/
    │
    ├── Documents/
    │   │
    │   └── projects/
    │       │
    │       ├── django-project/
    │       │
    │       ├── flask-project/
    │       │
    │       └── pandas-project/
    │
    ├── Downloads/
    │
    ├── Library/
    │
    ├── Movies/
    │
    ├── Music/
    │
    ├── Pictures/
    │
    ├── Public/
    │
    ├── opt/
    │
    └── venvs
        │
        ├── django-venv/
        │
        ├── flask-venv/
        │
        └── pandas-venv/
    

If you use this approach, it could be less effort to keep track of which virtual environments you’ve created. You can go to a single location on your operating system to inspect all virtual environments and decide which ones to keep and which ones to delete.

On the other hand, you won’t be able to activate your virtual environment quickly using a relative path when you’ve already navigated to your project folder. Instead, it’s best to activate it using the absolute path to the activate script in the respective virtual environment folder.

**Note:** Keep in mind is that you can use either of these two approaches and even mix and match them. You could create your virtual environments _anywhere_ on your system. Just remember that a clear structure is more user-friendly because you’ll know where to find the folders.

A third option is to leave this decision to your [integrated development environment (IDE)](https://realpython.com/python-ides-code-editors-guide/). Many of these programs include options to automatically create a virtual environment for you when you start a new project.

To learn more about how your favorite IDE handles virtual environments, check out its online documentation on the topic. For example, [VS Code](https://code.visualstudio.com/docs/python/environments) and [PyCharm](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html) have their own approaches to creating virtual environments.

### Treat Them as Disposables[](#treat-them-as-disposables "Permanent link")

Virtual environments are disposable folder structures that you should be able to safely delete and re-create at any time without losing information about your code project.

This means that you generally don’t put any additional code or information into your virtual environment manually. Anything that goes in there should be handled by your package manager, which will usually be `pip` or `conda`.

You also shouldn’t commit your virtual environment to [version control](https://realpython.com/python-git-github-intro/#version-control), and you shouldn’t ship it with your project.

Because virtual environments aren’t entirely self-sufficient Python installations but rely on the base Python’s standard library, you won’t create a portable application by distributing your virtual environment together with your code.

**Note:** If you want to learn how to distribute your Python project, then you can read about [publishing an open-source package to PyPI](https://realpython.com/pypi-publish-python-package/) or [using PyInstaller to distribute Python applications](https://realpython.com/pyinstaller-python/).

Virtual environments are meant to be lightweight, disposable, and isolated environments to develop your projects in.

However, you should be able to re-create your Python environment on a different computer so that you can run your program or continue developing it there. How can you do that when you treat your virtual environment as disposable and don’t commit it to version control?

### Pin Your Dependencies[](#pin-your-dependencies "Permanent link")

To make your virtual environment reproducible, you need a way to describe its contents. The most common way to do this is by creating a [`requirements.txt` file](https://realpython.com/what-is-pip/#using-requirements-files) while your virtual environment is active:

  * [Windows](#windows-47)
  * [Linux + macOS](#linux-macos-47)



Windows PowerShell
    
    
    (venv) PS> python -m pip freeze > requirements.txt
    

Shell
    
    
    (venv) $ python -m pip freeze > requirements.txt
    

This command pipes the output of `pip freeze` into a new file called `requirements.txt`. If you open the file, then you’ll notice that it contains a list of the external dependencies currently installed in your virtual environment.

This list is a recipe for `pip` to know which version of which package to install. As long as you keep this `requirements.txt` file up to date, you can always re-create the virtual environment that you’re working in, even after you delete the `venv/` folder or move to a different computer altogether:

  * [Windows](#windows-48)
  * [Linux + macOS](#linux-macos-48)



Windows PowerShell
    
    
    (venv) PS> deactivate
    PS> py -m venv new-venv\
    PS> new-venv\Scripts\activate
    (new-venv) PS> python -m pip install -r requirements.txt
    

Shell
    
    
    (venv) $ deactivate
    $ python3 -m venv new-venv/
    $ source new-venv/bin/activate
    (new-venv) $ python -m pip install -r requirements.txt
    

In the example code snippet above, you created a new virtual environment called _new-venv_ , activated it, and installed all external dependencies that you previously recorded in your `requirements.txt` file.

If you use `pip list` to inspect the currently installed dependencies, then you’ll see that both virtual environments, _venv_ and _new-venv_ , now contain the same external packages.

**Note:** By committing your `requirements.txt` file to version control, you can ship your project code with the recipe that allows your users and collaborators to re-create the same virtual environment on their machines.

Keep in mind that while this is a widespread way to ship dependency information with a code project in Python, it isn’t deterministic because of these issues:

  1. **Python Version:** This requirements file doesn’t include information about which version of Python you used as your base Python interpreter when creating the virtual environment.
  2. **Sub-Dependencies:** Depending on how you create your requirements file, it may not include version information about sub-dependencies of your dependencies. This means that someone could get a different version of a subpackage if that package was silently updated after you created your requirements file.



You can’t easily solve either of these issues with `requirements.txt` alone, but many third-party dependency management tools attempt to address them to guarantee deterministic builds:

  * [`requirements.txt` using `pip-tools`](https://pip-tools.readthedocs.io/en/latest/#example-usage-for-pip-compile)
  * [`Pipfile.lock` using Pipenv](https://pipenv.pypa.io/en/latest/pipfile.html)
  * [`poetry.lock` using Poetry](https://python-poetry.org/docs/basic-usage/#installing-with-poetrylock)



Projects that integrate the virtual environment workflow into their features and go beyond it will also often include ways to create lock files that allow deterministic builds of your environments.

### Avoid Virtual Environments in Production[](#avoid-virtual-environments-in-production "Permanent link")

You might wonder how to include and activate your virtual environment when deploying a project to production. In most cases, you don’t want to include your virtual environment folder in remote online locations:

  * **GitHub:** Don’t push the `venv/` folder to GitHub.
  * **CI/CD Pipelines:** Don’t include your virtual environment folder in your [continuous integration](https://realpython.com/python-continuous-integration/) or continuous delivery pipelines.
  * **Server Deployments:** Don’t set up a virtual environment on your deployment server unless you manage that server yourself and run multiple separate projects on it.



You still want isolated environments and reproducibility for your code projects. You’ll achieve that by pinning your dependencies instead of including the virtual environment folder that you’ve worked with locally.

Most remote hosting providers, including CI/CD pipeline tools and Platform-as-a-Service (PaaS) providers, such as [Heroku](https://realpython.com/django-hosting-on-heroku/) or [Google App Engine (GAE)](https://realpython.com/python-web-applications/), will automatically create that isolation for you.

When you push your code project to one of these hosted services, the service will often allocate a virtual fraction of a server to your application. Such virtualized servers are isolated environments by design, which means that your code will run in its separate environment by default.

In most hosted solutions, you won’t have to deal with creating the isolation, but you’ll still need to provide the information about what to install in the remote environment. For this, you’ll often use the pinned dependencies in your `requirements.txt` file.

**Note:** If you run multiple projects on a server that you host yourself, then you might benefit from setting up virtual environments on that server.

In that case, you’ll get to treat the server similarly to your local computer. Even then, you won’t copy the virtual environment folder. Instead, you’ll re-create the virtual environment on your remote server from your pinned dependencies.

Most hosted platform providers will also ask you to create a settings file specific to the tool that you’re working with. This file will include information that isn’t recorded in `requirements.txt` but that the platform needs to set up a functioning environment for your code. You’ll need to read up on these specific files in the documentation of the hosting service that you’re planning to use.

A popular option that takes virtualization to the next level and still allows you to create a lot of the setup yourself is [Docker](https://realpython.com/docker-continuous-integration/).

### Use Third-Party Tools[](#use-third-party-tools "Permanent link")

The Python community has created many additional tools that use virtual environments as one of their features and allow you to manage multiple virtual environments in a user-friendly manner.

Because many tools come up in online discussions and tutorials, you might wonder what each of them is about and how they can help you manage your virtual environments.

While discussing each of them is out of the scope of this tutorial, here’s an overview of popular projects, what they do, and where you can learn more:

  * **[virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)** is an extension to the virtualenv project that makes creating, deleting, and managing virtual environments less effort. It keeps all your virtual environments in one place, introduces user-friendly CLI commands for managing and switching between virtualenvs, and is also configurable and extensible. [`virtualenvwrapper-win`](https://github.com/davidmarble/virtualenvwrapper-win/) is a Windows port of this project.

  * **[Poetry](https://python-poetry.org)** is a tool for [Python dependency management](https://realpython.com/dependency-management-python-poetry/) and packaging. With Poetry, you can declare packages that your project depends on, similar to `requirements.txt`, but deterministic. Poetry will then install these dependencies in an auto-generated virtual environment and help you [manage your virtual environment](https://python-poetry.org/docs/managing-environments/).

  * **[uv](https://github.com/astral-sh/uv)** is a versatile command-line tool that aims to unify the management of Python packages, dependencies, and virtual environments. By abstracting over multiple tools like `pip`, virtualenv, and pyenv, uv provides a unified interface for tasks such as installing packages, managing virtual environments, and handling Python versions. Using [uv](https://realpython.com/python-uv/) can make maintaining a consistent and reproducible development environment more straightforward.

  * **[Hatch](https://hatch.pypa.io/latest/)** is a modern Python project manager that simplifies environment creation, dependency management, and packaging. It allows you to define project-specific configurations, automates the setup of isolated environments, and supports advanced features like multi-environment testing and version management. Hatch is a comprehensive tool for managing Python projects from development to deployment.

  * **[Pipenv](https://pipenv.pypa.io/en/latest/)** aims to improve packaging in Python. It creates and manages virtual environments for your projects using `virtualenv` in the back. Like Poetry, [Pipenv aims to improve dependency management](https://realpython.com/pipenv-guide/#dependency-management-with-requirementstxt) to allow for deterministic builds. It’s a relatively slow, high-level tool that’s been supported by the [Python Packaging Authority (PyPA)](https://www.pypa.io/en/latest/).

  * **[pipx](https://github.com/pypa/pipx)** allows you to [install Python applications](https://realpython.com/python-pipx/). These are packages that you’d habitually run as stand-alone executables in isolated environments. With pipx, you create a virtual environment for each tool and make it globally accessible. Aside from helping with code quality tools such as black, isort, flake8, Pylint, and mypy, it’s also useful for installing alternative Python interpreters, such as [bpython](https://realpython.com/bpython-alternative-python-repl/), [ptpython](https://realpython.com/ptpython-shell/), or [IPython](https://realpython.com/ipython-interactive-python-shell/).

  * **[pipx-in-pipx](https://github.com/mattsb42-meta/pipx-in-pipx)** is a wrapper you can use for installing pipx that takes the [recursive acronym for `pip`](https://en.wikipedia.org/wiki/Pip_\(package_manager\)#History) to the next level by allowing you to install and manage pipx using pipx itself.

  * **[pyenv](https://github.com/pyenv/pyenv)** isn’t inherently related to virtual environments, even though it’s often mentioned in relation to this concept. You can [manage multiple Python versions with pyenv](https://realpython.com/intro-to-pyenv/), which allows you to switch between a new release and an older Python version that you need for a project you’re working on. pyenv also has a Windows port called [pyenv-win](https://github.com/pyenv-win/pyenv-win).

  * **[pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)** is a plugin for [pyenv](https://realpython.com/intro-to-pyenv/) that combines pyenv with virtualenv, allowing you to create virtual environments for the pyenv-managed Python versions on UNIX systems. There’s even a plugin to mix pyenv with virtualenvwrapper, called [pyenv-virtualenvwrapper](https://github.com/pyenv/pyenv-virtualenvwrapper).




These tools can handle virtual environments for you, but doing so isn’t their core focus. As you may have gleaned from their short descriptions, they have partly overlapping objectives where virtual environments are only one piece of what they offer. Check out the links above if you want to learn more about any of them.

The Python community has built a whole host of third-party projects that can help you manage your Python virtual environments in a user-friendly manner. Remember that these projects are meant to make the process more convenient for you and aren’t _necessary_ for working with virtual environments.

## Conclusion[](#conclusion "Permanent link")

Congratulations on making it through this tutorial on Python virtual environments. Throughout the tutorial, you built a thorough understanding of what virtual environments are, why you need them, how they function internally, and how you can manage them on your system.

**In this tutorial, you learned how to:**

  * **Create** and **activate** a **Python virtual environment**
  * Explain **why** you want to **isolate external dependencies**
  * **Visualize what Python does** when you create a virtual environment
  * **Customize** your virtual environments using **optional arguments** to `venv`
  * **Deactivate** and **remove** virtual environments
  * Choose **additional tools for managing** your Python versions and virtual environments



Next time a tutorial tells you to create and activate a virtual environment, you’ll better understand why that’s a good idea and what exactly Python does for you behind the scenes.

## Frequently Asked Questions[](#frequently-asked-questions "Permanent link")

Now that you have some experience with creating and managing Python virtual environments, you can use the questions and answers below to check your understanding and recap what you’ve learned.

These FAQs are related to the most important concepts you’ve covered in this tutorial. Click the _Show/Hide_ toggle beside each question to reveal the answer.

****How do you create a Python virtual environment?**** Show/Hide

You create a Python virtual environment by using the `venv` module. Open your terminal or command prompt and run the command `python -m venv venv/`, replacing `venv/` with the folder name you want to give your virtual environment. This command sets up a new directory with a copy or symlink of the Python interpreter and a few supporting files.

****Why should you use virtual environments in Python?**** Show/Hide

You should use virtual environments in Python to manage dependencies for different projects separately. This prevents conflicts between package versions and keeps your global Python environment clean. Virtual environments ensure that each project can have its own set of dependencies, independent of one another and the system-wide Python packages.

****How do you activate a virtual environment on Windows?**** Show/Hide

To activate a virtual environment on Windows, navigate to your environment’s directory in the command prompt and run the command `venv\Scripts\activate`. Once activated, the environment name will appear in your command prompt, indicating that the virtual environment is active.

****Can you use different versions of Python in virtual environments?**** Show/Hide

Yes, you can use different versions of Python in virtual environments. When creating a virtual environment, you can specify the Python interpreter you want to use by providing the path to the desired Python executable. This allows you to maintain environments with different Python versions as needed for your projects.

****How do you install packages in a Python virtual environment?**** Show/Hide

Once you activate your virtual environment, you can install packages using `pip`. Run the command `python -m pip install <package-name>` to install a package in the active environment. This ensures that the installed package is isolated within the virtual environment, preventing conflicts with other projects.

**Get Your Cheat Sheet:** [Click here to download a free cheat sheet](https://realpython.com/bonus/python-virtual-environments-a-primer-pdf/) that summarizes the main venv commands you’ll learn about in this tutorial.

**Take the Quiz:** Test your knowledge with our interactive “Python Virtual Environments: A Primer” quiz. You’ll receive a score upon completion to help you track your learning progress:

* * *

[ ![Python Virtual Environments \(venv\)](https://files.realpython.com/media/Python-Virtual-Environments_Watermarked.4c787192d42f.jpg) ](/quizzes/python-virtual-environments-a-primer/)

**Interactive Quiz**

[Python Virtual Environments: A Primer](/quizzes/python-virtual-environments-a-primer/)

In this quiz, you'll test your understanding of Python virtual environments. With this knowledge, you'll be able to avoid dependency conflicts and help other developers reproduce your development environment.

Mark as Completed

[](/feedback/survey/article/python-virtual-environments-a-primer/liked/?from=article-footer "Liked it") [](/feedback/survey/article/python-virtual-environments-a-primer/disliked/?from=article-footer "Disliked it")

Share

Watch Now This tutorial has a related video course created by the Real Python team. Watch it together with the written tutorial to deepen your understanding: [**Working With Python Virtual Environments**](/courses/working-python-virtual-environments/)

🐍 Python Tricks 💌

Get a short & sweet **Python Trick** delivered to your inbox every couple of days. No spam ever. Unsubscribe any time. Curated by the Real Python team.

![Python Tricks Dictionary Merge](/static/pytrick-dict-merge.4201a0125a5e.png)

Send Me Python Tricks »

About **Martin Breuss**

[ ![Martin Breuss](/cdn-cgi/image/width=456,height=456,fit=crop,gravity=auto,format=auto/https://files.realpython.com/media/martin_breuss_python_square.efb2b07faf9f.jpg) ![Martin Breuss](/cdn-cgi/image/width=456,height=456,fit=crop,gravity=auto,format=auto/https://files.realpython.com/media/martin_breuss_python_square.efb2b07faf9f.jpg) ](/team/mbreuss/)

Martin is Real Python's Head of Content Strategy. With a background in education, he's worked as a coding mentor, code reviewer, curriculum developer, bootcamp instructor, and instructional designer.

[» More about Martin](/team/mbreuss/)

* * *

_Each tutorial at Real Python is created by a team of developers so that it meets our high quality standards. The team members who worked on this tutorial are:_

[![Aldren Santos](/cdn-cgi/image/width=500,height=500,fit=crop,gravity=auto,format=auto/https://files.realpython.com/media/Aldren_Santos_Real_Python.6b0861d8b841.png)](/team/asantos/)

[Aldren](/team/asantos/)

[![Brenda Weleschuk](/cdn-cgi/image/width=320,height=320,fit=crop,gravity=auto,format=auto/https://files.realpython.com/media/IMG_3324_1.50b309355fc1.jpg)](/team/bweleschuk/)

[Brenda](/team/bweleschuk/)

[![Bartosz Zaczyński](/cdn-cgi/image/width=1694,height=1694,fit=crop,gravity=auto,format=auto/https://files.realpython.com/media/coders_lab_2109368.259b1599fbee.jpg)](/team/bzaczynski/)

[Bartosz](/team/bzaczynski/)

[![Dan Bader](/cdn-cgi/image/width=1000,height=1000,fit=crop,gravity=auto,format=auto/https://files.realpython.com/media/daniel-square.d58bf4388750.jpg)](/team/dbader/)

[Dan](/team/dbader/)

[![Geir Arne Hjelle](/cdn-cgi/image/width=800,height=800,fit=crop,gravity=auto,format=auto/https://files.realpython.com/media/gahjelle.470149ee709e.jpg)](/team/gahjelle/)

[Geir Arne](/team/gahjelle/)

[![Joanna Jablonski](/cdn-cgi/image/width=800,height=800,fit=crop,gravity=auto,format=auto/https://files.realpython.com/media/jjablonksi-avatar.e37c4f83308e.jpg)](/team/jjablonski/)

[Joanna](/team/jjablonski/)

[![Kate Finegan](/cdn-cgi/image/width=400,height=400,fit=crop,gravity=auto,format=auto/https://files.realpython.com/media/VZxEtUor_400x400.7169c68e3950.jpg)](/team/kfinegan/)

[Kate](/team/kfinegan/)

[![Michael Herman](/cdn-cgi/image/width=160,height=160,fit=crop,gravity=auto,format=auto/https://files.realpython.com/media/mike.fa94729a1e81.jpg)](/team/mherman/)

[Michael](/team/mherman/)

Master _Real-World Python Skills_ With Unlimited Access to Real Python

![Locked learning resources](/static/videos/lesson-locked.f5105cfd26db.svg)

**Join us and get access to thousands of tutorials, hands-on video courses, and a community of expert  Pythonistas:**

[Level Up Your Python Skills »](/account/join/?utm_source=rp_article_footer&utm_content=python-virtual-environments-a-primer)

Master _Real-World Python Skills_  
With Unlimited Access to Real Python

![Locked learning resources](/static/videos/lesson-locked.f5105cfd26db.svg)

**Join us and get access to thousands of tutorials, hands-on video courses, and a community of expert Pythonistas:**

[Level Up Your Python Skills »](/account/join/?utm_source=rp_article_footer&utm_content=python-virtual-environments-a-primer)

What Do You Think?

**Rate this article:**

[](/feedback/survey/article/python-virtual-environments-a-primer/liked/?from=article-comments "Liked it") [](/feedback/survey/article/python-virtual-environments-a-primer/disliked/?from=article-comments "Disliked it")

[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Frealpython.com%2Fpython-virtual-environments-a-primer%2F) [Twitter](https://twitter.com/intent/tweet/?text=Interesting%20Python%20article%20on%20%40realpython%3A%20Python%20Virtual%20Environments%3A%20A%20Primer&url=https%3A%2F%2Frealpython.com%2Fpython-virtual-environments-a-primer%2F) [Bluesky](https://bsky.app/intent/compose?text=Interesting%20Python%20article%20on%20%40realpython.com%3A%20Python%20Virtual%20Environments%3A%20A%20Primer%20https%3A%2F%2Frealpython.com%2Fpython-virtual-environments-a-primer%2F) [Facebook](https://facebook.com/sharer/sharer.php?u=https%3A%2F%2Frealpython.com%2Fpython-virtual-environments-a-primer%2F) [Email](mailto:?subject=Python%20article%20for%20you&body=Python%20Virtual%20Environments%3A%20A%20Primer%20on%20Real%20Python%0A%0Ahttps%3A%2F%2Frealpython.com%2Fpython-virtual-environments-a-primer%2F%0A)

What’s your #1 takeaway or favorite thing you learned? How are you going to put your newfound skills to use? Leave a comment below and let us know.

**Commenting Tips:** The most useful comments are those written with the goal of learning from or helping out other students. [Get tips for asking good questions](https://realpython.com/python-beginner-tips/#tip-9-ask-good-questions) and [get answers to common questions in our support portal](https://support.realpython.com).

* * *

Looking for a real-time conversation? Visit the [Real Python Community Chat](/community/) or join the next [“Office Hours” Live Q&A; Session](/office-hours/). Happy Pythoning!

Keep Learning

Related Topics: [intermediate](/tutorials/intermediate/) [devops](/tutorials/devops/) [tools](/tutorials/tools/)

Recommended Video Course: [Working With Python Virtual Environments](/courses/working-python-virtual-environments/)

Related Tutorials:

  * [Managing Multiple Python Versions With pyenv](/intro-to-pyenv/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=python-virtual-environments-a-primer)
  * [Using Python's pip to Manage Your Projects' Dependencies](/what-is-pip/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=python-virtual-environments-a-primer)
  * [Beautiful Soup: Build a Web Scraper With Python](/beautiful-soup-web-scraper-python/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=python-virtual-environments-a-primer)
  * [Your Python Coding Environment on Windows: Setup Guide](/python-coding-setup-windows/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=python-virtual-environments-a-primer)
  * [Python MCP Server: Connect LLMs to Your Data](/python-mcp/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=python-virtual-environments-a-primer)



## Keep reading Real Python by creating a free account or signing in:

[![Keep reading](/static/videos/lesson-locked.f5105cfd26db.svg)](/account/signup/?intent=continue_reading&utm_source=rp&utm_medium=web&utm_campaign=rwn&utm_content=v1&next=%2Fpython-virtual-environments-a-primer%2F)

_[Continue »](/account/signup/?intent=continue_reading&utm_source=rp&utm_medium=web&utm_campaign=rwn&utm_content=v1&next=%2Fpython-virtual-environments-a-primer%2F)

Already have an account? [Sign-In](/account/login/?next=/python-virtual-environments-a-primer/)

Almost there! Complete this form and click the button below to gain instant access:

×

![Python Virtual Environments \(venv\)](https://files.realpython.com/media/Python-Virtual-Environments_Watermarked.4c787192d42f.jpg)

Python Virtual Environments: A Primer (Cheat Sheet)

Send PDF »

🔒 No spam. We take your privacy seriously.

##### Learn Python

  * [Start Here](/start-here/)
  * [Learning Resources](/search)
  * [Code Mentor](/mentor/)
  * [Python Reference](/ref/)
  * [Python Cheat Sheet](/cheatsheets/python/)
  * [Support Center](https://support.realpython.com/)



##### Courses & Paths

  * [Learning Paths](/learning-paths/)
  * [Quizzes & Exercises](/quizzes/)
  * [Browse Topics](/tutorials/all/)
  * [Live Courses](/live/)
  * [Books](/books/)



##### Community

  * [Podcast](/podcasts/rpp/)
  * [Newsletter](/newsletter/)
  * [Community Chat](/community/)
  * [Office Hours](/office-hours/)
  * [Learner Stories](/learner-stories/)



##### Membership

  * [Plans & Pricing](/account/join/)
  * [Team Plans](/account/join-team/)
  * [For Business](/account/join-team/inquiry/)
  * [For Schools](/account/join-team/education-inquiry/)
  * [Reviews](/learner-stories/)



##### Company

  * [About Us](/about/)
  * [Team](/team/)
  * [Mission & Values](/mission/)
  * [Editorial Guidelines](/editorial-guidelines/)
  * [Sponsorships](/sponsorships/)
  * [Careers](https://realpython.workable.com)
  * [Press Kit](/media-kit/)
  * [Merch](/merch)



[](https://www.youtube.com/realpython "YouTube") [](https://x.com/realpython "X/Twitter") [](https://www.linkedin.com/company/realpython-com "LinkedIn") [](https://www.facebook.com/LearnRealPython "Facebook") [](https://github.com/realpython/ "GitHub")

[Privacy Policy](/privacy-policy/) ⋅ [Terms of Use](/terms/) ⋅ [Security](/security/) ⋅ [Contact](/contact/)

Happy Pythoning!

© 2012–2025 DevCademy Media Inc. DBA Real Python. All rights reserved.  
REALPYTHON™ is a trademark of DevCademy Media Inc.  [ ![Real Python - Online Python Training \(logo\)](/static/real-python-logo-primary.973743b6d39d.svg) ](/)

Free Bonus: **Python Cheat Sheet** ×

Get a **Python Cheat Sheet (PDF)** and learn the basics of Python, like working with data types, dictionaries, lists, and Python functions:

![Python Cheat Sheet](/static/cheatsheet-stacked-sm.c9ac81c58bcc.png)

Send My Python Cheat Sheet »

![](https://www.facebook.com/tr?id=2220911568135371&ev=PageView&noscript=1)
