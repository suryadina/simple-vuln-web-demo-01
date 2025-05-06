# Dockerfile
FROM python:3.10-slim

# Install git
RUN apt-get update && apt-get install -y git && apt-get clean

# Clone the repository
RUN git clone https://github.com/suryadina/simple-vuln-web-demo-01 /opt/simple-vuln-web-demo-01

# Set working directory
WORKDIR /opt/simple-vuln-web-demo-01

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 80

# Start the app
CMD ["python", "app.py"]
