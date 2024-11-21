import json

data = [
        {"ID": "700001",
         "CharacterID": "1",
         "CharacterName": "Generic Elf",
         "Class": "FIGHTER",
         "Level": "1",
         "Race": "Elf",
         "Campaign": "The Black Forest"},
        {"ID": "700001",
         "CharacterID": "2",
         "CharacterName": "Generic Drow",
         "Class": "FIGHTER",
         "Level": "10",
         "Race": "Elf",
         "Campaign": "The Black Forest"},
        {"ID": "700002",
         "CharacterID": "2",
         "CharacterName": "Generic Dwarf",
         "Class": "BARBARIAN",
         "Level": "20",
         "Race": "Dwarf",
         "Campaign": "The Black Forest"},
        {"ID": "700003",
         "CharacterID": "2",
         "CharacterName": "James Bond",
         "Class": "ROUGE",
         "Level": "10",
         "Race": "Human",
         "Campaign": "The Black Forest"}
    ]

# Convert to JSON string
json_string = json.dumps(data,indent=4)
print(json_string)

# Write to a file
with open('characterData.json', 'w') as file:
    json.dump(data, file)