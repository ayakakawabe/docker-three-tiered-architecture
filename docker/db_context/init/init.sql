use sample_db;

create table sample_table(
    id integer not null,
    name char(20) not null,
    primary key (id)
    );

insert into sample_table(
    id,name
)
values(
    1,"sample_user"
);