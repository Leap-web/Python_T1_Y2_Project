# # class SportLeague:
    
# #     def __init__(self):
# #         self.dic = {}
# #         self.team_name = None
# #     def add_team(self,team_name):
# #         if team_name not in self.dic:
# #             self.dic[team_name]=[]
# #             return f"Team {team_name} added."
    
# #     def add_player(self,id,name,position):
# #         # if self.team_name in self.dic:
# #         #     self.dic[self.team_name].append(id,name,position)
# #         #     if any(['id']==id and ['name'] ==name):
# #         #         return f"{name} player has already exist."
# #         # return f"ID:{id}, Name:{name}, Position:{position}"
# #         # if self.team_name in self.dic:
# #             if any(player['id'] == id and player['name'] == name for player in self.dic[self.team_name]):
# #                 return f"Player:{name} has already exist. "
# #             new_list = {"ID":id,"Name":name,"Position":position}
# #             self.dic[self.team_name] = new_list
# #             return f"Player {name} added to team {self.team_name}"
    
# #     def view_team(self,team_name):
# #         if team_name in self.dic:
# #             return f"Team {team_name} players:\n{self.dic[team_name]}"
# #         else:
# #             return f"Team {team_name} not found."
# class SportLeague:
    
#     def __init__(self):
#         self.dic = {}
#         self.team_name = None  # Initialize team_name as an attribute
    
#     def add_team(self, team_name):
#         if team_name not in self.dic:
#             self.dic[team_name] = []
#             self.team_name = team_name  # Set the current team_name
#             return f"Team {team_name} added."
#         return f"Team {team_name} already exists."
    
#     def add_player(self, id_player, name, position):
#         if self.team_name is None or self.team_name not in self.dic:
#             return "No team selected. Please add or select a team first."
        
#         # Check if player already exists in the current team
#         if any(player['ID'] == id_player and player['Name'] == name for player in self.dic[self.team_name]):
#             return f"Player {name} already exists in team {self.team_name}."

#         # Add new player to the current team
#         new_player = {"ID": id_player, "Name": name, "Position": position}
#         self.dic[self.team_name].append(new_player)
#         return f"Player {name} added to team {self.team_name}"
    
#     def view_team(self, team_name):
#         if team_name in self.dic:
#             players = "\n".join(
#                 f"ID: {player['ID']}, Name: {player['Name']}, Position: {player['Position']}"
#                 for player in self.dic[team_name]
#             )
#             return f"Team {team_name} players:\n{players}"
#         return f"Team {team_name} not found."
    
#     def update_player(self,team_name,id_player,name = None,position = None):
#         # if team_name in self.dic:
#         #     # if any(player['id'] == id for player in self.dic[self.team_name]):
#         #     #     for player in self.dic:
#         #     #         if player['name'] not in None:
#         #     #             if player['position'] not in None:
            
#         #     for player in self.dic[team_name]:
#         #         if player ['id_player'] == id_player:
#         #             if name is not None:
#         #                 player['name'] = name
#         #                 if position is not None:
#         #                     player['position'] = position
#         #                     return f"Player {id_player} updated to team {team_name}."
#         #     new_list = {"ID":id_player,"Name":name,"Position":position} 
#         #     self.dic[team_name].append(new_list)                   
#         # else:
#         #     return f"{team_name} does not exist."
        
#         def update_player(self, team_name, id_player, name=None, position=None):
#             if team_name in self.dic:
#                 for player in self.dic[team_name]:
#                     if player['id_player'] == id_player:
#                         if name is not None:
#                             player['name'] = name  # Correct assignment
#                         if position is not None:
#                             player['position'] = position  # Correct assignment
#                         return f"Player {id_player} updated in team {team_name}."
                
#                 # If player with id_player not found, add new player
#                 new_player = {"id_player": id_player, "name": name, "position": position}
#                 self.dic[team_name].append(new_player)
#                 return f"Player {id_player} added to team {team_name}."
#             else:
#                 return f"Team {team_name} does not exist."

#     def remove_player(self,team_name,id_player):
#         if team_name not in self.dic:
#             return f"{team_name} does not exist."
#         for index,player in enumerate(self.dic[team_name]):
#             if player['id_player'] == id_player:
#                 remove = self.dic[team_name].pop(index)
#                 return f"{player} remove from the team {team_name}"
#         else:
#             return f"{team_name} does not exist."

# sportleague = SportLeague()

# print(sportleague.add_team("Tiger"))
# print(sportleague.add_player(1,"Serey","Goalkeeper"))
# print(sportleague.add_player(2,"Dy","Goalkeeper"))

# print(sportleague.add_team("Lion"))
# print(sportleague.add_player(1,"Dara","Striker"))
# print(sportleague.add_player(2,"Ly","Defender"))

# print(sportleague.update_player("Tiger",1,"Serey","Goalkeeper"))

# print(sportleague.view_team("Tiger"))



class SportLeague:
    
    def __init__(self):
        self.dic = {}
        self.team_name = None  
    
    def add_team(self, team_name):
        if team_name not in self.dic:
            self.dic[team_name] = []
            self.team_name = team_name  
            return f"Team {team_name} added."
        return f"Team {team_name} already exists."
    
    def add_player(self, id_player, name, position):
        if self.team_name is None or self.team_name not in self.dic:
            return "No team selected. Please add or select a team first."

        if any(player['ID'] == id_player and player['Name'] == name for player in self.dic[self.team_name]):
            return f"Player {name} already exists in team {self.team_name}."
        
        new_player = {"ID": id_player, "Name": name, "Position": position}
        self.dic[self.team_name].append(new_player)
        return f"Player {name} added to team {self.team_name}"
    
    def view_team(self, team_name):
        if team_name in self.dic:
            players = "\n".join(
                f"ID: {player['ID']}, Name: {player['Name']}, Position: {player['Position']}"
                for player in self.dic[team_name]
            )
            return f"Team {team_name} players:\n{players}"
        return f"Team {team_name} not found."
    
    def update_player(self, team_name, id_player, name=None, position=None):
        if team_name in self.dic:
            for player in self.dic[team_name]:
                if player['ID'] == id_player:
                    if name is not None:
                        player['Name'] = name  
                    if position is not None:
                        player['Position'] = position  
                    return f"Player {id_player} updated in team {team_name}."
            
            new_player = {"ID": id_player, "Name": name, "Position": position}
            self.dic[team_name].append(new_player)
            return f"Player {id_player} added to team {team_name}."
        else:
            return f"Team {team_name} does not exist."

    def remove_player(self, team_name, id_player):
        if team_name not in self.dic:
            return f"Team {team_name} does not exist."
        
        for index, player in enumerate(self.dic[team_name]):
            if player['ID'] == id_player:
                removed_player = self.dic[team_name].pop(index)
                return f"Player {removed_player} removed from team {team_name}."
        
        return f"Player with ID {id_player} not found in team {team_name}."

sportleague = SportLeague()

print(sportleague.add_team("Tiger"))
print(sportleague.add_player(1, "Serey", "Goalkeeper"))
print(sportleague.add_player(2, "Dy", "Goalkeeper"))

print(sportleague.add_team("Lion"))
print(sportleague.add_player(1, "Dara", "Striker"))
print(sportleague.add_player(2, "Ly", "Defender"))

print(sportleague.update_player("Tiger", 1, "Serey", "Goalkeeper"))

print(sportleague.view_team("Tiger"))
print(sportleague.remove_player("Tiger", 2))  
print(sportleague.view_team("Tiger"))
