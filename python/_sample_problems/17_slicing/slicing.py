def secretname(name: str, year: int, color: str) -> str:
    return name[:2] + str(year)[-2:] + color[:3]
