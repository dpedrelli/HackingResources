The enumeration phase makes use of network protocols to gather information such as:  account names, network shares, and misconfigured services.

* ### [NetBIOS / SMB](../../Techniques/NetBIOS_SMB_Samba/README.md#Enumerate)
  NetBIOS operates on ports:  UDP 137 (name services), UDP 138 (datagram services), and TCP 139 (session services).

  * The name service operates like DNS and provides [NetBIOS name resolution](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc738412(v=ws.10)?redirectedfrom=MSDN).
* ### SNMP
  