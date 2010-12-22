import csv
import datetime

rhCSV = csv.reader(open('RTAData.csv')) # read in the data 
whf = open('lcb_submit2.csv','w')       # create a file where the entry will be saved
wh = csv.writer(whf, lineterminator='\n');

date_format = "%Y-%m-%d %H:%M"

timeStamp = ["2010-08-03 10:28","2010-08-06 18:55","2010-08-09 16:19","2010-08-12 17:22","2010-08-16 12:13","2010-08-19 17:43","2010-08-22 10:19","2010-08-26 16:16","2010-08-29 15:04","2010-09-01 09:07","2010-09-04 09:07","2010-09-07 08:37","2010-09-10 15:46","2010-09-13 18:43","2010-09-16 07:40","2010-09-20 08:46","2010-09-24 07:25","2010-09-28 08:01","2010-10-01 13:04","2010-10-05 09:22","2010-10-08 16:43","2010-10-12 18:10","2010-10-15 14:19","2010-10-19 17:16","2010-10-23 10:28","2010-10-26 19:34","2010-10-29 11:34","2010-11-03 17:49","2010-11-07 08:01"]; # an Array with the cut-off points
forecastHorizon = [1,2,3,4,6,8,24,48,72,96]; # forecast horizon in multiples of 15 minutes

cutoff_times = set()
for t in timeStamp:
    cutoff_times.add(datetime.datetime.strptime(t, date_format))

header = next(rhCSV) # extract the header first
wh.writerow([""] + header[1:])

for data in rhCSV: # loop through the each remaining line
    current_date = datetime.datetime.strptime(data[0], date_format)

    if current_date in cutoff_times:
            # for each forecast horizon write the cut-off travel
            # time as the forecast (the definition of Naive)
            for i in forecastHorizon: 
                # calculate the prediction's datetime
                nextDate = current_date + datetime.timedelta(minutes=15*i)
                dateStr = datetime.datetime.strftime(nextDate, date_format)
                # write the timestamp and predictions to the first column of the CSV
                wh.writerow([dateStr] + data[1:])

# Done
whf.close()

