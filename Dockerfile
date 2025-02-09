# Use official Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /genre_app

# Copy all files to the container
COPY . /genre_app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit's default port
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "genre_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
