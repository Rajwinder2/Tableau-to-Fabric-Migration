FROM python:3.10-slim
# Standard practice is to use /app inside the container
WORKDIR /app 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy the app.py from your local folder to the /app folder in the container
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]