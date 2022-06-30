#!/usr/bin/env python3

import json
import re
import markdownify
import argparse
from bs4 import BeautifulSoup

import html2text
from html.parser import HTMLParser
from pyquery import PyQuery
from lxml.html import fromstring
from lxml.html import parse

"""
URLs
https://tryhackme.com/api/tasks/[roomname]
https://tryhackme.com/api/room/details?codes=[roomname]
"""

parser = argparse.ArgumentParser()
parser.add_argument("-t", type=str, dest="title", required=False, help="Include room/challenge title.")
parser.add_argument("-d", type=str, dest="desc", required=False, help="Include task descriptions.")
parser.add_argument("-s", type=str, dest="summary", required=False, help="Include Summary section.")
parser.add_argument("-ss", type=str, dest="ssummary", required=False, help="Include Summary section with opening and closing.")
parser.add_argument("-r", type=str, dest="res", required=False, help="Include Additional Resources section.")
parser.add_argument("-a", type=bool, dest="ans", required=False, help="Include answers to questions.")
parser.add_argument("-n", type=str, dest="name", required=False, help="Optional name to include.")
parser.add_argument("-m", type=str, dest="mode", required=True, help="Mode:  json, html, url.")
#parser.add_argument("-r", dest="run", action="store_true", required=False, help="Test.")
args = parser.parse_args()
#args.mode = "html"
#args.run = True

tags = re.compile(r'(<!--.*?-->|<[^>]*>)')

def get_items(value):
	return list(value.items())
def get_keys(value):
	return list(value.keys())
def get_values(value):
	return list(value.values())

def get_room_html_file():
	with open("room.html", "r") as f:
		return BeautifulSoup(f.read(), "html.parser")

def get_room_json_file():
	with open("room.json", "r") as f:
		return json.loads(f.read())

def get_room_details_json_file():
	with open("details.json", "r") as f:
		return json.loads(f.read())

def get_room_details():
	data = json.loads('{ "title": "", "description": "" }')
	if args.mode == "html":
		room = get_room()
		data["title"] = room.find("h1", {"id": "title"}).get_text()
		data["description"] = room.find("p", {"id": "description"}).get_text()
	elif args.mode == "json":
		details = get_room_details_json_file()
		data["title"] = get_json_title(details)
		data["description"] = get_json_desc(details)
	return data

def get_json_title(details):
	for key, value in details.items():
		return value["title"]

def get_json_desc(details):
	for key, value in details.items():
		return value["description"]

def get_tasks(room):
	if args.mode == "html":
		return room.find("div", {"id": "taskContent"})
	elif args.mode == "json":
		return room["data"]

def print_room(room, file):
	for task in room["tasks"]:
		taskNo = task["number"]
		taskTitle = task["title"]
		taskDesc = task["description"]
		file.write(f"## Task {taskNo} - {taskTitle}\n\n")
		if args.desc:
			file.write(taskDesc + "\n") # Need at least new line, to put questions on new lines.
		for question in task["questions"][0]:
			answer = ""
			if (question['answer'].startswith("No answer needed") | args.ans):
				answer = question['answer']
			file.write(tags.sub("","".join(f"```\n{question['question']}\n> {answer}\n```\n\n".replace("<p>", "").replace("</p>", ""))))
			# file.write(tags.sub("","".join(f"```\n{question['question']}\n> \n```\n\n".replace("<p>", "").replace("</p>", ""))))


def print_header(file):
	if args.name != None:
		file.write(f"## {args.name}\n\n")
	if args.ssummary:
		file.write("## Summary\n")
		file.write("## Summary\n\n")
	elif args.summary:
		file.write("## Summary\n\n")

def print_footer(file):
	if args.res:
		file.write("## Additional Resources")

def get_room():
	if args.mode == "html":
		return get_room_html_file()
	elif args.mode == "json":
		return get_room_json_file()

def generate_md(room):
	title = room["title"]
	desc = room["description"]
	with open(f"{title}.md".replace(":", "").replace(" ", "").replace("/", "_"), "w") as f:
		if args.title:
			f.write(f"# Try Hack Me - {title}\n")
			f.write(f"##### {desc}\n\n")
		print_header(f)
		print_room(room, f)
		print_footer(f)

