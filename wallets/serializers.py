from django.contrib.auth.models import User, Group

from rest_framework import serializers

from wallets.models import Wallet, CompanyData


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class CompanyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyData
        exclude = ('id',)


class WalletSerializer(serializers.ModelSerializer):
    company_data = CompanyDataSerializer(required=False, allow_null=True)
    account_number = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = Wallet
        fields = ('id', 'user', 'ballance', 'creation_date', 'active', 'company_data',
                  'country', 'account_number', 'is_company')

    def update(self, instance, validated_data):
        company_data = validated_data.get('company_data')
        if company_data:
            if instance.company_data:    # obiekt ma juz dane to robimy update
                CompanyData.objects.filter(id=instance.company_data.id).update(**company_data)
            else:   # obiekt nie ma danych wiec je tworzymy i przypisujemy
                c_data = CompanyData.objects.create(**company_data)
                instance.company_data = c_data
                instance.save()
        else:
            CompanyData.objects.filter(id=instance.company_data.id).delete()
            instance.company_data = None
            instance.save()
        return instance

