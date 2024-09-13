#!/bin/bash

# Set base directories
LETSENCRYPT_DIR="/etc/letsencrypt" # Default config directory for Certbot
LIB_DIR="/var/lib/letsencrypt"     # Default working directory

# Domain and certbot settings
DOMAIN="your-domain.com"           # Replace with your actual domain
WILDCARD="*.${DOMAIN}"             # Wildcard subdomain for the certificate
CHALLENGE="dns"                    # Preferred challenge method (DNS)
CERTBOT_EMAIL="your-email@example.com" # Replace with your email
CERTBOT_SERVER="https://acme-v02.api.letsencrypt.org/directory"

# Command for Certbot (New Script)
CERTBOT_CMD_NEW="certbot certonly --manual --preferred-challenges ${CHALLENGE} \
--manual-public-ip-logging-ok \
--agree-tos --email ${CERTBOT_EMAIL} \
--server ${CERTBOT_SERVER} \
-d ${DOMAIN} -d ${WILDCARD} \
--config-dir ${LETSENCRYPT_DIR} \
--work-dir ${LIB_DIR} \
--logs-dir ${LIB_DIR}/logs"

# Old Script (Original Version)
run_old_script() {
    DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
    docker run -it --rm --name letsencrypt \
        -v "${DIR}/etc/letsencrypt:/etc/letsencrypt" \
        -v "${DIR}/var/lib/letsencrypt:/var/lib/letsencrypt" \
        certbot/certbot:latest certonly \
        -d $1 \
        --manual \
        --preferred-challenges dns \
        --server https://acme-v02.api.letsencrypt.org/directory
}

# Function to choose script version
choose_script() {
    echo "Choose the script version to run:"
    echo "1) New script (Improved version)"
    echo "2) Old script (Original)"
    read -p "Enter your choice (1 or 2): " choice

    if [[ "$choice" == "1" ]]; then
        echo "Running the new script..."
        echo "${CERTBOT_CMD_NEW}"
        eval "${CERTBOT_CMD_NEW}"
    elif [[ "$choice" == "2" ]]; then
        echo "Running the old script..."
        read -p "Enter the domain for certificate (e.g., example.com): " user_domain
        run_old_script "$user_domain"
    else
        echo "Invalid choice. Please run the script again and choose 1 or 2."
        exit 1
    fi
}

# Run the function to choose the script
choose_script

# Print current working directory as a confirmation step
pwd
