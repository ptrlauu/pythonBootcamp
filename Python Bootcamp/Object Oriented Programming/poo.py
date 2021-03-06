#Definindo uma classe simples

##age default = 0 
class User:
    #Atributo da classe atribuido apenas uma vez.
    active_users = 0

    #Class Methods -> não é instancia -> class user
    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."
        
    @classmethod
    def from_string(cls, data_str):
        first,last,age = data_str.split(",")
        return cls(first, last, int = age)

    def __init__(self,first,last,age = 0):
        self.first = first
        self.last = last
        self.age = age
        User.active_users+=1
  
    def logout(self):
        User.active_users -=1
        return f"{self.first} has logged out."
    
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self,thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >=65 #boolean expression true or false.

    def birthday(self):
        self.age +=1
        return f"Happy {self.age}th, {self.first}"


#user1 eh objeto da classe User
#instanciando a classe abaixo ->

#user1 = User("Joe","Smith",68)
#user2 = User("Blanca","Lopez",41)
# print(user1.is_senior())
# print(user1.birthday())
# print(user1.likes("Ice Cream"))
# print(user2.initials())
# print(user2.full_name())

#print("Currently we have {} active users".format(User.active_users))
#print(user2.logout())
#print("Currently we have {} active users" .format(User.active_users))

#print(User.display_active_users())

#class method -> instanciando o user 
tom = User.from_string("Tom,Jones,89")
print(tom.first)
print(tom.full_name)
print(tom.birthday)