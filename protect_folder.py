import os
import sys
import ctypes

def hide_folder(folder_path):
    if os.path.exists(folder_path):
        ctypes.windll.kernel32.SetFileAttributesW(folder_path, 2)
        print(f"文件夹 {folder_path} 已隐藏。")
    else:
        print("文件夹不存在！")

def unhide_folder(folder_path):
    if os.path.exists(folder_path):
        ctypes.windll.kernel32.SetFileAttributesW(folder_path, 0)
        print(f"文件夹 {folder_path} 现在可见。")
    else:
        print("文件夹不存在！")

def protect_folder(folder_path, password):
    stored_password = "secure123"  
    if password == stored_password:
        unhide_folder(folder_path)
    else:
        hide_folder(folder_path)
        print("密码错误，无法访问文件夹！")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("使用方法: python protect_folder.py <文件夹路径> <密码>")
        sys.exit(1)

    folder_path = sys.argv[1]
    password = sys.argv[2]
    protect_folder(folder_path, password)
