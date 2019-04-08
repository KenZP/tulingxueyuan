# Django系统
- 环境
  - python3.6
  - Django1.8
- 参考资料
  - django架站的16堂课
# 环境搭建
- anaconda + pycharm
- anaconda使用：
  - conda list：显示当前环境安装包
  - conda env list：显示安装的虚拟环境列表
  - conda create -n evn_name python=3.6
  - 激活conda虚拟环境
    - activate env_name
  - django1.8 安装
    - conda install django=1.8
    
# 后台需要的流程
# 创建第一个django工程
- 命令行启动
    django-admin startproject django01
    cd django01
    python manager.py runserver
# 路由系统-urls
- 创建app
  - app：负责一个具体业务或者一类业务的模块
  - python manager.py startapp teacher
  
- 路由
  - 按照具体的请求url，导入相应的业务处理模块的一个功能
  - django的信息控制中枢
  - 本质上是接受的URL和相应的处理模块的一个映射
  - 在接受URL请求的匹配上使用了RE
  - URL的具体格式如urls.py所示

  
  