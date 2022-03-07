from my_site.models import Resume


def Years(age):
    data_age = Resume.objects.all()
    
    if str(data_age.age)[-1] == 1:
        return 'год'
    elif str(data_age.age)[-1] == range(2, 5):
        return 'года'
    else:
        return 'лет'
