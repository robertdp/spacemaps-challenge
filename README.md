# spacemaps-challenge

Checkout the project:

```sh
git clone https://github.com/robertdp/spacemaps-challenge.git
cd spacemaps-challenge
```

Build the Docker image using the tag `spacemaps-challenge`:

```sh
make build
```

Run the project on the sample input file:

```sh
make run
```

You can run it with custom arguments using:

```sh
docker run --rm spacemaps-challenge [source] [size of results]
```

See the Makefile for more details.
