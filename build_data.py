import sys
import os
import re
import json
from glob import glob
import copy
from json_tricks import dumps
from math import floor
from random import randrange
import subprocess
from pyreadline.rlmain import Readline
import numpy as np
import shutil

# save np.load
np_load_old = np.load

# modify the default parameters of np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

def main(input_args):
	path = os.path.join(os.getcwd(), "complete_particle_list.txt")

	rl = Readline()
	rl.parse_and_bind("control-v: paste")

	if "--help" in input_args or "-h" in input_args:
		print("\nPossible Parameters:")
		print("-h|--help               a list of all possible parameters")
		print("-b|--build              retrieve all particles from the content folder")
		print("-p|--path               set the path for the content folder")
		print("--force_parse           force to parse built particles again")
		print("-l_[max]|--limit_[max]  set a maximum of particles to process")
		print("--dump                  writes all particle information in particle_dump.json")
		print("--count                 print the count of all particles")
		print("--operator              write a list of all operators in result.txt")
		print("--operator_count        write a list of all operators with their total number of occurances in result.txt")
		print("--operator_example      write a list of all operators with an random example in result.txt")
		print("--operator_fields       write a list of all operators with all their fields and types in result_fields.txt")
		print("--field_types           write a list of all fields types with count in result_types.txt")
		print("--search_field_value    Searches for particles with tath field")
		print("\nValve Resource Format support:")
		print("--vrf_path              set the folder to search for 'Decompiler.exe'")
		print("-g|--game_path          set the path for the game folder")
		print("--vrf_build             include compiled particles in search and decompile them")
		print("--vrf                   use decompiled particles (doesn't decompile them)")
		sys.exit()

	if len(input_args) == 0:
		print("\nNo arguments given. Abort...")
		print("Refer to help (-h|--help) for more information about arguments")
		sys.exit()

	if "--path" in input_args or "-p" in input_args:
		cPath = ""
		while cPath == "":
			cPath = input("Content Path: ")
		if not os.path.exists(cPath):
			print("This path does not exist. Exit...")
			sys.exit()
		else:
			set_content_path(cPath)

	if "--game_path" in input_args or "-g" in input_args:
		gPath = ""
		while gPath == "":
			gPath = input("Game Path: ")
		if not os.path.exists(gPath):
			print("This path does not exist. Exit...")
			sys.exit()
		else:
			set_game_path(gPath)

	useVrf = False
	buildVrf = False
	if "--vrf_build" in input_args:
		useVrf = True
		buildVrf = True
		vrfPath = get_vrf_path()
		if not vrfPath:
			if get_user_input("No path for vrf decompiler given.", useYN=True):
				if get_user_input("Use current directory?", useYN=True, preset=False):
					set_vrf_path(os.getcwd())
				else:
					newPath = get_user_input("Enter path to search: ")
					set_vrf_path(newPath)
		vrfPath = get_vrf_path()
		if not vrfPath:
			print("No Decompiler.exe found. Exit...")
			sys.exit()

	if not useVrf:
		if "--vrf" in input_args:
			useVrf = True

	if "--build" in input_args or "-b" in input_args:
		build_main_file(useVrf, buildVrf)
	if not os.path.isfile(path):
		print("WARNING! complete_particle_list.txt does not exist!")
		answer = None
		while answer is None:
			userInput = input("Do you want to build it now? (y|n) ")
			if userInput.lower() == "y" or userInput.lower() == "yes":
				answer = True
			elif userInput.lower() == "n" or userInput.lower() == "no":
				answer = False
		if answer:
			build_main_file(useVrf, buildVrf)
		else:
			print("Exit...")
			sys.exit()

	limit = -1

	for arg in input_args:
		match = re.search(r'(--limit|-l)_(\d+)', arg)
		if match:
			limit = int(match.group(2))

	if "-p" in input_args: input_args.remove("-p")
	if "--path" in input_args: input_args.remove("--path")
	if len(input_args) == 0:
		sys.exit()

	forceParse = False
	if "--force_parse" in input_args:
		forceParse = True

	particles = parse_main_file(limit, forceParse)

	text = ""
	resDict = {}

	if "--count" in input_args:
		print("\n\nCOUNT: " + str(len(particles)))

	if "--dump" in input_args:
		text = ""
		newDict = {}
		for k,v in particles.items():
			newDict[k] = v["content"].to_json()
		text += json.dumps(newDict, indent=4)
		with open(os.path.join(os.getcwd(), "particle_dump.txt"), "w") as file:
			file.write(text)

	if "--operator" in input_args:
		for pName, particle in particles.items():
			pItem = particle["content"]
			for item in pItem.get_objects():
				opName = item.get_name()
				if opName != "":
					if not opName in resDict:
						resDict[opName] = {}

	if "--operator_count" in input_args:
		for pName, particle in particles.items():
			pItem = particle["content"]
			for item in pItem.get_objects():
				opName = item.get_name()
				if opName != "":
					if not opName in resDict:
						resDict[opName] = {}
					if not "count" in resDict[opName]:
						resDict[opName]["count"] = 1
					else:
						resDict[opName]["count"] += 1

	if "--operator_example" in input_args:
		for pName, particle in particles.items():
			pItem = particle["content"]
			for item in pItem.get_objects():
				opName = item.get_name()
				if opName != "":
					if not opName in resDict:
						resDict[opName] = {}
						resDict[opName]["example"] = particle["path"]
					if not "example" in resDict[opName]:
						resDict[opName]["example"] = particle["path"]
					else:
						if randrange(0, 100) < 2000 / len(particles):
							resDict[opName]["example"] = particle["path"]

	if "--operator_count" in input_args:
		resDict = {k: v for k, v in sorted(resDict.items(), key=lambda x: x[1]["count"], reverse=True)}

	for opName, opDict in resDict.items():
		countText = ""
		exampleText = ""
		if "count" in opDict:
			opCount = opDict["count"]
			tabCount = (1 if opCount >= 1000 else 2) + 1
			countText = str(opCount) + "\t" * tabCount
		if "example" in opDict:
			nameLen = len(opName.replace("\"", ""))
			nameTabs = "\t" * (12 - int(nameLen / 4))
			exampleText = nameTabs + opDict["example"]
		text +=  countText + opName.replace("\"", "") + exampleText + "\n"

	if text != "":
		with open(os.path.join(os.getcwd(), "result.txt"), "w") as file:
			file.write(text)

	if "--operator_fields" in input_args:
		opDict = {}
		for pName, particle in particles.items():
			pItem = particle["content"]
			for item in pItem.get_objects():
				opName = item.get_name()
				newDict = item.to_json("type")
				if len(newDict) > 0:
					if not opName in opDict:
						opDict[opName] = {}
					opDict[opName].update(newDict)


		text = json.dumps(opDict, indent=4)

		if text != "":
			with open(os.path.join(os.getcwd(), "result_fields.txt"), "w") as file:
				file.write(text)

	if "--field_types" in input_args:
		fDict = {}
		for pName, particle in particles.items():
			pItem = particle["content"]
			for item in pItem.get_objects():
				for field in item.get_properties():
					fType = field.get_type()
					if not fType in fDict:
						fDict[fType] = 1
					else:
						fDict[fType] += 1

		fDict = {k: v for k, v in sorted(fDict.items(), key=lambda x: x[1], reverse=True)}

		text = ""
		for typeName, count in fDict.items():
			countLen = len(str(count))
			countTabs = "\t" * (2 - int(countLen / 4))
			text += str(count) + countTabs + typeName + "\n"

		with open(os.path.join(os.getcwd(), "result_types.txt"), "w") as file:
			if text != "":
				file.write(text)

	if "--search_field_value" in input_args:
		name = "_"
		value = ""
		if len(input_args) > 1:
			name = input_args[1]
		if len(input_args) > 2:
			value = input_args[2]
		valString = "any value"
		if value != "":
			valString = " the value " + value
		print("Searching for " + name + " with " + valString)
		results = {}
		for pName, particle in particles.items():
			pItem = particle["content"]
			for item in pItem.get_objects():
				for fName, field in item.get_properties_with_name():
					if fName == name:
						if value == "" or field.get_val() == value:
							# print(pName, fName, field.get_type())
							results[pName] = field.get_val()
		if len(results) == 0:
			print("Nothing found")
		else:
			index = 0
			maxIndex = 25
			print("First " + str(min(maxIndex,len(results))) + " results:\n")
			for pName, fVal in results.items():
				if index >= maxIndex:
					break
				index += 1
				print(" - " + pName + "; with value \"" + fVal + "\"")

	print("\nDone.")

