
# syntax=docker/dockerfile:1


FROM python:3.10-slim
WORKDIR /cloudpulse
COPY . .
RUN pip install --upgrade pip && pip3 install Flask requests
CMD ["python3", "app.py"]
EXPOSE 5000
