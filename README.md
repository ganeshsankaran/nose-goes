by Ganesh Sankaran
<hr/>

Nose Goes is a (dumb) leader election algorithm.

**Algorithm**

The `n` process in the distributed system must be known a priori.

The process that initiates leader election does the following:
<pre>
timestamp = time()
msgs = {PID: timestamp}
broadcast(PID, timestamp)
broadcasted = True
</pre>

All processes do the following:
<pre>
while True:
    sender, timestamp = recv()
    msgs.update({sender: timestamp})
    
    if not broadcasted:
        timestamp = time()
        msgs.update({PID: timestamp})
        broadcast(PID, timestamp)
        broadcasted = True
        
    if len(msgs) == n:
        leader = max(msgs, key = msgs.get) # process corresponding to maximum timestamp
        break
</pre>

**Execution**

Start the processes P1 through P5

<pre>python3 process.py [PID]</pre>
