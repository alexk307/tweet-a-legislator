from git import Repo
from shutil import rmtree
from sys import exit


DATA_DIR = './data'


def _clear_data():
    rmtree(DATA_DIR, ignore_errors=True)


def clone():
    _clear_data()
    print 'Cloning congress-legislators...'
    try:
        Repo.clone_from(
            'git@github.com:unitedstates/congress-legislators.git', DATA_DIR
        )
    except:
        print 'Unable to clone `congress-legislators`. Exiting...'
        exit()
    print 'Done'


if __name__ == '__main__':
    clone()