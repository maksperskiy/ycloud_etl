zip:
	rm -fr ./.vscode && rm -fr etl.zip && zip -r etl.zip ./* -x /docs/* /.git/
