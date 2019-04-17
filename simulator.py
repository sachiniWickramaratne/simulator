import http.server
import socketserver
import random
import time
import multiprocessing as mp

def listen(PORT): 
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()

procs = []

def startProcess(port):
    p= mp.Process(target=listen, args=(port,))
    p.start()
    procs.append(p)
    return p

ps={}
rm=[]
def newProcess():
    if(len(rm)>0):
        rand=random.choice(rm)
        px=startProcess(rand)
        print("open " + str(rand))
        rm.remove(rand)
        ps[px]=rand


if __name__ == "__main__": 
    p0= startProcess(9000)
    p1= startProcess(9001)
    p2= startProcess(9002)
    p3= startProcess(9003)
    p4= startProcess(9004)
    p5= startProcess(9005)
    p6= startProcess(9006)

    ps={p0:9000,p1:9001,p2:9002,p3:9003,p4:9004,p5:9005,p6:9006}


    while True:
        if(len(procs)>0):

            print("----------------------------------------------------------------------------------------")
            pa=random.choice(procs)
            print("choice")
            print(pa)
            k = random.randint(0, 1)
            print(k)
            if(k==0):
                print("close" +str(ps[pa]))
                pa.terminate()
                rm.append(ps[pa])
                procs.remove(pa)
                ps.pop(pa)
            else:
                newProcess()
        else:
            newProcess()            
        time.sleep(5)



   

   
