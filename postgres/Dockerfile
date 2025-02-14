FROM postgres:latest

# Copy init scripts ke dalam container
COPY init-scripts /docker-entrypoint-initdb.d/

# Set environment variables (opsional, bisa diatur di Kubernetes juga)
ENV POSTGRES_USER=haidhi
ENV POSTGRES_PASSWORD=haidhi
ENV POSTGRES_DB=patient_database

EXPOSE 5432
