def isCyclicRotation(p: str, q: str) -> int:
    start=p[0]
    for i in range(len(p)):
        if q[i]==start:
            new=q[i:]+q[:i]
            if new==p:
                return 1
    return 0
