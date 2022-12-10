FROM node:18.12.1 as builder-base

RUN apt-get update -y && apt-get upgrade -y

FROM builder-base as builder

ADD . /workspace
WORKDIR /workspace

COPY . .
RUN npm install && npm run build

FROM builder as runner

ENV MODE="production"

EXPOSE 3000

CMD ["npm", "run", "start"]