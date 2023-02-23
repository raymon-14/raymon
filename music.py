import os

# 读取用户名信息
with open('usernames.txt') as f:
    for username in f:
        username = username.strip()
        
        # 删除用户
        os.system(f'userdel -r {username}')