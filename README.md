<p align="center"><a href="#readme"><img src="https://gh.kaos.st/gopack.svg"/></a></p>

<p align="center">
  <a href="https://github.com/essentialkaos/gopack/actions"><img src="https://github.com/essentialkaos/gopack/workflows/CI/badge.svg" alt="GitHub Actions Status" /></a>
  <a href="#license"><img src="https://gh.kaos.st/apache2.svg"></a>
</p>

<p align="center"><a href="#usage-demo">Usage demo</a> • <a href="#installation">Installation</a> • <a href="#usage">Usage</a> • <a href="#build-status">Build Status</a> • <a href="#license">License</a></p>

<br/>

`gopack` is a simple tool for packing Go package sources. This utility downloads package sources with all dependencies (through `glide`, `dep`, `go mod` or `go get`) and packs them into an archive.

`gopack-build` is a simple tool for building binaries from sources archive.

### Usage demo

#### `gopack`

[![demo](https://gh.kaos.st/gopack-1100.gif)](#usage-demo)

#### `gopack-build`

[![demo](https://gh.kaos.st/gopack-build-120.gif)](#usage-demo)

### Installation

#### From ESSENTIAL KAOS Public repository

```
sudo yum install -y https://yum.kaos.st/get/$(uname -r).rpm
sudo yum install gopack gopack-build
```

#### From GitHub repository

```bash
curl -o gopack https://kaos.sh/gopack/SOURCES/gopack
curl -o gopack-build https://kaos.sh/gopack/SOURCES/gopack-build
chmod +x gopack gopack-build
sudo mv gopack gopack-build /usr/bin/
```

Also, you can use the latest version of utilities without installation:

```bash
bash <(curl -fsSL https://kaos.sh/gopack/SOURCES/gopack) # pass options here
bash <(curl -fsSL https://kaos.sh/gopack/SOURCES/gopack-build) # pass options here
```

### Usage

#### `gopack`

```
Usage: gopack {options} package-path

Options

  --output, -o filename       Output file name
  --version, -v version       Package version
  --revision, -r revision     Target revision
  --branch, -b branch         Target branch
  --tag, -t tag               Target tag
  --preserve-vendor, -pv      Preserve old vendor data (unsafe, use with caution)
  --tmp, -T path              Path to temporary directory (/tmp by default)
  --verbose, -V               Verbose output
  --no-color, -nc             Disable colors in output
  --help, -h                  Show this help message

Examples

  gopack -v 1.0.1 github.com/essentialkaos/ssllabs_client
  Pack sources for version 1.0.1 and save result as ssllabs_client-1.0.1.tar.bz2

  gopack -o ssllabs-client-1.0.1.tar.bz2 github.com/essentialkaos/ssllabs_client
  Pack sources for version 1.0.1 and save result as ssllabs-client-1.0.1.tar.bz2

  gopack -o ssllabs-client-1.0.1.tgz -t v1.0.1 github.com/essentialkaos/ssllabs_client
  Fetch sources with tag v1.0.1, pack sources for version 1.0.1 and save result 
  as ssllabs-client-1.0.1.tgz

```

#### `gopack-build`
```
Usage: gopack-build {options} file

Options

  --output, -o directory     Output directory
  --tmp, -T path             Path to temporary directory (/tmp by default)
  --no-color, -nc            Disable colors in output
  --about                    Show information about version
  --help, -h                 Show this help message

Examples

  gopack yo-0.2.0.tar.bz2
  Build binary from local archive with sources

  gopack -o /home/user https://github.com/essentialkaos/yo/releases/download/v0.2.0/yo-0.2.0.tar.bz2
  Build binary from remote archive with sources and save result
  to directory /home/user

```

### Build Status

| Branch | Status |
|--------|--------|
| `master` | [![CI](https://github.com/essentialkaos/gopack/workflows/CI/badge.svg?branch=master)](https://github.com/essentialkaos/gopack/actions) |
| `develop` | [![CI](https://github.com/essentialkaos/gopack/workflows/CI/badge.svg?branch=develop)](https://github.com/essentialkaos/gopack/actions) |

### License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
