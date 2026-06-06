import csv
import numpy as np
import pandas as pd
from collections import Counter

FILE = "players.csv"

def load_players():
    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)

def get_runs(player):
    return int(player["runs"])

print("1. Read players.csv")
with open(FILE, "r") as f:
    content = f.read()
print(content)

print("2. Display all records")
players = load_players()
for p in players:
    print(p)
print()

print("3. Count total players")
print(f"Total Players = {len(players)}")
print()

print("4. Highest run scorer")
highest = max(players, key=get_runs)
print(f"Highest Run Scorer = {highest['player_name']} ({get_runs(highest)})")
print()

print("5. Lowest run scorer")
lowest = min(players, key=get_runs)
print(f"Lowest Run Scorer = {lowest['player_name']} ({get_runs(lowest)})")
print()

print("6. Average runs")
total_runs = sum(get_runs(p) for p in players)
avg_runs = total_runs / len(players)
print(f"Average Runs = {avg_runs:.2f}")
print()

print("7. Players scoring more than 600 runs")
for p in players:
    if get_runs(p) > 600:
        print(f"{p['player_name']} = {get_runs(p)}")
print()

print("8. Players scoring less than 500 runs")
for p in players:
    if get_runs(p) < 500:
        print(f"{p['player_name']} = {get_runs(p)}")
print()

print("9. Count players by team")
team_count = Counter(p["team"] for p in players)
for team, count in team_count.items():
    print(f"{team} = {count}")
print()

print("10. Total runs by team")
team_runs = {}
for p in players:
    t = p["team"]
    team_runs[t] = team_runs.get(t, 0) + get_runs(p)
for team, runs in team_runs.items():
    print(f"{team} = {runs}")
print()

print("11. Team with highest runs")
top_team = max(team_runs, key=team_runs.get)
print(f"Team with Highest Runs = {top_team} ({team_runs[top_team]})")
print()

print("12. Team with lowest runs")
low_team = min(team_runs, key=team_runs.get)
print(f"Team with Lowest Runs = {low_team} ({team_runs[low_team]})")
print()

print("13. Player with most fours")
most_fours = max(players, key=lambda p: int(p["fours"]))
print(f"Most Fours = {most_fours['player_name']} ({most_fours['fours']})")
print()

print("14. Player with most sixes")
most_sixes = max(players, key=lambda p: int(p["sixes"]))
print(f"Most Sixes = {most_sixes['player_name']} ({most_sixes['sixes']})")
print()

print("15. Total fours hit in tournament")
total_fours = sum(int(p["fours"]) for p in players)
print(f"Total Fours = {total_fours}")
print()

print("16. Total sixes hit in tournament")
total_sixes = sum(int(p["sixes"]) for p in players)
print(f"Total Sixes = {total_sixes}")
print()

print("17. Player names list sorted alphabetically")
names_list = sorted(p["player_name"] for p in players)
print(names_list)
print()

print("18. Unique teams set")
teams_set = set(p["team"] for p in players)
print(teams_set)
print()

print("19. Dictionary team : total_runs")
team_runs_dict = {}
for p in players:
    t = p["team"]
    team_runs_dict[t] = team_runs_dict.get(t, 0) + get_runs(p)
print(team_runs_dict)
print()

print("20. Dictionary player_name : runs")
player_runs_dict = {p["player_name"]: get_runs(p) for p in players}
print(player_runs_dict)
print()

print("21. find_top_scorer()")
def find_top_scorer():
    players = load_players()
    top = max(players, key=get_runs)
    return top["player_name"]
print(f"Top Scorer = {find_top_scorer()}")
print()

print("22. calculate_average_runs()")
def calculate_average_runs():
    players = load_players()
    return sum(get_runs(p) for p in players) / len(players)
print(f"Average Runs = {calculate_average_runs():.2f}")
print()

print("23. find_best_team()")
def find_best_team():
    players = load_players()
    team_runs = {}
    for p in players:
        t = p["team"]
        team_runs[t] = team_runs.get(t, 0) + get_runs(p)
    return max(team_runs, key=team_runs.get)
