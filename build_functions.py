import sys
import os
import jellyfish
import re
import json

helpDict = {}

def main(input_args):
	build_help()
	if len(input_args) > 0:
		build_md()
	else:
		file1, file2 = read_files()
		operators = build_list(file1, file2)

def read_files():
	path = os.getcwd()
	file1 = []
	file2 = {}
	with open(os.path.join(path, "particle_names.txt")) as file:
		file = list(map(lambda x: x.replace("\n", ""),file.readlines()))
		lastGroup = ""
		for line in file:
			if "!" in line:
				lastGroup = line[1:]
			else:
				# file1[line] = lastGroup
				file1.append((line, lastGroup))
		# file1 = [line for line in file1 if ("!" not in line) and ("" != line)]
	with open(os.path.join(path, "particle_operator_usage.txt")) as file:
		file = list(map(lambda x: x.replace("\n", ""),file.readlines()))
		pattern = r'\s*(\d+)\s+"(\w+)"'
		for line in file:
			match = re.match(pattern, line)
			if match:
				# file2.append((match.group(2), match.group(1)))
				file2[match.group(2)] = match.group(1)

	return file1, file2

def build_list(file1, file2):
	operatorList = []
	for name, count in file2.items():
		index = name.rfind("_")
		newName = name[index + 1:]
		maxRatio = 0
		partner = ""
		partnerGroup = ""
		for fullName, group in file1:
			newFullName = fullName.lower().replace(" ", "")
			ratio = jellyfish.jaro_distance(newName, newFullName)
			if ratio > maxRatio:
				maxRatio = ratio
				partner = fullName
				partnerGroup = group
		operatorList.append((name, partner, partnerGroup, count))
	
	path = os.getcwd()
	with open(os.path.join(path, "particle_operators.txt"), "w") as file:
		text = ""
		for a,b,c,d in operatorList:
			aLen = len(a)
			aTabs = "\t" * (12 - int(aLen / 4))
			bLen = len(b)
			bTabs = "\t" * (16 - int(bLen / 4))
			cLen = len(c)
			cTabs = "\t" * (4 - int(cLen / 4))
			text += a + aTabs + b + bTabs + c + cTabs + d + "\n"
		file.write(text)

	return operatorList

def build_md():
	print("Building .md file!")
	path = os.getcwd()
	operatorList = []
	operatorDict = {}
	with open(os.path.join(path, "particle_operators_final.txt")) as file:
		file = list(map(lambda x: x.replace("\n", ""),file.readlines()))
		pattern = r'^(\w+)\s*([\w|" "]+)\s*([\w|-]+)\s*(\d+)'
		for line in file:
			match = re.match(pattern, line)
			if match:
				operatorList.append((match.group(1), match.group(2), match.group(3), match.group(4)))

	for cName, name, fType, count in operatorList:
		if not fType in operatorDict:
			operatorDict[fType] = []
		operatorDict[fType].append((cName, name, fType, count))

	text = "## Contents\n"
	counts = {}
	for fType, oList in operatorDict.items():
		text += "- " + make_link(fType, 0) + "\n"
		for cName, name, fType, count in oList:
			count = 0
			if name in counts:
				count = counts[name]
				counts[name] += 1
			else:
				counts[name] = 1
			text += "\t- " + make_link(name, count) + "\n"

	fields = get_fields()
	origNames = get_orig_classnames()

	for fType, oList in operatorDict.items():
		text += "## " + fType + "\n"
		for cName, name, fType, count in oList:
			origName = cName
			if cName in origNames:
				origName = origNames[cName]
			else:
				pass
				# print(cName, "not in origNames!")
			text += "\n### " + name + "\n|" + name + "| |\n|--|--|\n"
			text += "|Id|`" + origName + "`|\n"
			text += "|Usage Count|" + str(count) + "|\n"
			text += "Description (Valve)|" + get_automatic_description(cName) + "|\n"
			text += "Additional Notes|------------------|\n---\n"
			# text += "|Fields| |\n|--|--|\n"
			text += build_fields(cName, fields)

	with open(os.path.join(path, "functions_generated.md.txt"), "w") as file:
		file.write(text)

