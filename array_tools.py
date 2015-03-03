def array_remove_array(array_from, array_to_remove):
	for i in array_to_remove:
		try:
			array_from.remove(i)
		except:
			print "Unable to remove entry: " + format(i)
	return array_from