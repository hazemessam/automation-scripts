#!/usr/bin/python3
from github import Github
import platform
import os
import sys


TOKEN_PATH = '/home/hazem/data/.gitoken'


# Handle the Error Messege
def error(msg):
    os.system('')
    print('\u001b[31m' + msg + '\u001b[0m')
    sys.exit()

# Check if There is a local Repo with the Same Name
def isLocal(cwdPath):
    gitDir =  os.path.join(cwdPath, '.git')
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
    try:
        with open(TOKEN_PATH) as target:
            return target.read().strip()
    except:
        error('Can not read the token')

# Set the Variables
repoName = None;
if platform.system() == 'Windows':
    repoName = os.getcwd().split('\\')[-1]
else:
    repoName = os.getcwd().split('/')[-1]
isPrivate = False
initCommitMsg = 'init commit'
cwdPath = os.getcwd()
token = getToken() 


# Check Default Varibale
repoNameInp = input('> Enter repo name (default: {0}): '.format(repoName))
if repoNameInp.lower() != '':
    repoName = repoNameInp
while True:
    isPrivateInp = input('> Is it a private repo (y/n) (default: public): ')
    if isPrivateInp.lower() == 'y': 
        isPrivate = True
        break
    elif isPrivateInp.lower() == 'n' or isPrivateInp == '':
        break
initCommitMsgInp = input('> Enter initial commit msg (default: init commit): ')
if initCommitMsgInp.lower() != '':
    initCommitMsg = initCommitMsgInp


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
        msg = f'{localPath} is already exist!\n{remotePath} was already exist!'
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
    os.system(f'echo # {repoName} >> README.md')
os.system('git init')
os.system('git add .')
os.system(f'git commit -m "{initCommitMsg}"')
os.system(f'git remote add origin https://github.com/{username}/{repoName}.git')
os.system(f'git push origin master')
print('\u001b[32m' + 'All done!' + '\u001b[0m')
