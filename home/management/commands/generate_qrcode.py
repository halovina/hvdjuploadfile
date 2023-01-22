from django.core.management.base import BaseCommand
from home.qr import make_base64_qr_code

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print(make_base64_qr_code("123456789012dfdfdf"))
        return