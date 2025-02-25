# Use an official Python runtime as a parent image
FROM python:3.9

# Install Tkinter dependencies
RUN apt-get update && apt-get install -y python3-tk

# Set the working directory inside the container
WORKDIR /app

# Copy the application code inside the container
COPY . /app

# Command to run the Tkinter application
CMD ["python", "testpython.py"]
