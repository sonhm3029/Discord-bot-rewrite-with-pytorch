FROM python:3.10.1

# set a directory for the app
WORKDIR /usr/src/app

# copy all files to container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number container should expose
EXPOSE 5000

# run command
CMD ["python", "src/app.py"]