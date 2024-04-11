# Preparations before running tests

Make sure to run the tests in a container or to run `sudo snap remove erigon --purge` before running tests to have a clean environment.

Keep a terminal window open with the logs during the tests using `sudo snap logs erigon -f`

### Check node status
The following steps will be referenced through out this document with `Check node status`.

| Steps                                 | Command                                                                                                                               | Expected result |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Check running version with RPC method | `curl -X POST -H "Content-Type: application/json" -d '{"id":1, "jsonrpc":"2.0", "method": "system_version"}' http://localhost:9933`   | The curl result should show the same version as is shown for the installed snap by running `snap info erigon` |
| Check node health                     | `curl -X POST -H "Content-Type: application/json" -d '{"id":1, "jsonrpc":"2.0", "method": "system_health"}' http://localhost:9933`    | The curl result should show that the node has peers and is syncing |
| Check sync state                      | `curl -X POST -H "Content-Type: application/json" -d '{"id":1, "jsonrpc":"2.0", "method": "system_syncState"}' http://localhost:9933` | Run the curl command twice with a short time between and check that the current block is increased |
| Check sync state                      | `curl -X POST -H "Content-Type: application/json" -d '{"id":1, "jsonrpc":"2.0", "method": "system_chain"}' http://localhost:9933`     | The curl result should show the configured chain (Erigon if not specified in service-args) |

Note: there is a utility script called [check_node_status.py](check_node_status.py) that can be used when running it on the same machine as the snap runs on.

# Edge tests
| Steps                                   | Command                                                                                                                             | Expected result |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Install the Erigon snap               | `sudo snap install erigon --channel=edge`                                                                                         |                 |
| Set --rpc-port in service-args          | `sudo snap set erigon service-args="--name=testing --rpc-port=9933 --prometheus-port=9900 --prometheus-external"` | Check logs that Erigon service was restarted and the new service-args where applied |
| Start Erigon                          | `sudo snap start erigon`                                                                                                          |                 |
| [Check node status](#Check-node-status) | See steps above                                                                                                                     |                 |

# Beta tests

# Candidate tests

# Stable tests

### Test initial installation

| Steps                                   | Command                                                                                                                             | Expected result |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Install the Erigon snap               | `sudo snap install erigon --channel=candidate`                                                                                    |                 |
| Set --rpc-port in service-args          | `sudo snap set erigon service-args="--name=testing --chain=<chain>"`                                                              |                 |
| Start Erigon                          | `sudo snap start erigon`                                                                                                          | Logs appear in log terminal |
| Set --rpc-port in service-args          | `sudo snap set erigon service-args="--name=testing --chain=<chain> --rpc-port=9933 --prometheus-port=9900 --prometheus-external"` | Check logs that Erigon service was restarted and the new service-args where applied |
| [Check node status](#Check-node-status) | See steps above                                                                                                                     |                 |



### Test setting --base-path

| Steps                                  | Command                                                                                                                         | Expected result |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Set --base-path in service-args config | `sudo snap set erigon service-args="--name=testing --rpc-port=9933 --prometheus-port=9900 --prometheus-external --base-path"` | The following should be presented in the terminal: error: cannot perform the following tasks: Run configure hook of "erigon" snap (run hook "configure": base-path is not allowed to pass as a service argument restoring to last used service-args. This path is alywas used instead /var/snap/erigon/common/erigon_base.) |

### Test downgrade

| Steps                                   | Command                                                      | Expected result |
|-----------------------------------------|--------------------------------------------------------------|-----------------|
| Get previous revision                   | `snap info erigon`                                         | The revision is between parentheses. Check the installed one and subtract one |
| Downgrade the Erigon snap             | `sudo snap refresh erigon --revision=<previous-revisison>` |                 |
| [Check node status](#Check-node-status) | See steps above                                              |                 |

### Test endure

| Steps                                   | Command                                                                                                                             | Expected result |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Upgrade to latest version               | `sudo snap refresh erigon`                                                                                                        |                 |
| [Check node status](#Check-node-status) | See steps above                                                                                                                     |                 |
| Enable endure config                    | `sudo snap set erigon endure=true`                                                                                                |                 |
| Downgrade the Erigon snap             | `sudo snap refresh erigon --revision=<previous-revisison>`                                                                        | Check in the logs that the service didn't restart |
| Check running version with RPC method   | `curl -X POST -H "Content-Type: application/json" -d '{"id":1, "jsonrpc":"2.0", "method": "system_version"}' http://localhost:9933` | The curl result should __NOT__ show the same version as is shown for the installed snap by running `snap info polkdaot` |
| Restart the service                     | `sudo snap restart erigon`                                                                                                        | 
| Check running version with RPC method   | `curl -X POST -H "Content-Type: application/json" -d '{"id":1, "jsonrpc":"2.0", "method": "system_version"}' http://localhost:9933` | The curl result should show the same version as is shown for the installed snap by running `snap info polkdaot` |

### Test Kusama, Westend and Rococo

For each of Kusama, Westend and Rococo
1. Clean the environment as described in the [preparation section](#preparations-before-running-tests)
1. Run [edge tests](#test-initial-installation)
