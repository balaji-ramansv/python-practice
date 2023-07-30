def get_container_with_most_water(heights):
    areas = []
    l_to_r = 0
    r_to_l = len(heights)
    
    while l_to_r < r_to_l-1:
        areas.append(min([heights[l_to_r], heights[r_to_l-1]]) * (r_to_l-1 - l_to_r))
        l_to_r += 1
        print(areas)
    print(areas)

get_container_with_most_water([1,8,6,2,5,4,8,3,7]) 