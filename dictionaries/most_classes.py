# The dictionary will be something like:
my_dic = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
 'Kenneth Love': ['Python Basics', 'Python Collections']}

# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#

def most_classes(dic):
    max_count = 0
    teacher_name = ''
    for key in dic:
        if max_count < len(dic[key]):
            max_count = len(dic[key])
            teacher_name = key
    print(teacher_name)
    return teacher_name

def num_teachers(dic):
    count = 0
    for key in dic:
        count += 1
    print(count)
    return count

def stats(dic):
    directory = []
    for key in dic:
        directory.append([key, len(dic[key])])
    print(directory)
    return directory

def courses(dic):
    directory = []
    for key in dic:
        directory += dic[key]
    print(directory)
    return directory


most_classes(my_dic)
num_teachers(my_dic)
stats(my_dic)
courses(my_dic)
