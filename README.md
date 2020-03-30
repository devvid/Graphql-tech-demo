# GraphQL Tech Demo

Frontend - Simple Angular setup
Backend  - Simple Flask app

GraphQL server and client will be loaded on both front & backend applications.

## Front end
### Startup
```
cd frontent
ng serve
```
### Setup
```
cd frontent
npm install
ng serve
```

## Back end
### Startup
Start script after application is installed
```
cd backend
. venv/bin/activate
export FLASK_APP=src
flask run
```
### Setup
Run the following code blocking before starting up the app for the first time.
```
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=src
flask db init
flask db migrate -m "init"
flask db upgrade
flask run
```
Once setup, inject test data into the database using the following command
(venv)`python seed.py`

## Example
On the following url in the browser
`http://localhost:5000/graphql-query`

Enter the following query
```
{
  allPosts {
    edges {
      node {
        id
      }
    }
  }
}
```

## Notes Secion
In GraphQL what's the meaning of “edges” and “node”?
https://stackoverflow.com/questions/42622912/in-graphql-whats-the-meaning-of-edges-and-node