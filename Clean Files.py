import os
import shutil


def organize_files(d):
    # 获取目录下的所有文件
    files = os.listdir(d)

    for file in files:
        # 忽略文件夹
        if os.path.isdir(file):
            continue

        # 获取文件的扩展名
        _, ext = os.path.splitext(file)

        # 根据扩展名创建对应的文件夹
        folder = os.path.join(d, ext[1:])
        if not os.path.exists(folder):
            os.makedirs(folder)

        # 移动文件到对应的文件夹
        shutil.move(os.path.join(d, file), os.path.join(folder, file))

    print("文件整理完成！")
    print("finish cleaning!")


# 指定要整理的目录
directory = "C:/"
organize_files(directory)
