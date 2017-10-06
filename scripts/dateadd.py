import datetime

def dayAdd(s,d):
	date = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
	date += datetime.timedelta(days=d)
	return (date.strftime('%Y-%m-%d %H:%M:%S'))

def main():
	s = "2017-10-06 13:19:37"
	print(s)
	print(dayAdd(s,3))

if __name__ == "__main__":
    main()