def get_field_type(name, field, indent = 1):
	fieldType = ""
	if isinstance(field, CProperty):
		fieldType = field.get_type()
	elif isinstance(field, list):
		fieldType += "\n\t[\n"
		for f in field:
			if isinstance(f, CProperty):
				fieldType += f.get_type()
			elif isinstance(f, dict):
				fieldType += "\t\t{\n"
				for fName, fProperty in f.items():
					fieldType += get_field_type(fName, fProperty, indent + 2)
				fieldType += "\t\t},\n"
		fieldType += "\t]"
	elif isinstance(field, dict):
		fieldType += "\n" + "\t" * indent + "{\n"
		for fName, fProperty in field.items():
			fieldType += get_field_type(fName, fProperty, indent + 1)
		fieldType += "\t" * indent + "}"
	return "\t" * indent + name + " = " + fieldType + "\n"

def get_user_input(text, useYN = False, preset = True):
	if useYN:
		if preset:
			print(text)
		answer = None
		while answer is None:
			if preset:
				userInput = input("Do you want to set it now? (y|n) ")
			else:
				userInput = input(text + " (y|n) ")
			if userInput.lower() == "y" or userInput.lower() == "yes":
				answer = True
			elif userInput.lower() == "n" or userInput.lower() == "no":
				answer = False
		if answer:
			return True
	else:
		userInput = input(text)
		return userInput

