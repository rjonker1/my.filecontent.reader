FROM python:3.6-alpine

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Log files to read
RUN mkdir -p /usr/src/app/files
ADD /filereader/files/datafile1 /usr/src/app/datafile1
ADD /filereader/files/datafile2 /usr/src/app/datafile2

# Bundle app source
COPY . /usr/src/app

ENTRYPOINT [ "python", "filereader" ]
