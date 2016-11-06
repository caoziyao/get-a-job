# get-a-job
找工作啦——在地图上找工作
---------------
[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)
[![platform](https://img.shields.io/badge/python-3.4-green.svg)]()

- 指定过滤条件抓取Lagou网的职位
- 调用百度地图API获取职位地理位置
- 所获信息存入sqlite数据库中
- 使用Flask提供web前端

支持浏览器：IE 11, Chrome, FireFox, Safari

* 主页：[https://github.com/caoziyao/get-a-job](https://github.com/caoziyao/get-a-job)
* 联系邮箱：wyzycao@gmail.com

界面清新
![platform](https://github.com/caoziyao/get-a-job/blob/master/static/img/2.PNG)  
![platform](https://github.com/caoziyao/get-a-job/blob/master/static/img/1.PNG)  

安装
----------
后台基于flask开发，可以用Python环境直接运行。
1. pip环境下安装在static下的package
 pip install -r requirements.txt
2. python app.py server
3. 访问 http://localhost:3000/

TODO
----
1. 搜索功能
2. 添加其他地图功能
3. 


License
--------
自用的小工具，欢迎提出意见，期待进一步改善
MIT

