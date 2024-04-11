# Erigon - snap

Basically the erigon service built as a snap.

## Building the snap

Clone the repo, then build with snapcraft

```
sudo snap install snapcraft --classic
cd snap-erigon
snapcraft pack --use-lxd --debug --verbosity=debug # Takes some time.
```

## Releasing

When a commit is made to the main branch a build will start in launchpad and if successful release to the edge channel.
To promote further follow the instructions in [this document](TESTING.md)

Promoting can be done either from [this webpage](https://snapcraft.io/erigon/releases)
or by running
`snapcraft release erigon <revision> <channel>`

## System requirements

* For an Archive node of Ethereum Mainnet we recommend >=3TB storage space: 1.8TB state (as of March 2022),
  200GB temp files (can symlink or mount folder `<datadir>/temp` to another disk). Ethereum Mainnet Full node (
  see `--prune*` flags): 400Gb (April 2022).

* Goerli Full node (see `--prune*` flags): 189GB on Beta, 114GB on Alpha (April 2022).

* Gnosis Chain Archive: 370GB (January 2023).

* Polygon Mainnet Archive: 5TB. (April 2022). `--prune.*.older 15768000`: 5.1Tb (Sept 2023). Polygon Mumbai Archive: 1TB. (April 2022).

SSD or NVMe. Do not recommend HDD - on HDD Erigon will always stay N blocks behind chain tip, but not fall behind.
Bear in mind that SSD performance deteriorates when close to capacity.

RAM: >=16GB, 64-bit architecture.

[Golang version >= 1.19](https://golang.org/doc/install); GCC 10+ or Clang; On Linux: kernel > v4

<code>🔬 more details on disk storage [here](https://erigon.substack.com/p/disk-footprint-changes-in-new-erigon?s=r)
and [here](https://ledgerwatch.github.io/turbo_geth_release.html#Disk-space).</code>

## Install snap

`sudo snap install <snap-file> --devmode`
or from snap store
`sudo snap install erigon`

### Configuration

#### service-args

default=--base-path=$SNAP_COMMON/erigon_base --name=<hostname>

For available arguments see  https://github.com/ledgerwatch/erigon.git
The value set here will be passed to the Erigon binary with a few exceptions listed below. 
* --name defaults to the systems hostname the first time the snap is installed.
* --base-path is always set by the snap to `$SNAP_COMMON/erigon_base` and is not allowed to be configured.

Example:

    sudo snap set erigon service-args="--name=my-westend-node --chain=westend"

#### endure

default=false

If true the Erigon service will not be restarted after a snap refresh.
Note that the Erigon service will still be restarted as the result of changing service-args, etc.

Use this when restarts should be avoided e.g. when running a validator.

### Start the service

`sudo snap start erigon`

### Check logs from erigon

`sudo snap logs erigon -f`

### Stop the service

`sudo snap stop erigon`

### Alternatively - use systemd

`sudo systemctl <stop|start> snap.erigon.erigon.service`
