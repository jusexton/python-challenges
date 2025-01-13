def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    if n == 0:
        return True

    for i in range(len(flowerbed)):
        left_vacant = i == 0 or flowerbed[i - 1] == 0
        right_vacant = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
        if flowerbed[i] == 0 and left_vacant and right_vacant:
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True
    return False
