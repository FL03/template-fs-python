FROM rust:latest as base

RUN apt-get update -y && apt-get upgrade -y

FROM base as langspace

RUN apt-get install -y \
    node

RUN rustup default nightly && \
    rustup target add wasm32-unknown-unknown wasm32-wasi --toolchain nightly

FROM langspace as builder-base

RUN npm install -g wasm-pack

FROM builder-base as builder

ADD . /workspace
WORKDIR /workspace

COPY . .
RUN npm install && npm run build

FROM builder as runner

ENV MODE="production"

EXPOSE 3000

CMD ["npm", "run", "start"]
