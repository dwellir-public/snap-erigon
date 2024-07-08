# Erigon - snap

Basically the Erigon service built as a snap.

## Building the snap

Clone the repo, then build with snapcraft

```
sudo snap install snapcraft --classic
cd snap-erigon
snapcraft pack --use-lxd --debug --verbosity=debug # Takes some time.
```

The snap currently ships all binaries (this will probably change in the future): 
* abigen 
* bootnode 
* capcli 
* caplin 
* debug  
* devnet  
* downloader  
* erigon         ->  /var/snap/current/bin/erigon
* erigoncustom  
* evm	
* hack  
* integration  
* observer  
* p2psim  
* pics  
* rlpdump  
* rpcdaemon  
* rpctest	
* sentinel  
* sentry  
* silkworm_api	
* snapshots  
* state  
* txpool  
* verkle


## Releasing

When a commit is made to the main branch a build will start in launchpad and if successful release to the edge channel.
To promote further follow the instructions in [this document](TESTING.md)

Promoting can be done either from [this webpage](https://snapcraft.io/erigon/releases)
or by running
`snapcraft release erigon <revision> <channel>`

NOTE: This is not ready at the moment. Realeasing section will be updated once its ready.

## System requirements

System requirements can be found [here](https://github.com/ledgerwatch/erigon)

## Install snap

`sudo snap install <snap-file> --devmode`
or from snap store
`sudo snap install erigon`

### Configuration
TODO
#### service-args

default=--base-path=$SNAP_COMMON/erigon_base --name=<hostname>

For available arguments see [here](https://github.com/ledgerwatch/erigon/blob/devel/DEV_CHAIN.md)
The value set here will be passed to the Erigon binary 
* --http.api=eth,net,web3,debug specifies which JSON-RPC API groups to enable. JSON-RPC is a remote procedure call protocol encoded in JSON. It's used here to specify which groups of RPC methods should be available.
* --txpool.pricelimit=0: This sets the transaction pool price limit to 0.
* --base-path is always set by the snap to `$SNAP_COMMON/erigon_base` and is not allowed to be configured.

Example:

    sudo snap set erigon service-args="--private.api.addr=127.0.0.1:9092"


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
