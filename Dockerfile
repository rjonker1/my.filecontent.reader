FROM python:3.6-alpine

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Log files to read
RUN mkdir -p /usr/src/app/files
ADD /filereader/files/2018-05-25-UsBankPivotPrivate.log /usr/src/app/2018-05-25-UsBankPivotPrivate.log
ADD /filereader/files/2018-05-24-UsBankPivotPrivate.log /usr/src/app/2018-05-24-UsBankPivotPrivate.log
# RUN cd /usr/src/app/files/2018-05-25-UsBankPivotPrivate.log 


# Bundle app source
COPY . /usr/src/app

ENTRYPOINT [ "python", "filereader" ]
