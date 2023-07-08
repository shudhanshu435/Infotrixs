import os
import pandas as pd


def title():
    print("\nWelcome to Contact Management System\n")


os.system('cls')
title()


def add():
    name = input("Enter your Name: ")
    email = input("Enter email: ")
    phone = input("Enter 10 digit phone number: ")
    while len(phone) != 10:
        phone = input("\tPlease enter 10 digit phone number: ")
    gender = input("Enter gender: ")
    address = input("Enter address: ")

    dif = pd.DataFrame({'Name': [name], 'Email': [email], 'Phone': [phone], 'Gender': [gender], 'Address': [address]})

    df = pd.read_csv('contact.csv')
    vertical_concat = pd.concat([df, dif], axis=0, ignore_index=True)
    vertical_concat.to_csv("contact.csv", index=False)


def view():
    df = pd.read_csv('contact.csv')
    print(df.to_string())


def search():
    search_student = input("Enter the name of student? ")
    df = pd.read_csv('contact.csv')
    df = df[df['Name'].str.lower().str.contains(search_student.lower())]
    if df.empty:
        print("Not found ")
    else:
        print(df.to_string())


def delete():
    delete_name = input("Enter the name of the person you want to delete? ")
    df = pd.read_csv('contact.csv')
    if delete_name in df['Name'].unique():
        df = df.drop(df[df.Name == delete_name].index)
        df.to_csv('contact.csv', index=False)
        print("\nContact has been deleted successfully!")
    else:
        print("\nNo such contact found!")


def update():
    update_name = input("Enter the name of the contact you want to update: ")
    df = pd.read_csv('contact.csv')
    if update_name in df['Name'].unique():
        df = df.drop(df[df.Name == update_name].index)
        df.to_csv('contact.csv', index=False)
        add()
        print("\nFile has been updated!")
    else:
        print("\nNo such existing contact found!")


def main():

    while True:
        print("\n***************** MAIN MENU *****************")
        print(" 1- Add a new Contact ")
        print(" 2- View Contacts ")
        print(" 3- Search Contact ")
        print(" 4- Delete Contact ")
        print(" 5- Update Contact ")
        print(" 6- Exit ")

        choice = int(input("Enter your choice(1-6): "))

        if choice == 1:
            add()
            print("\nContact added successfully!")
        elif choice == 2:
            view()
        elif choice == 3:
            search()
        elif choice == 4:
            delete()
        elif choice == 5:
            update()
        elif choice == 6:
            break


if __name__ == '__main__':
    main()

