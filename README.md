# spacemaps-challenge

This project is split into 3 small sections:

1. Command line parsing
2. Request streaming (over HTTP with gzip)
3. Results collection (using a size-limited priority queue)

There is minimal input validation or error recovery. The requirements are simple enough that these can be skipped here.

## Instructions

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
