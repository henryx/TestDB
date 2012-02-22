CREATE GENERATOR test_seq;

CREATE TABLE test1
(
  ins      INTEGER,
  date_ins INTEGER,
  hour_ins INTEGER,
  txt      VARCHAR(30),
  CONSTRAINT test1_check CHECK(date_ins <= 16391231)
);
CREATE TABLE test10
(
  ins      INTEGER,
  date_ins INTEGER,
  hour_ins INTEGER,
  txt      VARCHAR(30),
  CONSTRAINT test10_check CHECK(date_ins >= 19800101)
);
CREATE TABLE test2
(
  ins      INTEGER,
  date_ins INTEGER,
  hour_ins INTEGER,
  txt      VARCHAR(30),
  CONSTRAINT test2_check CHECK(date_ins >= 16400101 AND date_ins <= 16791231)
);
CREATE TABLE test3
(
  ins      INTEGER,
  date_ins INTEGER,
  hour_ins INTEGER,
  txt      VARCHAR(30),
  CONSTRAINT test3_check CHECK(date_ins >= 16800101 AND date_ins <= 17191231)
);
CREATE TABLE test4
(
  ins      INTEGER,
  date_ins INTEGER,
  hour_ins INTEGER,
  txt      VARCHAR(30),
  CONSTRAINT test4_check CHECK(date_ins >= 17200101 AND date_ins <= 17591231)
);
CREATE TABLE test5
(
  ins      INTEGER,
  date_ins INTEGER,
  hour_ins INTEGER,
  txt      VARCHAR(30),
  CONSTRAINT test5_check CHECK(date_ins >= 17600101 AND date_ins <= 17991231)
);
CREATE TABLE test6
(
  ins      INTEGER,
  date_ins INTEGER,
  hour_ins INTEGER,
  txt      VARCHAR(30),
  CONSTRAINT test6_check CHECK(date_ins >= 18000101 AND date_ins <= 18391231)
);
CREATE TABLE test7
(
  ins      INTEGER,
  date_ins INTEGER,
  hour_ins INTEGER,
  txt      VARCHAR(30),
  CONSTRAINT test7_check CHECK(date_ins >= 18400101 AND date_ins <= 18791231)
);
CREATE TABLE test8
(
  ins      INTEGER,
  date_ins INTEGER,
  hour_ins INTEGER,
  txt      VARCHAR(30),
  CONSTRAINT test8_check CHECK(date_ins >= 18800101 AND date_ins <= 19391231)
);
CREATE TABLE test9
(
  ins      INTEGER,
  date_ins INTEGER,
  hour_ins INTEGER,
  txt      VARCHAR(30),
  CONSTRAINT test9_check CHECK(date_ins >= 19400101 AND date_ins <= 19791231)
);

CREATE VIEW test (ins, date_ins, hour_ins, txt)
AS   
SELECT ins, date_ins, hour_ins, txt FROM test1
UNION
SELECT ins, date_ins, hour_ins, txt FROM test2
UNION
SELECT ins, date_ins, hour_ins, txt FROM test3
UNION
SELECT ins, date_ins, hour_ins, txt FROM test4
UNION
SELECT ins, date_ins, hour_ins, txt FROM test5
UNION
SELECT ins, date_ins, hour_ins, txt FROM test6
UNION
SELECT ins, date_ins, hour_ins, txt FROM test7
UNION
SELECT ins, date_ins, hour_ins, txt FROM test8
UNION
SELECT ins, date_ins, hour_ins, txt FROM test9
UNION
SELECT ins, date_ins, hour_ins, txt FROM test10;

CREATE INDEX idx_test_1 ON test1 (date_ins);
CREATE INDEX idx_test_10 ON test10 (date_ins);
CREATE INDEX idx_test_2 ON test2 (date_ins);
CREATE INDEX idx_test_3 ON test3 (date_ins);
CREATE INDEX idx_test_4 ON test4 (date_ins);
CREATE INDEX idx_test_5 ON test5 (date_ins);
CREATE INDEX idx_test_6 ON test6 (date_ins);
CREATE INDEX idx_test_7 ON test7 (date_ins);
CREATE INDEX idx_test_8 ON test8 (date_ins);
CREATE INDEX idx_test_9 ON test9 (date_ins);

