import os, time, getpass, shutil

def sortAdded( addedlist, oldpath, newpath):
	for f in addedlist:
		if f.endswith(('.png', '.jpg', '.jpeg')):
			shutil.move(oldpath + f, newpath + f)
			print "we got an image " + f  
		elif f.endswith(('.gif', '.gifv')):
			shutil.move(oldpath + f, newpath +"GIFs\\"+ f)
			print "we got a gif " + f  

if __name__ == '__main__':
	username = getpass.getuser()
	path_to_watch = "C:\\Users\\"+ username + "\\Downloads\\"
	image_path = "C:\\Users\\"+ username + "\\Pictures\\"
	before = dict ([(f, None) for f in os.listdir (path_to_watch)])
	while True:
		time.sleep (10)
		after = dict ([(f, None) for f in os.listdir (path_to_watch)])
		added = [f for f in after if not f in before]
		#removed = [f for f in before if not f in after]
		if added:
			print " Added: ", ", ".join (added)
			sortAdded(added, path_to_watch, image_path)
		#if removed: print "Removed: ", ", ".join (removed)
		before = after
