FROM python:3.11-slim
RUN pip install uv
WORKDIR /app

COPY . /app

RUN uv pip install .  --system


CMD ["python", "main.py"]
