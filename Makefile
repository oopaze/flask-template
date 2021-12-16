ifneq (,$(wildcard ./.env))
    include .env
    export
endif

initialize_database:
	flask db init
	flask db migrate
	flask db upgrade
	
purge_database:
ifeq ($(FLASK_ENV), production)
		echo "You cannot do it in a production environment"
else ifeq ($(FLASK_ENV), '')
		echo "You cannot do it in a production environment"
else
		rm -rf migrations;
		ls | grep -P ".*storage\.db" | xargs -d"\n" rm
endif