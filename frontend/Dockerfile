FROM node:latest as builder-base

RUN apt-get update -y && apt-get upgrade -y

FROM builder-base as builder

ADD . /workspace
WORKDIR /workspace

COPY . .
RUN npm install && npm run build

FROM builder as development

EXPOSE 4173
EXPOSE 5173

CMD ["npm", "run", "dev", "--host"]

FROM builder as preview

EXPOSE 4173
EXPOSE 5173

CMD ["npm", "run", "preview", "--host"]