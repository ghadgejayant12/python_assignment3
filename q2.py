# Build a retry decorator with retry time and retry interval to run a function 3 time with interval of 3 sec
import time
def retry(func):
	def gap_call(times,interval):
		for i in range(times):
			print('The function',func.__name__,'will now be called after an interval of',interval,'seconds')
			time.sleep(interval)
			func(times,interval)
			print('The function was called',i+1,'times')
			print('----------------------------------------------------------------------------------')
	return gap_call

@retry
def trying(times,interval):
	print('Inside the function trying(), this function was called from the decorator')

trying(3,3)