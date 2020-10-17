CREATE TABLE users (
        id INIGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nme TEXT username TEXT,
        scheduleTag TEXT,
        auto_posting_time TIME,
        is_today BOOLEAN
)
CREATE TABLE organizations(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
organizations TEXT,
faculty TEXT,
studGroup TEXT,
tag TEXT
);
CREATE TABLE schedule(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
tag TEXT, day TEXT,
number INTEGER,
type TEXT,
startTime TEXT,
endTime,TEXT
title TEXT,
classroom TEXT,
lecturer
);
CREATE TABLE reports(
report_id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
report TEXT,
date DATETIME
);
