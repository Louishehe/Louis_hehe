import os
import hashlib
import base64
import time
 
 
def mine():
 
    print("-------------------------------------批量加密工具-------------------------------------")
    print("使用告知：\n【加密后的文件后缀会多出AI，是为了方便软件检测，请勿乱改加密后的后缀名】")
    print("【要加密或解密的文件命名不可有“./\”字符，否则会出错】")
    print("【此程序的密码可以使用中文、英文、字符串、数字进行加密，可使用中文和中文字符串】")
    print("【重点要注意：：程序一旦开始加密或解密，中途不可退出，否则会丢失数据，直到运行完毕方可退出】")
    print("-------------------------------------批量加密工具-------------------------------------\n")
    DATA_1 = input('请输入要加密或解密的文件路径(不含文件)：')
    if DATA_1 == '':
        print('程序不得为空，请重新输入！！！')
        time.sleep(2)
        os.system('cls')
        mine()
    else:
        pass
 
    DATA_1 = DATA_1.replace("\\", "/")  # 替换
    if os.path.isdir(DATA_1) == True:
        pass
    else:
        print('路径错误或文件夹不存在，请重新输入！！！')
        time.sleep(2)
        os.system('cls')
        mine()
 
    str = input('请输入最高可加密的内存MB：')
    # 判断是否填写
    if int(str) == '':
        print('错误，请重新输入！！！')
        time.sleep(2)
        os.system('cls')
        mine()
    else:
        pass
 
    PassWord_1 = input('请输入要加密或解密的密码(密码)：')
    # 判断是否填写
    if PassWord_1 == '':
        print('密码不得为空，请重新输入！！！')
        time.sleep(2)
        os.system('cls')
        mine()
    else:
        pass
 
 
    def iterbrowse(path):
        for home, dirs, files in os.walk(path):
            for filename in files:
                yield os.path.join(home, filename)
 
 
    for fullname in iterbrowse(DATA_1):
        NAME = fullname
        NAME = NAME.replace("\\", "/")  # 替换
 
        def get_FileSize(filePath):
            fsize = os.path.getsize(filePath)
            fsize = fsize / float(1024 * 1024)
            size = "%.0f" % fsize
            if int(size) >= int(str):
                print('[-!-]: ',NAME, '\t- - - - 内存过大！！！')
                pass
            else:
                #写入的文件
                if NAME.split(".")[-1][-10:] == 'DATAAES-AI':  # 检测是否是已经加密后的文件，用于检测后缀的DATAAES-AI
                    #解密
                    F = NAME.split(os.path.sep)[0].replace("AI", "")  #去除DATAAES-AI
                    print(f'[-.·J·.-]: ',NAME, '\t- - - - 解密成功！！！')
                else:
                    #加密
                    F = NAME.split(os.path.sep)[0]+"AI"
                    print(f'[+·J·+]: ', NAME, '\t+ + + + 加密成功！！！')
 
 
 
 
                a = open(NAME, "rb")  #读取文件
                b = open(F, "wb")    #写入文件
 
 
 
                #使用MD5进行加密(双层加密）
                hl = hashlib.md5()
                hl.update(PassWord_1.encode(encoding='utf-8'))
                password_list = hl.hexdigest()
                #使用MD5进行加密(双层加密）
                hl.update(password_list.encode(encoding='utf-8'))
                password_list2 = hl.hexdigest()
                password_data = password_list+password_list2
 
 
                #加密
                def Encryption_and_decryption():
                    count = 0  #索引
                    for now in a:
                        for nowByte in now:
                            newByte = nowByte ^ ord(password_data[count % len(password_data)])  #循环遍历出密码的ord值，单个循环
                            count += 1
                            b.write(bytes([newByte]))   #转换
                Encryption_and_decryption()
 
 
 
                a.close()
                b.close()
                os.remove(f'{NAME}')
        get_FileSize(NAME)
    print('操作完成！！！')
    print('正在返回！！！')
    time.sleep(2)
    os.system('cls')
    mine()
mine()
