from logic.exercisesOne import save_course, search_currency


def designOneList():
    course = input("what is the course name?  ")
    result = save_course(course)
    print(result)

def designOneDict():
    currency = input("what is the currency name? ")
    print(search_currency(currency))