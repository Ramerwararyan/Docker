


# Step 1: Use an official Python base image from Docker Hub
FROM python:3.9-slim

# Step 2: Set a working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements.txt (or your dependencies file) to the container
COPY requirements.txt /app/

# Step 4: Install the Python dependencies (e.g., Flask)
#RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy your application code into the container
COPY . /app/

# Step 6: Expose the port the app will run on (default Flask port is 5000)
#EXPOSE 5000

# Step 7: Set the command to run your application
CMD ["python", "app.py"]
