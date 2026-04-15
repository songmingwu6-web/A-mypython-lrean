def get_place(city,country,population=''):
    """生成函数，返回城市和国家的组合"""
    
    if population:
        place = f"{city}, {country}"
        place += f"人口{population}"
    else:
        place = f"{city}, {country}"
        print(place)
    return place
