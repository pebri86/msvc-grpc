package config

import (
	"fmt"

	"github.com/jmoiron/sqlx"
	_ "github.com/lib/pq"
)

var DB *sqlx.DB

func ConnectDB() *sqlx.DB {
	DB = getDBConnection()

	return DB
}

func getDBConnection() *sqlx.DB {
	var dbConnectionStr string

	dbConnectionStr = fmt.Sprintf(
		"host=%s port=%d dbname=%s user=%s password=%s sslmode=disable",
		"localhost",
		5432,
		"grpc_auth",
		"root",
		"root",
	)

	db, err := sqlx.Open("postgres", dbConnectionStr)
	if err != nil {
		panic(err)
	}

	err = db.Ping()
	if err != nil {
		panic(err)
	}

	db.SetMaxIdleConns(1)
	db.SetMaxOpenConns(5)

	fmt.Println("Connected to DB")
	return db
}