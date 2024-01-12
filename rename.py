import os

if __name__ == '__main__':
    rootPath = '/Users/mickliu/Downloads/mipmap-xxxhdpi'
    list_path = os.listdir(rootPath)
    for index in list_path:
        name = index.split('.')[0]
        kid = index.split('.')[-1]
        filename = rootPath + '/' + index
        new_path = rootPath + '/' +"weather_ic_"+name + '.' + kid
        os.rename(filename, new_path)

    print('Success!')
