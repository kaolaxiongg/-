import requests
from multiprocessing import Pool


def temp(i):
    url = "https://sohu.com-v-sohu.com/20180830/12209_04e8a79a/800k/hls/9c7a4b3b217%04d.ts" % i
    # 上面%04d为4位数占位符号，，1显示001，将i 传入url里面替换地址
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5702.400 QQBrowser/10.2.1893.400"
    }
    r = requests.get(url, headers=headers)
    #print(r.content)
    with open('./mp4/{}'.format(url[-10:]), 'wb') as f:
        # 在MP4文件夹下面创建文件，将r 里面的二进制文件保存里面。
        f.write(r.content)
        print(url)


if __name__ == '__main__':
    pool = Pool(20)
    # pool 为开20个进程，加快保存速度，多进程保存
    for i in range(1973):  # 完整视频最后的.ts 文件序号。
        pool.apply_async(temp, (i,))

    pool.close()
    pool.join()

# CMD命令进入文件目录下输入 copy /b *.ts abc.mp4   ，把所有文件拼接为一个文件
