import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
django.setup()

from users.models import User, EmailVerification
from users.tasks import send_email_verification

try:
    u = User.objects.create_user('test_no_worker3', 'no_worker3@example.com', 'pass1234')
    print('Created user id', u.id)

    send_email_verification.delay(u.id)

    exists = EmailVerification.objects.filter(user=u).exists()
    print('EmailVerification exists:', exists)
    print('is_verified_email:', User.objects.get(id=u.id).is_verified_email)
except Exception as e:
    import traceback
    print('ERROR during test script')
    traceback.print_exc()
