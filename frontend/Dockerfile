FROM rust:latest as base

RUN apt-get update -y && apt-get upgrade -y

FROM base as langspace

RUN apt-get install -y \
    nodejs \
    yarn

RUN rustup default nightly && \
    rustup target add wasm32-unknown-unknown wasm32-wasi --toolchain nightly

FROM langspace as builder-base

RUN npm install -g wasm-pack

FROM builder-base as builder

ADD . /workspace
WORKDIR /workspace

COPY . .
RUN npm install && npm run build

FROM builder as development

ENV MODE="production"

EXPOSE 3000
CMD [ "npm", "run", "start" ]

FROM node:lts-alpine as runner

RUN apt-get update -y && apt-get upgrade -y

COPY --chown=55 --from=builder /workspace/build ./build

FROM runner

ENV MODE="production"

EXPOSE 3000
CMD ["node", "build/index.js"]
