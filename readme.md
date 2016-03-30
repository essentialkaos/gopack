## GoPack

`gopack` is simple tool for packing go packages sources. This utility downloads package sources with all dependencies and pack into tar.bz2 archive.

#### Usage demo

[![asciicast](https://asciinema.org/a/40694.png)](https://asciinema.org/a/40694)

#### Installation

###### From ESSENTIAL KAOS Public repo for RHEL6/CentOS6

```bash
yum install -y http://release.yum.kaos.io/i386/kaos-repo-6.8-0.el6.noarch.rpm
yum install gopack
```

###### From github repo

```bash
wget https://raw.githubusercontent.com/essentialkaos/gopack/master/SOURCES/gopack
chmod +x gopack
sudo mv gopack /usr/bin/gopack
```

#### Usage

```
Usage: gopack options package-path

Options

  --output, -v filename    Output file name (without extension)
  --version, -v version    Package version
  --revision, -r revision  Target revision (will be set after sources fetching)
  --branch, -b branch      Target branch (will be set after sources fetching)
  --tag, -t tag            Target tag (will be set after sources fetching)
  --tmp, -T path           Path to temporary directory (/tmp by default)
  --verbose, -V            Verbose output
  --help, -h               Show this help message

Examples

  gopack -v 1.0.1 github.com/essentialkaos/ssllabs_client
  Pack sources for version 1.0.1 and save result as ssllabs_client-1.0.1.tar.bz2

  gopack -o ssllabs-client-1.0.1 github.com/essentialkaos/ssllabs_client
  Pack sources for version 1.0.1 and save result as ssllabs-client-1.0.1.tar.bz2

  gopack -o ssllabs-client-1.0.1 -t v1.0.1 github.com/essentialkaos/ssllabs_client
  Fetch sources with tag v1.0.1, pack sources for version 1.0.1 and save result 
  as ssllabs-client-1.0.1.tar.bz2

```

#### License

[EKOL](https://essentialkaos.com/ekol)
