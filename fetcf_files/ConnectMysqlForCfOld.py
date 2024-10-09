import os

import mysql.connector
import paramiko
from scp import SCPClient

def get_user_input():
    return input("请输入档案号: ")

# 连接配置信息
config = {
    'user': 'root',  # 你的MySQL用户名
    'password': 'taxBook@2021',  # 你的MySQL密码
    'host': '192.168.1.106',  # 数据库服务器地址
    'port': 3308,  # 端口
    'database': 'zzdb',  # 数据库名
    'raise_on_warnings': True
}

# 建立连接
try:
    # user_input = 'HEB1700356'
    user_input = get_user_input()
    conn = mysql.connector.connect(**config)

    # 创建游标对象
    cursor = conn.cursor()

    # 执行SQL查询 并 拼接参数
    query = "SELECT filename FROM lose_mod_file f inner join lose l on l.id = f.loseid " \
            "where l.zongxuhao = %s "
    cursor.execute(query, (user_input,))

    # 获取查询结果
    results = cursor.fetchall()
    # 打印查询结果
    for result in results:
        print(result)

    # 服务器连接配置
    linux_hostname = '192.168.1.109'
    linux_port = 22
    linux_username = 'root'
    linux_password = 'dazu123.com'

    # 创建SSH客户端
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接到服务器
    ssh.connect(linux_hostname, linux_port, linux_username, linux_password)

    # 目标文件夹路径
    source_path = '/dazu/www/zssite/uptownfile-bak'
    target_path = '/target-dir/'+user_input

    # 确保目标目录存在
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    # 创建SCP客户端
    scp = SCPClient(ssh.get_transport())

    # 复制文件
    for file_tuple in results:
        file_name = file_tuple[0]
        source_file = f'{source_path}/{file_name}'
        target_file = f'{target_path}/{file_name}'
        print(f'Copying {source_file} to {target_file}')
        scp.get(source_file, target_file)

    print('文件下载完成')
    # 关闭连接
    scp.close()
    ssh.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # 关闭游标和连接
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
