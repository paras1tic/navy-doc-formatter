FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy application files
COPY app /app
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 5070

# Run the application
CMD ["python", "main.py"]
