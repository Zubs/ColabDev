# Backend
This is the backend repo.

## Technologies
- Flask (Python)
- PostgresSQL

## Platform
The application is hosted on Render with a PostgresSQL database and automatic deployment from the `main` branch on GitHub.

## Project Setup
- Install required packages
```sh
pip install -r requirements.txt
```

- Create `.env` and `.env.local` file in the root directory using the `.env.example` file
```sh
cp env.example .env
cp env.example .env.local
```

- Activate the virtual environment
```sh
.venv/bin/activate
```

- Freeze the requirements (if you install any new package)
```sh
pip freeze > requirements.txt
```

- Run the server
```sh
flask --app index run
```
