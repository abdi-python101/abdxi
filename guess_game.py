# importing function
import webbrowser

new=2;
# the urls for the lose/win screens
url= "https://www.youtube.com/watch?v=VnQKkN6Mm-8";
url2 =  "https://www.youtube.com/watch?v=-auktieRCgw";


# improrting pythons build in module
import random
i = (random.randint(0,10))

lose_msg = "You lost get out of here!"
win_msg = "you won!!!"


welcome_msg = "Welcome to the guess game, you have 3 chances to win the game."
print(welcome_msg.upper())
guess_limit = 3
guess_count = 0
secret_num = i
while guess_count < guess_limit:
     guess = int(input("Guess my number from 0-10: "))
     guess_count += 1
     if guess == secret_num:
                print(win_msg.upper())
                webbrowser.open(url,new=new);
                break

else:
     print(lose_msg.upper())
     webbrowser.open(url2,new=new);


