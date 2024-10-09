import os

import mysql.connector
import paramiko
from scp import SCPClient


def get_user_input():
    return input("请输入档案号,用逗号（英文,）分隔: ")


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
    user_input = get_user_input()
    fileIds = user_input.split(',')
    for itemId in fileIds:
        conn = mysql.connector.connect(**config)
        # 创建游标对象
        cursor = conn.cursor()
        # 执行SQL查询 并 拼接参数
        query = "SELECT filename FROM lose_mod_file f inner join lose l on l.id = f.loseid " \
                "where l.zongxuhao = %s "
        cursor.execute(query, (itemId,))
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
        source_path1 = '/dazu/www/zssite/uptownfile-bak'
        source_path2 = '/dazu/www/zssite/uptownfile'
        target_path = '/target-dir/' + itemId

        # 确保目标目录存在
        if not os.path.exists(target_path):
            os.makedirs(target_path)

        # 创建SCP客户端
        scp = SCPClient(ssh.get_transport())
        print('*' * 40)
        failedFileNames = ''
        # 复制文件
        for file_tuple in results:
            file_name = file_tuple[0]
            source_file1 = f'{source_path1}/{file_name}'
            target_file = f'{target_path}/{file_name}'
            try:
                scp.get(source_file1, target_file)
                print(f'已拷贝文件：{file_name}')
                # 复制文件异常时，收集没有找到的文件名，到另外一个目录查询
            except Exception as e:
                failedFileNames = failedFileNames + file_name + '@@'


        # 尝试从第二个目录中获取数据
        if len(failedFileNames) > 1:
            failedFileNameList = failedFileNames.split('@@')
            for itemFailedFileName in failedFileNameList:
                # 剔除文件格式有误的文件
                if '.' not in itemFailedFileName:
                    continue
                source_file2 = f'{source_path2}/{itemFailedFileName}'
                target_file = f'{target_path}/{itemFailedFileName}'
                try:
                    scp.get(source_file2, target_file)
                    print(f'已拷贝文件：{itemFailedFileName}')
                except Exception as e:
                    print(f'****** 未找到文件 ******：{itemFailedFileName}')
        print(f'文件下载完成,目录：{target_path}')
        # 关闭连接
        scp.close()
        ssh.close()
    print(f"文件均下载完成，档案号：{user_input}")
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # 关闭游标和连接
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
