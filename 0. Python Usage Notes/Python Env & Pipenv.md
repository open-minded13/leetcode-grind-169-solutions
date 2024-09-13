# Python Environment Configuration & Virtual Environment Management

## Configure Environment Variables for Python

```sh
$ which python
/Users/username/opt/anaconda3/bin/python

$ ls      
Applications    Desktop         Downloads       Library         Music           Public          opt
Autodesk        Documents       Fusion 360 CAM  Movies          Pictures        copytranslator

$ ls -a
.                    ..              .zprofile                   
Music                Public          Pictures
# It should have a lot of other files and directories showing up here

# Open the .zprofile file in the vim editor to add or modify environment variables or aliases related to Python
# Saving and exiting vim using `esc` + `:` + `w` + `q`
$ vim .zprofile

# Run `source .zprofile`x to apply the changes made in the `.zprofile` file to the current shell session
$ source .zprofile

$ which python3
python3: aliased to /usr/local/bin/python3

$ python3
Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Use quit() or Ctrl-D (i.e. EOF) to exit
>>> quit()
```

## Create, Run, and Remove a Virtual Environment

### Step 1 - Create a virtual environment

```sh
cd ~/Desktop/MyProject
pipenv install requests
```

```sh
-----------------------------------------------------------------
Creating a virtualenv for this project...
Pipfile: /Users/username/Desktop/MyProject/Pipfile
Using default python from /opt/homebrew/opt/python@3.11/bin/python3.11 (3.11.3) to create virtualenv...
⠸ Creating virtual environment...created virtual environment CPython3.11.3.final.0-64 in 307ms
  creator CPython3Posix(dest=/Users/username/.local/share/virtualenvs/MyProject-fPjN32K2, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/username/Library/Application Support/virtualenv)
    added seed packages: pip==23.1.2, setuptools==67.7.2, wheel==0.40.0
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment!
Virtualenv location: /Users/username/.local/share/virtualenvs/MyProject-fPjN32K2
Creating a Pipfile for this project...
Installing requests...
Resolving requests...
Adding requests to Pipfile's [packages] ...
✔ Installation Succeeded
Pipfile.lock not found, creating...
Locking [packages] dependencies...
Building requirements...
Resolving dependencies...
✔ Success!
Locking [dev-packages] dependencies...
Updated Pipfile.lock (ff88c6939e3090788e917cfdecf1af872168b83c8803457853061495493b5a71)!
Installing dependencies from Pipfile.lock (3b5a71)...
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
-----------------------------------------------------------------
```

### Step 2 - Run the virtual environment

```sh
pipenv shell
```

```sh
-----------------------------------------------------------------
Launching subshell in virtual environment...
 . /Users/username/.local/share/virtualenvs/MyProject-fPjN32K2/bin/activate            
(MyProject) $ . /Users/username/.local/share/virtualenvs/MyProject-fPjN32K2/bin/activate
(MyProject) $ 
-----------------------------------------------------------------
```

### Step 3 - View the path of the virtual environment, where Python is running

```sh
(MyProject) $ python
```

```sh
-----------------------------------------------------------------
Python 3.11.3 (main, Apr  7 2023, 20:13:31) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.executable
'/Users/username/.local/share/virtualenvs/MyProject-fPjN32K2/bin/python'
-----------------------------------------------------------------
```

### Step 4 - Deactivate the virtual environment

NOTE: Use "exit" instead of "deactivate."

```sh
(MyProject) $ exit  
```

```sh
-----------------------------------------------------------------
Saving session...
...copying shared history...
...saving history...truncating history files...
...completed.
-----------------------------------------------------------------
```

### Step 5 - Run a Python file directly in the virtual environment

```sh
$ pipenv run python
# OR:
$ pipenv run python YourCodeName.py
```

```sh
-----------------------------------------------------------------
Python 3.11.3 (main, Apr  7 2023, 20:13:31) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.executable
'/Users/username/.local/share/virtualenvs/MyProject-fPjN32K2/bin/python'
>>> exit()
-----------------------------------------------------------------
```

### Step 6 - Install/Uninstall packages using existing requirements.txt if provided

```sh
pipenv install -r PATH_TO_YOUR_requirements.txt
pipenv uninstall requests
```

### Step 7 - Remove the virtual environment completely

NOTE: "Pipfile" and "Pipfile.lock" in the MyProject folder will not be deleted. Next time, the same environment specified in the Pipfile file will be created by running `pipenv install`.

```sh
pipenv --rm                       
```

```sh
-----------------------------------------------------------------
Removing virtualenv (/Users/username/.local/share/virtualenvs/MyProject-fPjN32K2)...
-----------------------------------------------------------------
```

#### Completely Remove a Virtual Environment Even if You Don’t Know Its Path

In the root of the project where the `Pipfile` is located, you can run:

```sh
pipenv --venv
```

This will return the location of the virtual environment, such as:

- **Linux/OS X**: `/Users/your_user_name/.local/share/virtualenvs/project_name-xxxx`
  
- **Windows**: `C:\Users\your_user_name\.virtualenvs\project_name-xxxx`

To remove the environment:

- **Bash/Zsh**:
  
  ```sh
  rm -rf /Users/your_user_name/.local/share/virtualenvs/project_name-xxxx
  ```

- **Powershell**:

  ```sh
  Remove-Item -Recurse -Force 'C:\Users\your_user_name\.virtualenvs\project_name-xxxx'
  ```

- **Command Prompt**:

  ```sh
  rmdir /s "C:\Users\your_user_name\.virtualenvs\project_name-xxxx"
  ```

### Other: Recreate the virtual environment with a different Python version

- Check the tutorial: [YouTube](https://youtu.be/zDYL22QNiWk?t=1245)
- Check the official website: [pipenv.pypa.io](https://pipenv.pypa.io/en/latest/)
