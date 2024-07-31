create table project_test_link
(
    project_id  varchar(7)   null,
    test_kit_id varchar(10)  not null
        primary key,
    route       varchar(30)  null,
    order_date  date         null,
    customer    varchar(100) null,
    dn_number   varchar(100) null,
    constraint project_test_link_ibfk_1
        foreign key (project_id) references project_code (project_id)
);

create index project_id
    on project_test_link (project_id);

INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C1', '24071001', 'test', '2024-07-17', 'greco si fu', 'DN_!@##');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C0', '24072001', 'consignmnet', '2024-07-17', 'dr yousuf', 'DN_1283638');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C0', '24072002', 'consignmnet', '2024-07-17', 'dr yousuf', 'DN_1283638');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072003', '', '2024-07-17', '', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072004', '', '2024-07-17', '', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072005', 'cknbk', '2024-07-17', 'sad', 'sdd');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072006', 'cknbk', '2024-07-17', 'sad', 'sdd');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072007', 'cknbk', '2024-07-17', 'sad', 'sdd');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072008', 'cknbk', '2024-07-17', 'sad', 'sdd');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072009', 'cknbk', '2024-07-17', 'sad', 'sdd');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072010', 'cknbk', '2024-07-17', 'sad', 'sdd');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072011', 'cknbk', '2024-07-17', 'sad', 'sdd');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072012', 'cknbk', '2024-07-17', 'sad', 'sdd');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C100', '24072013', 'test', '2024-07-17', 'test', 'test');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C100', '24072014', 'test', '2024-07-17', 'test', 'test');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C100', '24072015', 'consigmnet', '2024-07-19', 'any name', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C100', '24072016', 'consigmnet', '2024-07-19', 'any name', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C100', '24072017', 'consigmnet', '2024-07-19', 'any name', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C100', '24072018', 'consigmnet', '2024-07-19', 'any name', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C100', '24072019', 'consigmnet', '2024-07-19', 'any name', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C100', '24072020', 'consigmnet', '2024-07-19', 'any name', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C100', '24072021', 'consigmnet', '2024-07-19', 'any name', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C100', '24072022', 'consigmnet', '2024-07-19', 'any name', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C100', '24072023', 'consigmnet', '2024-07-19', 'any name', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C100', '24072024', 'consigmnet', '2024-07-19', 'any name', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072025', 'consignmnet', '2024-07-25', 'janey', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072026', 'consignmnet', '2024-07-25', 'janey', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072027', 'consignmnet', '2024-07-25', 'janey', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072028', 'consignmnet', '2024-07-25', 'janey', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072029', 'consignmnet', '2024-07-25', 'janey', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072030', 'consignmnet', '2024-07-25', 'janey', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072031', 'consignmnet', '2024-07-25', 'janey', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072032', 'consignmnet', '2024-07-25', 'janey', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072033', 'consignmnet', '2024-07-25', 'janey', '');
INSERT INTO biomed_db.project_test_link (project_id, test_kit_id, route, order_date, customer, dn_number) VALUES ('C10', '24072034', 'consignmnet', '2024-07-25', 'janey', '');
