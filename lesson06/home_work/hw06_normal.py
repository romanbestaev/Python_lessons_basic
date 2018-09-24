import random
# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

# Класс человек с атрибутами ФИО, и метдом печати ФИО
class person():
    def __init__(self,last_name=None,first_name=None,patronymic_name=None):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic_name = patronymic_name
    def print_fio(self,end_='\n'):
        print('{} {}.{}.'.format(
                                 self.last_name,
                                 self.first_name[0],
                                 self.patronymic_name[0]),
     end=end_)
        

# Класс ученик, наследует от класса человек, имеет атрибуты "отец", "мать", 
# класс, в котором учиться и методы печати информации о классе
class student(person):
    def __init__(self, last_name, 
                       first_name, 
                       patronymic_name, 
                       father=None, 
                       mother=None):
        person.__init__(self, last_name, first_name,  patronymic_name)
        self.father = father
        self.mother = mother
    def set_grade(self,grade):
        self.grade=grade
    def set_perents(self,father,mother):
        self.father = father
        self.mother = mother

# Класс учитель, наследует от класса человек, имеет "предмет"
# список классов, в которых преподает
class teacher(person):
    def __init__(self, last_name, 
                       first_name, 
                       patronymic_name, 
                       subject=None, 
                       grade_list=[]):
        person.__init__(self, last_name, first_name, patronymic_name)
        self.subject = subject
        self.grade_list = grade_list
    def set_subject(self,subject):
        self.subject = subject
    def set_grade(self,grade):
        self.grade_list.append(grade)
    def remove_grade(self,grade):
        self.grade_list.remove(grade)
    def print_info(self):
        print('{} {}.{}. предмет: {}'.format(self.last_name,
              self.first_name[0],self.patronymic_name[0], self.subject))

# Класс "класс", имеет атрибуты список учеников, словарь предмет:учитель
class grade():
    def __init__(self,lavel,index,student_list=[],subject_n_teacher={}):
        self.lavel = lavel
        self.index = index
        self.grade_name = str(lavel)+index
        self.student_list = student_list
        self.subject_n_teacher = subject_n_teacher
    def set_student(self,student):
        self.student_list.append(student)
    def remove_student(self,student):
        self.student_list.remove(student)
    def set_subject_n_teacher(self,subject,teacher):
        self.subject_n_teacher[subject] = teacher
        

# Данные для заполнения
#  Перечень имен/фамилий/отчеств
names_male = ['Александр', 'Максим', 'Иван', 'Артём', 'Никита', 'Дмитрий', 
           'Егор', 'Даниил', 'Михаил', 'Андрей', 'Алексей', 'Илья', 'Кирилл',
           'Сергей', 'Владислав', 'Роман', 'Владимир', 'Тимофей', 'Матвей', 
           'Георгий', 'Николай', 'Павел', 'Арсений', 'Денис', 'Степан',
           'Фёдор', 'Данила', 'Антон', 'Константин', 'Глеб', 'Ярослав', 
           'Григорий', 'Игорь', 'Евгений', 'Тимур', 'Руслан', 'Пётр', 
           'Олег', 'Вадим', 'Василий', 'Вячеслав', 'Виктор', 'Юрий', 
           'Артемий', 'Леонид', 'Давид', 'Марк', 'Лев', 'Семён', 'Артур']
names_female = ['Анастасия', 'Мария', 'Дарья', 'Анна', 'Елизавета', 'Виктория', 
           'Полина', 'Екатерина', 'Софья', 'Александра', 'Ксения', 'София', 
           'Арина', 'Алина', 'Вероника', 'Варвара', 'Валерия', 'Кристина', 
           'Алиса', 'Юлия', 'Ульяна', 'Ольга', 'Диана', 'Алёна', 'Ирина', 
           'Татьяна', 'Елена', 'Василиса', 'Кира', 'Таисия', 'Яна', 
           'Маргарита', 'Вера', 'Ангелина', 'Евгения', 'Светлана', 'Марина', 
           'Надежда', 'Милана', 'Ева', 'Олеся', 'Наталья', 'Карина', 'Милена', 
           'Злата', 'Амина', 'Любовь', 'Элина', 'Ярослава', 'Лилия']
names_last = ['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 
           'Соколов', 'Михайлов', 'Новиков', 'Федоров', 'Морозов', 'Волков', 
           'Алексеев', 'Лебедев', 'Семенов', 'Егоров', 'Павлов', 'Козлов', 
           'Степанов', 'Николаев', 'Орлов', 'Андреев', 'Макаров', 'Никитин', 
           'Захаров', 'Зайцев', 'Соловьев', 'Борисов', 'Яковлев', 'Григорьев', 
           'Романов', 'Воробьев', 'Сергеев', 'Кузьмин', 'Фролов', 
           'Александров', 'Дмитриев', 'Королев', 'Гусев', 'Киселев', 'Ильин', 
           'Максимов', 'Поляков', 'Сорокин', 'Виноградов', 'Ковалев', 'Белов', 
           'Медведев', 'Антонов', 'Тарасов']
