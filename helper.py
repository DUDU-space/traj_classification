from math import radians, cos, sin, atan, tan, acos, degrees, atan2


def getDistance(latA, lonA, latB, lonB):
    latA, lonA = lonA, latA
    latB, lonB = lonB, latB
    ra = 6378140  # radius of equator: meter
    rb = 6356755  # radius of polar: meter
    flatten = (ra - rb) / ra  # Partial rate of the earth
    # change angle to radians
    radLatA = radians(latA)
    radLonA = radians(lonA)
    radLatB = radians(latB)
    radLonB = radians(lonB)

    pA = atan(rb / ra * tan(radLatA))
    pB = atan(rb / ra * tan(radLatB))
    x = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(radLonA - radLonB))
    c1 = (sin(x) - x) * (sin(pA) + sin(pB)) ** 2 / cos(x / 2) ** 2
    c2 = (sin(x) + x) * (sin(pA) - sin(pB)) ** 2 / sin(x / 2) ** 2
    dr = flatten / 8 * (c1 - c2)
    distance = ra * (x + dr)
    return distance


def getDegree(latA, lonA, latB, lonB):
    latA, lonA = lonA, latA
    latB, lonB = lonB, latB
    """
    Args:
        point p1(latA, lonA)
        point p2(latB, lonB)
    Returns:
        bearing between the two GPS points,
        default: the basis of heading direction is north
    """
    radLatA = radians(latA)
    radLonA = radians(lonA)
    radLatB = radians(latB)
    radLonB = radians(lonB)
    dLon = radLonB - radLonA
    y = sin(dLon) * cos(radLatB)
    x = cos(radLatA) * sin(radLatB) - sin(radLatA) * cos(radLatB) * cos(dLon)
    brng = degrees(atan2(y, x))   # 反正切函数
    brng = (brng + 360) % 360
    return brng


if __name__ == '__main__':
    print(getDegree(30, 120, 30, 130))
