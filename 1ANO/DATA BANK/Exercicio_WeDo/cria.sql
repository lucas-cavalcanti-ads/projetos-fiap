-- Gerado por Oracle SQL Developer Data Modeler 19.4.0.350.1424
--   em:        2020-08-21 12:32:41 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g

CREATE TABLE t_wedo_cli_end (
    cd_cliente           NUMBER(9) NOT NULL,
    nr_endereco          NUMBER(3) NOT NULL,
    nr_logradouro        NUMBER(10) NOT NULL,
    nr_rua               VARCHAR2(12),
    ds_ponto_referencia  VARCHAR2(100),
    ds_complemento       VARCHAR2(30 BYTE),
    dt_inicio            DATE,
    dt_termino           DATE,
    st_ativo             CHAR(1)
);

ALTER TABLE t_wedo_cli_end
    ADD CONSTRAINT t_wedo_cli_end_ck_ativo CHECK ( st_ativo IN (
        'S',
        'N'
    ) );

ALTER TABLE t_wedo_cli_end ADD CONSTRAINT pk_wedo_cliente_end PRIMARY KEY ( cd_cliente,
                                                                            nr_endereco );

CREATE TABLE t_wedo_cli_fisica (
    cd_cliente       NUMBER(9) NOT NULL,
    nr_cpf           NUMBER(12),
    nr_rg            NUMBER(12),
    ds_genero        VARCHAR2(30 BYTE) NOT NULL,
    dt_nascimento    DATE,
    ds_est_civil     VARCHAR2(20 BYTE) NOT NULL,
    ds_escolaridade  VARCHAR2(40 BYTE) NOT NULL
);

ALTER TABLE t_wedo_cli_fisica ADD CONSTRAINT pk_wedo_cli_fisica PRIMARY KEY ( cd_cliente );

ALTER TABLE t_wedo_cli_fisica ADD CONSTRAINT uk_wedo_nr_cpf UNIQUE ( nr_cpf );

ALTER TABLE t_wedo_cli_fisica ADD CONSTRAINT uk_wedo_nr_rg UNIQUE ( nr_rg );

CREATE TABLE t_wedo_cli_juridica (
    cd_cliente             NUMBER(9) NOT NULL,
    nr_cnpj                NUMBER(14) NOT NULL,
    nr_inscricao_estadual  NUMBER(12),
    dt_fundacao            DATE NOT NULL
);

ALTER TABLE t_wedo_cli_juridica ADD CONSTRAINT pk_wedo_cli_juridica PRIMARY KEY ( cd_cliente );

ALTER TABLE t_wedo_cli_juridica ADD CONSTRAINT un_wedo_nr_cnpj UNIQUE ( nr_cnpj );

ALTER TABLE t_wedo_cli_juridica ADD CONSTRAINT un_wedo_nr_insc_est UNIQUE ( nr_inscricao_estadual );

CREATE TABLE t_wedo_cliente (
    cd_cliente   NUMBER(9) NOT NULL,
    nm_cliente   VARCHAR2(150 BYTE) NOT NULL,
    dt_cadastro  DATE NOT NULL,
    st_ativo     CHAR(1) NOT NULL
);

ALTER TABLE t_wedo_cliente
    ADD CONSTRAINT t_wedo_cliente_ck_ativo CHECK ( st_ativo IN (
        'S',
        'N'
    ) );

ALTER TABLE t_wedo_cliente ADD CONSTRAINT pk_wedo_cliente PRIMARY KEY ( cd_cliente );

CREATE TABLE t_wedo_endereco_correio (
    nr_logradouro  NUMBER(10) NOT NULL,
    nm_estado      VARCHAR2(30) NOT NULL,
    sg_estado      CHAR(2) NOT NULL,
    nm_cidade      VARCHAR2(50) NOT NULL,
    nm_bairro      VARCHAR2(50 BYTE) NOT NULL,
    ds_logradouro  VARCHAR2(100 BYTE) NOT NULL,
    nr_cep         NUMBER(8)
);

ALTER TABLE t_wedo_endereco_correio ADD CONSTRAINT pk_wedo_end_correio PRIMARY KEY ( nr_logradouro );

CREATE TABLE t_wedo_entrega_semana (
    nr_lista_desejo  NUMBER(10) NOT NULL,
    nr_item          NUMBER(4) NOT NULL,
    dt_entrega       DATE NOT NULL,
    cd_produto       NUMBER(10) NOT NULL,
    nm_dia_semana    VARCHAR2(15) NOT NULL,
    qt_entregue      NUMBER(8, 2),
    vl_unitario      NUMBER(8, 2),
    st_pagto         VARCHAR2(10) NOT NULL,
    st_entrega       VARCHAR2(15) NOT NULL
);

