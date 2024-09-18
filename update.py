import os
from datetime import datetime 

def update():
    os.system("git add .")
    now = datetime.now()
    date_time_string = now.strftime("%Y-%m-%d %H:%M:%S")
    command = f'git commit -m "{date_time_string}"'
    os.system(command)
    os.system("git push https://github.com/jack-frings/Benchball")

if __name__ == "__main__":
    update()

