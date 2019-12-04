<p align="center"><a href="#readme"><img src="https://gh.kaos.st/gopack.svg"/></a></p>

<p align="center">
  <a href="https://travis-ci.com/essentialkaos/gopack"><img src="https://travis-ci.com/essentialkaos/gopack.svg"></a>
  <a href="https://essentialkaos.com/ekol"><img src="https://gh.kaos.st/ekol.svg"></a>
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

#### From ESSENTIAL KAOS Public repo for RHEL6/CentOS6

```
[sudo] yum install -y https://yum.kaos.st/kaos-repo-latest.el6.noarch.rpm
[sudo] yum install gopack gopack-build
```

#### From ESSENTIAL KAOS Public repo for RHEL7/CentOS7

```
[sudo] yum install -y https://yum.kaos.st/kaos-repo-latest.el7.noarch.rpm
[sudo] yum install gopack gopack-build
```

#### From GitHub repository

```bash
wget https://kaos.sh/gopack/SOURCES/gopack
wget https://kaos.sh/gopack/SOURCES/gopack-build
chmod +x gopack gopack-build
[sudo] mv gopack gopack-build /usr/bin/
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
| `master` | [![Build Status](https://travis-ci.com/essentialkaos/gopack.svg?branch=master)](https://travis-ci.com/essentialkaos/gopack) |
| `develop` | [![Build Status](https://travis-ci.com/essentialkaos/gopack.svg?branch=develop)](https://travis-ci.com/essentialkaos/gopack) |

### License

[EKOL](https://essentialkaos.com/ekol)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
