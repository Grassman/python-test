# --- Created by Ebean DDL
# To stop Ebean DDL generation, remove this comment and start using Evolutions

# --- !Ups

create table accesspoint (
  ap_id                     bigint auto_increment not null,
  ssid                      varchar(255),
  mac                       varchar(255),
  encrypted                 varchar(255),
  constraint pk_accesspoint primary key (ap_id))
;




# --- !Downs

SET REFERENTIAL_INTEGRITY FALSE;

drop table if exists accesspoint;

SET REFERENTIAL_INTEGRITY TRUE;

