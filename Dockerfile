# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the app runs on
EXPOSE 1336

# Set the environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_PORT=1336
ENV FLASK_ENV=development

# Run the application
CMD ["python", "app.py"]
