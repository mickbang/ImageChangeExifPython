import os
import re
#<a class="fancybox img-item-view" rel="sn_photo_view" title="111" href="https://s3-ap-southeast-2.amazonaws.com/greendeals3test/uploads/pvd_serial_number/photo/5666206/WX20230110-160918_2x.bmp">

if __name__ == '__main__':
    html = open('job.html','r').readlines()
    regex_pattener =  r"<a class=\"fancybox img-item-view\" rel=\"sn_photo_view\" title=\"[(\d|\w)]*\" href=\"[(\d|\w):/\.-]*\">"
    matchs = re.findall(regex_pattener,str(html))
    image_url_pattener = r"https://[(\d|\w)/\.-]+"
    for match in matchs:
        url_matchs = re.findall(image_url_pattener,str(match))
        for url_match in url_matchs:
            print(url_match)

    # regex = regex_pattener
    # test_str = str(html)
    # matches = re.finditer(regex, test_str, re.MULTILINE)
    # for matchNum, match in enumerate(matches, start=1):
    #     print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    #     for groupNum in range(0, len(match.groups())):
    #         groupNum = groupNum + 1
    #         print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
