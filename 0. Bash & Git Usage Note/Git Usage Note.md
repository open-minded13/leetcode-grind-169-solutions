# Comprehensive Guide to Git Commands

## Introduction

This guide covers commonly used Git commands with explanations, usage, examples, and practice sessions to help users master version control using Git.

## Configuration Commands

### `git config`

- **Purpose:** Configure user information and other options for all local repositories.
- **Usage:** `git config --global user.name "[name]"`, `git config --global user.email "[email address]"`, `git config --global color.ui auto`
- **Example:**`git config --global user.name "Jane Doe"` `git config --global user.email "jane@example.com"`

## Working with Repositories

### `git init`

- **Purpose:** Initialize a new Git repository in your current directory.
- **Usage:** `git init`
- **Example:** `git init`

### `git status`

- **Purpose:** Display the state of the working directory and staging area.
- **Usage:** `git status`
- **Example:** `git status`

### `git add`

- **Purpose:** Add files to the staging area before committing.
- **Usage:** `git add <file>`
- **Example:** `git add README.md`

### `git restore --staged <file>`

- **Purpose:** Unstage files that were previously staged.
- **Usage:** `git restore --staged <file>`
- **Example:** `git restore --staged README.md`

### `git commit`

- **Purpose:** Commit your staged content as a new commit snapshot.
- **Usage:** `git commit -m "Your message"`
- **Example:** `git commit -m "Initial commit"`

## Branching and Merging

### `git branch`

- **Purpose:** List, create, or delete branches.
- **Usage:** `git branch <branch>`
- **Example:** `git branch feature`

### `git checkout -B <branch>`

- **Purpose:** Create a new branch and switch to it in one step.
- **Explanation:** The `-B` option is a combination of `-b` (create new branch) and `--force` (reset an existing branch if it exists, similar to deleting and recreating it).
- **Usage:** `git checkout -B <branch>`
- **Example:** `git checkout -B feature`

### `git push -u origin <branch>`

- **Purpose:** Push the branch to the remote repository and set the upstream tracking.
- **Explanation:** The `-u` option sets the upstream for the branch, which makes future `git pull` or `git push` commands more convenient as they can omit the branch name.
- **Usage:** `git push -u origin <branch>`
- **Example:** `git push -u origin feature`

## Resolving Conflicts

### `git log --merge`

- **Purpose:** List commit logs that are involved in a merge conflict.
- **Usage:** `git log --merge`
- **Example:** `git log --merge`

### `git diff`

- **Purpose:** Show changes between commits, working tree, etc.
- **Usage:** `git diff`, `git diff HEAD <file>`, `git diff <branch1> <branch2>`, `git diff <hash_id1> <hash_id2>`
- **Explanation:** Use `git log --pretty=oneline` to find commit hashes and then compare changes between two specific commits.
- **Example:** `git diff`, `git diff HEAD README.md`, `git diff master feature`, `git diff 9e2ad9b 7a5c2d3`

### `git add <fixed_file>`

- **Purpose:** Mark merge conflicts as resolved by adding the fixed files to the staging area.
- **Usage:** `git add <fixed_file>`
- **Example:** `git add README.md`

### `git commit -m 'fix merge conflicts'`

- **Purpose:** Commit the resolution to a merge conflict.
- **Usage:** `git commit -m 'fix merge conflicts'`
- **Example:** `git commit -m 'fix merge conflicts'`

### `git push -u origin feature2`

- **Purpose:** Push the resolved changes to a specific branch on the remote and set the upstream tracking.
- **Usage:** `git push -u origin feature2`
- **Example:** `git push -u origin feature2`

## Advanced Topics

### `git blame`

- **Purpose:** Show what revision and author last modified each line of a file.
- **Usage:** `git blame <file>`, `git blame -L <num1,num2> <file>`, `git blame -l <file>`
- **Explanation:** The `-l` option changes the display format to include more detailed information. Use `git log -p <hash_id>` to see detailed commit changes for a specific commit.
- **Example:** `git blame README.md`, `git blame -L 1,10 README.md`, `git blame -l README.md`
- **Detailing Commit Changes:** `git log -p 9e2ad9b`

### `git log --pretty=oneline`

- **Purpose:** Simplify the commit logs to a single line each.
- **Usage:** `git log --pretty=oneline`
- **Example:** `git log --pretty=oneline`

## Conclusion

This guide provides a comprehensive understanding of Git commands and best practices for using them effectively. Practice each command to become proficient in managing and collaborating on software projects with Git.
