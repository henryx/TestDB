PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE test1 (ins INTEGER, date_ins INTEGER, hour_ins INTEGER, txt VARCHAR(30));
CREATE TABLE test2 (ins INTEGER, date_ins INTEGER, hour_ins INTEGER, txt VARCHAR(30));
CREATE TABLE test3 (ins INTEGER, date_ins INTEGER, hour_ins INTEGER, txt VARCHAR(30));
CREATE TABLE test4 (ins INTEGER, date_ins INTEGER, hour_ins INTEGER, txt VARCHAR(30));
CREATE TABLE test5 (ins INTEGER, date_ins INTEGER, hour_ins INTEGER, txt VARCHAR(30));
CREATE TABLE test6 (ins INTEGER, date_ins INTEGER, hour_ins INTEGER, txt VARCHAR(30));
CREATE TABLE test7 (ins INTEGER, date_ins INTEGER, hour_ins INTEGER, txt VARCHAR(30));
CREATE TABLE test8 (ins INTEGER, date_ins INTEGER, hour_ins INTEGER, txt VARCHAR(30));
CREATE TABLE test9 (ins INTEGER, date_ins INTEGER, hour_ins INTEGER, txt VARCHAR(30));
CREATE TABLE test10 (ins INTEGER, date_ins INTEGER, hour_ins INTEGER, txt VARCHAR(30));
CREATE INDEX idx_test_1 ON test1 (date_ins);
CREATE INDEX idx_test_2 ON test2 (date_ins);
CREATE INDEX idx_test_3 ON test3 (date_ins);
CREATE INDEX idx_test_4 ON test4 (date_ins);
CREATE INDEX idx_test_5 ON test5 (date_ins);
CREATE INDEX idx_test_6 ON test6 (date_ins);
CREATE INDEX idx_test_7 ON test7 (date_ins);
CREATE INDEX idx_test_8 ON test8 (date_ins);
CREATE INDEX idx_test_9 ON test9 (date_ins);
CREATE INDEX idx_test_10 ON test10 (date_ins);
COMMIT;
