user_data1 = {
    'first_name': "dan",
    'last_name': "Danerson",
    'email': 'dan@dan.com',
    'age': 43,
    'is_rewards_member': False,
    'gold_card_points': 0,
    'amount': 50
}

user_data2 = {
    'first_name': "Amy",
    'last_name': "Amison",
    'email': 'Amy1@aol.com',
    'age': 30,
    'is_rewards_member': True,
    'gold_card_points': 500,
    'amount': 50
}




class UserData:
    def __init__(self,data_dict):
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.age = data_dict['age']
        self.is_rewards_member = data_dict['is_rewards_member']
        self.gold_card_points = data_dict['gold_card_points']
        self.amount = data_dict['amount']


    def hello(self):
        print(f"name:{self.first_name}")
        print(f"Last name:{self.last_name}")
        print(f"email:{self.email}")
        print(f"age:{self.age}")
        print(f"reward member:{self.is_rewards_member}")
        print(f"gold card points:{self.gold_card_points}")

    def enroll(self):
        self.gold_card_points = 200
        self.is_rewards_member = True
        print(self.is_rewards_member)
        print(self.gold_card_points)   

    def spend_points(self):
        self.gold_card_points -= 50   
        print(f"you spent {self.amount} points!")
        print(f"Your balance is {self.gold_card_points} points!")  
        

user_1 = UserData(user_data1)
user_2 = UserData(user_data2)
print(user_1.age,user_1.email,user_1.first_name,user_1.last_name,user_1.gold_card_points,user_1.is_rewards_member)  
print(user_2.age,user_2.email,user_2.first_name,user_2.last_name,user_2.gold_card_points,user_2.is_rewards_member) 

# user_1.hello()
# user_1.enroll()
user_1.spend_points()
user_2.spend_points()
        


# user_1 = UserData("dan","Danerson","dan@dan.com",43)    
# print(user_1.age,user_1.email,user_1.first_name,user_1.last_name)    
