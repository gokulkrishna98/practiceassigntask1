import numpy as np


#appointment slots data
Appointment = [
  {
    "d4p1:AppointmentDate": "2017-11-20T08:30:00",
    "d4p1:Id": "1"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T08:40:00",
    "d4p1:Id": "2"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T08:50:00",
    "d4p1:Id": "3"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T09:10:00",
    "d4p1:Id": "4"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T09:20:00",
    "d4p1:Id": "5"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T09:30:00",
    "d4p1:Id": "6"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T09:40:00",
    "d4p1:Id": "7"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T09:50:00",
    "d4p1:Id": "8"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T10:00:00",
    "d4p1:Id": "9"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T10:10:00",
    "d4p1:Id": "10"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T10:20:00",
    "d4p1:Id": "11"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T10:30:00",
    "d4p1:Id": "12"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T10:40:00",
    "d4p1:Id": "13"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T10:50:00",
    "d4p1:Id": "14"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T11:00:00",
    "d4p1:Id": "15"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T11:10:00",
    "d4p1:Id": "16"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T11:20:00",
    "d4p1:Id": "17"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T11:30:00",
    "d4p1:Id": "18"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T11:40:00",
    "d4p1:Id": "19"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T11:50:00",
    "d4p1:Id": "20"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T12:00:00",
    "d4p1:Id": "21"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T12:10:00",
    "d4p1:Id": "22"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T12:20:00",
    "d4p1:Id": "23"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T13:30:00",
    "d4p1:Id": "24"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T13:40:00",
    "d4p1:Id": "25"
  },
  {
    "d4p1:AppointmentDate": "2017-11-20T13:40:00",
    "d4p1:Id": "25"
  }
]

#preference details of patients
Preference = {
  "preferred_datetimes": [
    {
      "start_date": "2018-01-08",
      "end_date": "2018-01-13",
      "preferred_times": [
        {
          "start_time": "08:00",
          "end_time": "12:00"
        },
        {
          "start_time": "16:00",
          "end_time": "19:30"
        }
      ],
      "time_exceptions": [
        {
          "start_time": "09:45",
          "end_time": "10:15"
        }
      ]
    },
    {
      "start_date": "2018-02-03",
      "end_date": "2018-02-12",
      "preferred_times": [
        {
          "start_time": "16:00",
          "end_time": "19:00"
        }
      ],
      "time_exceptions": [
        
      ]
    }
  ],
  "weekdays": [
    "1",
    "2",
    "3",
    "5"
  ],
  "date_exceptions": [
    {
      "start_date": "2018-01-09",
      "end_date": "2018-01-09"
    },
    {
      "start_date": "2018-02-05",
      "end_date": "2018-02-06"
    }
  ]
}

#output for Patient1 
Output1 = []

start = int(Preference["preferred_datetimes"][0]["start_date"].split("-")[2])
end = int(Preference["preferred_datetimes"][0]["end_date"].split("-")[2]) + 1

startdate = Preference["preferred_datetimes"][0]["start_date"]

for i in range(start,end):
	if(i<=9):
		tempstring =  startdate.split("-")[0]+"-"+startdate.split("-")[1]+"-"+ "0"+str(i)
		Output1.append({
	      "date": tempstring,
	      "date_slots": []
	    })
	else:
		tempstring = startdate.split("-")[0]+"-"+startdate.split("-")[1]+"-"+str(i)
		Output1.append({
	      "date": tempstring,
	      "date_slots": []
	    })

#Output variable for patient2
Output2=[]

start = int(Preference["preferred_datetimes"][1]["start_date"].split("-")[2])
end = int(Preference["preferred_datetimes"][1]["end_date"].split("-")[2]) + 1

for i in range(start,end):
	if(i<=9):
		tempstring = "2018-02-0" + str(i)
		Output2.append({
	      "date": tempstring,
	      "date_slots": []
	    })
	else:
		tempstring = "2018-02-" + str(i)
		Output2.append({
	      "date": tempstring,
	      "date_slots": []
	    })

