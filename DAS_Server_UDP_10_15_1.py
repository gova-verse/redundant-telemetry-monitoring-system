# Primary Telemetry Server Interface

import socket
import struct

# Example multicast configuration (sanitized)
MCAST_GRP = "XXX.XXX.XXX.XXX"
MCAST_PORT = XXXX

IS_ALL_GROUPS = True

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.settimeout(0.5)

if IS_ALL_GROUPS:
    sock.bind(('', MCAST_PORT))
else:
    sock.bind((MCAST_GRP, MCAST_PORT))

mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


def data_read():
    """
    Reads telemetry packet and returns list of channel values
    """

    try:
        data, _ = sock.recvfrom(4096)

        # Example placeholder decoding
        values = []

        # TODO: Add actual packet decoding here

        return values

    except Exception:
        return None