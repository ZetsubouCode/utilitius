from typing import Union
from datetime import date, datetime, timedelta

def date_manipulator(base_date:date=date.today(), day:int=0, week:int=0,month:int=0, year:int=0, format:str="") -> Union[str,date]:
    
    new_month = (base_date.month + month) % 12
    new_year = base_date.year + ((base_date.month + month) // 12)
    
    manipulated_date = base_date + timedelta(days=day,weeks=week)
    manipulated_date = manipulated_date.replace(month=new_month,year=new_year)

    if format is not None and format != "":
        manipulated_date = manipulated_date.strftime(format)
        
    return manipulated_date
    