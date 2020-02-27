def next_permutation(arr):

    n = len(arr)-1
    i = n
    while arr[i-1] > arr[i]:
        i -= 1
        if i == 0:
            return -1

    j = i-1
    diff = 10000
    position_to_switch = 0
    for k in range(i, n+1):
        if arr[k]-arr[j] > 0:
            diff = min(diff, arr[k]-arr[j])
    for m in range(i, n+1):
        if arr[m]==arr[j]+diff:
            position_to_switch = m
            break
    temp = arr[j]
    arr[j] = arr[position_to_switch]
    arr[position_to_switch] = temp
    temp_list = arr[j+1:]
    temp_list.sort()
    arr = arr[:j+1]
    arr = arr + temp_list
    #arr[j+1:].sort()
    return arr


if __name__=='__main__':

    num_of_city = int(input())
    weight = []
    for i in range(num_of_city):
        weight.append(list(map(int, input().split())))
    
    city = []
    for i in range(num_of_city):
        city.append(i)

    # the number of permutation
    num_of_per = 1
    for i in range(num_of_city-1):
        num_of_per *= i+1
 
    possible_path = []

    # making cycle path
    path = city[0:]
    path.append(city[0])
    possible_path = path[0:]
    
    cost = 1000000 * num_of_city
    temp_cost = 0
    for j in range(len(possible_path)-1):
        if j != len(possible_path)-1:
            temp_cost += weight[possible_path[j]][possible_path[j+1]]

        # when w[i][j]==0
        if weight[possible_path[j]][possible_path[j+1]]==0:
            temp_cost = 1000000 * num_of_city
            break
    cost = min(cost, temp_cost)

    middle_point = path[:-1]
    for j in range(num_of_per-1):
        middle_point = next_permutation(middle_point)
        path2 = middle_point[0:]
        path2.append(middle_point[0])
        possible_path = path2[0:]

        temp_cost = 0
        for k in range(len(possible_path)-1):
            temp_cost += weight[possible_path[k]][possible_path[k+1]]

            # when w[i][j]==0
            if weight[possible_path[k]][possible_path[k+1]]==0:
                temp_cost = 1000000 * num_of_city
                break
        cost = min(cost, temp_cost)
    print(cost)



    