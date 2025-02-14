# Use Python as base
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy requirements.txt first to leverage Docker caching
COPY ./requirements.txt /app/requirements.txt

# Copy application files
COPY ./app /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5070

# Run the application
CMD ["python", "main.py"]
