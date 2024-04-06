# FROM python:3.7
# COPY . /app
# WORKDIR /app
# RUN pip install -r requirements.txt
# EXPOSE $PORT
# CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app


FROM python:3.7
RUN pip install streamlit
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
