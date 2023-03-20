class Things:
    # status example: [('paralyzed', true), ('bloodied', false)]  true false表示玩家自己能不能看到
    # status在前端是鼠标悬浮上面显示的东西
    def __init__(self, world, coordinate, hp, max_hp, invisible, transparent, defense, appearance, status):
        self.world = world
        self.coordinate = coordinate
        self.hp = hp
        self.max_hp = max_hp
        self.invisible = invisible
        self.defense = defense
        self.appearance = appearance
        self.status = status
        self.transparent = transparent

    def search(self, val):
        if val >= self.invisible:
            self.invisible = 0

    def attack(self, val):
        if "AC" not in self.defense:
            return True
        if val >= self.defense["AC"]:
            return True
        return False

    def damage(self, val, dmg_type):
        out1 = val
        out2 = val
        if dmg_type in self.defense:
            if isinstance(self.defense[dmg_type], int):
                out1 -= self.defense[dmg_type]
            elif isinstance(self.defense[dmg_type], str):
                out1 *= 1 - float(self.defense[dmg_type][:-1]) / 100
        if "all" in self.defense:
            if isinstance(self.defense["all"], int):
                out2 -= self.defense["all"]
            elif isinstance(self.defense["all"], str):
                out2 *= 1 - float(self.defense["all"][:-1]) / 100
        out = min(out1, out2)
        self.hp = max(0, self.hp - out)
        return self.hp

    def heal(self, val):
        self.hp += val
        self.hp = min(self.hp, self.max_hp)


class Indestructible(Things):
    def __init__(self, world, coordinate, invisible, transparent, appearance, status):
        super(Indestructible, self).__init__(world, coordinate, 1, 1, invisible, transparent, {"AC": 0, "all": "100%"}, appearance, status)


preset = {
    'grass': (10, 10, 0, False, {"AC": 0, "fire": "-100%", "psychic": "100%", "piercing": "50%"}, "www.grass.com", {'name': 'Grass', 'type': 'object'})
}


class PresetThing(Things):
    def __init__(self, world, coordinate, name):
        assert (name in preset)
        super(PresetThing, self).__init__(world, coordinate, preset[name][0], preset[name][1], preset[name][2], preset[name][3], preset[name][4], preset[name][5], preset[name[6]])


class Creature(Things):
    def __init__(self, world, coordinate, hp, max_hp, invisible, transparent, defense, appearance, status, actions, attrs):
        super(Creature, self).__init__(world, coordinate, hp, max_hp, invisible, transparent, defense, appearance, status)
        self.actions = actions
        self.attrs = attrs


class World:
    def __init__(self, world_map, characters):
        self.world_map = world_map
        self.characters = characters

