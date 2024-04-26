#!/bin/bash

# Choose main IP adress and custom token for cluster initialization.
k3s_server_IP="YOUR_K3S_SERVER_IP"
k3s_custom_token="YOUR_K3S_CUSTOM_TOKEN"

# Function for K3S installation, when the programme is not installed yet.
install_k3s() {
    if [[ "$(hostname)" == master1 ]]; then
        curl -sfL https://get.k3s.io | sh -s - server \
              --token ${k3s_custom_token} \               
              --cluster-init \
              --node-taint CriticalAddonsOnly=true:NoExecute \
              --write-kubeconfig-mode "0644" \
              --disable servicelb 

    elif [[ "$(hostname)" == master* ]]; then
        curl -sfL https://get.k3s.io | sh -s - server \
              --token ${k3s_custom_token} \
              --server https://${k3s_server_IP}:6443 \
              --node-taint CriticalAddonsOnly=true:NoExecute \

    elif [[ "$(hostname)" == worker* ]]; then
        curl -sfL https://get.k3s.io | K3S_TOKEN=${k3s_custom_token} sh -s - agent --server https://${k3s_server_IP}:6443

    else
        echo "Unknown node type. Cannot install k3s."
    fi
}

# Find out, whether K3S is installed. If yes, K3S will be reinstalled.
if command -v k3s &> /dev/null; then
    echo "k3s is installed."

    # Find out, whether it is master or worker node.
    if [[ "$(hostname)" == master* ]]; then
        echo "This is a k3s server node."
        echo "Uninstalling k3s server..."
        sudo /usr/local/bin/k3s-server-uninstall.sh

    elif [[ "$(hostname)" == worker* ]]; then
        echo "This is a k3s agent node."
        echo "Uninstalling k3s agent..."
        sudo /usr/local/bin/k3s-agent-uninstall.sh

    else
        echo "Unknown node type. Cannot uninstall k3s."
    fi

    # Installation function start
    install_k3s
else
    echo "k3s is not installed."
    echo "Installing k3s..."

    # Installation function start
    install_k3s
fi
