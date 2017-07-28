import save
import loading
def start():
	print "                      Welcome                    "
	print "                      Loading...                 "
	e,f=save.load_data_wrapper()
	net=loading.Network([784,30,30,10])
	s,t=net.SGD(e, 100, 5, 3.0)
	print "                  Press p to start               "
	print "               press p to stop(two times)        "
	print "               press l for next loop             "
	return(s,t)

