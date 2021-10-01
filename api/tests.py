from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Daily
from .serializers import DailySerializer
import uuid

DAILYS_URL = '/api/dailys/'


def create_daily():
    defaults = {
        'id': uuid.uuid4(),
        'do': 'test',
        'study': 'test',
        'review': 'test',
        'score': 'good',
        'created_at': '2020-12-08',
    }
    return Daily.objects.create(**defaults)


def detail_daily_url(daily_id):
    return reverse('api:daily-detail', args=[daily_id])


class ApiTests(TestCase):
    def test_1_1_should_get_dailys(self):
        create_daily()
        res = self.client.get(DAILYS_URL)
        dailys = Daily.objects.all()
        serializer = DailySerializer(dailys, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_1_2_should_get_single_dailys(self):
        daily = create_daily()
        url = detail_daily_url(daily.id)
        res = self.client.get(url)
        serializer = DailySerializer(daily)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_1_3_should_create_new_daily_successfully(self):
        payload = {
            'id': uuid.uuid4(),
            'do': 'testcreate',
            'study': 'testcreate',
            'review': 'testcreate',
            'score': 'good',
            'created_at': '2020-12-08',
        }
        res = self.client.post(DAILYS_URL, payload)
        daily = Daily.objects.get(id=res.data['id'])
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(payload['do'], daily.do)
        self.assertEqual(payload['study'], daily.study)
        self.assertEqual(payload['review'], daily.review)
        self.assertEqual(payload['score'], daily.score)
        # self.assertEqual(payload['created_at'], daily.created_at)


    def test_1_4_should_partial_update_daily(self):
        daily = create_daily()
        payload = {'score': 'bad'}
        url = detail_daily_url(daily.id)
        self.client.patch(url, payload)
        daily.refresh_from_db()
        # self.assertEqual(res.status_code, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
        self.assertEqual(daily.score, payload['score'])

    # def test_1_5_should_update_daily(self):
    #     daily = create_daily()
    #     payload = {
    #         'do': 'update',
    #         'study': 'update',
    #         'review': 'update',
    #         'score': 'bad',
    #         'created_at': '2020-12-09',
    #     }
    #     url = detail_daily_url(daily.id)
    #     self.assertEqual(daily.do, 'test')
    #     self.client.put(url, payload)
    #     daily.refresh_from_db()
    #     self.assertEqual(daily.do, payload['do'])


    def test_1_6_should_delete_daily(self):
        daily = create_daily()
        self.assertEqual(1, Daily.objects.count())
        url = detail_daily_url(daily.id)
        self.client.delete(url)
        self.assertEqual(0, Daily.objects.count())