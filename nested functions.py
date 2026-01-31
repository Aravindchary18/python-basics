def yaya():
    count=1

    def gaga():
        nonlocal count
        count+=3
        return count
    return gaga
gaga=yaya()
print(gaga())