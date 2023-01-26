def format_date(date_selected):
    return date_selected[6:] + "-" + date_selected[3:5] + "-" + date_selected[:2]

def format_date_to_year_month(date_selected):
    return date_selected[6:] + "-" + date_selected[3:5]