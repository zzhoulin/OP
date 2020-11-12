##### 项目简介：  
             operation2.0版本的接口自动化测试脚本，分离测试数据和脚本，生成allure报告  
  
###### 安装要求
* 安装pycharm  
* 安装pytest库   
* 安装依赖包：requests allure yaml  
###### 安装步骤  
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
           
         allure几个特性  
         @allure.feature # 用于描述被测试产品需求  
         @allure.story # 用于描述feature的用户场景，即测试需求  
         with allure.step # 用于描述测试步骤，将会输出到报告中  
         allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据，截图等  
         @pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤   
         生成报告命令：py.test test/ --alluredir ./result/                      ./result/中保存了本次测试的结果数据  
                      allure generate ./result/ -o ./report/ --clean          –clean选项目的是先清空测试报告目录，再生成新的测试报告  
         
![allure报告](https://github.com/zzhoulin/OP/blob/main/B3495A8F-7810-40c4-868D-76C7D5474829.png)
