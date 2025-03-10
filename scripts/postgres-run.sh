#! /bin/bash

docker run --name postgres \
       -e POSTGRES_USER="$DATAREADER_PG_USER" \
       -e POSTGRES_PASSWORD="$DATAREADER_PG_PASSWORD" \
       -e POSTGRES_DB="$DATAREADER_PG_DATABASE" \
       -p 5432:5432 \
       -d postgres
