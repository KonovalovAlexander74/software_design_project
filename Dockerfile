FROM python:latest
COPY . .
pip3 install -r /app/requirements.txt --no-cache-dir
RUN pip3 install -r ./requirements.txt --no-cache-dir
RUN chmod +x main.py
CMD python main.py
