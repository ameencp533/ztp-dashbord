from ncclient import manager

def start_netconf_session(ip_address, username='nieg', password='sify@123'):
    try:
        with manager.connect(
            host=ip_address,
            port=830,
            username=username,
            password=password,
            hostkey_verify=False
        ) as m:
            # Perform NETCONF operations
            print(f"NETCONF session started with {ip_address}")
            # Example: Get the device's capabilities
            capabilities = m.server_capabilities
            for capability in capabilities:
                print(capability)
    except Exception as e:
        print(f"Failed to start NETCONF session with {ip_address}: {e}")
