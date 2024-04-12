# Comprehensive Git Workflow Exercise

## Introduction

This exercise is designed to give hands-on experience with various Git commands through the lifecycle of a project called "MyProject". You will setup your environment, create and manage features, and learn how to handle conflicts and merges.

## 1. Setup

### Initialize Your Project

- **Task**: Set up your Git configuration and initialize your repository.
- **Solution**:

  ```bash
  mkdir MyProject
  cd MyProject
  git init
  
  # Configure user.name and user.email specifically for a single repository
  git config user.name "Your Name"
  git config user.email "your.email@example.com"
  
  # OR configure user.name and user.email globally
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```

  To remove your name and email:

  ```bash
  git config --unset user.name
  git config --unset user.email
  
  # OR remove them globally
  git config --global --unset user.name
  git config --global --unset user.email
  ```

### Create and Commit Initial Files

- **Task**: Create a README.md file with a project description.
- **Solution**:

  ```bash
  echo "# MyProject" > README.md
  echo "This project is about building a responsive web application." >> README.md
  git add README.md
  git commit -m "Initialize project with README"
  ```

### Create a Repository on GitHub, Connect to It, and Push to It

- **Explanation**: GitHub suggests using git branch -M main to rename your current branch to main due to a change in default branch naming conventions. Historically, Git used master as the default name for the initial branch. However, due to concerns about the connotations of the term "master," GitHub and other Git hosting services have moved to use main as the default branch name.
  - `-M` Flag: This flag forces the renaming even if a branch named main already exists. It's a more assertive version of the -m flag, ensuring that the rename operation succeeds.
  - `origin` Flag: This is the default name Git gives to the remote repository from which a project was initially cloned. "Origin" is a shorthand name for the remote repository URL. Using `git push -u main` would result in an error because Git expects you to specify the remote name before the branch unless the remote has been set in a way that defaults can omit the remote name, which is unusual.
  
  ```bash
  git branch -M main
  git remote add origin https://github.com/yourusername/MyProject.git
  git push -u origin main
  ```

## 2. Feature Development and Branch Management

### Start a New Feature

- **Task**: Develop a new feature in a separate branch.
- **Solution**:

  ```bash
  git checkout -B feature-login
  echo "Login Page Code" > login.html
  git add login.html
  git commit -m "Add login page"
  git push -u origin feature-login
  ```

  Compare & Pull Requests on GitHub: Go to the repository you created on GitHub, where you will see the "Compare and Pull Requests" button at the top.

## 3. Handling Team Changes and Conflicts

### Simulate a Team Change and Resolve Conflicts

- **Task**: Update the README.md with setup instructions and simulate a conflict.
- **Solution**:

    Update on main branch:

    ```bash
    git checkout main
    git pull
    echo "\n## Setup Instructions\n1. Clone the repository.\n2. Navigate to the repository directory." >> README.md
    git add README.md
    git commit -m "Add setup instructions"
    ```

    Simulate another team member's conflicting changes:

    ```bash
    git checkout feature-login
    echo "\n## Setup Instructions\n1. Download the repository.\n2. Start the server." >> README.md
    git add README.md
    git commit -m "Update setup instructions"
    git checkout main
    git merge feature-login # After executing this command you should see merge conflicts.
    ```

### 4. How to Merge When Facing Conflicts

- **Explanation**: When Git can't automatically resolve differences in code between commits, it stops the merge and asks you to resolve the conflicts manually.
  - Open the conflicting file and you will see sections marked with `<<<<<<<`, `=======`, and `>>>>>>>`. These markers define the conflicting sections between the two branches.
  - Edit the file to resolve the conflicts. This might involve choosing one side's changes, merging elements from both sides, or making a new change.
  - After editing, save the file and mark the conflict as resolved by staging the file:
  
  ```bash
  # git add <filename>
  git add README.md
  ```

- Finally, complete the merge with a commit:
  
  ```bash
  git commit -m "Resolve merge conflict in README.md"
  git push -u origin main
  ```

## Reviewing Changes and Finalizing

### Review and Merge the Feature

- **Task**: Review changes and merge the feature branch into main.
- **Solution**:

    Create an new index.html in the feature-login branch:

    ```bash
    git checkout feature-login
    touch index.html
    echo "Hello World" > index.html
    git add index.html
    git commit -m "Added an index.html"
    ```

    Review changes and merge them:

    ```bash
    git log --pretty=oneline
    git diff origin/main feature-login
    git checkout main
    git merge feature-login
    ```

### Tagging a Release

- **Task**: Tag the release after merging all features.
- **Solution**:

    ```bash
    git tag -a v1.0 -m "Release version 1.0"
    git push origin main --tags
    ```

- **Explanation**:
  - `git tag -a v1.0 -m "Release version 1.0"`:
    - `git tag`: This command is used to create, list, delete, or verify a tag object signed with GPG in Git. Tags are often used to mark release points (e.g., v1.0, v2.0).
    - `-a v1.0`: The -a flag stands for "annotated tag". Annotated tags are stored as full objects in the Git database. They are checksummed; contain the tagger name, email, and date; have a tagging message; and can be signed and verified with GNU Privacy Guard (GPG). v1.0 is the name of the tag.
    - `-m "Release version 1.0"`: The -m flag specifies a tagging message, which is similar to the message you would provide with a commit. In this case, "Release version 1.0" is the description of the tag, which usually denotes what this release or point in the history represents.
  - `git push origin main --tags`:
    - `--tags`: This flag tells Git to push all of your tags along with the commits they refer to the remote repository. This is useful for sharing your tags with other developers.
  - Why don't we add `-u` in `git push origin main --tags`? The -u flag sets the upstream branch for the branch you're pushing. This is typically used when you first push a new branch to establish a tracking relationship between your local branch and its upstream counterpart, making subsequent pushes (and pulls) simpler because you won’t need to specify the branch again.

## Conclusion

This exercise provides a practical approach to learning Git by simulating a real-world workflow. By completing it, you will gain familiarity with Git commands and scenarios, enhancing your proficiency in version control.
