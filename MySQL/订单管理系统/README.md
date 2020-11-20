修改framework.py中order和execut_crud_sql函数mysql服务器配置信息（密码等）
## Create Database
 ```
create database orders charset=utf8;
create table orders( 
 	id int not null auto_increment primary key,
	count int not null, 
	price decimal(10,2) not null, 
	freight decimal(10,2) not null, 
	user varchar(50) not null,
	status enum('待支付','待发货','待收货') default '待支付' not null, 
	time date not null 
);
 ```
## Add Data
```
  cd scripts
  mysql –uroot –p
  use orders;
  source orders;
```
## Running Code
```
  python web.py 8000
```
