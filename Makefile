migration_create:
	docker exec crypto-api /bin/sh -c 'alembic revision -m "$(message)"'

migration_generate:
	docker exec crypto-api /bin/sh -c 'alembic revision --autogenerate -m "$(message)"'

migration_run:
	docker exec crypto-api /bin/sh -c 'alembic upgrade head'

migration_revert:
	docker exec crypto-api /bin/sh -c 'alembic downgrade -1'