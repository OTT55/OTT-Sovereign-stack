
powers = []
energy = {
     "kol": {
        "firstname": 'Kolakanwi',
        "lastname": 'Van Tegha',
        "ability": 'light manipulation',
        "weakness": 'absence of light for long',
    },
    "ja": {
        "firstname": 'Jolakanwi',
        "lastname": 'Van Tegha',
        "ability": 'aura manipulation',
        "weakness": 'drains his energy frequently',
    },
    "kianni": {
        "firstname": 'Kianni',
        "lastname": 'Sol',
        "ability": 'Vibrate and teleport',
        "weakness": 'can use the two interchangably for long',
    },
    "jade" : {
        "firstname": 'Jade',
        "lastname": 'Sol Van Tegha',
        "ability": 'physics manipulation',
        "weakness": 'excess physical strain and trauma',
    },
    "kirby" : {
        "firstname": 'Kirby',
        "lastname": 'Okante',
        "ability": 'Kinetic shell',
        "weakness": 'shell activates only on impact',
    },
    "luente" : {
        "firstname": 'Luente',
        "lastname": 'Tening',
        "ability": 'Thermal manipulation',
        "weakness": 'cold environments for too long',
    },
}
biokinetics = {
    "gaelle": {
        "firstname": 'Gaelle',
        "lastname": 'Antri',
        "ability": 'Seraphim',
        "weakness": 'cannot heal while flying',
    },
    "brandon": {
        "firstname": 'Brandon',
        "lastname": 'Okante',
        "ability": 'metamorphosis',
        "weakness": 'starts hurting after a while',
    },
    "sofia": {
        "firstname": 'Sofia',
        "lastname": 'Selman',
        "ability": 'hunter',
        "weakness": 'sensory overload in chaotic environments',
    },
    "jemimah": {
        "firstname": 'Jemimah',
        "lastname": 'Selman',
        "ability": 'predator',
        "weakness": 'susceptible to cat weaknesses',
    },
    "ulysis": {
        "firstname": 'Ulysis',
        "lastname": 'Ghazi',
        "ability": 'blood puppetry',
        "weakness": 'his he over uses blood, he becomes weak',
    },


}
powers = [energy, biokinetics]
for power in powers:
     for person, traits in power.items():
          print(f"Username : {person}")
          print(f"\tName : {traits['firstname']} {traits['lastname']}")
          print(f"\tAbilities : {traits['ability'].capitalize()}")
          print(f"\tWeaknesses : {traits['weakness'].capitalize()}")