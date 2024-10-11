# Bash Commands Usage Guide

This guide provides an overview of common Bash commands, their purposes, usages, examples, and practice questions with answers. It's designed to help beginners understand and practice basic file manipulation and command line operations in Unix-like operating systems.

## Table of Contents

- [Bash Commands Usage Guide](#bash-commands-usage-guide)
  - [Table of Contents](#table-of-contents)
  - [`cd` (Change Directory)](#cd-change-directory)
  - [`ls` (List)](#ls-list)
  - [`rm` (Remove)](#rm-remove)
  - [`mv` (Move)](#mv-move)
  - [`touch`](#touch)
  - [`cp` (Copy)](#cp-copy)
  - [`mkdir` (Make Directory)](#mkdir-make-directory)
  - [`pwd` (Print Working Directory)](#pwd-print-working-directory)
  - [`cat` (Concatenate)](#cat-concatenate)
  - [`less`](#less)
  - [`grep` (Global Regular Expression Print)](#grep-global-regular-expression-print)
  - [`chmod` (Change Mode)](#chmod-change-mode)
  - [Piping and Redirection](#piping-and-redirection)
    - [Piping (`|`)](#piping-)
    - [Redirection](#redirection)
      - [Standard Output (`stdout`) and Standard Error (`stderr`)](#standard-output-stdout-and-standard-error-stderr)
      - [Standard Input (`stdin`)](#standard-input-stdin)

## `cd` (Change Directory)

- **Purpose**: Navigate between directories.
- **Usage**:
  - `cd [directory]` - Change to `[directory]`.
  - `cd ..` - Move up one directory level.
  - `cd` or `cd ~` - Change to the user's home directory.
- **Examples**:
  - `cd Documents` changes to the `Documents` directory.
  - `cd /var/log` changes to the `/var/log` directory.
- **Practice**:
  1. **Q**: Move to the parent directory. **A**: `cd ..`
  2. **Q**: Change to your home directory. **A**: `cd` or `cd ~`

## `ls` (List)

- **Purpose**: Display contents of directories.
- **Usage**:
  - `ls` - List files and directories.
  - `ls -l` - List with details.
  - `ls -1` - This command lists all files and directories in the current directory, with each entry on a new line (-1 option ensures that, especially useful when piping).
  - `ls -a` - Include hidden files.
- **Examples**:
  - `ls` displays visible files.
  - `ls -la /home/user` lists all files in `/home/user` with details.
- **Practice**:
  1. **Q**: List all files, including hidden ones. **A**: `ls -a`
  2. **Q**: View detailed information of files. **A**: `ls -l`

## `rm` (Remove)

- **Purpose**: Delete files or directories.
- **Usage**:
  - `rm [file]` - Remove a file.
  - `rm -r [directory]` - Recursively remove a directory and its contents.
- **Examples**:
  - `rm example.txt` deletes `example.txt`.
  - `rm -r folderName` deletes `folderName` and all its contents.
- **Practice**:
  1. **Q**: Delete a file named `old.txt`. **A**: `rm old.txt`
  2. **Q**: Remove a directory and all its contents named `archive`. **A**: `rm -r archive`

## `mv` (Move)

- **Purpose**: Move or rename files and directories.
- **Usage**:
  - `mv [source] [destination]` - Move or rename.
- **Examples**:
  - `mv old.txt new.txt` renames `old.txt` to `new.txt`.
  - `mv file.txt /home/user/Documents` moves `file.txt` to the specified directory.
- **Practice**:
  1. **Q**: Rename `file1.txt` to `file2.txt`. **A**: `mv file1.txt file2.txt`
  2. **Q**: Move `photo.jpg` to the `Pictures` directory. **A**: `mv photo.jpg Pictures`

## `touch`

- **Purpose**: Create a new file or update the timestamp.
- **Usage**:
  - `touch [file]` - Create or update a file.
- **Examples**:
  - `touch newfile.txt` creates or updates `newfile.txt`.
- **Practice**:
  1. **Q**: Create a new file named `example.txt`. **A**: `touch example.txt`

## `cp` (Copy)

- **Purpose**: Copy files or directories.
- **Usage**:
  - `cp [source] [destination]` - Copy files or directories.
- **Examples**:
  - `cp source.txt destination.txt` copies `source.txt` to `destination.txt`.
  - `cp -r sourceDir/ destinationDir/` copies a directory recursively.
- **Practice**:
  1. **Q**: Copy `report.txt` to `backup_report.txt`. **A**: `cp report.txt backup_report.txt`
  2. **Q**: Recursively copy the `project` directory to a new directory `project_backup`. **A**: `cp -r project project_backup`

## `mkdir` (Make Directory)

- **Purpose**: Create a new directory.
- **Usage**:
  - `mkdir [directory]` - Create a directory.
- **Examples**:
  - `mkdir newDir` creates `newDir`.
- **Practice**:
  1. **Q**: Create a directory named `Homework`. **A**: `mkdir Homework`

## `pwd` (Print Working Directory)

- **Purpose**: Show the current directory path.
- **Usage**:
  - `pwd` - Display current directory.
- **Examples**:
  - `pwd` might output `/home/user`.
- **Practice**:
  1. **Q**: How do you display the current directory path? **A**: `pwd`

## `cat` (Concatenate)

- **Purpose**: Read, concatenate files.
- **Usage**:
  - `cat [file]` - Display file content.
  - `cat [file1] [file2] > [newfile]` - Concatenate files.
- **Examples**:
  - `cat file.txt` displays `file.txt` content.
  - `cat file1.txt file2.txt > combined.txt` combines files.
- **Practice**:
  1. **Q**: Display the contents of `notes.txt`. **A**: `cat notes.txt`
  2. **Q**: Concatenate `part1.txt` and `part2.txt` into `full.txt`. **A**: `cat part1.txt part2.txt > full.txt`

## `less`

- **Purpose**: View file contents page by page.
- **Usage**:
  - `less [file]` - Open file for page-wise viewing.
- **Examples**:
  - `less largefile.log` for viewing larger files.
- **Practice**:
  1. **Q**: View `report.log` in a paginated manner. **A**: `less report.log`

## `grep` (Global Regular Expression Print)

- **Purpose**: Search text using patterns.
- **Usage**:
  - `grep [pattern] [file]` - Search for pattern in file.
  - `grep -r [pattern] [directory]` - Recursively search in directory.
  - `grep -i [pattern] [file]` - The `-i` option makes `grep` search case-insensitively, allowing it to match the pattern regardless of case.
  - `grep -w [pattern] [file]` - The `-w` option restricts `grep` to match only whole words, meaning the pattern must appear as a distinct word.
- **Examples**:
  - `grep "error" log.txt` finds "error" in `log.txt`.
  - `grep -r "config" /etc/` searches for "config" in `/etc/` directory.
  - `grep -i "error" log.txt`: This command searches for the word "error" in `log.txt`, ignoring case. It matches "error", "Error", "ERROR", etc.
  - `grep -w "config" settings.ini`: Searches for "config" only where it stands as a whole word in `settings.ini`. It will not match "preconfig" or "configurations".
  - `grep -wi "example" file.txt`: This will search for the whole word "example" in `file.txt`, ignoring case.
- **Practice**:
  1. **Q**: Find the word "success" in `output.log`. **A**: `grep "success" output.log`
  2. **Q**: Recursively search for "NotFound" in the current directory. **A**: `grep -r "NotFound" .`
  3. **Q**: How would you search for "warning" in `events.log` without regard to case? **A**: `grep -i "warning" events.log`
  4. **Q**: How do you find the whole word "user" in the file `users.txt`? **A**: `grep -w "user" users.txt`

## `chmod` (Change Mode)

- **Purpose**: Change file or directory permissions.
- **Usage**:
  - `chmod [options] [permissions] [file]` - Change permissions.
- **Examples**:
  - `chmod 755 script.sh` sets read, write, and execute permissions for the owner, and read and execute permissions for others.
- **Practice**:
  1. **Q**: Make `run_me.sh` executable by everyone. **A**: `chmod +x run_me.sh`

> The above guide covers the basics to get you started with Unix-like operating systems. Experiment with these commands and use the `man` command for more detailed information on each.

## Piping and Redirection

Understanding how to use piping and redirection in the command line can significantly enhance your ability to manipulate data and automate tasks. Here's a brief guide on these concepts:

### Piping (`|`)

Piping allows you to use the output of one command as the input for another. This is extremely useful for chaining commands together to perform complex operations.

- **Usage**: `command1 | command2`
- **Example**:
  - `ls -l | grep "Jan"`: Lists files modified in January. `ls -l` generates a list, and `grep "Jan"` filters this list to only show files modified in January.
- **Practice**:
  1. **Q**: How would you list all directories and files, then count how many items are there? **A**: `ls -l | wc -l`
  2. **Q**: How would you list all directories and files, then count how many items are there in the given directory level? **A**: `ls -1 | wc -l`

### Redirection

Redirection allows you to direct the input or output of a command to/from a file or another command.

#### Standard Output (`stdout`) and Standard Error (`stderr`)

- **Usage**:
  - Redirecting `stdout` to a file: `command > file`
  - Redirecting `stderr` to a file: `command 2> file`
  - Redirecting both `stdout` and `stderr` to a file: `command > file 2>&1`
- **Examples**:
  - `ls > files.txt`: Saves the output of `ls` to `files.txt`.
  - `grep "text" file.txt 2> errors.log`: Redirects any error messages to `errors.log`.
- **Practice**:
  1. **Q**: How would you save the output of `ls -l` to a file named `list.txt` and error messages to `list-errors.txt`? **A**: `ls -l > list.txt 2> list-errors.txt`

#### Standard Input (`stdin`)

- **Usage**: Redirecting `stdin` from a file: `command < file`
- **Example**:
  - `grep "search text" < file.txt`: Searches for "search text" in `file.txt`.
- **Practice**:
  1. **Q**: How would you use `cat` to display the contents of `file.txt` without directly using `file.txt` as an argument to `cat`? **A**: `cat < file.txt`

> This section on piping and redirection introduces you to powerful tools for command line data manipulation. By mastering these concepts, you can greatly improve your efficiency and effectiveness in shell scripting and command line tasks.
