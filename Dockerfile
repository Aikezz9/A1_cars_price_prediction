# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the Flask port (5000 by default)
EXPOSE 5000

# Command to run the Flask app
CMD ["python3", "app.py"]
