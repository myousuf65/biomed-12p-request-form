create table serial_number_storage
(
    id        varchar(4)  null,
    test_name varchar(20) null,
    val       int         null
);

INSERT INTO biomed_db.serial_number_storage (id, test_name, val) VALUES ('1', '16s', 1);
INSERT INTO biomed_db.serial_number_storage (id, test_name, val) VALUES ('2', 'qPCR', 34);
INSERT INTO biomed_db.serial_number_storage (id, test_name, val) VALUES ('3', 'platinum', 0);
INSERT INTO biomed_db.serial_number_storage (id, test_name, val) VALUES ('4', 'oral qPCR', 0);
INSERT INTO biomed_db.serial_number_storage (id, test_name, val) VALUES ('5', 'pet', 0);
INSERT INTO biomed_db.serial_number_storage (id, test_name, val) VALUES ('6', 'PATIENT', 9329);
