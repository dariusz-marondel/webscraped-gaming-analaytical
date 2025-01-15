-- players table
create table players_dg_tmp
(
    "index"  INTEGER,
    nickname TEXT
        constraint players_pk
            primary key,
    tagline  TEXT,
    role     TEXT
);

insert into players_dg_tmp("index", nickname, tagline, role)
select "index", nickname, tagline, role
from players;

drop table players;

alter table players_dg_tmp
    rename to players;

create index ix_players_index
    on players ("index");


-- champion_pool table

create table champion_pool_dg_tmp
(
    "index"  INTEGER
        constraint champion_pool_pk
            primary key,
    role     TEXT,
    champion TEXT
);

insert into champion_pool_dg_tmp("index", role, champion)
select "index", role, champion
from champion_pool;

drop table champion_pool;

alter table champion_pool_dg_tmp
    rename to champion_pool;

create index ix_champion_pool_index
    on champion_pool ("index");

-- champions table 
create table champions_dg_tmp
(
    "index"              INTEGER,
    id                   TEXT
        constraint champions_pk
            primary key,
    name                 TEXT,
    title                TEXT,
    attack               INTEGER,
    defense              INTEGER,
    magic                INTEGER,
    difficulty           INTEGER,
    tags                 TEXT,
    partype              TEXT,
    hp                   INTEGER,
    hpperlevel           INTEGER,
    mp                   INTEGER,
    mpperlevel           REAL,
    movespeed            INTEGER,
    armor                INTEGER,
    armorperlevel        REAL,
    spellblock           INTEGER,
    spellblockperlevel   REAL,
    attackrange          INTEGER,
    hpregen              REAL,
    hpregenperlevel      REAL,
    mpregen              REAL,
    mpregenperlevel      REAL,
    crit                 INTEGER,
    critperlevel         INTEGER,
    attackdamage         INTEGER,
    attackdamageperlevel REAL,
    attackspeedperlevel  REAL,
    attackspeed          REAL
);

insert into champions_dg_tmp("index", id, name, title, attack, defense, magic, difficulty, tags, partype, hp,
                             hpperlevel, mp, mpperlevel, movespeed, armor, armorperlevel, spellblock,
                             spellblockperlevel, attackrange, hpregen, hpregenperlevel, mpregen, mpregenperlevel, crit,
                             critperlevel, attackdamage, attackdamageperlevel, attackspeedperlevel, attackspeed)
select "index",
       id,
       name,
       title,
       attack,
       defense,
       magic,
       difficulty,
       tags,
       partype,
       hp,
       hpperlevel,
       mp,
       mpperlevel,
       movespeed,
       armor,
       armorperlevel,
       spellblock,
       spellblockperlevel,
       attackrange,
       hpregen,
       hpregenperlevel,
       mpregen,
       mpregenperlevel,
       crit,
       critperlevel,
       attackdamage,
       attackdamageperlevel,
       attackspeedperlevel,
       attackspeed
from champions;

drop table champions;

alter table champions_dg_tmp
    rename to champions;

create index ix_champions_index
    on champions ("index");