# Use Python 3.9 slim image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first to leverage Docker caching
COPY backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the model directory (FIX)
COPY models/ models/

# Copy the rest of the application files
COPY backend/ .

# Run the application
CMD ["python", "app.py"]