def parse_question(question, answer):
	json_question = json.loads('{ "question": "", "answer": "" }')
	q = ""
	a = ""
	if args.mode == "html":
		#value = question.find("div", {"class": "room-task-question-details"}).get_text().strip().replace("\n", "")
		json_question["question"] = question.find("div", {"class": "room-task-question-details"}).get_text().strip().replace("\n", "")
		value = answer.find("input", {"class": "room-answer-field"}).get('value')
		placeholder = answer.find("input", {"class": "room-answer-field"}).get('placeholder')
		if (value != None):
			json_question["answer"] = value
		else:
			json_question["answer"] = placeholder
	elif args.mode == "json":
		json_question["question"] = question["question"]
		json_question["answer"] = question["answerDesc"]

	return json_question

def parse_questions(task):
	questions = []
	
	if args.mode == "html":
		room_task_questions = task.find_all("div", {"class": "room-task-questions"})
		room_task_input = task.find_all("div", {"class": "room-task-input"})
		for x in range(0, len(room_task_questions)):
			questions.append(parse_question(room_task_questions[x], room_task_input[x]))
	elif args.mode == "json":
		for question in task["tasksInfo"]:
			questions.append(parse_question(question, {}))
		# for question in task["questions"]:
		# 	process_question(question, file)
	return questions

def parse_task_description(desc):
	# Using lxml.html - looks terrible.
	#doc = fromstring(desc)
	#return doc.text_content()

	# Using markdownify - lots of whitespace, broken lines, mostly plaintext, little formatting.
	#return markdownify.markdownify(desc, heading_style="ATX")

	# Using PyQuery - very clean, but just plain text.
	pq = PyQuery(desc)
	#pq.text().replace("<0xa0>", " ").replace("<0xfeff>", " ") ## This line is a comment, to clarify what is being replaced.
	clean = pq.text().replace(" ", " ").replace("﻿", " ")
	if (clean.startswith("Start Machine" + "\n")):
		clean = clean.replace("Start Machine" + "\n", "")
	elif (clean.startswith("Start Machine ")):
		clean = clean.replace("Start Machine ", "")
	elif (clean.startswith("View Site" + "\n")):
		clean = clean.replace("View Site" + "\n", "")
	elif (clean.startswith("View Site ")):
		clean = clean.replace("View Site ", "")
	return clean

	# Using html2text - Usable, but produces red lines and requires some clean-up.
	#h = html2text.HTML2Text()
	#return h.handle(desc)

def parse_task(task):
	json_task = json.loads('{ "number": 0, "title": "", "description": "", "questions": [] }')
	if args.mode == "html":
		# taskNo, json_task["title"] = task.a.get_text().strip().split("  ")
		output = task.a.get_text().strip().split("  ")
		strip_alpha = re.compile(r'[^\d.]+')
		json_task["number"] = strip_alpha.sub('', output[0])
		for x in range(1, len(output)):
			json_task["title"] += output[x] + " "
		room_task_desc_data = task.find("div", {"class": "room-task-desc-data"})
		json_task["description"] = parse_task_description(room_task_desc_data.prettify())
	elif args.mode == "json":
		json_task["number"] = task["taskNo"]
		json_task["title"] = task["taskTitle"]
		json_task["description"] = parse_task_description(task["taskDesc"])
	json_task["questions"].append(parse_questions(task))
	return json_task

def parse_tasks(room, json_room):
	tasks = get_tasks(room)
	if args.mode == "html":
		for x in range(1, len(tasks) + 1):
			task = tasks.find("div", {"id": f"task-{x}"})
			json_room["tasks"].append(parse_task(task))
	elif args.mode == "json":
		for task in tasks:
			json_room["tasks"].append(parse_task(task))
	return json_room

def parse_room():
	json_room = json.loads('{ "title": "", "description": "", "tasks": [] }')
	room_details = get_room_details()
	json_room["title"] = room_details["title"]
	json_room["description"] = room_details["description"]
	return parse_tasks(get_room(), json_room)

if __name__ == "__main__":
	room = parse_room()
	generate_md(room)
