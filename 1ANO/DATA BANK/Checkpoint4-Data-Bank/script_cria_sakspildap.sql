CREATE TABLE t_sk_bairro (
    cd_bairro  NUMBER(8) NOT NULL,
    cd_cidade  NUMBER(3) NOT NULL,
    nm_bairro  VARCHAR2(20 BYTE) NOT NULL
);

ALTER TABLE t_sk_bairro ADD CONSTRAINT pk_sk_bairro PRIMARY KEY ( cd_bairro );

CREATE TABLE t_sk_cidade (
    cd_cidade  NUMBER(3) NOT NULL,
    cd_estado  NUMBER(2) NOT NULL,
    nm_cidade  VARCHAR2(20 BYTE) NOT NULL
);

ALTER TABLE t_sk_cidade ADD CONSTRAINT pk_sk_cidade PRIMARY KEY ( cd_cidade );

CREATE TABLE t_sk_colaborador (
    id_colaborador   NUMBER(10) NOT NULL,
    cd_departamento  NUMBER(10) NOT NULL,
    dt_nascimento    DATE NOT NULL,
    nm_estado_civil  VARCHAR2(20 BYTE) NOT NULL,
    nm_nome          VARCHAR2(20 BYTE) NOT NULL
);

--  ERROR: Table constraint name length exceeds maximum allowed length(30) 
ALTER TABLE t_sk_colaborador ADD constraint ck_sk_colaborador_ds_estado_civil CHECK ( ds_estado civil IN (
    `solteiro`,
    `casado`,
    `divorciado`
) );
ALTER TABLE t_sk_colaborador ADD CONSTRAINT pk_sk_colaborador PRIMARY KEY ( id_colaborador );

CREATE TABLE t_sk_colaborador_endereco (
    nr_cep            NUMBER(8) NOT NULL,
    cd_tipo_endereco  NUMBER(4) NOT NULL,
    id_colaborador    NUMBER(10) NOT NULL,
    ds_complemento    VARCHAR2(20 BYTE) NOT NULL,
    nr_lougradouro    NUMBER(8) NOT NULL
);

ALTER TABLE t_sk_colaborador_endereco
    ADD CONSTRAINT pk_sk_colaborador_endereco PRIMARY KEY ( nr_cep,
                                                            cd_tipo_endereco,
                                                            id_colaborador );

CREATE TABLE t_sk_colaborador_projeto (
    id_colaborador  NUMBER(10) NOT NULL,
    cd_projeto      NUMBER(10) NOT NULL
);

ALTER TABLE t_sk_colaborador_projeto ADD CONSTRAINT pk_sk_colaborador_projeto PRIMARY KEY ( id_colaborador,
                                                                                            cd_projeto );

CREATE TABLE t_sk_departamento (
    cd_departamento  NUMBER(10) NOT NULL,
    nm_nome          VARCHAR2(30) NOT NULL
);

ALTER TABLE t_sk_departamento ADD CONSTRAINT pk_sk_departamento PRIMARY KEY ( cd_departamento );

CREATE TABLE t_sk_endereco (
    nr_cep              NUMBER(8) NOT NULL,
    cd_bairro           NUMBER(8) NOT NULL,
    cd_tipo_logradouro  NUMBER(10) NOT NULL,
    ds_logradouro       VARCHAR2(30 BYTE) NOT NULL
);

ALTER TABLE t_sk_endereco ADD CONSTRAINT pk_sk_endereco PRIMARY KEY ( nr_cep );

CREATE TABLE t_sk_estado (
    cd_estado  NUMBER(2) NOT NULL,
    nm_estado  VARCHAR2(20 BYTE) NOT NULL,
    sg_estado  VARCHAR2(20 BYTE)
);

ALTER TABLE t_sk_estado ADD CONSTRAINT pk_sk_estado PRIMARY KEY ( cd_estado );

CREATE TABLE t_sk_projeto (
    cd_projeto    NUMBER(10) NOT NULL,
    dt_inicio     DATE NOT NULL,
    dt_fim        DATE NOT NULL,
    ds_descricao  VARCHAR2(200) NOT NULL,
    ds_papel      VARCHAR2(200) NOT NULL,
    vl_budget     NUMBER(8, 2) NOT NULL
);

ALTER TABLE t_sk_projeto ADD CONSTRAINT pk_sk_projeto PRIMARY KEY ( cd_projeto );

