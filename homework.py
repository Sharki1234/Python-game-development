group_names = ["Abnegation","Amnity","Candor","Dauntless","Erudite"]

group1_details = ("Abnegation","30","6/7/26","Kingston_Academy","Gold")
group2_details = ("Amnity","30","7/7/26","Tiffin_Girls","Gold")
group3_details = ("Candor","30","8/7/26","Fern_Hill","Silver")
group4_details = ("Dauntless","30","9/7/26","Latchmere","Bronze")
group5_details = ("Erudite","30","10/7/26","St_Lukes","Bronze")

for a in group1_details:
    print(a,end = " ")
for b in group2_details:
    print(b,end = " ")
for c in group3_details:
    print(c,end = " ")
for d in group4_details:
    print(d,end = " ")
for e in group5_details:
    print(e,end = " ")
print("\n")
group_name,group_size,competition_date,venue,medal_type =  group1_details
print("\n") 
group_name,group_size,competition_date,venue,medal_type =  group2_details
print("\n") 
group_name,group_size,competition_date,venue,medal_type =  group3_details
print("\n") 
group_name,group_size,competition_date,venue,medal_type =  group4_details 
print("\n") 
group_name,group_size,competition_date,venue,medal_type =  group5_details 

print(group_name)
print("\n") 
print(group_size)
print("\n") 
print(competition_date)
print("\n") 
print(venue)
print("\n") 
print(medal_type)