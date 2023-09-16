# Use an official Python runtime as the base image
FROM python:3.11.4

# Set the working directory in the container
WORKDIR /app

# Install Tesseract and other dependencies
RUN pip install --upgrade pip

# Copy the project files to the container
COPY app/ /app
COPY requirements.txt /app

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your application will run on (if applicable)
EXPOSE 8000

# Define the command to run your application
CMD ["python", "app.py"]