overview_alluredir = allure-results
kata_alluredir = allure-results

overview_test:
	pytest pytest_overview --alluredir=${overview_alluredir}

kata_test:
	pytest fizz_buzz_kata --alluredir=${kata_alluredir}

test:
	make overview_test
	make kata_test

report:
	make test
	allure generate ${overview_alluredir} -o allure-report --clean