ALTER TABLE t_wedo_entrega_semana ADD CONSTRAINT t_wedo_ent_semana_ck_vlunit CHECK ( vl_unitario >= 0 );

ALTER TABLE t_wedo_entrega_semana
    ADD CONSTRAINT t_wedo_ent_semana_ck_stat CHECK ( st_entrega IN (
        'A ENTREGAR',
        'ENTREGUE',
        'AUSENTE'
    ) );

ALTER TABLE t_wedo_entrega_semana
    ADD CONSTRAINT pk_wedo_entrega_semana PRIMARY KEY ( nr_lista_desejo,
                                                        nr_item,
                                                        dt_entrega );

CREATE TABLE t_wedo_img_produt0 (
    cd_produto   NUMBER(10) NOT NULL,
    nr_img       NUMBER(3) NOT NULL,
    ft_img       BLOB,
    dt_cadastro  DATE,
    st_ativo     CHAR(1)
);

ALTER TABLE t_wedo_img_produt0
    ADD CONSTRAINT t_wedo_img_produt0_ck_ativo CHECK ( st_ativo IN (
        'S',
        'N'
    ) );

ALTER TABLE t_wedo_img_produt0 ADD CONSTRAINT pk_wedo_img_produto PRIMARY KEY ( nr_img,
                                                                                cd_produto );

CREATE TABLE t_wedo_item_lista_desejo (
    nr_lista_desejo  NUMBER(10) NOT NULL,
    nr_item          NUMBER(4) NOT NULL,
    cd_produto       NUMBER(10) NOT NULL,
    qt_solicitada    NUMBER(8, 2),
    vl_unitario      NUMBER(9, 2),
    st_item_lista    VARCHAR2(12) NOT NULL
);

ALTER TABLE t_wedo_item_lista_desejo
    ADD CONSTRAINT t_wedo_item_list_des_ck_ativo CHECK ( st_item_lista IN (
        'A',
        'I'
    ) );

ALTER TABLE t_wedo_item_lista_desejo ADD CONSTRAINT t_wedo_item_list_des_ck_vluni CHECK ( vl_unitario >= 0 );

ALTER TABLE t_wedo_item_lista_desejo ADD CONSTRAINT pk_wedo_item_lista_desejo PRIMARY KEY ( nr_lista_desejo,
                                                                                            nr_item );

CREATE TABLE t_wedo_lista_desejo (
    nr_lista_desejo  NUMBER(10) NOT NULL,
    cd_cliente       NUMBER(9) NOT NULL,
    nr_endereco      NUMBER(3) NOT NULL,
    dt_hr_cadastro   DATE,
    vl_total_lista   NUMBER(9, 2),
    ds_forma_pagto   VARCHAR2(20) NOT NULL,
    st_entrega       VARCHAR2(15) NOT NULL
);

CREATE UNIQUE INDEX t_wedo_lista_desejo__idx ON
    t_wedo_lista_desejo (
        cd_cliente
    ASC,
        nr_endereco
    ASC );

ALTER TABLE t_wedo_lista_desejo
    ADD CONSTRAINT t_wedo_lista_desejo_ck_entreg CHECK ( st_entrega IN (
        'A ENTREGAR',
        'ENTREGUE',
        'AUSENTE'
    ) );

ALTER TABLE t_wedo_lista_desejo ADD CONSTRAINT t_wedo_lista_desejo_ck_vltot CHECK ( vl_total_lista >= 0 );

ALTER TABLE t_wedo_lista_desejo ADD CONSTRAINT pk_wedo_lista_desejo PRIMARY KEY ( nr_lista_desejo );

CREATE TABLE t_wedo_produto (
    cd_produto            NUMBER(10) NOT NULL,
    cd_barras             NUMBER(11),
    nm_produto            VARCHAR2(70 BYTE) NOT NULL,
    ds_detalhada_produto  VARCHAR2(300 BYTE) NOT NULL,
    ds_embalagem          VARCHAR2(30) NOT NULL,
    vl_produto            NUMBER(9, 2),
    qt_estoque_prd        NUMBER(8, 2),
    dt_cadastro           DATE,
    st_ativo              CHAR(1) NOT NULL
);

ALTER TABLE t_wedo_produto
    ADD CONSTRAINT t_wedo_produto_ck_ativo CHECK ( st_ativo IN (
        'S',
        'N'
    ) );

ALTER TABLE t_wedo_produto ADD CONSTRAINT t_wedo_produto_ck_vlprd CHECK ( vl_produto >= 0 );

ALTER TABLE t_wedo_produto ADD CONSTRAINT pk_wedo_produto PRIMARY KEY ( cd_produto );

CREATE TABLE t_wedo_tel_cliente (
    cd_telefone  NUMBER(9) NOT NULL,
    cd_cliente   NUMBER(9) NOT NULL,
    cd_ddd       NUMBER(2),
    nr_telefone  NUMBER(15),
    tp_telefone  VARCHAR2(20) NOT NULL
);

