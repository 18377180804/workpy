# !/usr/bin/python
# -*- coding: UTF-8 -*-
import  re

# inputname="王歌"
# # CHINESE_NAME_REGEXP ="^[\\p{IsHan}\\ue863]+(·[\\p{IsHan}\\ue863]+)*$"
# # CHINESE_NAME_PATTERN = re.compile(r'^[\\p{IsHan}\\ue863]+(·[\\p{IsHan}\\ue863]+)*$')
# # CHINESE_NAME_VALIDATOR = CHINESE_NAME_PATTERN.findall(inputname)
# #
# # m=re.match(CHINESE_NAME_PATTERN, inputname)
# #
# #
# # print(m)

# 定义正则表达式对象（全局变量大写）
# 验证汉字
RE_CHINESE = re.compile(r'^[\u4e00-\u9fa5\u36c3\u4DAE][\u4e00-\u9fa5·\u36c3\u4DAE]{0,30}[\u4e00-\u9fa5\u36c3\u4DAE]$')
RE_CHINESE_START = re.compile(r'^[u4e00-\u9fa5]')
RE_CHINESE_END = re.compile(r'^[u4e00-\u9fa5]$')
RE_CHINESE1 = re.compile(r'^[\u4E00-\u9FA5\uf900-\ufa2d·s]{2,20}$')
ER_SHA256 = re.compile(r'^([0-9a-fA-F]){64}$')
ER_MD5 = re.compile(r'^([0-9a-fA-F]){32}$')


# 定义汉字验证函数
def verify_chinese(name):
    sd = RE_CHINESE.match(name)
    sd_start = RE_CHINESE_START.match(name)
    sd_end = RE_CHINESE_END.findall(name)
    return sd

def is_sha256(uchar,type):
   sha1 = ER_SHA256.match(uchar)
   sha2 = (type==2 or type==4)
   sha3 = len(uchar)==64
   return ER_SHA256.match(uchar) and (type==2 or type==4) and len(uchar)==64

def is_md5(uchar,type):
   md1 = ER_MD5.match(uchar)
   md2 = type==3
   md4 = len(uchar)==32
   return ER_MD5.match(uchar) and type==3 and len(uchar)==32

# 定义密码验证函数
def verify_password(re_pwd,pwd):
    if re_pwd.match(pwd):
        return 'True'
    else:
        return 'False'

# 定义主函数
def main():
    name = '周杰·伦好的·'
    sha256 = 'e72d5256143a1a2dda3b58948c0410bfdfb1ec8b76fa1233e28791ffc73b6792'
    md5 = '20fb3f03aab77abcd744917006e0e978'
    # a = verify_chinese(name)
    b = is_sha256(sha256,2)
    c = is_md5(md5,4)

    strr=str(None)

    if verify_chinese(name):
        print('True')
    else:
        print('Flase')

    pwd = 'Pingan_5200'


# 判断是否终端运行此文件，终端运行为__main__,导入模块为__module__
if __name__ == "__main__":
    main()
