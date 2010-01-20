from django.core.management.base import LabelCommand, CommandError
from booster_simulator.models import Card

class Command(LabelCommand):
    help = "Imports netrunner cards from the import file"

    requires_model_validation = True

    def handle_label(self, label, **options):
        f = open(label)
        card_lines = f.readlines()
        for line in card_lines:
            c = line.split(",")
            card = Card(card_name=c[0], player=c[1], rarity=c[2], filename=c[3].strip())
            if (Card.objects.filter(player = card.player, card_name = card.card_name, filename = card.filename, edition="Limited")):
                print "found"
            else:
                card.save()
                print "saved"
    