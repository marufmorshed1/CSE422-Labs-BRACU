#####################TASK 01####################

def tracker(graph_matrix):
    area = 0
    visited = []
    for i in range(len(graph_matrix)):
        for j in range(len(graph_matrix[i])):
            if(graph_matrix[i][j] == 1 and (i,j) not in visited):
                area = max(DFS(i,j,len(graph_matrix),len(graph_matrix[0]),graph_matrix,visited),area)
    return area

##### DFS Implementation ######## 
def DFS(i,j,row,column,graph_matrix,visited):
    answer = 1
    visited.append((i,j))
    steps = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for x, y in steps:
        temp_loc = (i + x, j + y)
        if 0 <= temp_loc[0] < row and 0 <= temp_loc[1] < column:
            if temp_loc not in visited and graph_matrix[temp_loc[0]][temp_loc[1]]==1:
                answer += DFS(temp_loc[0], temp_loc[1], row, column, graph_matrix, visited)
    return answer


graph_matrix =[]
with open('problem1.txt') as file:
    lines= file.readlines()

for j in lines:  
    row = []
    for sign in j.split():
        if sign =="Y":
            row.append(1)
        else:
            row.append(0)
    graph_matrix.append(row)

max_area = tracker(graph_matrix)
print("Problem 1 output:", max_area)



################### PROBLEM : 02 #######################
def find_position(city):
    human_location = []
    alien_location = []
    for i in range(len(city)):
        for j in range(len(city[i])):
            if city[i][j] == 'A':
                alien_location.append((i, j))
            elif city[i][j] == 'H':
                human_location.append((i, j))
    return alien_location, human_location

##### BFS Implementation ######## 
def bfs(city, alien):
    time = -1
    steps = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    queue = []
    visited =[]
    for i in alien:
        visited.append(i);
        queue.append(i)
    while queue:
        level_size = len(queue);
        while (level_size):
            s = queue.pop(0)
            i = s[0];
            j = s[1]
            for x, y in steps:
                temp_loc = (i + x, j + y)
                if 0 <= temp_loc[0] < len(city) and 0 <= temp_loc[1] < len(city[0]):
                    if temp_loc not in visited and city[temp_loc[0]][temp_loc[1]] == 'H':
                        visited.append(temp_loc);
                        queue.append(temp_loc)
            level_size -= 1
        time += 1
    return time, len(visited) - len(alien)

# ------------driver code-----------#


file = open('problem2.txt', 'r+').readlines()

ROW = int(file[0])
COL = int(file[1])

city = []

for x in range(2, len(file)):
    arr = file[x].split(' ')
    row = []
    for j in arr:
        if(j != '\n'):
            row.append(j[0])
    city.append(row)
    alien, human = find_position(city)
    time, attacked_count = bfs(city, alien)   
    remaining = len(human) - attacked_count
print("\nProblem 2 output: ")
print("Time:", time, "minutes")
print(remaining, "survived! GGWP!") if remaining > 0 else print("No survivors left\n")

