FROM python:latest
COPY . .
RUN pip3 install -r ./requirements.txt --no-cache-dir
RUN chmod +x main.py
CMD python main.py
