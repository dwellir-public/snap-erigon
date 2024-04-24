#!/usr/bin/env python3

import requests
import json

HEADERS = {'Content-Type': 'application/json'}

def rpc_request(method: str, params: list = [], req_id: int = 67):
    """
    Sends a JSON-RPC request to the specified Ethereum node.

    Args:
    - method (str): The JSON-RPC method to call.
    - params (list): The parameters for the JSON-RPC method.
    - req_id (int): The ID for the JSON-RPC request.

    Returns:
    - dict: The JSON response from the server.
    """
    data = {
        'jsonrpc': '2.0',
        'method': method,
        'params': params,
        'id': req_id
    }
    try:
        response = requests.post('http://localhost:8545', json=data, headers=HEADERS, timeout=5)
        response.raise_for_status()  # Raises an exception for HTTP errors
        return response.json()
    except requests.RequestException as e:
        return {'error': str(e)}

def main():
    print("Protocol Version:")
    print(rpc_request('eth_protocolVersion', req_id=67))

    print("Current price per gas in wei:")
    print(rpc_request('eth_gasPrice', req_id=73))

    print("Chain ID:")
    print(rpc_request('eth_chainId', req_id=67))

    print("Most recent block:")
    print(rpc_request('eth_blockNumber', req_id=83))

    print("Storage at position:")
    print(rpc_request('eth_getStorageAt', ["0x295a70b2de5e3953354a6a8344e616ed314d7251", "0x0", "latest"],req_id=1))


if __name__ == '__main__':
    main()
