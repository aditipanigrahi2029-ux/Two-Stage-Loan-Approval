
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY api.py app.py loan.py start.py ./

COPY data/stage_1_rf_classifier_pipeline.pkl data/
COPY data/stage_2_rf_regression_pipeline.pkl data/

EXPOSE 8501

CMD ["python", "start.py"]
