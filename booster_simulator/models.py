from django.db import models

RARITY_TYPES = (
    (u'V', u'Vital',),
    (u'R', u'Rare',),
    (u'U', u'Uncommon',),
    (u'C', u'Common',),
)
PLAYER_TYPES = (
    (u'C', u'Corporation',),
    (u'R', u'Runner',),
)

class Card(models.Model):
    card_name = models.CharField(null=False, blank=False, max_length=200)
    player = models.CharField(null=False, blank=False,max_length = 1, choices=PLAYER_TYPES)
    rarity = models.CharField(null=False, blank=False,max_length = 1, choices=RARITY_TYPES)
    filename = models.CharField(null=True, blank=True, max_length = 200)
    edition = models.CharField(null=True, blank=False, max_length = 100)
    
    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"{%s}[%s] %s" % (self.player, self.rarity, self.card_name,) 
