import threading
import datetime
import time

total_no_of_events = 0

ts_events_dict = {}

ts_precision = 1

def eventOccurred():
    global total_no_of_events
    total_no_of_events += 123
    
    
def store_evt_ct(Counting):
  
  #while Counting:
      eventOccurred()
  #threading.Timer(ts_precision, store_evt_ct).start()
      ts = int (datetime.datetime.now().timestamp())
  #print(ts)
      print ("events count = ", total_no_of_events, "time stamp = ", ts)
      ts_events_dict[ts] = total_no_of_events
      time.sleep(1)
  #threading.Timer(ts_precision, store_evt_ct).cancel()

store_evt_ct(True)
#threading.Timer(ts_precision, store_evt_ct).cancel()

for counter in range(20):
    time.sleep (1)
    result_ts = int (datetime.datetime.now() - datetime.timedelta(seconds=5))
    print ("events happened in last five seconds = ", ts_events_dict[result_ts])
