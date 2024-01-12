import os
import shutil

def tidyFile(path):
    path_root_head = path + '/mipmap-'
    android_dirs = ['hdpi','xhdpi','xxhdpi','xxxhdpi']
    for android_dir in android_dirs:
        res_dir = path_root_head+android_dir
        if(os.path.exists(res_dir) != True):
            os.makedirs(res_dir)
                    
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path,file)
        if (os.path.isfile(file_path)):
            if(file_path.__contains__('@1.5x')):
                shutil.move(file_path,path_root_head+android_dirs[0])
            if(file_path.__contains__('@2x')):
                shutil.move(file_path,path_root_head+android_dirs[1])
            if(file_path.__contains__('@3x')):
                shutil.move(file_path,path_root_head+android_dirs[2])
            if(file_path.__contains__('@4x')):
                shutil.move(file_path,path_root_head+android_dirs[3])
            print(file_path)



if __name__ == '__main__':
    image_path = input('请输入figma到处的倍图路径：').replace('\\','',100)

    print('input输入路径='+image_path)
    print('========================开始处理=========================')
    tidyFile(image_path)
    print('========================开始处理=========================')