ALTER TABLE t_wedo_tel_cliente ADD CONSTRAINT pk_wedo_cli_tel PRIMARY KEY ( cd_telefone );

ALTER TABLE t_wedo_lista_desejo
    ADD CONSTRAINT fk_wedo_cli_end_list_desejo FOREIGN KEY ( cd_cliente,
                                                             nr_endereco )
        REFERENCES t_wedo_cli_end ( cd_cliente,
                                    nr_endereco );

ALTER TABLE t_wedo_cli_fisica
    ADD CONSTRAINT fk_wedo_cli_fisica FOREIGN KEY ( cd_cliente )
        REFERENCES t_wedo_cliente ( cd_cliente );

ALTER TABLE t_wedo_cli_juridica
    ADD CONSTRAINT fk_wedo_cli_juridica FOREIGN KEY ( cd_cliente )
        REFERENCES t_wedo_cliente ( cd_cliente );

ALTER TABLE t_wedo_cli_end
    ADD CONSTRAINT fk_wedo_cliente_end FOREIGN KEY ( cd_cliente )
        REFERENCES t_wedo_cliente ( cd_cliente );

ALTER TABLE t_wedo_tel_cliente
    ADD CONSTRAINT fk_wedo_cliente_tel FOREIGN KEY ( cd_cliente )
        REFERENCES t_wedo_cliente ( cd_cliente );

ALTER TABLE t_wedo_cli_end
    ADD CONSTRAINT fk_wedo_end_correio FOREIGN KEY ( nr_logradouro )
        REFERENCES t_wedo_endereco_correio ( nr_logradouro );

ALTER TABLE t_wedo_img_produt0
    ADD CONSTRAINT fk_wedo_img_prod FOREIGN KEY ( cd_produto )
        REFERENCES t_wedo_produto ( cd_produto );

ALTER TABLE t_wedo_entrega_semana
    ADD CONSTRAINT fk_wedo_lista_desejo_ent FOREIGN KEY ( nr_lista_desejo,
                                                          nr_item )
        REFERENCES t_wedo_item_lista_desejo ( nr_lista_desejo,
                                              nr_item );

ALTER TABLE t_wedo_item_lista_desejo
    ADD CONSTRAINT fk_wedo_lista_desejo_item FOREIGN KEY ( nr_lista_desejo )
        REFERENCES t_wedo_lista_desejo ( nr_lista_desejo );

ALTER TABLE t_wedo_entrega_semana
    ADD CONSTRAINT fk_wedo_produto_ent FOREIGN KEY ( cd_produto )
        REFERENCES t_wedo_produto ( cd_produto );

ALTER TABLE t_wedo_item_lista_desejo
    ADD CONSTRAINT fk_wedo_produto_item FOREIGN KEY ( cd_produto )
        REFERENCES t_wedo_produto ( cd_produto );

CREATE OR REPLACE TRIGGER trg_arc_t_wedo_cli_fisica BEFORE
    INSERT OR UPDATE OF cd_cliente ON t_wedo_cli_fisica
    FOR EACH ROW
DECLARE
    d NUMBER(9);
BEGIN
    SELECT
        a.cd_cliente
    INTO d
    FROM
        t_wedo_cliente a
    WHERE
        a.cd_cliente = :new.cd_cliente;

    IF ( d IS NULL OR d <> :new.cd_cliente ) THEN
        raise_application_error(-20223, 'O cliente pessoa física com o código ' || to_char(:new.cd_cliente) || ' não está na tabela genérica T_WEDO_CLIENTE. Favor verificar!');
    END IF;

EXCEPTION
    WHEN no_data_found THEN
        NULL;
    WHEN OTHERS THEN
        RAISE;
END;
/

CREATE OR REPLACE TRIGGER trg_arc_t_wedo_cli_juridica BEFORE
    INSERT OR UPDATE OF cd_cliente ON t_wedo_cli_juridica
    FOR EACH ROW
DECLARE
    d NUMBER(9);
BEGIN
    SELECT
        a.cd_cliente
    INTO d
    FROM
        t_wedo_cliente a
    WHERE
        a.cd_cliente = :new.cd_cliente;

    IF ( d IS NULL OR d <> :new.cd_cliente ) THEN
        raise_application_error(-20223, 'O cliente pessoa jurídica com o código ' || to_char(:new.cd_cliente) || ' não está na tabela genérica T_WEDO_CLIENTE. Favor verificar!');
    END IF;

EXCEPTION
    WHEN no_data_found THEN
        NULL;
    WHEN OTHERS THEN
        RAISE;
END;
/



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            11
-- CREATE INDEX                             1
-- ALTER TABLE                             37
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           2
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
