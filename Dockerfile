FROM mongo
ADD mongo-seed/mongo-init.js /docker-entrypoint-initdb.d/
