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

### Database
# Create a new migration
```sh
flask db migrate -m "Description of changes"
```

# Apply migrations
```sh
flask db upgrade
```

# Rollback one migration
```sh
flask db downgrade
```

# View migration history
```sh
flask db history
```

# Current migration status
```sh
flask db current
```
