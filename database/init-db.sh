#!/bin/bash
set -e

# Check if the user exists
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --tuples-only --command "SELECT 1 FROM pg_user WHERE usename = '$POSTGRES_USER'" | grep -q 1 || psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --command "CREATE USER \"$POSTGRES_USER\" WITH PASSWORD '$POSTGRES_PASSWORD'";

# Check if the database exists
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --tuples-only --command "SELECT 1 FROM pg_database WHERE datname = '$POSTGRES_DATABASE'" | grep -q 1 || psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --command "CREATE DATABASE \"$POSTGRES_DATABASE\"";
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --command "GRANT ALL PRIVILEGES ON DATABASE \"$POSTGRES_DATABASE\" TO \"$POSTGRES_USER\"";
