class Student:
    
    #Global variables
    school = 'Online school'
    num_students = 0 #we will continue to update number of students going to online school

    def __init__(self, first_name, last_name, major):
        """Class constructor

        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            major (str): course of study
        """
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        
        # Count of students in school increases by 1
        Student.num_students += 1
        
    def fullname_with_major(self):
        """Class method

        Returns:
            string: Student's full name with major.
        """
        return f'{self.first_name} {self.last_name} is majoring in {self.major}!'
    
    def fullname_major_school(self):
        """Class method

        Returns:
            string: Student's full name with major and school
        """
        return f'{self.first_name} {self.last_name} is majoring in {self.major} at {self.school}!'
    
    @classmethod
    def set_online_school(cls, new_school):
        """Class method

        Args:
            new_school (str): name of school.
        """
        cls.school = new_school
    
    @classmethod
    def split_students(cls, student_str):
        """Class method

        Args:
            student_str (str): Name of student separated by period ('.')

        Returns:
            class: an initialized instance of the Student class
        """
        first_name, last_name, major = student_str.split('.')
        return cls(first_name, last_name, major)


student_1 = Student('Eric', 'Roby', 'Computer Science')
student_2 = Student('John', 'Miller', 'Math')
new_student = 'Adil.Yutzy.English'
student_3 = Student.split_students(new_student)
print(student_3.fullname_major_school())
