# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7

def not_equal(arr, pos):
    for x in range(pos, len(arr)):
        if arr[x]!= arr[pos]:
            return arr[x]
    return arr[pos]    


def pick_peaks(arr):
    pos = []
    peaks = []
    for x in range(1, len(arr)-1):
        if arr[x] > arr[x+1] and arr[x] > arr[x-1]:
            pos.append(x)
            peaks.append(arr[x])
            
        elif arr[x] > arr[x-1] and arr[x] == arr[x+1]:
            if not_equal(arr, x) < arr[x]:
                pos.append(x)
                peaks.append(arr[x])
    return {"pos": pos, "peaks": peaks} 