#use lightweight image of python
FROM python:3.11-slim

#setting up working directory
WORKDIR /app

#copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

#expose port
EXPOSE 5000

#run application
CMD ["python", "app.py"]


