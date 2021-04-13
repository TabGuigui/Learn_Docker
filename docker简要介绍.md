#docker platform#
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

