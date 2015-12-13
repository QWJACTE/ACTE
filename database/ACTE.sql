/* 
** 注：因为数据库数据默认的编码拉丁文，所以需要改变mysql的配置文件，
** 来让它支持中文，具体方法是：在/etc/mysql/my.cnf文件里的[mysqld]下
** 增加
**      character_set_server=utf8
**      init_connect='SET NAMES utf8'
** 这样两行。
*/
drop database if exists ACTE;
create database ACTE;
use ACTE;

-- 第一个用户默认设成unknown
create table User (
    id          int             not null auto_increment,
    UID         varchar(20)     not null,
    password    varchar(20)     not null,
    nickname    varchar(20),
    sex         enum('man','woman','secret')    default 'secret',
    headpic     varchar(100),
    birthday    date    default null,
    email       varchar(50),
    location    varchar(20),
    description varchar(50) default null,
    status      enum('N','Y') default 'N',
    primary key(id),
    unique(UID)
);
insert into User(UID,password) values('unknown', 'unknown');
-- 第一个活动举办者默认设成unknown
create table Sponsor (
    id          int             not null auto_increment,
    SID         varchar(20)     not null,
    password    varchar(20)     not null,
    ACT_type    varchar(20)     not null,
    company_name varchar(50)    not null,
    nickname    varchar(20),
    sex         enum('man','woman','secret')    default 'secret',
    headpic     varchar(100),
    birthday    date    default null,
    email       varchar(50),
    location    varchar(20),
    description varchar(50) default null,
    status      enum('N','Y') default 'Y',
    primary key(id),
    unique(SID)
);
insert into Sponsor(SID, password, ACT_type, company_name) values('unknown','unknown','unknown','unknown');
create table City (
    CID         int             not null,
    name        varchar(20)     not null,
    weather     varchar(100),
    primary key(CID)
);
-- 全国城市代码 还有很多
insert into City(name, CID) values
    ('北京',101010100),
    ('上海',101020100),
    ('广州',101280101),
    ('珠海',101280701),
    ('赣州',101240701);

create table follow (
    Uid         int             not null,
    Sid         int             not null,
    follow_date timestamp,
    foreign key(Uid) references User(id),
    foreign key(Sid) references Sponsor(id),
    primary key(Uid, Sid)
);
-- 第一个活动默认设成unknown
create table Activity (
    id          int             not null auto_increment,
    owner_id    int             not null,
    AID         varchar(50)     not null,
    full_name   varchar(50)     not null,
    ActPic      varchar(100)    not null, -- 12/14/2015添加
    begin_date  timestamp       not null,
    end_date    timestamp       not null,
    create_date timestamp,
    introduction    varchar(200) default 'none',
    location    varchar(100)    not null,
    type        varchar(20) default 'others',
    primary key(id),
    foreign key(owner_id) references Sponsor(id)
);

create table subscribe (
    Uid         int             not null,
    Aid         int             not null,
    subscribe_date timestamp,
    primary key(Uid, Aid),
    foreign key(Uid) references User(id),
    foreign key(Aid) references Activity(id)
);

create table favorite (
    Uid         int             not null,
    Aid         int             not null,
    subscribe_date timestamp,
    primary key(Uid, Aid),
    foreign key(Uid) references User(id),
    foreign key(Aid) references Activity(id)
);

create table grade (
    id          int             not null auto_increment,
    Uid         int             not null,
    Aid         int             not null,
    star        enum('0','1','2','3','4','5') not null,
    grade_date  timestamp,
    primary key(id, Uid, Aid),
    foreign key(Uid) references User(id),
    foreign key(Aid) references Activity(id)
);

create table comment (
    id          int             not null auto_increment,
    Uid         int             not null,
    Aid         int             not null,
    content     varchar(1000)   not null,
    comment_date timestamp,
    primary key(id, Uid, Aid),
    foreign key(Uid) references User(id),
    foreign key(Aid) references Activity(id)  
);