class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.followers_list = []
        self.following = 0

    def print_name(self):
        print(f"User {self.id} is {self.username} and has {self.followers} followers.")

    def print_followers(self):
        if self.followers == 0:
            print(f"{self.username} has no followers")
        else:
            print(f"{self.username} has {self.followers} followers. They are {', '.join(self.followers_list)}")

    def follow(self, user):
        user.followers += 1
        user.followers_list.append(self.username)
        self.following += 1


user1 = User("0001", "Jonathan Rider")
user2 = User("0002", "Garima Rider")
user3 = User("003", "Amrita Rider")

user1.follow(user2)
user3.follow(user2)

user1.print_name()
user1.print_followers()
user2.print_name()
user2.print_followers()
