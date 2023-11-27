FROM node:21.2.0-alpine3.17 as build
WORKDIR /app
COPY ./package*.json ./
RUN npm install
COPY . .
RUN npm run build
FROM nginx:alpine
COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist/client /usr/share/html
EXPOSE 80