def set_content_path(path):
	filePath = os.path.join(os.getcwd(), "settings.json")
	settings = {}
	if os.path.exists(filePath):
		with open(filePath, "r") as file:
			settings = json.load(file)
	with open(filePath, "r+") as file:
		settings["content_path"] = path
		json.dump(settings, file)
		subprocess.check_call(["attrib","+H","./settings.json"])

def get_content_path():
	if os.path.isfile(os.path.join(os.getcwd(), "settings.json")):
		with open(os.path.join(os.getcwd(), "settings.json"), "r") as file:
			settings = json.load(file)
			if "content_path" in settings:
				return settings["content_path"]
	return False

def set_game_path(path):
	filePath = os.path.join(os.getcwd(), "settings.json")
	settings = {}
	if os.path.exists(filePath):
		with open(filePath, "r") as file:
			settings = json.load(file)
	with open(filePath, "r+") as file:
		settings["game_path"] = path
		json.dump(settings, file)
		subprocess.check_call(["attrib","+H","./settings.json"])

def get_game_path():
	if os.path.isfile(os.path.join(os.getcwd(), "settings.json")):
		with open(os.path.join(os.getcwd(), "settings.json"), "r") as file:
			settings = json.load(file)
			if "game_path" in settings:
				return settings["game_path"]
	return False

def set_vrf_path(path):
	decPath = os.path.join(path, "Decompiler.exe")
	if not os.path.exists(decPath):
		print("No Decompiler.exe found. Exit...")
		sys.exit()

	filePath = os.path.join(os.getcwd(), "settings.json")
	settings = {}
	if os.path.exists(filePath):
		with open(filePath, "r") as file:
			settings = json.load(file)
	with open(filePath, "r+") as file:
		settings["vrf_path"] = path
		json.dump(settings, file)
		subprocess.check_call(["attrib","+H","./settings.json"])

def get_vrf_path():
	if os.path.isfile(os.path.join(os.getcwd(), "settings.json")):
		with open(os.path.join(os.getcwd(), "settings.json"), "r") as file:
			settings = json.load(file)
			if "vrf_path" in settings:
				return settings["vrf_path"]
	return False

