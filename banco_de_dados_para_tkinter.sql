create database Banco_Pack_Py;
use Banco_Pack_Py;

create table func(id_func varchar(6) primary key, cpf varchar(14));

create table cliente(
cpf varchar(14) primary key, 
nome varchar(45), 
dataNasc varchar(10), 
genero enum("M","F"), 
email varchar(50), 
senha varchar(8),
saldo float);

insert into func (id_func, cpf) values ('080910','111.222.333-44');
select * from cliente;
select * from func;