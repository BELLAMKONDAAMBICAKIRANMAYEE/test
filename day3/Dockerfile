FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]

#build and start everything
#docker compose up --build 

#docker compose up --build -d



#see logs
#docker compose logs app
#docker compose logs -f app
#docker ps
#docker ps -a
#docker compose up --build
#stop everything
#docker compose down

#elastic bean-cli
#amplify