def compile_files(decList):
	path = get_game_path()
	if not path:
		if get_user_input("No game path given.", useYN=True):
			newPath = get_user_input("Game Path:")
			if os.path.isdir(newPath):
				set_vrf_path(newPath)
			else:
				print("This path does not exit. Exit...")
				sys.exit()

	nameList = []
	for decPath in decList:
		namePattern = r'\\(.*?(\w+)\.vpcf)'
		nameMatch = re.search(namePattern, decPath)
		if nameMatch:
			name = nameMatch.group(2)
			nameList.append(name)


	results = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.vpcf_c'))]

	newResults = []
	for res in results:
		namePattern = r'\\(.*?(\w+)\.vpcf_c)'
		nameMatch = re.search(namePattern, res)
		if nameMatch:
			name = nameMatch.group(2)
			if not name in nameList:
				newResults.append(res)

	tempPath = "./temp_decompiled"

	pathCreated = False
	while not pathCreated:
		try:
			if os.path.isdir(tempPath):
				shutil.rmtree(tempPath)
			os.makedirs(tempPath)
			pathCreated = True
		except:
			pass
	
	subprocess.check_call(["attrib","+H",tempPath])

	vrfPath = os.path.join(get_vrf_path(), "Decompiler.exe")
	FNULL = open(os.devnull, 'w')

	maxCount = len(newResults)
	for i,res in enumerate(newResults):
		print_status("Decompiling found .vpcf_c files...", maxCount, i+1)
		relativePath = res.replace(path, "")[1:][:-2]
		command = vrfPath  + " -i \"%s\" -o \"%s\" --vpk_decompile" % (res, os.path.join(tempPath, relativePath))
		subprocess.call(command, shell=True, stdout=FNULL)

def build_main_file(useVrf, buildVrf):
	path = get_content_path()

	if not path:
		print("WARNING! you haven't set a path to your content folder yet!")
		answer = None
		while answer is None:
			userInput = input("Do you want to set it now? (y|n) ")
			if userInput.lower() == "y" or userInput.lower() == "yes":
				answer = True
			elif userInput.lower() == "n" or userInput.lower() == "no":
				answer = False
		if answer:
			cPath = ""
			while cPath == "":
				cPath = input("Content Path: ")
			if not os.path.exists(cPath):
				print("WARNING! This path does not exist!")
				sys.exit()
			else:
				set_content_path(cPath)

	path = get_content_path()

	print("Building main file...")
	# path = "C:\\SteamLibrary\\steamapps\\common\\dota 2 beta\\content\\dota\\particles"
	results = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.vpcf'))]

	if buildVrf:
		compile_files(results)

	if useVrf and os.path.isdir("./temp_decompiled"):
		results += [y for x in os.walk("./temp_decompiled") for y in glob(os.path.join(x[0], '*.vpcf'))]

	maxCount = len(results)
	index = 1
	completeText = ""
	for result in results:
		print_status("Retrieving data...", maxCount, index)
		index += 1

		namePattern = r'particles\\(.*?(\w+)\.vpcf)'
		nameMatch = re.search(namePattern, result)
		name = "!None\n"
		if nameMatch:
			name = "!" + nameMatch.group(2) + " (\"" + nameMatch.group(1) + "\")\n"

		with open(result) as file:
			text = file.read()
			completeText += name + text + "\n"

	print("Writing to complete_particle_list.txt...")
	with open(os.path.join(os.getcwd(), "complete_particle_list.txt"), "w") as file:
		file.write(completeText)

def parse_main_file(limit=-1,forceParse=False):
	parsedPath = os.path.join(os.getcwd(), "parsed_particles.npz")
	if os.path.exists(parsedPath) and not forceParse:
		print("Reading parsed particles...")
		saveFiles = np.load(parsedPath)
		newParticleDict = dict(zip(saveFiles["keys"][:limit], saveFiles["vals"][:limit]))
		return newParticleDict

	print("Reading main file...")
	particleDict = {}
	with open(os.path.join(os.getcwd(), "complete_particle_list.txt")) as file:
		pattern = r'(!(\w+)\s*?\((\".*?\")\)).*?(?P<tabs>^ *){\s(.*?^(?P=tabs))}'
		allMatches = re.finditer(pattern, file.read(), flags=re.S|re.M)
		test = None
		index = 0
		matches = []
		maxCount = 0
		for match in allMatches:
			maxCount += 1
			matches.append(match)
		for match in matches:
			print_status("Reading particle effects...", maxCount, index + 1)
			name = match.group(2)
			particleDict[name] = {}
			particleDict[name]["path"] = match.group(3)
			particleDict[name]["text"] = match.group(5)
			particleDict[name]["content"] = {}

			index += 1
			if limit > 0:
				if index > limit:
					break

	newParticleDict = copy.deepcopy(particleDict)
	maxCount = len(particleDict)
	index = 1
	for pName, pAttr in particleDict.items():
		print_status("Parsing particle effects...", maxCount, index)
		index += 1
		text = pAttr["text"]
		newParticleDict[pName]["content"] = add_content(text, pName)
		del newParticleDict[pName]["text"]

	print("Saving parsed particles...")
	np.savez(parsedPath, keys=list(newParticleDict.keys()), vals=list(newParticleDict.values()))

	return newParticleDict

