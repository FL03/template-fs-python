# FL03/pzzld-eth-app

[![Clippy](https://github.com/FL03/pzzld-eth-app/actions/workflows/clippy.yml/badge.svg)](https://github.com/FL03/pzzld-eth-app/actions/workflows/clippy.yml)
[![Desktop](https://github.com/FL03/pzzld-eth-app/actions/workflows/desktop.yml/badge.svg)](https://github.com/FL03/pzzld-eth-app/actions/workflows/desktop.yml)
[![Docker](https://github.com/FL03/pzzld-eth-app/actions/workflows/docker.yml/badge.svg)](https://github.com/FL03/pzzld-eth-app/actions/workflows/docker.yml)
[![Rust](https://github.com/FL03/pzzld-eth-app/actions/workflows/rust.yml/badge.svg)](https://github.com/FL03/pzzld-eth-app/actions/workflows/rust.yml)

***

pzzld-eth-app

## Getting Started

### Building from the Source

Make sure you have rust installed on your host system

#### *Clone the repository*

```bash
git clone https://github.com/FL03/pzzld-eth-app
```

#### *Setup the environment*

```bash
cargo xtask setup
```

#### *Start the application*

```bash
cargo xtask start
```

### Docker

Make sure you have docker installed on the target system

#### *Pull the image*

```bash
docker pull jo3mccain/pzzld-ui:latest
```

#### *Build the image locally (optional)*

```bash
docker buildx build --tag jo3mccain/pzzld-ui:latest .
```

#### *Run the image*

```bash
docker run -p 3000:3000 jo3mccain/pzzld-ui:latest
```

## Usage

### Builder (xtask)

```bash
    cargo xtask -h 
```

## Contributors

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

- [Apache-2.0](https://choosealicense.com/licenses/apache-2.0/)
- [MIT](https://choosealicense.com/licenses/mit/)
