""" Challenge: List of lists 9.4"""
# Calculates the totl, the mean and the median of students and tuition fees.
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


# enrollment_stats() should return two lists: the first containing all of
# the student enrollment values and the second containing all of the
# tuition fees.

def enrollment_stats(list_of_lists):
    """This Function returns two lists, number of students and tuition fees."""
    students_enrolled = []
    tuition_fees = []
    if not isinstance(list_of_lists, list):
        return print('Debe introducir una lista de listas.')
    elif isinstance(list_of_lists, list) and len(list_of_lists) > 1:
        for values in list_of_lists:
            if isinstance(values, list):
                students_enrolled.append(values[1])
                tuition_fees.append(values[2])
            else:
                return print('Todos los elementos de la lista deben de ser lista.')
    else:
        return print('La lista tiene que cotener mas de un elemento.')

    return students_enrolled, tuition_fees


# Next, define a mean() and a median() function. Both functions should
# take a single list as an argument and return the mean and median of
# the values in each list.

def mean(lis):
    """This Function calculates the mean of a list of values"""
    total = 0
    if not isinstance(lis, list):
        return print('Debe introducir una lista de listas.')
    elif isinstance(lis, list) and len(lis) > 1:
        for value in lis:
            if isinstance(value, int):
                total += value
            else:
                return print('Todos los valores deben de ser enteros.')
    else:
        return print('La lista tiene que cotener mas de un elemento.')
    return total / len(lis)


def median(lis):
    """This Function calculates the median of a list of values"""
    total = []
    if not isinstance(lis, list):
        return print('Debe introducir una lista de listas.')
    elif isinstance(lis, list) and len(lis) > 1:
        for value in lis:
            if isinstance(value, int):
                total.append(value)

            else:
                return print('Todos los valores deben de ser enteros.')
    else:
        return print('La lista tiene que cotener mas de un elemento.')
    total.sort()
    even = []
    if len(total) % 2 == 0:
        n = len(total)
        m = (n - 1) // 2
        even.append(total[m])
        even.append(total[m + 1])
    else:
        m = (len(total) + 1) // 2
        index = m - 1
        m = total[index]
        return m
    m = sum(even) / 2
    return m


enrolled_students, tuition_fee = enrollment_stats(universities)

print('*' * 50)
print(f'Total students: {sum(enrolled_students):,}.')
print(f'Total tuition fees: $ {sum(tuition_fee):,.2f}')
print(f'\nStudents mean: {mean(enrolled_students):,.0f}.')
print(f'Students median: {median(enrolled_students):,}.')
print(f'\nTuition mean: $ {mean(tuition_fee):,.2f}')
print(f'Tuition mean: $ {median(tuition_fee):,.2f}')
print('*' * 50)
