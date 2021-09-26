# syntax=docker/dockerfile:1
FROM node:14.15.4-alpine3.11

RUN apk add --no-cache python2 alpine-sdk
WORKDIR /app/frontend
COPY . /app/frontend/

RUN npm install

EXPOSE 8080
CMD ["npm", "start"]