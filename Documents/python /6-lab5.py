# class FirewallRule:
    
#     def apply_rule(self):
#         return "Applying generic rule."
    
# class IPBlockRule(FirewallRule):
    
#     def apply_rule(self):
#         return "Blocking IP address."
    
# class PortBlockRule(FirewallRule):
    
#     def apply_rule(self):
#         return "Blocking port number."
    
# firewallrule = [FirewallRule(),IPBlockRule(),PortBlockRule()]

# for i in firewallrule:
#     print("Firewall Action:",i.apply_rule())



#Exercise6
class FirewallRule:
    def apply_rule(self):
        print("Applying generic rulde.")
class IPBlockRule(FirewallRule):
    def apply_rule(self):
        print("Blocking IP address.")
class PortBlockRule(FirewallRule):
    def apply_rule(self):
        print("Blocking port nmber.")

firewallrule = [FirewallRule(),IPBlockRule(),PortBlockRule()]

for i in firewallrule:
    print("Firewall Action:",end="")
    if i is not None:
        print(i.apply_rule())