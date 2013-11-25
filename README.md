# Sistema de suporte para empresas de TI
---

O sistema de suporte com atualmente as seguintes funcionalidades:

* Cadastro de funcionários
* Cadastro de clientes/empresas
* Cadastro de usuários (contatos para as empresas)
* Portal de acesso para os clientes com as seguintes funções:
* * Abertura de solicitações
* * Visualização dos dados cadastrais

---

### Estado da arte

---

* O sistema ainda está em faze de desenvolvimento ainda faltam algumas funcionalidades essenciais como:
* Possibilidade de envio de e-mail para o cliente quando for aberta uma solicitação.
* Quando adicionar uma solicitação poder marcar se a mesma é privada ou não.
* Qualquer outra ideia, faça um pull request que a mesma será análisada e incorporada =)

---

### Instalação

---

1. Clone o projeto

```
git clone
```

2. Rode o requirements.txt

```
pip install -r requirements.txt
```

3. Rode o banco

```
./manage.py syncdb
```

4. Rode o projeto

```
./manage.py runserver
```