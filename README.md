# Mahjong API

This is a repository for a Mahjong score tracker. The goal is to have the following features:

- Score your Mahjong hand according to several scoring systems, including Hong-Kong Old Scoring or Chinese International Scoring
- Track the score throughout a game by submitting hands
- Access this through the front-end web app, synced between players here

## How to run locally

First, initialise the venv with

```bash
make venv
```

then run the local instance via

```bash
make start
```

that runs the API on default port 8000.

---

Placeholders

It is hosted on https://mahjong-api.onrender.com/ - useful initial endpoints include GET `/api` summarising the endpoints, or the OpenAPI auot-generated `/openapi.json` endpoint.

The front end TypeScript React app can be found \_\_\_

### Setting up Dev Postgres

These instructions are for Ubuntu - for Mac, Windows or other OS set up, follow appropriate documentation for installing & initialising PSQL

## Local Development Setup (Ubuntu)

1. **Install PostgreSQL**

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo service postgresql start
```

2. **Create a dev user and database**

```bash
# Switch to the postgres user
sudo -i -u postgres
psql

# In the psql prompt - grant appropriate privileges:

CREATE USER mahjong_user WITH PASSWORD 'mahjong_pass'; # or any password you want - change it in the DATABASE_URL below too
CREATE DATABASE mahjong_dev;
GRANT ALL PRIVILEGES ON DATABASE mahjong_dev TO mahjong_user;

\q
exit
```

3. **Create .env.dev in the project root:**

```env
DATABASE_URL=postgresql+psycopg2://mahjong_user:mahjong_pass@localhost:5432/mahjong_dev
```

4. **Run the FastAPI server**

```bash
make start
```

with optional seeding

```bash
make seed-dbs
```
