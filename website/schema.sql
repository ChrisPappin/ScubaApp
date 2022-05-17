drop table if exists accounts;
    create table accounts (
        id integer primary key autoincrement,
        username text not null,
        password text not null,
        totalDives integer not null,
        uniqueLoc integer not null,
        totalTime text

);
