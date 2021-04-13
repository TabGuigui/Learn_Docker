#docker学习日志#
author : TabGui  

docker如何解决应用之间的隔离问题？
- 
（在一个机器上跑程序所需要的环境换一台机器需要重新配置相同环境，这就很麻烦）  
  
通过镜像，将所需要的环境打包成一个镜像，在新的机器上只需要拉取该镜像就可以直接进行开发或者测试（解决环境问题）  

docker底层通过linux containers来实现应用隔离  
linux和docker的区别：![](https://pic2.zhimg.com/v2-a17759859f1e5c8bc9657d641b68fcc1_r.jpg)

docker通过将一整套环境打包成镜像，解决环境带来的各种问题

#今日实例 爬取有道翻译并构建docker#

    import json
	import urllib.request
	import urllib.parse
	
	url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
	
	str_input = input('请输入: ')
	data = {
	    'i' : str_input,
	    'from' : 'auto',
	    'to' : 'auto',
	    'smartresult' : 'dict',
	    'client' : 'fanyideskweb',
	    'salt' : '16057996372935',
	    'sign' : '0965172abb459f8c7a791df4184bf51c',
	    'lts' : '1605799637293',
	    'bv' : 'f7d97c24a497388db1420108e6c3537b',
	    "doctype" : 'json',
	    'version' : '2.1',
	    'kerfrom' : 'fanyi.web',
	    'action' : 'fy_by_reatlme',
	}
	
	
	data = urllib.parse.urlencode(data).encode('utf-8')
	
	response = urllib.request.urlopen(url,data)
	html = response.read().decode('utf-8')
	result = json.loads(html)['translateResult'][0][0]['tgt']
	print('翻译结果是：', result)
代码实现输入英文并爬取有道翻译的结果。

- 构建docker流程：  
-
1 在所要push的代码文件夹中添加库依赖（requirements.txt)和Dockerfile文件内（注意这两个文件的命名必须为此） 

    # 基础镜像
	FROM python:3.6
	# 修改path 即增加/usr/local/bin这个环境变量 
	ENV PATH /usr/local/bin:$PATH
	# 第一个参数. 代表本地路径 /// 第二个参数是虚拟容器中的路径
	ADD . /code 
	# 用上一步建立的路径
	WORKDIR /code
	# 需要下载的库
	RUN pip install -r requirements.txt
	# 运行指令
	CMD python translate.py 
2 在命令行中 输入命令
 
    docker build -t {镜像名} .
此时在docker image中就会有 {镜像名}这样一个镜像  
3 在命令行中 输入命令

    docker run -i {镜像名} # 以交互模式运行容器   
（注意这里**必须要用 -i新开一个交互窗口** ，如果没有-i 在实验的时候，python的input函数会报错，报错内容为"EOFError：EOF when reading a line"，这个报错应该是所进行的程序并作为子进程进行，因此无法从键盘input，**推断如果没有新开一个命令行，那么container就会作为一个子进程进行？**  

4  结果

![](https://github.com/TabGuigui/Learn_Docker/raw/main/img/1.png)
