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
    full_name   varchar(50),
    ActPic      varchar(100)    not null,
    create_date timestamp,
    begin_date  timestamp       not null,
    end_date    timestamp       not null,
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

insert into User(UID,password,nickname,sex,birthday,email,location) values
    ('andy','123456','andee','man',null,null,'珠海');

insert into Sponsor(SID,password,ACT_type,company_name) values
    ('jamoeba','19940818','acg','acte'),
    ('jingle','19940818','music','acte');

insert into Activity(owner_id,AID,full_name,ActPic,begin_date,end_date,create_date,introduction,location,type) values
    ('2','happyeve','幸福生活每一天','2','20150818','20160818','20151201','大家聚 在一起享受快乐幸福的生活','珠海','others'),
    ('2','goodmorning','健康早操','3','20151101','20161101','20151201','美好生活从早上做起','珠海','others'),
    ('3','百人漫展','happyacg','4','20150818','20160818','20151201','在这里什么都不想，就是玩！','珠海','acg'),
    ('3','百人漫展','happyacg','5','20150818','20160818','20151201','在这里什么都不想，就是玩！','珠海','acg'),
    ('3','百人漫展','happyacg','6','20150818','20160818','20151201','在这里什么都不想，就是玩！','珠海','acg'),
    ('3','百人漫展','happyacg','7','20150818','20160818','20151201','在这里什么都不想，就是玩！','珠海','acg');
