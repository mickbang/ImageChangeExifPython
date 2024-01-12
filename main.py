# ！/usr/bin/env python3
# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random

from PIL import Image
import os
import piexif
import shutil
import math
from decimal import *

lat = -37.444
lon = 141.152

root_path = "/Users/mickliu/Desktop/stc/GWT659248"

files = ['installer_signature_selfie.png']

times = ['2023:12:14 13:21:27']

# 将所有文件拷贝到after文件夹
def copy_file_to_after(path, output):
    print("========开始复制文件到after文件夹===========")
    if not os.path.exists(output):
        os.mkdir(output)
    for i_path in os.listdir(path):
        # 拼接绝对路径
        if not i_path.split('.')[0] == '':
            full_dir = os.path.join(path, i_path)
            if os.path.isfile(full_dir):
                shutil.copy(full_dir, output)
    print("========复制文件结束===========")


def format_latlng(latlng):
    """经纬度十进制转为分秒"""
    degree = int(latlng)
    res_degree = latlng - degree
    minute = int(res_degree * 60)
    res_minute = res_degree * 60 - minute
    seconds = round(res_minute * 60.0, 3)
    return (degree, 1), (minute, 1), (int(seconds * 1000), 1000)


def correction_exif(path, _dict):
    image = Image.open(path)
    if "exif" in image.info:
        exif_dict = piexif.load(image.info['exif'])
        """原始的exif信息"""
        print("原始的exif信息：" + str(exif_dict))
        # exif_dict['GPS'][piexif.GPSIFD.GPSAltitude] = _dict['alt']  # 修改高度，GPSAltitude是内置变量，不可修改
        exif_dict['GPS'][piexif.GPSIFD.GPSLongitude] = _dict['lng']  # 修改经度
        exif_dict['GPS'][piexif.GPSIFD.GPSLatitude] = _dict['lat']  # 修改纬度
        exif_dict['GPS'][piexif.GPSIFD.GPSLongitudeRef] = _dict['lng_ref']  # odm需要读取，一般为’W'
        exif_dict['GPS'][piexif.GPSIFD.GPSLatitudeRef] = _dict['lat_ref']  # 一般为‘N'
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, path)
        print("修改后的的exif信息：" + str(readExif(path)))
    else:
        print("修改后的的exif信息失败：")


def correction_exif_time(path, time):
    print(path + ":" + time)
    image = Image.open(path)
    exif_dict = piexif.load(image.info['exif'])
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = time  # 修改高度，GPSAltitude是内置变量，不可修改
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, path)


def readExif(path):
    image = Image.open(path)
    exif_dict = piexif.load(image.info['exif'])
    return exif_dict


def change_all(path):
    print("========开始写入经纬度===========")
    for image_path in os.listdir(path):
        full_path = os.path.join(path, image_path)
        _dict = {"lat": format_latlng(random_gps(lat.__abs__())),
                 "lat_ref": "N" if lat > 0 else "S",
                 "lng": format_latlng(random_gps(lon.__abs__())),
                 "lng_ref": "E" if lon > 0 else "W"}
        correction_exif(full_path, _dict)
    print("========写入经纬度完成===========")

def change_all_sameSimple(path):
    print("========开始写入经纬度===========")
    lat2 = -31.9028819
    lon2 = 115.8371682
    lat1 = lat2.__abs__()
    lon1 = lon2.__abs__()
    for image_path in os.listdir(path):
        full_path = os.path.join(path, image_path)
        _dict = {"lat": format_latlng(lat1),
                 "lat_ref": "N" if lat2 > 0 else "S",
                 "lng": format_latlng(lon1),
                 "lng_ref": "E" if lon2 > 0 else "W"}
        correction_exif(full_path, _dict)
    print("========写入经纬度完成===========")

#没有7位小数的补足7位小数
def random_gps(input_gps):
    gps_digsts = str(input_gps).split('.')
    point_len = len(gps_digsts[len(gps_digsts)-1])
    max_point = 7
    if(point_len>=max_point):
        return float(input_gps)
    else:
        n = max_point-point_len
        last = Decimal(Decimal(random.randint(10**(n-1), 10**n-1))*Decimal(math.pow(0.1, max_point))).quantize(Decimal('0.0000000'))
        result = float(Decimal(last+Decimal(input_gps)).quantize(Decimal('0.0000000')))
        return result
