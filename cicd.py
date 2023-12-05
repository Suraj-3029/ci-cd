
import git
import os
import subprocess

# Define the repository path
repo_path = "D:\Work\//vired\ci-cd"
path=f"D:\Work\//vired\ci-cd\cicd.py"

# Define the branch to deploy
branch_to_deploy = "main"

def pull_changes():
    # Pull the latest changes from the repository
    print(repo_path)
    repo = git.Repo(repo_path)
    origin = repo.remote()
    origin.pull()
    print("Changes pulled successfully")

def check_for_new_commits():
    # Check if there are any new commits on the branch
    repo = git.Repo(repo_path)
    origin = repo.remote()
    origin.fetch()
    commits_behind = list(repo.iter_commits(f"HEAD..origin/{branch_to_deploy}"))
    return commits_behind

def main():
    # Check for new commits
    commits_behind = check_for_new_commits()
    if len(commits_behind) == 0:
        print("No new commits found. Skipping deployment.")
        return

    # Check if the specified branch is the latest
    repo = git.Repo(repo_path)
    current_branch = repo.active_branch.name
    if current_branch != branch_to_deploy:
        print(f"Skipping deployment as current branch is {current_branch}, not {branch_to_deploy}")
        return

    # Pull the latest changes from the repository
    pull_changes()

if __name__ == "__main__":
    main()