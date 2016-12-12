FROM node:7.2.1
WORKDIR /app/
RUN npm install -g yarn
COPY package.json yarn.lock /app/
RUN yarn
COPY .env /app/
COPY public /app/public/
COPY src /app/src/
RUN yarn run build
ENTRYPOINT ["yarn", "pushstate-server", "build/"]
