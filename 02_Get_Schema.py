from ncclient import manager

host = "sandbox-iosxe-latest-1.cisco.com"
port = "830"
username = "developer"
password = "C1sco12345"

with manager.connect(host=host, port=port, username=username,
                     password=password, hostkey_verify=False) as man:

    man.connected

    schema = man.get_schema("Cisco-IOS-XE-native")
    print(schema)
