def returntrueifequal(fir, op, sec, summ):
	fir=float(fir)
	sec=float(sec)
	summ=float(summ)
	if op=='+':
		if fir+sec==summ:
			return True
		else:
			return False
	elif op=='-':
		if fir-sec==summ:
			return True
		else:
			return False
	elif op=='*':
		if fir*sec==summ:
			return True
		else:
			return False
	elif op=='/':
		if fir/sec==summ:
			return True
		else:
			return False
	else:
		return None