-31.90
def correction_exif_location_random(path,lat,lon):
        _dict = {"lat": format_latlng(random_gps(lat.__abs__())),
                 "lat_ref": "N" if lat > 0 else "S",
                 "lng": format_latlng(random_gps(lon.__abs__())),
                 "lng_ref": "E" if lon > 0 else "W"}
        correction_exif(path, _dict)

def change_time_path(path):
    if(os.path.isdir):
        after_path = path+"/after"
        if not os.path.exists(after_path):
            copy_file_to_after(path, after_path)
        image_paths = os.listdir(after_path)
        sorted_files = sorted(image_paths, key=lambda x: os.path.getmtime(os.path.join(after_path, x)),reverse=True)
        for file in sorted_files:
            print(file)
        print('Input time arrays(eg.2023:12:14 13:21:27|2023:12:14 13:21:27) sort must match up print files')
        time = input('Please input time arrays(use | split):')
        times = [str(s) for s in time.split('|')]
        if len(times) != len(sorted_files):
            print('length of time is ',len(times),'not equal to length of file ',len(sorted_files))
        else:
            for index,file in enumerate(sorted_files):
                correction_exif_time(path=os.path.join(after_path,file),time=times[index])        
    else:
        new_time = input('input time(eg.2023:12:14 13:21:27):')
        correction_exif_time(path=path,time=new_time)
    print('---------------------------change time success------------------------------------')
    

def change_location(path):
    if(os.path.isdir):
        after_path = path+"/after"
        if not os.path.exists(after_path):
            copy_file_to_after(path, after_path)
        image_paths = os.listdir(after_path)
        sorted_files = sorted(image_paths, key=lambda x: os.path.getmtime(os.path.join(after_path, x)),reverse=True)
        for file in sorted_files:
            print(file)
        print('Input time arrays(eg.lat lon|lat lon) sort must match up print files')
        print('eg.-37.444 141.152')
        location = input('Please input location arrays(use | split):')
        locations = [str(s) for s in location.split('|')]
        if len(locations)!=1 and len(locations) != len(sorted_files):
            print('length of time is not equal to length of file')
        else:
            for index,file in enumerate(sorted_files):
                if(len(locations) == 1):
                    locations1 = locations[0].split()
                    lat = float(locations1[0])
                    lng = float(locations1[1])
                    correction_exif_location_random(path=os.path.join(after_path,file),lat=lat,lon=lng)   
                else:
                    locations1 = locations[index].split()
                    lat = float(locations1[0])
                    lng = float(locations1[1])
                    correction_exif_location_random(path=os.path.join(after_path,file),lat=lat,lon=lng)        
    else:
        print('eg.-37.444 141.152')
        geo_location = input('input location(eg.lat lon):')
        locations = geo_location.split()
        lat = float(locations[0])
        lng = float(locations[1])
        correction_exif_location_random(path=path,lat=lat,lon=lng)
    print('---------------------------change location success------------------------------------')

if __name__ == '__main__':
    default_path = '/Users/mickliu/Desktop/stc'
    print('---------------------------start------------------------------------')
    print('Please select action:')
    print('1.Change geo time in gwt dir. ',default_path)
    print('2.Change geo location random in gwt dir. ',default_path)
    print('3.Change geo time custom dir.')
    print('4.Change geo location random custom dir.')
    action = input('Action:')
    if (action == '1'):
        print('---------------------------start change time------------------------------------')
        gwt = input('Please type gwt:').replace('\'','')
        path = os.path.join(default_path,gwt)
        change_time_path(path)
    elif ('2' == action):
        print('---------------------------start change location------------------------------------')
        gwt = input('Please type gwt:').replace('\'','')
        path = os.path.join(default_path,gwt)
        change_location(path)
    elif ('3' == action):
        print('---------------------------start change time------------------------------------')
        path = input('Please type file or dir:').replace('\'','')
        change_time_path(path=path)
    elif ('4' == action):
        print('---------------------------start change location------------------------------------')
        path = input('Please type file or dir:').replace('\'','')
        change_location(path=path)
    else:
        print('action not define')