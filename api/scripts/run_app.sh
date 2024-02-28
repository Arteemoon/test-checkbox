aerich upgrade

echo 'Migration apply'

uvicorn main:app --reload --port 8000 --host 0.0.0.0