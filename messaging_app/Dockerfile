FROM python:3.10
# set working Directory
WORKDIR /app

# copy requirments.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app code
COPY . .

# Expose the port Django runs on
EXPOSE 8000

# Define the default command to run the app (can be customized)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

