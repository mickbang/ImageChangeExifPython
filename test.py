import os
import re

current_version_file = 'config.gradle'

def current_version(version_file):
    version_current = None
    version_parttern = r'            versionName      : "(\d+\.\d+\.\d+)",'
    f = open(version_file)
    lines = f.readlines()
    f.close

    for line in lines:
        line_str = str(line)
        print(line_str)
        match1 = re.match(version_parttern, line_str)
        if match1:
            version_current = match1.group(1)
    return version_current

def increase_version(version):
    nums = version.split(".")
    nums[len(nums) - 1] = str(int(nums[len(nums) - 1]) + 1)
    return '.'.join(str(x) for x in nums)

def update_version(versionFile, versionCurrent, versionLast):
    currentText = '            versionName      : "%s",' % versionCurrent
    lastText = '            versionName      : "%s",' % versionLast
    replace_file(versionFile, currentText, lastText)

def replace_file(filePath, fromStr, toStr):
    content = ""
    f1 = open(filePath, "rb")
    for line in f1:
        strline = line.decode('utf8')
        if fromStr in strline:
            content += strline.replace(fromStr, toStr)
        else:
            content += strline
    f1.close()
    f2 = open(filePath, "wb")
    f2.write(content.encode('utf8'))
    f2.close()

if __name__=='__main__':
    current_version1 = current_version(current_version_file)
    print(current_version1)
    last = increase_version(current_version1)
    print(last)

    update_version(current_version_file,current_version1,last)
