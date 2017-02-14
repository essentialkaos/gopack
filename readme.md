## GoPack [![Code Climate](https://codeclimate.com/github/essentialkaos/gopack/badges/gpa.svg)](https://codeclimate.com/github/essentialkaos/gopack) [![License](https://gh.kaos.io/ekol.svg)](https://essentialkaos.com/ekol)

`gopack` is simple tool for packing Go package sources. This utility downloads package sources with all dependencies and pack into archive.

### Usage demo

[![demo](https://gh.kaos.io/gopack-112.gif)](#usage-demo)

### Installation

##### From ESSENTIAL KAOS Public repo for RHEL6/CentOS6

```
[sudo] yum install -y https://yum.kaos.io/6/release/i386/kaos-repo-7.2-0.el6.noarch.rpm
[sudo] yum install gopack
```

##### From ESSENTIAL KAOS Public repo for RHEL7/CentOS7

```
[sudo] yum install -y https://yum.kaos.io/7/release/x86_64/kaos-repo-7.2-0.el7.noarch.rpm
[sudo] yum install gopack
```

##### From github repo

```bash
wget https://raw.githubusercontent.com/essentialkaos/gopack/master/SOURCES/gopack
chmod +x gopack
sudo mv gopack /usr/bin/gopack
```

### Usage

```
Usage: gopack {options} package-path

Options

  --output, -o filename      Output file name
  --version, -v version      Package version
  --revision, -r revision    Target revision (will be set after sources fetching)
  --branch, -b branch        Target branch (will be set after sources fetching)
  --tag, -t tag              Target tag (will be set after sources fetching)
  --tmp, -T path             Path to temporary directory (/tmp by default)
  --glide, -G                Use glide for downloading dependencies
  --verbose, -V              Verbose output
  --about                    Show information about version
  --help, -h                 Show this help message

Examples

  gopack -v 1.0.1 github.com/essentialkaos/ssllabs_client
  Pack sources for version 1.0.1 and save result as ssllabs_client-1.0.1.tar.bz2

  gopack -o ssllabs-client-1.0.1.tar.bz2 github.com/essentialkaos/ssllabs_client
  Pack sources for version 1.0.1 and save result as ssllabs-client-1.0.1.tar.bz2

  gopack -o ssllabs-client-1.0.1.tgz -t v1.0.1 github.com/essentialkaos/ssllabs_client
  Fetch sources with tag v1.0.1, pack sources for version 1.0.1 and save result 
  as ssllabs-client-1.0.1.tgz

```

### License

[EKOL](https://essentialkaos.com/ekol)
