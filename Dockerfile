FROM python:3.7.6

# set a directory for the app
WORKDIR /house_price_prediction

# copy all the files to the container
COPY . /house_price_prediction

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
EXPOSE 5060/tcp
EXPOSE 5060/udp

# run the command to start the app
CMD [ "python", "./app/app.py","-path","./app/model.pickle"]
