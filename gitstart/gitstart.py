#!/usr/bin/python3

"""
Automates the process of:
    - Creating a remote GitHub repo.
    - Initializing a local repo.
    - Connecting the local repo to the remote repo.
    - Pushing the init commit to the remote repo.
"""

from github import Github
import platform
import os
import sys


# Handle the Error Messege
def error(msg):
    os.system('')
    print('\u001b[31m' + msg + '\u001b[0m')
    sys.exit()


# Check if There is a local Repo with the Same Name
def isLocal(cwdPath):
    gitDir = os.path.join(cwdPath, '.git')
    return {'status': os.path.exists(gitDir), 'gitDirPath': gitDir}


# Check if There is a Remote Repo with the Same Name
def isRemote(repoName, gitRepos):
    try:
        for repo in gitRepos:
            if repo.name == repoName:
                return {'status': True, 'repoPath': repo.full_name}
        return {'status': False, 'repoPath': ''}
    except Exception as e:
        print(e)
        error('Access denied!')


def getToken():
    token = os.environ.get('GIT_TOKEN', None)
    if not token:
        error('Can not read the token')
    return token


# Set the Variables
repoName = None
if platform.system() == 'Windows':
    repoName = os.getcwd().split('\\')[-1]
else:
    repoName = os.getcwd().split('/')[-1]
isPrivate = False
initCommitMsg = 'init commit'
cwdPath = os.getcwd()
token = getToken()


# Check Default Varibale
repoNameInp = input(f'> Remote repo name [{repoName}]: ')
if repoNameInp.lower() != '':
    repoName = repoNameInp


while True:
    isPublicInp = input('> Public repo (yes/no) [yes]: ')
    if isPublicInp.lower() in ['yes', 'y', '']: break
    elif isPublicInp.lower() in ['no', 'n']:
        isPrivate = True
        break


initCommitMsgInp = input('> Init commit msg [init commit]: ')
if initCommitMsgInp.lower() != '':
    initCommitMsg = initCommitMsgInp


# Connect to the GitHub repo
githubCon = Github(token)
gitUser = githubCon.get_user()
gitRepos = gitUser.get_repos()
username = gitUser.login


# Check if the Repo is Already Exist
localOut = isLocal(cwdPath)
remoteOut = isRemote(repoName, gitRepos)
localStatus, remoteStatus = localOut['status'], remoteOut['status']
localPath, remotePath = localOut['gitDirPath'], remoteOut['repoPath']
if localStatus or remoteStatus:
    if localStatus and remoteStatus:
        msg = f'{localPath} is already exist!\n{remotePath} is already exist!'
    elif localStatus:
        msg = f'{localPath} is already exist!'
    else:
        msg = f'{remotePath} is already exist!'
    error(msg)


# Create the Remote Repo
gitRepo = gitUser.create_repo(repoName, private=isPrivate, auto_init=False)


# Create the Local Repo
os.chdir(cwdPath)
if not os.path.exists('README.md'):
    os.system(f'echo "# {repoName}" >> README.md')
os.system('git init')
os.system('git add README.md')
os.system(f'git commit -m "{initCommitMsg}"')
os.system('git branch -M main')


# Conect the local repo to the remote repo
os.system(f'git remote add origin https://github.com/{username}/{repoName}.git')


# Push the init commit to the remote repo
os.system(f'git push -u origin main')


print('\u001b[32m' + 'All done!' + '\u001b[0m')
