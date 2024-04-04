from django import forms
from .models import CorporateSubscription, Month, UserSubscription
from django.core.mail import send_mail
from django.conf import settings

class CorporateSubscriptionForm(forms.ModelForm):
    issues = forms.ModelMultipleChoiceField(
        queryset=Month.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Выберите нужные номера'
    )

    class Meta:
        model = CorporateSubscription
        fields = [
            'type', 'year', 'issues', 'amount', 'org_name', 'phone', 'inn',
            'kpp', 'real_address', 'corporate_address', 'email', 'contact'
        ]
        widgets = {
            'org_name': forms.Textarea(attrs={'rows': 1}),
            'real_address': forms.Textarea(attrs={'rows': 2}),
            'corporate_address': forms.Textarea(attrs={'rows': 2}),
        }
        labels = {
            'type': 'Варианты получения журнала',
            'year': 'Год',
            'amount': 'Количество экземпляров',
            'org_name': 'Наименование организации',
            'phone': 'Телефон',
            'inn': 'ИНН',
            'kpp': 'КПП',
            'real_address': 'Адрес фактический',
            'corporate_address': 'Адрес Юридический',
            'email': 'Электронный почтовый адрес e-mail',
            'contact': 'Контактное лицо',
        }
        
    def send_email_notification(self):
        cleaned_data = self.cleaned_data
        subject = f'Новая подписка #{self.instance.id}'
        message = f'''
            Новая подписка #{self.instance.id}:

            Варианты получения журнала: {cleaned_data["type"]}
            Год: {cleaned_data["year"]}
            Количество экземпляров: {cleaned_data["amount"]}
            Наименование организации: {cleaned_data["org_name"]}
            Телефон: {cleaned_data["phone"]}
            ИНН: {cleaned_data["inn"]}
            КПП: {cleaned_data["kpp"]}
            Адрес фактический: {cleaned_data["real_address"]}
            Адрес Юридический: {cleaned_data["corporate_address"]}
            Электронный почтовый адрес e-mail: {cleaned_data["email"]}
            Контактное лицо: {cleaned_data["contact"]}
            Выбранные номера: {", ".join(str(issue) for issue in cleaned_data["issues"])}
        '''
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['admin@a0881073.xsph.ru',])

    def save(self, commit=True):
        instance = super().save(commit)
        self.send_email_notification()
        return instance


class UserSubscriptionForm(forms.ModelForm):
    issues = forms.ModelMultipleChoiceField(
        queryset=Month.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Выберите нужные номера'
    )

    class Meta:
        model = UserSubscription
        fields = ['type', 'year', 'issues', 'amount', 'contact', 'phone', 'real_address', 'email']
        labels = {
            'type': 'Варианты получения журнала',
            'year': 'Год',
            'amount': 'Количество экземпляров',
            'contact': 'ФИО',
            'phone': 'Телефон',
            'real_address': 'Адрес фактический',
            'email': 'Электронный почтовый адрес e-mail',
        }
        widgets = {
            'issues': forms.CheckboxSelectMultiple
        }
        
    def send_email_notification(self):
        cleaned_data = self.cleaned_data
        subject = f'Новая подписка #{self.instance.id}'
        message = f'''
            Новая подписка #{self.instance.id}:

            Варианты получения журнала: {cleaned_data["type"]}
            Год: {cleaned_data["year"]}
            Количество экземпляров: {cleaned_data["amount"]}
            ФИО: {cleaned_data["contact"]}
            Телефон: {cleaned_data["phone"]}
            Адрес фактический: {cleaned_data["real_address"]}
            Электронный почтовый адрес e-mail: {cleaned_data["email"]}
            Выбранные номера: {", ".join(str(issue) for issue in cleaned_data["issues"])}
        '''
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['admin@a0881073.xsph.ru',])

    def save(self, commit=True):
        instance = super().save(commit)
        self.send_email_notification()
        return instance