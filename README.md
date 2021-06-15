# Flask Test Web App

## Setup & Installtion

```bash
git clone <repo-url>
```

DB should be installed for the app: 

```bash
docker run --name postgres -e POSTGRES_PASSWORD={DEFINE_PASSWORD} -p 5432:5432 -d postgres
```
Install requirements
```bash
pip3 install -r requirements.txt
```

## Running The App

```bash
python main.py
```

## Viewing The App

Go to `http://127.0.0.1:5000`