def add_content(content, itemName=""):

	newItem = CItem(itemName)

	subPattern = r'(\w+) =\s+?(?P<tabs>^\s*)\[\s(.*?^(?P=tabs))\]'
	subMatches = re.finditer(subPattern, content, flags=re.S|re.M)
	for subMatch in subMatches:
		name = subMatch.group(1)
		text = subMatch.group(3)
		content = content.replace(subMatch.group(0), "")

		if name == "m_controlPointConfigurations":
			continue

		listPattern = r'(?P<tabs>^\s*){\s(.*?^(?P=tabs))}'
		listMatches = re.finditer(listPattern, text, flags=re.S|re.M)

		for listMatch in listMatches:
			text = listMatch.group(2)
			newItem.add_object(name, add_content(text))

		listPattern = r'(\w+)(,|\s*])'
		listMatches = re.finditer(listPattern, text, flags=re.S|re.M)

		attrText = "[ "
		for listMatch in listMatches:
			attrText += listMatch.group(1) + ","
		attrText += " ]"
		if attrText != "[  ]":
			newItem.add_attribute(name, CProperty("vector", attrText))

	subPattern = r'(\w+) =\s+?(?P<tabs>^\s*){\s(.*?^(?P=tabs))}'
	subMatches = re.finditer(subPattern, content, flags=re.S|re.M)

	for subMatch in subMatches:
		name = subMatch.group(1)
		text = subMatch.group(3)
		content = content.replace(subMatch.group(0), "")

		newItem.add_object(name, add_content(text))

	attrPattern = r'(\w+) = (\"\"\"(.*)\"\"\"|\"(.*?)\"|[\w|.-:\" \[,\]]+)'
	attrMatches = re.finditer(attrPattern, content, flags=re.S)
	for attrMatch in attrMatches:
		attrName = attrMatch.group(1)
		attrNamePrefixMatch = re.match(r'm_([a-z]+)', attrName)
		attrNamePrefix = ""
		if attrNamePrefixMatch:
			attrNamePrefix = attrNamePrefixMatch.group(1)
		attrType = get_type(attrNamePrefix)
		attrVal = attrMatch.group(2)
		if attrMatch.group(4) is not None:
			attrVal = attrMatch.group(4)
		if "\"\"\"" in attrVal:
			attrVal = attrMatch.group(3).lstrip()
		if attrName == "m_ChildRef":
			attrType = "resource"
		newProperty = CProperty(attrType, attrVal)
		newItem.add_attribute(attrName, newProperty)

	return newItem

class CProperty():
	def __init__(self, cType, val):
		self.cType = cType
		self.val = val
		if self.val.find("[") >= 0:
			matches = re.finditer(r'(\w+)(,|\s*])', self.val)
			self.val = []
			self.cType = "vector"
			for match in matches:
				self.val.append(match.group(1))

	def is_type(self, cType):
		return self.cType == cType

	def get_val(self):
		return str(self.val)

	def get_type(self):
		return self.cType

	def to_json(self):
		return str(self)

	def __str__(self):
		typeString = ""
		if self.cType != "":
			typeString = " (" + str(self.cType) + ")"
		return str(self.val) + typeString

	def __repr__(self):
		typeString = ""
		if self.cType != "":
			typeString = " (" + str(self.cType) + ")"
		return "<" + str(self.val) + typeString + ">"

	def __json_encode__(self):
		return {"cType": self.cType, "value": self.val}