CREATE TABLE t_sk_telefone (
    nr_ddi       NUMBER(4) NOT NULL,
    nr_ddd       NUMBER(3) NOT NULL,
    nr_telefone  NUMBER(9) NOT NULL
);

ALTER TABLE t_sk_telefone
    ADD CONSTRAINT pk_sk_telefone PRIMARY KEY ( nr_ddi,
                                                nr_telefone,
                                                nr_ddd );

CREATE TABLE t_sk_telefone_colaborador (
    nr_ddi          NUMBER(4) NOT NULL,
    nr_telefone     NUMBER(9) NOT NULL,
    nr_ddd          NUMBER(3) NOT NULL,
    id_colaborador  NUMBER(10) NOT NULL
);

ALTER TABLE t_sk_telefone_colaborador
    ADD CONSTRAINT pk_sk_telefone_colaborador PRIMARY KEY ( nr_ddi,
                                                            nr_telefone,
                                                            nr_ddd,
                                                            id_colaborador );

CREATE TABLE t_sk_tipo_endereco (
    cd_tipo_endereco  NUMBER(4) NOT NULL,
    nm_tipo_endereco  VARCHAR2(20 BYTE) NOT NULL
);

ALTER TABLE t_sk_tipo_endereco ADD CONSTRAINT pk_sk_tipo_endereco PRIMARY KEY ( cd_tipo_endereco );

CREATE TABLE t_sk_tipo_logradouro (
    cd_tipo_logradouro  NUMBER(10) NOT NULL,
    nm_tipo_logradouro  VARCHAR2(20 BYTE) NOT NULL
);

ALTER TABLE t_sk_tipo_logradouro ADD CONSTRAINT pk_sk_tipo_logradouro PRIMARY KEY ( cd_tipo_logradouro );

ALTER TABLE t_sk_endereco
    ADD CONSTRAINT relacao_bairro_endereco FOREIGN KEY ( cd_bairro )
        REFERENCES t_sk_bairro ( cd_bairro );

ALTER TABLE t_sk_bairro
    ADD CONSTRAINT relacao_cidade_bairro FOREIGN KEY ( cd_cidade )
        REFERENCES t_sk_cidade ( cd_cidade );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE t_sk_colaborador_endereco
    ADD CONSTRAINT relacao_colaborador_colaborador_endereco FOREIGN KEY ( id_colaborador )
        REFERENCES t_sk_colaborador ( id_colaborador );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE t_sk_colaborador_projeto
    ADD CONSTRAINT relacao_colaborador_colaborador_projeto FOREIGN KEY ( id_colaborador )
        REFERENCES t_sk_colaborador ( id_colaborador );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE t_sk_telefone_colaborador
    ADD CONSTRAINT relacao_colaborador_telefone_colaborador FOREIGN KEY ( id_colaborador )
        REFERENCES t_sk_colaborador ( id_colaborador );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE t_sk_colaborador
    ADD CONSTRAINT relacao_departamento_colaborador FOREIGN KEY ( cd_departamento )
        REFERENCES t_sk_departamento ( cd_departamento );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE t_sk_colaborador_endereco
    ADD CONSTRAINT relacao_endereco_colaborador_endereco FOREIGN KEY ( nr_cep )
        REFERENCES t_sk_endereco ( nr_cep );

ALTER TABLE t_sk_cidade
    ADD CONSTRAINT relacao_estado_cidade FOREIGN KEY ( cd_estado )
        REFERENCES t_sk_estado ( cd_estado );

ALTER TABLE t_sk_endereco
    ADD CONSTRAINT relacao_lougradouro_endereco FOREIGN KEY ( cd_tipo_logradouro )
        REFERENCES t_sk_tipo_logradouro ( cd_tipo_logradouro );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE t_sk_colaborador_projeto
    ADD CONSTRAINT relacao_projeto_colaborador_projeto FOREIGN KEY ( cd_projeto )
        REFERENCES t_sk_projeto ( cd_projeto );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE t_sk_telefone_colaborador
    ADD CONSTRAINT relacao_telefone_telefone_colaborador FOREIGN KEY ( nr_ddi,
                                                                       nr_telefone,
                                                                       nr_ddd )
        REFERENCES t_sk_telefone ( nr_ddi,
                                   nr_telefone,
                                   nr_ddd );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE t_sk_colaborador_endereco
    ADD CONSTRAINT relacao_tipo_endereco_colaborador_endereco FOREIGN KEY ( cd_tipo_endereco )
        REFERENCES t_sk_tipo_endereco ( cd_tipo_endereco );

