# Primeira API em Django

## Sobre o projeto

Esse projeto foi um teste para aprender um pouco sobre APIs Rest com Django, como primeiros contatos com **criações de APIs para back-end**. Os dados armazenados são dados muito simples de usuários para um prograama qualquer, e o CRUD possibilita a criação de novos ítens para a API, edição, exclusão e visualização.

O repositório, ideia e código foram 100% baseados neste vídeo https://www.youtube.com/watch?v=Q2tEqNfgIXM, portanto, gostaria de agradecer ao criador ao disponibilizar seu código e tornar possível a compreensão das APIs Rest com python. Vi muito valor no vídeo e no aprendizado que tive com APIs seguindo este tutorial.

## Como rodar em sua máquina

1. Tendo algum editor de código, Git e Python instalados, rode o comando abaixo e entre na pasta pelo seu editor de código (ex: VSCode)

   ```console
   git clone https://github.com/nogsposito/django-primeira-api.git
   ```

2. Instale todas as dependências doo requirement.txt instaladas (frameworks e bibliotecas), sendo elas:

     ```console
     asgiref==3.8.1
     Django==4.2.17
     django-cors-headers==4.6.0
     djangorestframework==3.15.2
     sqlparse==0.5.2
     typing-extensions==4.12.2
     ```

3. Então, use os comandos abaixo para poder rodar o projeto no seu servidor local (http://127.0.0.1:8000/) e acesse a interface principal pelo http://127.0.0.1:8000/api/. (ATENÇÃO: OS COMANDOS PODEM VARIAR DEPENDENDO DE SUA MÁQUINA, O COMANDO USADO NO LINUX SERIA "python3" MAS NO WINDOWS PROVAVELMENTE "python")

   ```console
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py runserver
   ```

4. Para poder praticar visualizar o CRUD, talvez seja necessário instalar o Insomnia, mas poderá ser editado os dados pela página de admin do Django (http://127.0.0.1:8000/admin/), mas seria necessáril criar um superuser primeiro. Se faz isso com o comando abaixo, que pedirá a criação de um usuário admin com uma senha costumizada (Porém, sem o Insomnia ou outra tecnologia similar seria mais difícil ver as funcionalidades do CRUD programadas funcionando):

   ```console
   python3 manage.py createsuperuser
   ```

5. Dado isso e fazendo todas as outras configurações necessárias, deveria se poder navegar pelo programa facilmente. Caso haja algum problema ou dúvida sobre a instalação ou sobre o código, me contate pelo meu e-mail (viniciussposito3103@gmail.com) e estarei mais que feliz de ajudá-lo e consertar qualquer problema.
