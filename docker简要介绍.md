#docker platform#
author : TabGui
- 简要介绍 -
-
使用docker可以打包项目并且实现在一个隔离的环境中运行该程序（这种环境可以被称为容器），容器中包括了所有需要运行该程序的组件，所以不需要重新配置所需要的环境。  
使用场景  
1. 不同开发者在本地开发项目，利用docker容器进行共享。  
2. 将项目push到测试环境中，进行自动化测试。  
3. 开发人员发现bug，可以在本地进行debug，并且将修复后的程序部署到测试环境中。  

- docker中不同的角色 -
-
1. docker daemon，docker守护程序：监听所有的api请求并且管理镜像、容器等。  
2. docker clien，docker 可以理解为用户，例如向docker daemon申请使用镜像，docker daemon将从dockerhub中取出相应的。  
3. docker register, docker的注册表，docker hub可以理解为一个公用的注册表，当使用 docker run/ pull指令时，docker daemon会从默认的register中取出相应的镜像， 当使用 docker push指令时，会将创建好的镜像传入默认的register中。  
4. images 镜像， 镜像可以理解成面向对象编程中的类。一个镜像往往基于已存在的镜像，例如4.13构造的有道词典翻译的docker image 是基于 python3.6的镜像，同时构造自己的需要的镜像还要添加一系列指令（例如额外的库，运行指令等），这也就是写Dockerfile（这是docker中比较重要的环节），Dockerfile每行语句可以看作一个layer， 如果要调整image ，可以从某一个layer进行修改，这也就是为什么docker可以快速 轻量化的进行开发。
5. container 容器，容器可以理解成面向对象编程中的实例。 利用Docker API可以创建、运行、删除容器等

-tutorial-
-
    
	docker run -d -p 80:80 docker/getting-started # -d 后台模式运行 -p 80:80 port的映射 本地的80映射到容器的80
这样一个docker容器就被运行起来了，docker的容器其实就是与host所有进程隔离的一个进程，这种隔离需要基于linux系统的kernel namespace和cgroup。  

**从头构建一个镜像和容器**   
[https://github.com/docker/getting-started/tree/master/app](https://github.com/docker/getting-started/tree/master/app)进入该github下git clone到本地，在本地app文件夹中添加Dockerfile如下。  

    FROM node:12-alpine
	RUN apk add --no-cache python g++ make
	WORKDIR /app
	COPY . .
	RUN yarn install --production
	CMD ["node", "src/index.js"]

接下来需要构建镜像：
    
    docker build -t getting-started .
这个. 在docker build命令的末尾，docker应该在当前目录中查找Dockerfile。  
接下来运行一个容器: 在windows命令行中：  
    
    docker run -dp 3000:3000 getting-started

**更新镜像**   
在更新之前，需要把之前的容器移除  
    
    docker ps # 查看运行中的容器
	docker stop <id> # 停止
	docker rm <id> # 移除 
首先需要去源码进行更新  
更新好源码好与之前一样重新build
    
    docker build -t getting-started .
重新build好以后重新run
    
    docker run -dp 3000:3000 getting-started