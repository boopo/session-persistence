<h2>Session 持久化中心</h2>

此项目实现了某门户,某系统,某书馆,某卡通的四种session的持久化处理，~~因为一些不可说的原因并不能直接开源~~

由某小助的持久化层分离而来,方便后期做微服务以及水平扩容

具体实现思想为CAU(check and update) ~~我编的~~

性能参考



| URL  | 冷加载(ms) | 热加载(ms)    |
|-------|:---:|-----------|
| 某融合门户  | 1000 | 300     | 
| 某教务系统 | 2000  | 100      | 
| 某图书馆  | 1000   | 200 |
| 某一卡通  | 6000   | 500 |



运行方法
    
Linux:

      Dcoker 一键部署:
           docker build -t session-kxz:1.0 .
           docker run -p 12001:22222 -d -it cumt-kxz:1.0  --restrat=always
      
      直接部署：
           使用gunicorn
           pip insall -r requirements.txt
           gunicorn -w 4 -b 127.0.0.1:22222 manage:app    //w为线程数 b 指定端口
           
           使用Tornado
           pip insall -r requirements.txt
           python tornado_server.py
Windows：

           pip insall -r requirements.txt
           python tornado_server_win.py    
           
Apidoc生成：

       npm install apidoc
       apidoc -i src/ -o apidoc/
 因为前几天发现除了某系统和某图书馆别的都不需要内网环境，所以为了保证服务的高可用，可以将此项目重新拆分，一部分部署在serverless上，一部分放到内网服务器上     


       
       
       

