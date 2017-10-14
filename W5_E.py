def move_disks(n, fromTower, toTower, auxTower, sol):
    if n > 0:
        move_disks(n - 1, fromTower, auxTower, toTower, sol)
        sol.append('Move disk ' + str(n) + ' from ' + fromTower + ' to ' + toTower)
        move_disks(n - 1, auxTower, toTower, fromTower, sol)
        return sol
    else:
        return sol

ans = []
print move_disks(3, 'A', 'B', 'C', ans)