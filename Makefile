PYTHONPATH=./
IMAGE_NAME=tes-etl
CONTAINER_NAME=tes-etl-container
FORCE?=false
login:
	cat key.json | docker login --username json_key --password-stdin cr.yandex
debug:
	PYTHONPATH=${PYTHONPATH} uvicorn --reload src.main:app
image:
	docker build -t ${IMAGE_NAME} -f Dockerfile .
container:
	docker run --env-file .env -p 8080:8080 -t ${IMAGE_NAME}
zip:
	rm -fr ./.vscode && rm -fr etl.zip && zip -r etl.zip ./src/functions ./src/utils ./requirements.txt -x /docs/* /.git/
generate-migration:
	PYTHONPATH=${PYTHONPATH} alembic -c alembic.ini revision --autogenerate
migrate:
	PYTHONPATH=${PYTHONPATH} alembic -x force=${FORCE} -c alembic.ini upgrade +1
downgrade:
	PYTHONPATH=${PYTHONPATH} alembic -x force=${FORCE} -c alembic.ini downgrade -1