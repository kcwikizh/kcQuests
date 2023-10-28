import os

from src.__main__ import run

if __name__ == '__main__':
    root_path = os.path.dirname(__file__)
    print(root_path)
    run(root_path)
