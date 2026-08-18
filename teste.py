Create database if not exists sustentavel;
use sustentavel;

create table if not exists usuario (
 id int,
 nome varchar (255),
 idade int);

create table if not exists residencia (
 id int auto_increment primary key,
 propriedario varchar (255),
 QuandidadeDeResidentes int,
 endereço varchar (255));

create table if not exists energia (
 id int,
 id_residencia int,
 quilowattsPorHora decimal (10, 2),
 precoDoQuilowattsPorHora decimal (10, 2),
 FOREIGN KEY (id_residencia) REFERENCES residencia(id) ON DELETE CASCADE
 );

create table if not exists agua (
 id int,
 id_residencia int,
 litrosDeAguaUsados decimal(10, 2),
 precoPorLitro decimal(10, 2),
 FOREIGN KEY (id_residencia) REFERENCES residencia(id) ON DELETE CASCADE
 );
 
create table if not exists lixo (
 id int,
 id_residencia int,
 QuiloDeLixo decimal(10, 2),
 multaPorQuiloDELixo decimal(10, 2),
 FOREIGN KEY (id_residencia) REFERENCES residencia(id) ON DELETE CASCADE
 );
