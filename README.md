## Usage

Run the application:

    make run

And open it in the browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

Run tests:

    make test

## Alternative

If you are not able to run make then run the following:

    virtualenv --python=python3 venv && venv/bin/python setup.py develop
    FLASK_APP=simple_shortener SIMPLE_SHORTENER_SETTINGS=../settings.cfg venv/bin/flask run

## Prerequisites

This is built to be used with Python 3. Update `Makefile` to switch to Python 2 if needed.

Some Flask dependencies are compiled during installation, so `gcc` and Python header files need 
to be present.
For example, on Ubuntu:

    apt install build-essential python3-dev
    
## Design choices

Below are a few design choices which have been made and the justification.

When a url is submitted to be shortened a new alias is created even if that url is already stored.
This was done to allow analytics and deletion of the aliases by the user in the future.

Aliases are generated randomly instead of sequentially. The disadvantage of this is that we might
create an alias is already used (even if this is very unlikely given that there are 64 ^ 8 options)
but the advantage is that an attacker can't sequentially visit all of the shortened urls.

## Scalability

TinyDB was used because it does not require any external software which makes this project easy 
to run. To scale this service out TinyDB can be replaced with another NoSQL database. This is 
preferred over an SQL database because we don't make any complex queries and don't use transactions
or any other ACID properties. The database can be further sharded based on the alias.

A simple cache is used but to improve the performance this should be replaced by a more robust 
cache such as Memcached. To further reduce cache misses a path based load balancing strategy can 
be used. 

Given that the service is stateless it will be possible to scale it horizontally without losing 
performance.