def build_fields(cName, fields):
	description = False
	tooltip = False

	for name, values in helpDict["attributes"].items():
		if values["parent"] == cName:
			if values["description"] != "":
				description = True
			if values["tooltip"] != "":
				tooltip = True
	
	if not tooltip and not description and cName not in fields:
		return ""
		# return "|Fields| |\n|--|--|\n"

	text = "|Fields|Type|\n|--|--|\n"
	if description and tooltip:
		text = "|Fields|Type|Description|Tooltip|\n|--|--|--|--|\n"
	elif description:
		text = "|Fields|Type|Description|\n|--|--|--|\n"
	elif tooltip:
		text = "|Fields|Type|Tooltip|\n|--|--|--|\n"

	for name, attType in fields[cName].items():
		attNamePrefixMatch = re.match(r'm_([a-z]+)', name)
		attNamePrefix = ""
		attName = ""
		if attNamePrefixMatch:
			attNamePrefix = attNamePrefixMatch.group(1)
		attName = get_name_from_string(name)

		if name in helpDict["attributes"]:
			attName = helpDict["attributes"][name]["name"].lower() if helpDict["attributes"][name]["name"] != "" else attName

		text += "|" + attName + "|" + attType + "|"

		if name in helpDict["attributes"]:
			if description:
				attDescription = helpDict["attributes"][name]["description"] if helpDict["attributes"][name]["description"] != "" else "-----"
				text += attDescription + "|"
			if description:
				attTooltip = helpDict["attributes"][name]["tooltip"] if helpDict["attributes"][name]["tooltip"] != "" else "-----"
				text += attTooltip + "|"

		text += "\n"

	# print("\nBuilding", text)
	return text

def get_fields():
	fields = {}
	with open(os.path.join(os.getcwd(), "result_fields.txt")) as file:
		data = json.load(file)
		for operator, val in data.items():
			if operator not in fields:
				fields[operator.lower()] = {}
			for attrName, attrType in val.items():
				if "m_nOp" not in attrName and "m_flOp" not in attrName and attrName != "m_bDisableOperator":
					if isinstance(attrType, str):
						fType = attrType
					else:
						fType = get_special_type(attrType, attrName)
					if fType != "":
						fields[operator.lower()][attrName] = fType
	return fields

def get_orig_classnames():
	classNames = {}
	with open(os.path.join(os.getcwd(), "result_fields.txt")) as file:
		data = json.load(file)
		for name in data.keys():
			classNames[name.lower()] = name
	return classNames


def get_special_type(typeDict, attrName):
	if isinstance(typeDict, dict):
		for key, val in typeDict.items():
			if "Literal" in key:
				return val + " (special)"
		for key, val in typeDict.items():
			if "Input" in key:
				return val + " (special)"
		if "path" in attrName.lower():
			return "path params (special)"
		if attrName == "VisibilityInputs":
			return "visibility inputs (special)"
		if "list" in attrName.lower():
			firstElem = ""
			for k,_ in typeDict.items():
				firstElem = k
				break
			return "list (" + get_name_from_string(firstElem) + ")"
		if "controlpoint" in attrName.lower():
			return "control point"
	else:
		if attrName == "m_MaterialVars":
			return "list (material vars)"
		return ""
	return "SPECIAL"

def get_name_from_string(name):
	newName = ""
	nameMatch = re.search(r'[A-Z]\w+', name)
	if nameMatch:
		newName = nameMatch.group()
		nameList = re.sub( r"([A-Z|\d])", r" \1", newName).split()
		nameList = list(map(lambda x: x.lower() if len(x) > 1 else x, nameList))
		newName = ""
		lastN = ""
		for n in nameList:
			if lastN != "":
				newName += " "
			
			if len(n) > 1:
				if lastN == "":
					newName += " "
				lastN = n
			else:
				lastN = ""
			newName += n
		newName = newName.lstrip()
	else:
		nameMatch = re.search(r'm_(\w+)', name)
		if nameMatch:
			newName = nameMatch.group(1)
	return newName

def get_automatic_description(cName):
	if cName in helpDict:
		if helpDict[cName]["description"] != "":
			return helpDict[cName]["description"]
	return "------------------"

def make_link(name, count):
	countString = ""
	if count:
		if count > 0:
			countString = "-" + str(count)
	return "[" + name + "](#" + name.lower().replace(" ", "-") + countString + ")"

def build_help():
	global helpDict
	helpDict["attributes"] = {}
	path = os.getcwd()
	with open(os.path.join(path, "operator_help.txt")) as file:
		data = json.load(file)
	for obj in data["m_Entries"]:
		objId = obj["m_Id"]
		if "Element" in objId:
			cName = objId[8:].lower()
			helpDict[cName] = {}
			helpDict[cName]["name"] = obj["m_FriendlyName"]
			helpDict[cName]["description"] = obj["m_HelpText"].replace("\n","")
		else:
			cName = objId[objId.rfind(".") + 1:]
			helpDict["attributes"][cName] = {}
			helpDict["attributes"][cName]["name"] = obj["m_FriendlyName"]
			helpDict["attributes"][cName]["description"] = obj["m_HelpText"].replace("\n","")
			helpDict["attributes"][cName]["tooltip"] = obj["m_TooltipOverride"]
			helpDict["attributes"][cName]["parent"] = objId[10:objId.rfind(".")].lower()


if __name__ == "__main__":
	main(sys.argv[1:])