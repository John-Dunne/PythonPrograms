#John Dunne (Jd5an)

def big_root(a,b,c):
    root1= (-b+((b**2)-4*a*c)**(1/2))/2*a
    root2= (-b - ((b ** 2) - 4 * a * c) ** (1 / 2)) / 2 * a
    return max(root1,root2)
def small_root(a,b,c):
    root1= (-b+((b**2)-4*a*c)**(1/2))/2*a
    root2= (-b - ((b ** 2) - 4 * a * c) ** (1 / 2)) / 2 * a
    return min(root1,root2)
