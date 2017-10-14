def wind_chill_temp(ta, v):
    v_time = v ** 0.16;
    twc = 35.74 + 0.6215 * ta - 35.75 * v_time + 0.4275 * ta * v_time
    return twc