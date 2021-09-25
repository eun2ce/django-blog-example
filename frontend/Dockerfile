FROM node:12

WORKDIR /app/frontend
COPY package.json /app/frontend

RUN npm install

EXPOSE 8080
CMD ["npm", "start"]