class CItem():
	def __init__(self, name=""):
		self.name = ""
		self.attributes = {}
		self.objects = {}

	def add_attribute(self, name, val):
		if name == "_class":
			self.name = val.get_val()
		self.attributes[name] = val

	def add_object(self, name, obj):
		if name not in self.objects:
			self.objects[name] = []
		self.objects[name].append(obj)

	def has_attribute(self, name):
		return name in self.attributes

	def has_object(self, name):
		found = False
		for k,v in self.objects.items():
			for item in v:
				if name == item.get_name():
					found = True
		return found

	def has_object_list(self, name):
		return name in self.objects

	def get_name(self):
		return self.name

	def get_attributes(self):
		return self.attributes

	def get_object_list(self):
		return self.objects

	def get_objects(self):
		newList = []
		for k,v in self.objects.items():
			for item in v:
				newList.append(item)
		return newList

	def get_properties(self):
		newList = []
		for k,v in self.attributes.items():
			newList.append(v)
		for k,v in self.objects.items():
			for item in v:
				newList += item.get_properties()
		return newList

	def get_properties_with_name(self):
		newKeys = []
		newVals = []
		for k,v in self.attributes.items():
			newKeys.append(k)
			newVals.append(v)
		for k,v in self.objects.items():
			for item in v:
				for keys, vals in item.get_properties_with_name():
					newKeys.append(keys)
					newVals.append(vals)
		return list(zip(newKeys, newVals))

	def to_json(self, parseType="normal"):
		newDict = {}
		for k,v in self.attributes.items():
			if parseType == "normal":
				newDict[k] = str(v)
			elif parseType == "type" and k != "_class":
				newDict[k] = v.get_type()
		for k,v in self.objects.items():
			if len(v) == 1:
				newDict[k] = v[0].to_json(parseType)
			elif len(v) > 1:
				newDict[k] = []
				for item in v:
					newDict[k].append(item.to_json(parseType))
		return newDict

	def __str__(self):
		mainDict = self.to_json()
		# return json.dumps(mainDict)
		return "Item(" + self.name + ") " + str(mainDict)

	def __repr__(self):
		return "<CItem(" + self.name + "; attr:" + str(len(self.attributes)) + "; obj:" + str(len(self.objects)) + ")>"


def get_type(typeString):
	if typeString == "n" or typeString == "i":
		return "integer"
	elif typeString == "fl" or typeString == "f" or typeString == "cube" or typeString == "render" or typeString == "cutoff" or typeString == "fsize":
		return "float"
	elif typeString == "b" or typeString == "use":
		return "boolean"
	elif typeString == "vec" or typeString == "values":
		return "vector"
	elif typeString == "ang":
		return "angle"
	elif typeString == "h":
		return "resource"
	elif typeString == "model" or typeString == "preview" or typeString == "output":
		return "model"
	elif typeString == "entity":
		return "[self|parent]"
	elif typeString == "name" or typeString == "str":
		return "string"
	elif typeString == "attach" or typeString == "attachment":
		return "attachment"
	elif typeString == "sequence":
		return "sequence"
	elif typeString == "material":
		return "material"
	elif typeString == "hitbox":
		return "hitbox"
	elif typeString == "spline" or typeString == "tangents" or typeString == "v":
		return "vector2D"
	elif typeString == "drivers":
		return "CPs"
	elif typeString == "psz":
		return "sound name | snapshot"
	elif typeString == "specular" or typeString == "rim":
		return "color vector"
	elif typeString == "p":
		return "texture"
	elif typeString == "sz":
		return "render attribute"
	elif typeString == "ground":
		return "ground type"
	if typeString != "":
		# print("unknown type: ", typeString)
		pass
	return "string"

def print_status(message, maxC, curC):
	count = floor(20 * (curC / maxC))
	smallCount = int(200 * (curC / maxC)) % 10
	print(message + "   [" + "#" * count + " " * (20 - count) + "]   " + ">" * smallCount + " " * 10, end = "\r")
	if maxC == curC:
		print(message + "   [" + "#" * 20 + "]   DONE")

if __name__ == "__main__":
	main(sys.argv[1:])