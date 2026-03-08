# ================= REAL-TIME TELEMETRY MONITOR =================

import matplotlib
matplotlib.use("Qt5Agg")

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
from matplotlib import style

import numpy as np
import time
import threading
import queue

# ======== IMPORT DATA SOURCES ========
import DAS_Server_UDP_10_15_1 as server1
import DAS_Redn_Sim as server2
import DAS_CDT_Reception10_9 as cdt
import csv_read_10_9 as csv

style.use("fivethirtyeight")

# ======== CONFIGURATION ========
x_len = 2000
interval_ms = 100

FAIL_TIMEOUT = 0.40
SWITCH_COOLDOWN = 0.6
QUEUE_MAX = 500
PREFERRED_ID = 2

# ======== CONFIG FROM CSV ========
y_range = csv.y_range()
chno = csv.read_chno()
CH_INDEX = int(chno[0])

# ======== THREAD STATE ========
q1 = queue.Queue(maxsize=QUEUE_MAX)
q2 = queue.Queue(maxsize=QUEUE_MAX)

stop_event = threading.Event()

last_packet_1 = 0.0
last_packet_2 = 0.0
packet_lock = threading.Lock()

# ======== CDT STATE ========
latest_cdt = "00:00:00:000"
cdt_lock = threading.Lock()

# ======== RECEIVER THREAD ========
def receiver_loop(server_mod, out_q, server_id):

    global last_packet_1, last_packet_2

    while not stop_event.is_set():

        try:
            dt_list = server_mod.data_read()

            if dt_list is None:
                continue

            y = float(dt_list[CH_INDEX]) if 0 <= CH_INDEX < len(dt_list) else np.nan

            now = time.monotonic()

            with packet_lock:
                if server_id == 1:
                    last_packet_1 = now
                else:
                    last_packet_2 = now

            try:
                out_q.put_nowait(y)

            except queue.Full:

                try:
                    out_q.get_nowait()
                except queue.Empty:
                    pass

                out_q.put_nowait(y)

        except Exception:
            continue