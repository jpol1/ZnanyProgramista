from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)

class ChangeEmailTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.email)

account_activation_token = AccountActivationTokenGenerator()

change_email_token = ChangeEmailTokenGenerator()