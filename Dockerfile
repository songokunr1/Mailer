# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . .

# Set the environment variables
ENV email_portfolio=${email_portfolio}
ENV assistent_login=${assistent_login}
ENV assistent_password=${assistent_password}

# Expose the Flask app port
EXPOSE 8888

# Run the Flask application
CMD ["python", "app.py"]