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