##### 项目简介：  
             operation2.0版本的接口自动化测试脚本，分离测试数据和脚本，生成allure报告  
  
###### 安装要求
* 安装pycharm  
* 安装pytest库   
* 安装依赖包：requests allure yaml  
安装步骤  
* pip安装：pip install -U pytest
* setting直接安装或者pip install requests、yaml等

##### 目录结构：   
                 config：配置管理，存放环境、数据库连接等配置信息  
                 data：yaml格式的接口参数  
                 tests：存放case  
                 utils：存放读取测试数据函数  
                 report：执行生成报告命令后自动生成的目录，分别存放html和result  
                 pytest.ini：配置文件，主要作用改变pytest的默认行为  
###### 重点记录：  
         参数化装饰器：@pytest.mark.parametrize，自动对list解包并赋值给装饰器的第一参数  
         fixture机制：@pytest.fixture，利用它提前读取配置信息  
         
![allure报告](https://github.com/zzhoulin/OP/blob/main/B3495A8F-7810-40c4-868D-76C7D5474829.png)
