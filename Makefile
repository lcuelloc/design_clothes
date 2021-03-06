.PHONY: install upgrade run shell cove clean-test clean-celery test-all

install:
	pip install -r requirements/local.txt

upgrade:
	pip install --upgrade -r requirements/local.txt

run:
	python manage.py runserver_plus 192.168.1.86:8001


worker:
	celery --app=v1.taskapp.celery worker -l DEBUG

beat:
	celery --app=v1.taskapp.celery beat -l DEBUG

shell:
	python manage.py shell_plus

clean-celery:
	rm -f celerybeat-schedule

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -fr

