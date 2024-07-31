create table q_answers
(
    test_kit_id varchar(10)  not null
        primary key,
    question1   varchar(100) null,
    question2   varchar(100) null,
    question3   varchar(100) null,
    question4   varchar(100) null,
    question5   varchar(100) null,
    question6   varchar(100) null,
    question7   varchar(255) null,
    question8   varchar(255) null,
    question9   varchar(255) null,
    question10  varchar(255) null,
    question11  varchar(255) null,
    question12  varchar(100) null,
    question13  varchar(100) null,
    question14  varchar(100) null,
    question15  varchar(100) null,
    question16  varchar(100) null,
    question17  varchar(100) null,
    constraint test_kit_id
        unique (test_kit_id),
    constraint q_answers_ibfk_1
        foreign key (test_kit_id) references project_test_link (test_kit_id)
);

INSERT INTO biomed_db.q_answers (test_kit_id, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14, question15, question16, question17) VALUES ('24072015', '中度 Moderate', '嚴重 Serious', 'Yes, recurrent illness 有，而且病情反覆發作', '中度 Moderate', 'Caesarean delivery 剖腹產', 'No 沒有', 'Not sure 不清楚', 'No 沒有', 'No 沒有', 'No 沒有', 'No 沒有', 'Severely too heavy/too light 嚴重過重/過輕', 'Sometimes (1-2 times a month) 有時（每個月1-2次）', 'Frequently (once in 2 weeks or more) 經常', 'All of them 全部三種', 'Yes 有', 'Yes 有');
