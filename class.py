class Book:
    def __init__(self,category,title): # __init__ is a constructor method that initializes the attributes of the class    
        self.category = category
        self.title = title
         # self is a reference to the current instance of the class, and category is an attribute that holds the value passed during object creation
        # not required any variable to be declared before using it in the class, we can directly use it in the constructor method
        #which is called dynamic variable, it can be created and assigned a value at runtime
        # object { category: "Fiction" } is created when we create an instance of the Book class and pass "Fiction" as an argument to the constructor method

    def get_category(self):
        print("The category of the book is:", self.category) # self.category is used to access the category attribute of the current instance of the class
    def get_title(self):
        print("The title of the book is:", self.title) # self.title is used to access the title attribute of the current instance of the class    

class eBook(Book):
    def __init__(self,category,title,file_format):
        super().__init__(category,title)
        self.file_format = file_format # file_format is an additional attribute specific to the eBook 
    def print_details(self):
        print("The category of the eBook is:", self.category)
        print("The title of the eBook is:", self.title)
        print("The file format of the eBook is:", self.file_format)

# creating an instance of the Book class
book1 = eBook(category="fiction",title="The Great Gatsby",file_format="PDF")
book1.print_details() # Output: The category of the eBook is: Fiction
                    #         The title of the eBook is: The Great Gatsby
                    #         The file format of the eBook is: PDF

class DetailBook(eBook):
    def __init__(self,category,title,file_format,author):
        super().__init__(category,title,file_format)
        self.author = author # author is an additional attribute specific to the DetailBook class
    def print_details(self):
        super().print_details() # calling the print_details method of the parent class (eBook) to print the category, title, and file format
        print("The author of the DetailBook is:", self.author) # printing the author attribute specific to the DetailBook class

# creating an instance of the DetailBook class
detail_book1 = DetailBook(category="fiction",title="The Great Gatsby",file_format="PDF",author="F. Scott Fitzgerald")
detail_book1.print_details() # Output: The category of the eBook is: Fiction
