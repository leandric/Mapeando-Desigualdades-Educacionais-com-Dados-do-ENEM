.PHONY: airflow-init up-airflow

airflow-init:
	@if [ ! -d "venv" ]; then \
		echo "Criando ambiente virtual..."; \
		python3 -m venv venv; \
	fi
	@echo "Ativando ambiente virtual e configurando Airflow..."
	@mkdir -p dags data
	@. venv/bin/activate && \
	export AIRFLOW_HOME=/home/leandric/Documents/Mapeando-Desigualdades-Educacionais-com-Dados-do-ENEM/Airflow && \
	AIRFLOW_VERSION=3.0.2 && \
	PYTHON_VERSION="$$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')" && \
	CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-$${AIRFLOW_VERSION}/constraints-$${PYTHON_VERSION}.txt" && \
	pip install "apache-airflow==$${AIRFLOW_VERSION}" --constraint "$${CONSTRAINT_URL}" && \
	if [ -f requirements.txt ]; then \
		echo "Instalando dependências do requirements.txt..."; \
		pip install -r requirements.txt; \
	fi

up-airflow:
	@echo "Iniciando o Airflow em modo standalone..."
	@export AIRFLOW_HOME=/home/leandric/Documents/Mapeando-Desigualdades-Educacionais-com-Dados-do-ENEM/Airflow && \
	. venv/bin/activate && \
	airflow standalone
