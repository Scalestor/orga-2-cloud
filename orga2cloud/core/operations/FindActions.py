import os

"""
Basically, find the action in the action folder


"""

action_repositories = ["C:\\Users\malte\PycharmProjects\orga-2-cloud\orga2cloud\\actions"]



def operation_find_action(name):

    found_files = []
    for repo in action_repositories:
        files =  os.listdir(repo)
        if name+".py" in files:
            print(f"Found action {name} in repository {repo}")
            return os.path.join(repo,name+".py")