#getting the timeslot for both patient1
b = []
bexception = []

alpha = Preference["preferred_datetimes"][0]["preferred_times"]
beta = Preference["preferred_datetimes"][0]["time_exceptions"]

for i in alpha:
	b.append([i["start_time"],i["end_time"]])

for i in beta:
	bexception.append([i["start_time"],i["end_time"]])

temp = []

for i in range(0,len(b)):
	temp.append(filter(lambda x: (((x["d4p1:AppointmentDate"].split("T")[-1] >= b[i][0]) & (x["d4p1:AppointmentDate"].split("T")[-1]<=b[i][1]))),Appointment))


O1 = temp[0]

for i in temp:
	O1 = np.union1d(O1,i)

for i in bexception:
	O1 =  filter(lambda x: ((x["d4p1:AppointmentDate"].split("T")[-1] <= i[0]) or (x["d4p1:AppointmentDate"].split("T")[-1] >= i[1])),O1)

if(len(O1)==0):
	O1 = ["no slots available"]
else:
	O1 = map(lambda x: "time-" + x["d4p1:AppointmentDate"].split("T")[-1] + " id -" + x["d4p1:Id"] ,O1)

#filtering based on dates
for i in Output1 :
	a1 = Preference["preferred_datetimes"][0]["start_date"]
	a2 = Preference["preferred_datetimes"][0]["end_date"]
	a3 = Preference["date_exceptions"][0]["start_date"]
	a4 = Preference["date_exceptions"][0]["end_date"]

	if((i["date"]>= a1) & (i["date"] <= a2)&(not((i["date"]>=a3) and (i["date"] <= a4)))):
  		i["date_slots"] = O1
  	else:
  		i["date_slots"] = "date_exceptions"

# printing details of patient1
print("<-------Patient 1----------->\n")
for i in Output1:
	print(i["date"])
	print(i["date_slots"])
	print("\n")




#getting the timeslot for both patient2
b = []
bexception = []

alpha = Preference["preferred_datetimes"][1]["preferred_times"]
beta = Preference["preferred_datetimes"][1]["time_exceptions"]

for i in alpha:
	b.append([i["start_time"],i["end_time"]])

for i in beta:
	bexception.append([i["start_time"],i["end_time"]])

temp = []

for i in range(0,len(b)):
	temp.append(filter(lambda x: (((x["d4p1:AppointmentDate"].split("T")[-1] >= b[i][0]) & (x["d4p1:AppointmentDate"].split("T")[-1]<=b[i][1]))),Appointment))


O2 = temp[0]

for i in temp:
	O2 = np.union1d(O2,i)

for i in bexception:
	O2 =  filter(lambda x: ((x["d4p1:AppointmentDate"].split("T")[-1] <= i[0]) or (x["d4p1:AppointmentDate"].split("T")[-1] >= i[1])),O2)

if(len(O2)==0):
	O2 = ["no slots available"]
else:
	O2 = map(lambda x: "time-" + x["d4p1:AppointmentDate"].split("T")[-1] + " id -" + x["d4p1:Id"] ,O2)

#filtering based on dates
for i in Output2 :
	d1 = Preference["preferred_datetimes"][1]["start_date"]
	d2 = Preference["preferred_datetimes"][1]["end_date"]
	d3 = Preference["date_exceptions"][1]["start_date"]
	d4 = Preference["date_exceptions"][1]["end_date"]

	if((i["date"]>= d1) & (i["date"] <= d2)&(not((i["date"]>=d3) and (i["date"] <= d4)))):
  		i["date_slots"] = O2
  	else:
  		i["date_slots"] = "date_exception"

print("<-------Patient 2----------->\n")
# printing details of patient2
for i in Output2:
	print(i["date"])
	print(i["date_slots"])
	print("\n")