print(f"Best Team = {find_best_team()}")
print()

print("24. find_total_boundaries()")
def find_total_boundaries():
    players = load_players()
    total_fours = sum(int(p["fours"]) for p in players)
    total_sixes = sum(int(p["sixes"]) for p in players)
    return total_fours + total_sixes
print(f"Total Boundaries = {find_total_boundaries()}")
print()

print("25. Handle missing CSV file")
try:
    with open("missing_file.csv", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("Error: CSV file not found.")
print()

print("26. Handle invalid run values")
test_rows = [
    {"player_id": "999", "player_name": "Test", "team": "X", "matches": "14", "runs": "abc", "fours": "10", "sixes": "5"},
]
for row in test_rows:
    try:
        runs = int(row["runs"])
    except ValueError:
        print(f"Error: Invalid run value '{row['runs']}' for player {row['player_id']}.")
print()

print("27. Handle invalid match counts")
test_rows2 = [
    {"player_id": "998", "player_name": "Test", "team": "X", "matches": "xyz", "runs": "100", "fours": "10", "sixes": "5"},
]
for row in test_rows2:
    try:
        matches = int(row["matches"])
    except ValueError:
        print(f"Error: Invalid match count '{row['matches']}' for player {row['player_id']}.")
print()

print("28. NumPy array of runs")
players = load_players()
runs_array = np.array([get_runs(p) for p in players])
print(f"Runs Array         = {runs_array}")
print(f"Total Runs         = {np.sum(runs_array)}")
print(f"Average Runs       = {np.mean(runs_array):.2f}")
print(f"Maximum Runs       = {np.max(runs_array)}")
print(f"Minimum Runs       = {np.min(runs_array)}")
print(f"Standard Deviation = {np.std(runs_array):.2f}")
print(f"Median             = {np.median(runs_array):.2f}")
print()

print("29. Read CSV using Pandas")
df = pd.read_csv(FILE)
print(df)
print()

print("30. Top 5 run scorers")
top5 = df.nlargest(5, "runs")
print(top5[["player_id", "player_name", "team", "runs"]])
print()

print("31. Players sorted by runs descending")
sorted_df = df.sort_values("runs", ascending=False).reset_index(drop=True)
print(sorted_df[["player_name", "team", "runs"]])
print()

print("32. Group by team and calculate total runs")
team_total = df.groupby("team")["runs"].sum().reset_index()
team_total.columns = ["team", "total_runs"]
print(team_total)
print()

print("33. Group by team and calculate average runs")
team_avg = df.groupby("team")["runs"].mean().reset_index()
team_avg.columns = ["team", "average_runs"]
print(team_avg)
print()

print("34. Players with runs > 600")
high_scorers = df[df["runs"] > 600]
print(high_scorers[["player_name", "team", "runs"]])
print()

print("35. Top team")
top_team_df = df.groupby("team")["runs"].sum()
print(f"Top Team = {top_team_df.idxmax()} ({top_team_df.max()})")
print()


print("REPORT GENERATION")
print()

players = load_players()
all_runs = [get_runs(p) for p in players]
team_rev = {}
for p in players:
    t = p["team"]
    team_rev[t] = team_rev.get(t, 0) + get_runs(p)

top5_players = sorted(players, key=get_runs, reverse=True)[:5]
most_fours_p = max(players, key=lambda p: int(p["fours"]))
most_sixes_p = max(players, key=lambda p: int(p["sixes"]))

report = f"""===== Report =====

Total Players        : {len(players)}
Total Runs           : {sum(all_runs)}
Average Runs         : {sum(all_runs)/len(all_runs):.2f}
Highest Scorer       : {max(players, key=get_runs)['player_name']} ({max(all_runs)})
Lowest Scorer        : {min(players, key=get_runs)['player_name']} ({min(all_runs)})

Team Wise Runs:
"""
for team, runs in sorted(team_rev.items()):
    report += f"  {team:<15} : {runs}\n"

report += "\nTop 5 Players:\n"
for p in top5_players:
    report += f"  {p['player_name']:<20} : {get_runs(p)}\n"

report += f"\nMost Fours : {most_fours_p['player_name']} ({most_fours_p['fours']})\n"
report += f"Most Sixes : {most_sixes_p['player_name']} ({most_sixes_p['sixes']})\n"

with open("cricket_report.txt", "w") as f:
    f.write(report)

print("File 'cricket_report.txt' created.")
print(report)


print("BONUS TASKS")
print()

print("36. top_players.csv (runs above 600)")
df["runs"] = df["runs"].astype(int)
top_players = df[df["runs"] > 600]
top_players.to_csv("top_players.csv", index=False)
print("File 'top_players.csv' created.")
print(top_players.to_string(index=False))
print()

print("37. team_summary.csv")
team_summary = df.groupby("team").agg(
    total_runs=("runs", "sum"),
    average_runs=("runs", "mean"),
    player_count=("player_name", "count")
).reset_index()
team_summary.to_csv("team_summary.csv", index=False)
print("File 'team_summary.csv' created.")
print(team_summary.to_string(index=False))
print()

print("38. Menu-Driven Application")

def player_analysis():
    players = load_players()
    print(f"\n{'ID':<8}{'Player':<22}{'Team':<6}{'Matches':<10}{'Runs':<8}{'Fours':<8}{'Sixes'}")
    for p in players:
        print(f"{p['player_id']:<8}{p['player_name']:<22}{p['team']:<6}{p['matches']:<10}{p['runs']:<8}{p['fours']:<8}{p['sixes']}")
    print(f"\nHighest Scorer : {max(players, key=get_runs)['player_name']} ({max(get_runs(p) for p in players)})")
    print(f"Lowest Scorer  : {min(players, key=get_runs)['player_name']} ({min(get_runs(p) for p in players)})")
    print(f"Average Runs   : {sum(get_runs(p) for p in players)/len(players):.2f}")

def team_analysis():
    players = load_players()
    team_runs = {}
    team_count = Counter(p["team"] for p in players)
    for p in players:
        t = p["team"]
        team_runs[t] = team_runs.get(t, 0) + get_runs(p)
    print(f"\n{'Team':<8}{'Players':<10}{'Total Runs'}")
    for team in sorted(team_runs):
        print(f"{team:<8}{team_count[team]:<10}{team_runs[team]}")
    print(f"\nTop Team : {max(team_runs, key=team_runs.get)}")

def boundary_analysis():
    players = load_players()
    total_fours = sum(int(p["fours"]) for p in players)
    total_sixes = sum(int(p["sixes"]) for p in players)
    most_fours = max(players, key=lambda p: int(p["fours"]))
    most_sixes = max(players, key=lambda p: int(p["sixes"]))
    print(f"\nTotal Fours  : {total_fours}")
    print(f"Total Sixes  : {total_sixes}")
    print(f"Most Fours   : {most_fours['player_name']} ({most_fours['fours']})")
    print(f"Most Sixes   : {most_sixes['player_name']} ({most_sixes['sixes']})")

def export_reports():
    df = pd.read_csv(FILE)
    df["runs"] = df["runs"].astype(int)
    df[df["runs"] > 600].to_csv("top_players.csv", index=False)
    team_summary = df.groupby("team").agg(
        total_runs=("runs", "sum"),
        average_runs=("runs", "mean"),
        player_count=("player_name", "count")
    ).reset_index()
    team_summary.to_csv("team_summary.csv", index=False)
    print("\nExported: top_players.csv")
    print("Exported: team_summary.csv")

menu_options = {
    "1": ("Player Analysis", player_analysis),
    "2": ("Team Analysis", team_analysis),
    "3": ("Boundary Analysis", boundary_analysis),
    "4": ("Export Reports", export_reports),
}

print("\nRunning all menu options automatically:")
for key in ["1", "2", "3", "4"]:
    label, func = menu_options[key]
    print(f"\n[{key}] {label}")
    func()

print("\n[5] Exit")
print("Exiting application.")
