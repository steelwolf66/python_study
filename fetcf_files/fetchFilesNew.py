import os
import pymysql
import paramiko
from scp import SCPClient
import sys
import time
import socket
import logging

# 设置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def get_user_input():
    return input("请输入档案号,用逗号（英文,）分隔: ")

# 连接配置信息
config = {
    'user': 'root',
    'password': 'taxBook@2021',
    'host': '192.168.1.106',
    'port': 3308,
    'database': 'zzdb',
    'charset': 'utf8mb4',
    'connect_timeout': 10,
}

def connect_to_database(max_attempts=3):
    for attempt in range(max_attempts):
        try:
            logger.info(f"尝试连接数据库... 第 {attempt + 1} 次")
            # 尝试创建连接
            conn = pymysql.connect(**config)
            logger.info("数据库连接成功！")
            return conn
        except pymysql.Error as err:
            logger.error(f"MySQL 错误: {err}")
        except Exception as e:
            logger.error(f"发生未知错误: {str(e)}")
            logger.error(f"错误类型: {type(e)}")
        
        if attempt < max_attempts - 1:
            logger.info("等待 5 秒后重试...")
            time.sleep(5)
        else:
            logger.error("达到最大重试次数")
            return None

def main():
    try:
        logger.info("程序开始执行")
        user_input = get_user_input()
        logger.info(f"用户输入: {user_input}")
        
        fileIds = user_input.split(',')
        logger.info(f"解析的档案号: {fileIds}")
        
        for itemId in fileIds:
            logger.info(f"\n处理档案号: {itemId}")
            
            # 连接数据库
            conn = connect_to_database()
            if not conn:
                logger.error("无法建立数据库连接，程序退出")
                sys.exit(1)
            
            cursor = conn.cursor()
            
            try:
                # 执行SQL查询
                query = """SELECT filename 
                          FROM lose_mod_file f 
                          INNER JOIN lose l ON l.id = f.loseid 
                          WHERE l.zongxuhao = %s"""
                logger.info(f"执行查询: {query} with {itemId}")
                cursor.execute(query, (itemId,))
                results = cursor.fetchall()
                
                if not results:
                    logger.info(f"未找到档案号 {itemId} 的相关文件")
                    continue

                logger.info(f"找到 {len(results)} 个文件")

                # 服务器连接配置
                linux_hostname = '192.168.1.109'
                linux_port = 22
                linux_username = 'root'
                linux_password = 'dazu123.com'

                # 创建SSH客户端
                logger.info("正在连接远程服务器...")
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                try:
                    ssh.connect(
                        linux_hostname, 
                        linux_port, 
                        linux_username, 
                        linux_password,
                        timeout=10
                    )
                    logger.info("远程服务器连接成功")

                    source_path = '/dazu/www/zssite/uptownfile'
                    target_path = f'/target-dir/{itemId}'

                    # 确保目标目录存在
                    if not os.path.exists(target_path):
                        os.makedirs(target_path)
                        logger.info(f"创建目标目录: {target_path}")

                    # 创建SCP客户端
                    with SCPClient(ssh.get_transport()) as scp:
                        logger.info('开始复制文件...')
                        for file_tuple in results:
                            file_name = file_tuple[0]
                            source_file = f'{source_path}/{file_name}'
                            target_file = f'{target_path}/{file_name}'
                            try:
                                scp.get(source_file, target_file)
                                logger.info(f'已成功复制: {file_name}')
                            except Exception as e:
                                logger.error(f'复制失败 {file_name}: {str(e)}')

                except paramiko.SSHException as ssh_err:
                    logger.error(f"SSH连接错误: {ssh_err}")
                except Exception as e:
                    logger.error(f"文件传输错误: {e}")
                finally:
                    ssh.close()
                    logger.info("SSH连接已关闭")

            finally:
                cursor.close()
                conn.close()
                logger.info("数据库连接已关闭")

        logger.info(f"\n所有文件处理完成，档案号：{user_input}")

    except Exception as e:
        logger.error(f"程序执行出错: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()