from art import logo
from art import vs
from game_data import data
import random

print(logo)


def compare(ca ,cb):
    if ca>cb:
        return choosen_a
    elif ca<cb:
        return choosen_b
    else:
        return 0
lost=True
choosen_a = random.choice(list(data))
count=0
while lost:
    print(
        f"Compare A :{choosen_a['name']} is ' {choosen_a['description']} ' from {choosen_a['country']}")
    choosen_b = random.choice(list(data))
    print(vs)
    while choosen_a == choosen_b:
        choosen_b = random.choice(list(data))
    print(
        f"Compare B :{choosen_b['name']} is ' {choosen_b['description']} ' from {choosen_b['country']} \n")
    a = int(choosen_a["follower_count"])
    b = int(choosen_b["follower_count"])
    c_val = compare(a, b)
    choice=input("which one is higher A or B :").lower()
    if  choice=="a":
        if c_val==choosen_a:
            print(
                f"Compare A :{choosen_a['name']} follower count: {choosen_a['follower_count']}")
            print(
                f"Compare B :{choosen_b['name']} follower count: {choosen_b['follower_count']} ")
            print("you won the game\n")
            choosen_a=c_val
            compare(a,b)
            count+=1
            lost=True
        else:
            print("you lost the game")
            print(f"score {count}")
            lost=False
    elif choice=="b":
        if c_val==choosen_b:
            print(
                f"Compare A :{choosen_a['name']} follower count: {choosen_a['follower_count']}")
            print(
                f"Compare B :{choosen_b['name']} follower count: {choosen_b['follower_count']} ")
            print("you won the game\n\n")
            choosen_a=c_val
            compare(a,b)
            count += 1
            lost=True
        else:
            print("you lost the game")
            print(f"score {count}")
            lost=False
    else:
        print("enter the correct choice")

