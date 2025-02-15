# Use an official Python runtime as a parent image
FROM python:3.10-slim
# Copy the rest of the application code
COPY . .
# Install the requirements 
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
