def solution(food_times, k):
    answer = 0
    remove_set = {0}
    left_food = food_times
    for i in range(len(food_times)):
        min_time = min(left_food)
        print(left_food)
        print(min_time)
        if k < min_time * len(food_times):
            break
        for j in range(len(left_food)):
            left_food[j] = left_food[j] - min_time
        left_food = [i for i in left_food if i not in remove_set]
        k -= min_time * len(left_food)

    return answer

solution([3,1,2], 5)