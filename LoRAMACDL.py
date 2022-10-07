import os
from macCMDFormatter import LinkADRReq
import sys
import json
import time
import grpc
from chirpstack_api.ns import NetworkServerServiceStub
from chirpstack_api.ns.ns_pb2 import CreateMACCommandQueueItemRequest

host = "localhost:8000"


channel = grpc.insecure_channel(host)

ns = NetworkServerServiceStub(channel)


def send_MAC(devEUI, mac):
    macCmd = CreateMACCommandQueueItemRequest()
    linkAdrReq = bytes.fromhex(mac)

    # cList =[devStatusReq]
    macCmd.dev_eui = bytes.fromhex(devEUI)
    macCmd.cid = 3
    macCmd.commands.extend([linkAdrReq])
    ns.CreateMACCommandQueueItem(macCmd)


# devStatusReq = bytes.fromhex("06")
# print(devStatusReq)

devEUIs = ['dead2483dead0001','dead2483dead0002','dead2483dead0003','dead2483dead000b']
#devEUIs = ['dead2483dead0001']
#devEUIs = ['dead2483dead0001','dead2483dead0002']
# cList = [devStatusReq, linkAdrReq, devStatusReq
# print(macCmd.dev_eui)
LinkADRList = [
    "0355020001",
    "0345010001",
    "0335040001",
    "0325020001",
    "0315010001",
    "0305010001",
    "0352040001",
    "0342010001",
    "0335010001",
    "0325010001",
    "0315020001",
    "0305010001",
    "0325040001",
    "0335020001",
    "0345010001",
    "0355010001",
    "0302040001",
    "0342010001",
    "0335010001",
    "0325010001",
    "0315020001",
    "0305010001",
    "0325040001",
    "0335020001",
    "0345010001",
    "0355010001",
    "0302040001",
    "0302010001",
    "0355010001",
    "0305010001",
]
time.sleep(30)
i = 1

for l in LinkADRList:
    for devEUI in devEUIs:
        send_MAC(devEUI, l)
    print("Send LinkADRReq ", i)
    i = i + 1
    time.sleep(60)


# r = ns.CreateMACCommandQueueItem(macCmd)

# print(r)
