# Use the official Python image as a base image
FROM alpine:3.19.1

# Set the working directory in the container
WORKDIR /app

RUN apk add py3-pip tzdata

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
#RUN pip install --upgrade python-pip

RUN python3 -m venv venv && . venv/bin/activate
RUN venv/bin/pip install -r requirements.txt


# Copy the rest of the application code into the container
COPY . .

# Expose the port that your Django app will run on
EXPOSE 8000

RUN cd mysafe
# Define the command to run your application
CMD ["venv/bin/python", "mysafe/manage.py", "runserver", "0.0.0.0:8000"]
