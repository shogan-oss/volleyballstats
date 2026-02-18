
def hitting_percentage(kills, errors, attempts):
    if attempts == 0:
        return 0
    return round((kills - errors) / attempts, 3)

def serve_percentage(in_serves, total):
    if total == 0:
        return 0
    return round(in_serves / total, 3)

def pass_average(p1, p2, p3):
    total = p1 + p2 + p3
    if total == 0:
        return 0
    score = (1*p1 + 2*p2 + 3*p3)
    return round(score / total, 2)
