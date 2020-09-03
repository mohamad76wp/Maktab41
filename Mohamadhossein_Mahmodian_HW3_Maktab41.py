import datetime
import os

# def week_generator(start_date,end_date,week_day):
#     start_date = start_date.split('-')
#     start_date = datetime.date(int(start_date[0]),int(start_date[1]),int(start_date[2]))

#     end_date = end_date.split('-')
#     end_date = datetime.date(int(end_date[0]),int(end_date[1]),int(end_date[2]))

#     if week_day == 0:
#         week_day = 7
#     crusor_day = datetime.date(1970,1,1)

#     wday = start_date.weekday()

#     my_day = abs(wday - week_day)

#     delta = datetime.timedelta(days = my_day)
#     crusor_day = start_date + delta

#     while crusor_day <= end_date:
#         yield crusor_day.strftime('%d, %B, %Y')
#         delta_week = datetime.timedelta(weeks=1)
#         crusor_day = crusor_day + delta_week



# result = week_generator('2020-2-18','2020-5-2',3)


# while True:
#     print(next(result))


# #___________________________________________________Hanoi Tower__________________________________________________

def HanoiTower(n,start,mid,end):
    if n == 1:
        print(f'Move Disk 1 From {start} to {end}')
    else:
        HanoiTower(n-1,start,end,mid)
        print(f'Move Disk {n} from {start} to {end}')
        HanoiTower(n-1,mid,start,end)

HanoiTower(2,"A", "B", "C")