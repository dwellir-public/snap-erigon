# Preparations for running tests

## Environment Setup
- Operating System: Ubuntu 20.04 LTS
- Snap Version: Erigon v2.59.3
- Configuration: Dev mode

## Install the snap:
 ```
 sudo snap install --devmode --dangerous path/to/your/snapfile.snap
```

## Make sure service is running
- ```
  sudo snap services erigon
  ```
- If the service `erigon.erigon` is disabled/inactive, then run the following commands to start it:
  ```
  sudo snap enable erigon.erigon
  ```
- Then,
  ```
  sudo snap start erigon.erigon
  ```
- List the services again and you'll the active service.
  ```
  sudo snap services erigon
  ```

## Test Cases
### Test Case 1: Starting the Node
#### Objective: Ensure that the Erigon node starts correctly with the necessary configurations.

#### Procedure:

- Run the following command to start Erigon:
```
sudo snap run erigon.erigon --datadir=dev --chain=dev --private.api.addr=localhost:9090 --mine
```

- Observe the output and check for any errors related to the startup process.

####  Expected Results:

- The node starts without errors.
- Logs indicate that HTTP APIs are starting on port 8545.
- The miner starts and begins to mine new blocks.

#### Screenshot:
Result may look similar like this:
![StartNodeLogs](https://github.com/dwellir-public/snap-erigon/assets/116648836/67398f7e-b494-4752-ba5a-0e2fbda70c9c)

### Test Case 2: RPC Interaction
#### Objective: Verify the RPC server's responsiveness and correctness of the data returned.

#### Procedure:

Test basic RPC functionality by fetching the `chainId`:
- Open the terminal while your node is running and run the following curl command:
```
  curl -X POST -H "Content-Type: application/json" --data '{"jsonrpc": "2.0", "method": "eth_chainId", "params": [], "id":1}' localhost:8545
```
- You should get something similar like this as result:
```
  {"jsonrpc":"2.0","id":1,"result":"0x539"}
```
### Test Case 3: Simultaneous Commands and Log Monitoring
#### Objective: Test the node's ability to handle simultaneous operations and monitor the logs for real-time feedback and enode information.

#### Procedure:

- In one terminal, start the Erigon node as described in Test Case 1.
```
sudo snap run erigon.erigon --datadir=dev --chain=dev --private.api.addr=localhost:9090 --mine
```
- In a second terminal, start another Erigon instance or another component, observing port management and API access:
```
sudo snap run erigon.erigon --datadir=dev2 --private.api.addr=localhost:9091 --http.api=eth,erigon,web3,net,debug,trace,txpool,parity --torrent.port=42071
```
- Monitor both terminals for log outputs, specifically looking for enode information which can be used for peer connections.
- Enode may look like this:
  ![enode](https://github.com/dwellir-public/snap-erigon/assets/116648836/d81f46a8-d085-402f-a993-2fde3105d39f)

### Test Case 4: Peer Connectivity Using enode
#### Objective: Use enode information to manually add peers and verify connectivity.

#### Procedure:

- Use the enode URL from the logs of the first node to add it as a peer to the second node using the admin_addPeer RPC method:
- For `admin_addPeer`:
  ```
  curl -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0", "method":"admin_addPeer", "params":["<enode-url>"],"id":1}' http://localhost:<RPC-port>```
For example:

```
curl -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"admin_addPeer","params":["enode://970a1acefc271198b44e166beef2ccd57ea05cc4b2cada2673011e4cd809182bebf5ba447abd1c48d69b57234ce02e096756d635645d4818d79e22090738755b@127.0.0.1:30305?discport=0"],"id":1}' http://localhost:8545
```
Result:
```
{"jsonrpc":"2.0","id":1,"result":true}
```

- Similarly, verify the connection by listing the peers:
```
  curl -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0", "method":"admin_peers","params":[],"id":1}' http://localhost:<RPC-port>
```

#### Expected Results:

- The admin_addPeer command should return true, confirming the peer was added.
- The admin_peers command should list the newly added peer, verifying connectivity.

### Check node status
- You can chech thr status of the node by running te script like below:
```
python3 chekc_node_status.py
```
Expected results may look like this:
![CheckNodeStatus](https://github.com/dwellir-public/snap-erigon/assets/116648836/01dadd35-42a9-4a16-933a-02fe33d2468d)


# Edge tests
TODO: How to test the snap will be added later. 

# Beta tests
TODO: How to test the snap will be added later. 

# Candidate tests
TODO: How to test the snap will be added later. 

# Stable tests
TODO: How to test the snap will be added later. 

### Test initial installation
TODO: How to test the snap will be added later. 

### Test setting --base-path
TODO: How to test the snap will be added later. 

### Test downgrade
TODO: How to test the snap will be added later. 

### Test endure
TODO: How to test the snap will be added later. 

### Test Kusama, Westend and Rococo
TODO: How to test the snap will be added later. 