names_patronymic = [
        x for x in names_male if x[-1] not in ['а','й','я','ь']
        ]
# Перечень предметов
subjects = ['Русский язык','Литература','Математика','История',
'Физика','Химия','Биология','Обществознание','Физкультура','ОБЖ',
'Информатика','Труды']
# Перечень номеров и букв для классов
grade_lavel = [1,2,3,4,5,6,7,8,9,10,11]
grade_index = ['А','Б','В','Г','Д']
# Функция генерации ФИО человека
def random_fio(names_last, names_male, names_female, names_patronymic,sex):
    isex = random.choice(sex)
    return  random.choice(names_last)+'а'*abs(1-isex), \
            random.choice(names_female*abs(isex-1)+names_male*isex), \
            random.choice(names_patronymic)+'ов'+'ич'*isex+'на'*abs(isex-1)

Nteachers = 30
Ngrades = 5
Nstu_in_grade = 20
Nstudents = Nstu_in_grade*Ngrades

# Генерируем список всех учеников школы
students = []
for i in range(Nstudents):
    last_name,first_name,patronymic_name = random_fio(
            names_last, names_male, names_female, names_patronymic,[0,1]
            )
    students.append(student(last_name,first_name,patronymic_name))

#  Генерируем родителей учеников
for x in students:
    last_name,first_name,patronymic_name = random_fio(
            [x.last_name], 
            [x.patronymic_name.replace('ович','').replace('овна','')], 
            names_female, names_male,[1])
    father = person(last_name,first_name,patronymic_name)
    last_name,first_name,patronymic_name = random_fio(
            [x.last_name], names_male, names_female, patronymic_name,[0])
    mother = person(last_name,first_name,patronymic_name)
    x.set_perents(father,mother)

# Генерируем список учителей
teachers = []
subjects_n_teachers = dict(zip(subjects,[[] for _ in range(len(subjects))]))
for i in range(Nteachers):
    last_name,first_name,patronymic_name = random_fio(
            names_last, names_male, names_female, names_patronymic,[0,1])
    sub = random.choice(subjects)
    teach = teacher(last_name,first_name,patronymic_name,sub,[])
    teachers.append(teach)
    subjects_n_teachers[sub].append(teach)
# Для пустых предметов нанимаем учителе:
for sub in subjects_n_teachers:
    if len(subjects_n_teachers[sub])==0:
        last_name,first_name,patronymic_name = random_fio(
                names_last, names_male, names_female, names_patronymic,[0,1])
        teach = teacher(last_name,first_name,patronymic_name,sub,[])
        teachers.append(teach)
        subjects_n_teachers[sub].append(teach)

# Генерируем список классов, заполняем их учениками, присваиваем учителей
grades = []
for i in range(Ngrades):
    grades.append(grade(random.choice(grade_lavel),random.choice(grade_index),[],{}))
    for stud in students[i*Nstu_in_grade:(i+1)*Nstu_in_grade]:
        grades[-1].set_student(stud)
        stud.set_grade(grades[-1])
    for sub in subjects_n_teachers:
        grades[-1].set_subject_n_teacher(sub,random.choice(subjects_n_teachers[sub]))


#1. Получить полный список всех классов школы
print('\nСписок всех классов школы')
for x in grades:
    print(str(x.lavel)+x.index)

#2. Получить список всех учеников в указанном классе
xgrade = random.choice(grades)
print('\nСписок всех учеников '+ xgrade.grade_name + ':')
for x in xgrade.student_list:
    x.print_fio()

#3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
xstudent = random.choice(students)
print('\nИнфо по случайному ученику школы:')
xstudent.print_fio(' --> \n')
print(xstudent.grade.grade_name,end=' --> \n')
print('Учителя -->')
for x in xstudent.grade.subject_n_teacher:
    xstudent.grade.subject_n_teacher[x].print_info()

# 4. Узнать ФИО родителей указанного ученика
print('Родители -->')
print('Отец: ',end=' ')
xstudent.father.print_fio()
print('Мать: ',end=' ')
xstudent.mother.print_fio()

# 5. Получить список всех Учителей, преподающих в указанном классе
xgrade = random.choice(grades)
print('\n\nУчителя ',xgrade.grade_name, ' класса:')
for x in xgrade.subject_n_teacher:
    xgrade.subject_n_teacher[x].print_info()
#%% Черновик
#fid = open('names_1.txt','r')
#fid2 = open('names_m.txt','w')
#fid3 = open('names_f.txt','w')
#for line in fid:
#    l = line.split(' ' )
#    fid2.write('\''+l[1] + '\', ')
#    fid3.write('\''+l[-1].rstrip() + '\', ')
#fid2.close()
#fid3.close()
#
#fid = open('names_2.txt','r')
#fid2 = open('names_l.txt','w')
#for line in fid:
#    l = line.split(' ' )
#    fid2.write('\''+l[-1].rstrip() + '\', ')
#fid2.close()

#subjects_n_teachers = dict.fromkeys(subjects)
#subjects_n_teachers = dict(zip(subjects,[[]]*len(subjects))) # Так не пойдет
