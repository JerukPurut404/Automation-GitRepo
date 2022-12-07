import os

repo_dir = input(u'Repo input? ')

branch = input("What's the branch? ") 

message = input("What's the message? ")

def repo_git(repo_dir, branch, message):
    os.chdir(repo_dir)
    print("Change the current working directory to the Git repository.")
    os.system(f"git pull origin {branch}")
    print("Perform a `git pull` to update the local repository.")
    os.system("git add .")
    print("Add all modified and untracked files to the staging area.")
    os.system(f'git commit -m "{message}"')
    print("reate a new commit with the specified message.")
    os.system(f"git push origin {branch}")
    print("ush the commit to the specified branch on the remote repository.") 
def repo_git_no_pull(repo_dir, branch, message):
    os.chdir(repo_dir)
    print("Change the current working directory to the Git repository.")
    os.system(f"git pull origin {branch}")
    print("Perform a `git pull` to update the local repository.")
    os.system("git add .")
    print("Add all modified and untracked files to the staging area.")
    os.system(f'git commit -m "{message}"')
    print("reate a new commit with the specified message.")
    os.system(f"git push origin {branch}")
    print("ush the commit to the specified branch on the remote repository.") 

choice = input("1. Pull included, 2. No Pull: ")
if choice == "1":
    repo_git(repo_dir, branch, message)
if choice == "2":
    repo_git_no_pull(repo_dir, branch, message)

