# Mahjong API

This is a repository for a Mahjong score tracker. The goal is to have the following features:

- Score your Mahjong hand according to several scoring systems, including Hong-Kong Old Scoring or Chinese International Scoring
- Track the score throughout a game by submitting hands
- Access this through the front-end web app, synced between players here

Placeholders

The live version is hosted on https://mahjong-api.onrender.com/, although the free-tier cold boot can take up to 3 minutes to load - useful initial endpoints include GET `/api` summarising the endpoints, or the OpenAPI auot-generated `/openapi.json` endpoint.

The front end TypeScript React app can be found \_\_\_<!-- TODO -->, with the github profile \_\_\_<!-- TODO --> here

## How to run locally

Firstly, initialise the python virtual environment - on Ubuntu, this is

```bash
source venv/bin/activate
```

Then install python dependencies

```bash
pip install -r requirements.txt
```

Initialise the dev and test databases with

```bash
make setup-dbs
```

Create a file named `.env.test` in the project root with the following content. (You may also specify the PGHOST and PGPORT, or alternatively supply the DATABASE_URL directly)

```env
# .env.test
PGDATABASE=mahjong_test
PGUSER=<yourname>
PGPASSWORD=<yourpassword>


# .env.dev
PGDATABASE=mahjong
PGUSER=<yourname>
PGPASSWORD=<yourpassword>
```

then run the local instance via

```bash
make start
```

that runs the API on default port 8000.

---

4. **Run the FastAPI server**

```bash
make start
```

with optional seeding

```bash
make seed-dbs
```

---

Alembic is used to keep models and db tables in sync, on changing models then follow the following steps.

Compare models to database:

```bash
alembic revision --autogenerate -m "<your-message>"
```

Apply changes:

```bash
alembic upgrade head
```
