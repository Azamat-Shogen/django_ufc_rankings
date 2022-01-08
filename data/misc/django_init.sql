DROP DATABASE IF EXISTS ufc_rankings_db;

-- DROP TABLE IF EXISTS athletes_athlete;
-- DROP TABLE IF EXISTS athletes_weightclass;
-- DROP TABLE IF EXISTS athletes_fighter;

CREATE DATABASE ufc_rankings_db;

DROP TABLE IF EXISTS athletes_fighter;

CREATE TABLE IF NOT EXISTS athletes_fighter(
    id SERIAL PRIMARY KEY,
    athlete_name VARCHAR (200) NOT NULL,
    image_src VARCHAR(240),
    record VARCHAR(200),
    nickname VARCHAR(200),
    weight_class VARCHAR(200)
);


\c ufc_rankings_db

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;