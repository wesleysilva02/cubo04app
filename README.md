# cubo04app

Aplicação web desenvolvida com **Python e Django** para cadastro de usuários e acesso por uma tela de login. O projeto utiliza o **SQLite** como banco de dados.

## Prévia

<!-- Substitua o caminho abaixo pela imagem de uma captura de tela do app no repositório. -->
![Prévia do cubo04app](docs/images/cubo04-preview.png)

> Para exibir a imagem no GitHub, adicione uma captura de tela em `docs/images/cubo04-preview.png` ou atualize o caminho acima.

## Funcionalidades

- Cadastro de usuários.
- Login de usuários.
- Persistência de dados com SQLite.

## Tecnologias

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- SQLite

## Requisitos

- Python instalado.
- `pip`, o gerenciador de pacotes do Python.
- Git, caso queira clonar o repositório.

## Como executar

1. Clone o repositório e acesse a pasta do projeto:

	```bash
	git clone <URL_DO_REPOSITORIO>
	cd cubo04
	```

2. Crie e ative um ambiente virtual:

	```bash
	python -m venv .venv
	```

	No Windows:

	```powershell
	.venv\Scripts\Activate.ps1
	```

	No macOS ou Linux:

	```bash
	source .venv/bin/activate
	```

3. Instale o Django:

	```bash
	pip install Django
	```

4. Na pasta que contém `manage.py`, aplique as migrações e inicie o servidor:

	```bash
	python manage.py migrate
	python manage.py runserver
	```

5. Acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/) no navegador.

> Se o projeto tiver um arquivo `requirements.txt`, instale as dependências com `pip install -r requirements.txt` em vez de instalar apenas o Django.

## Banco de dados

O SQLite é usado para armazenar os dados da aplicação. O comando `python manage.py migrate` cria ou atualiza as tabelas necessárias, conforme as migrações do projeto.

## Imagens do projeto

Para adicionar capturas reais, crie a pasta `docs/images/`, salve as imagens nela e atualize os caminhos das imagens neste README. Por exemplo:

```markdown
![Tela de login](docs/images/login.png)
```

## Contribuição

Sugestões e melhorias são bem-vindas. Abra uma issue para relatar um problema ou envie um pull request com sua contribuição.

## Licença

Nenhuma licença foi informada. Consulte o responsável pelo projeto antes de reutilizar ou distribuir o código.
sistema de cadastro de usúarios juntamente com a tela de login ligado ao banco SQL lite , projeto feito com Python  Django
